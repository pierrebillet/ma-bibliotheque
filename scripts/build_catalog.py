#!/usr/bin/env python3
"""Génère catalog.json à partir des livres HTML du dépôt.

Deux formats sont acceptés :
- livres/nom-du-livre.html ;
- livres/nom-du-livre/index.html (ou, par compatibilité, un unique fichier HTML
  dans ce sous-dossier).

Bibliothèque standard uniquement. Le script est volontairement tolérant : une erreur
sur un livre ne bloque pas les autres et le titre dérivé de son identifiant reste le
fallback ultime.
"""

from __future__ import annotations

import argparse
import codecs
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, Sequence

SCHEMA_VERSION = 1
SCAN_CHUNK_BYTES = 64 * 1024
MAX_SCAN_BYTES = 4 * 1024 * 1024
ENCODING_PROBE_BYTES = 16 * 1024
COVER_EXTENSIONS = ("webp", "png", "jpg")
BOOK_META_NAMES = {
    "book:title",
    "book:author",
    "book:description",
    "book:tags",
    "book:date",
}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_PATTERNS = (
    (re.compile(r"^\d{4}$"), "year"),
    (re.compile(r"^\d{4}-\d{2}$"), "month"),
    (re.compile(r"^\d{4}-\d{2}-\d{2}$"), "day"),
)
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
WHITESPACE_RE = re.compile(r"\s+")
META_TAG_RE = re.compile(br"<meta\b[^>]*>", re.IGNORECASE)
CHARSET_ATTR_RE = re.compile(
    br"\bcharset\s*=\s*(?:[\"']\s*)?([A-Za-z0-9._:+-]+)", re.IGNORECASE
)
CONTENT_ATTR_RE = re.compile(
    br"\bcontent\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))",
    re.IGNORECASE,
)
HTTP_EQUIV_RE = re.compile(
    br"\bhttp-equiv\s*=\s*(?:\"\s*content-type\s*\"|'\s*content-type\s*'|content-type)",
    re.IGNORECASE,
)
CHARSET_IN_CONTENT_RE = re.compile(br"charset\s*=\s*([A-Za-z0-9._:+-]+)", re.IGNORECASE)


@dataclass(frozen=True)
class AdditionDate:
    instant: datetime
    source: str


class MetadataParser(HTMLParser):
    """Extracteur tolérant fondé sur le parseur HTML de la bibliothèque standard."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.values: dict[str, list[str]] = {name: [] for name in BOOK_META_NAMES}
        self.titles: list[str] = []
        self._in_title = False
        self._title_parts: list[str] = []
        self.saw_head = False
        self.head_closed = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        lowered = tag.lower()
        if lowered == "head":
            self.saw_head = True
        elif lowered == "title":
            if self._in_title:
                self._finish_title()
            self._in_title = True
            self._title_parts = []
        elif lowered == "meta":
            self._read_meta(attrs)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "meta":
            self._read_meta(attrs)

    def handle_endtag(self, tag: str) -> None:
        lowered = tag.lower()
        if lowered == "title" and self._in_title:
            self._finish_title()
        elif lowered == "head" and self.saw_head:
            self.head_closed = True

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)

    def close(self) -> None:
        if self._in_title:
            self._finish_title()
        super().close()

    def _read_meta(self, attrs: list[tuple[str, str | None]]) -> None:
        attr_map: dict[str, str] = {}
        for key, value in attrs:
            if value is not None and key.lower() not in attr_map:
                attr_map[key.lower()] = value

        name = normalize_text(attr_map.get("name", "")).lower()
        if name not in BOOK_META_NAMES:
            return

        content = normalize_text(attr_map.get("content", ""))
        if content:
            self.values[name].append(content)

    def _finish_title(self) -> None:
        title = normalize_text("".join(self._title_parts))
        if title:
            self.titles.append(title)
        self._in_title = False
        self._title_parts = []


def normalize_text(value: object) -> str:
    text = html.unescape(str(value))
    text = CONTROL_RE.sub("", text)
    text = unicodedata.normalize("NFC", text)
    return WHITESPACE_RE.sub(" ", text).strip()


def comparison_key(value: str) -> str:
    decomposed = unicodedata.normalize("NFD", value)
    without_marks = "".join(char for char in decomposed if not unicodedata.combining(char))
    return without_marks.casefold()


def humanize_slug(slug: str) -> str:
    value = WHITESPACE_RE.sub(" ", slug.replace("-", " ")).strip()
    if not value:
        return slug
    return value[0].upper() + value[1:]


def annotation_escape(value: object) -> str:
    return (
        str(value)
        .replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
    )


def warn(message: str, relative_path: str | None = None) -> None:
    escaped = annotation_escape(message)
    if relative_path:
        print(f"::warning file={annotation_escape(relative_path)}::{escaped}", file=sys.stderr)
    else:
        print(f"::warning::{escaped}", file=sys.stderr)


def detect_declared_encoding(prefix: bytes) -> str | None:
    for tag in META_TAG_RE.findall(prefix):
        direct = CHARSET_ATTR_RE.search(tag)
        if direct:
            return direct.group(1).decode("ascii", errors="ignore")

        if not HTTP_EQUIV_RE.search(tag):
            continue
        content_match = CONTENT_ATTR_RE.search(tag)
        if not content_match:
            continue
        content = next((group for group in content_match.groups() if group is not None), b"")
        declared = CHARSET_IN_CONTENT_RE.search(content)
        if declared:
            return declared.group(1).decode("ascii", errors="ignore")
    return None


def choose_encoding(path: Path, relative_path: str) -> tuple[str, str, bool]:
    try:
        with path.open("rb") as stream:
            prefix = stream.read(ENCODING_PROBE_BYTES)
    except OSError:
        raise

    if prefix.startswith(codecs.BOM_UTF8):
        return "utf-8-sig", "strict", False
    if prefix.startswith(codecs.BOM_UTF32_LE) or prefix.startswith(codecs.BOM_UTF32_BE):
        return "utf-32", "strict", False
    if prefix.startswith(codecs.BOM_UTF16_LE) or prefix.startswith(codecs.BOM_UTF16_BE):
        return "utf-16", "strict", False

    declared = detect_declared_encoding(prefix)
    if declared:
        try:
            canonical = codecs.lookup(declared).name
            return canonical, "strict", False
        except LookupError:
            warn(f"Encodage déclaré inconnu ignoré : {declared}", relative_path)

    try:
        prefix.decode("utf-8", errors="strict")
        return "utf-8", "strict", False
    except UnicodeDecodeError:
        return "cp1252", "replace", True


def scan_metadata(path: Path, relative_path: str) -> MetadataParser:
    encoding, errors, used_fallback = choose_encoding(path, relative_path)
    if used_fallback:
        warn("Décodage Windows-1252 de secours utilisé.", relative_path)

    try:
        return _scan_metadata_with_encoding(path, encoding, errors)
    except UnicodeDecodeError:
        warn(
            f"Décodage {encoding} impossible ; reprise en Windows-1252 avec remplacement.",
            relative_path,
        )
        return _scan_metadata_with_encoding(path, "cp1252", "replace")


def _scan_metadata_with_encoding(path: Path, encoding: str, errors: str) -> MetadataParser:
    parser = MetadataParser()
    decoder = codecs.getincrementaldecoder(encoding)(errors=errors)
    total = 0

    with path.open("rb") as stream:
        while total < MAX_SCAN_BYTES:
            chunk = stream.read(min(SCAN_CHUNK_BYTES, MAX_SCAN_BYTES - total))
            if not chunk:
                parser.feed(decoder.decode(b"", final=True))
                break

            total += len(chunk)
            parser.feed(decoder.decode(chunk, final=False))
            if parser.head_closed:
                break
        else:
            parser.feed(decoder.decode(b"", final=True))

    parser.close()
    return parser


def first_scalar(
    values: Sequence[str],
    field_name: str,
    relative_path: str,
) -> str | None:
    if len(values) > 1:
        warn(
            f"Plusieurs métadonnées {field_name} non vides : la première est utilisée.",
            relative_path,
        )
    return values[0] if values else None


def deduplicate_tags(raw_values: Iterable[str]) -> list[str]:
    tags: list[str] = []
    seen: set[str] = set()
    for raw_value in raw_values:
        for candidate in raw_value.split(","):
            tag = normalize_text(candidate)
            if not tag:
                continue
            key = comparison_key(tag)
            if key in seen:
                continue
            seen.add(key)
            tags.append(tag)
    return tags


def parse_book_date(values: Sequence[str], relative_path: str) -> tuple[str | None, str | None]:
    valid_values: list[tuple[str, str]] = []
    for value in values:
        parsed = validate_book_date(value)
        if parsed is None:
            warn(f"Date book:date invalide ignorée : {value}", relative_path)
        else:
            valid_values.append(parsed)

    if len(valid_values) > 1:
        warn("Plusieurs dates book:date valides : la première est utilisée.", relative_path)
    return valid_values[0] if valid_values else (None, None)


def validate_book_date(value: str) -> tuple[str, str] | None:
    for pattern, precision in DATE_PATTERNS:
        if not pattern.fullmatch(value):
            continue
        try:
            if precision == "year":
                date(int(value), 1, 1)
            elif precision == "month":
                year, month = (int(part) for part in value.split("-"))
                date(year, month, 1)
            else:
                year, month, day = (int(part) for part in value.split("-"))
                date(year, month, day)
        except ValueError:
            return None
        return value, precision
    return None


def warn_long_values(
    title: str,
    author: str | None,
    description: str | None,
    tags: Sequence[str],
    relative_path: str,
) -> None:
    limits = (("titre", title, 160), ("auteur", author, 120), ("description", description, 600))
    for label, value, limit in limits:
        if value and len(value) > limit:
            warn(f"Le champ {label} dépasse {limit} caractères.", relative_path)
    for tag in tags:
        if len(tag) > 40:
            warn(f"Le tag « {tag} » dépasse 40 caractères.", relative_path)
    if len(tags) > 20:
        warn("Le livre comporte plus de 20 tags.", relative_path)


def cover_signature_is_valid(path: Path, extension: str) -> bool:
    try:
        with path.open("rb") as stream:
            prefix = stream.read(16)
    except OSError:
        return False

    if extension == "png":
        return prefix.startswith(b"\x89PNG\r\n\x1a\n")
    if extension == "jpg":
        return prefix.startswith(b"\xff\xd8\xff")
    if extension == "webp":
        return len(prefix) >= 12 and prefix[:4] == b"RIFF" and prefix[8:12] == b"WEBP"
    return False


def resolve_cover(root: Path, slug: str) -> dict[str, str] | None:
    covers_dir = root / "couvertures"
    valid: list[tuple[Path, str]] = []

    for extension in COVER_EXTENSIONS:
        candidate = covers_dir / f"{slug}.{extension}"
        if not candidate.is_file():
            continue
        relative = candidate.relative_to(root).as_posix()
        if not cover_signature_is_valid(candidate, extension):
            warn("Couverture ignorée : signature binaire incompatible avec son extension.", relative)
            continue
        valid.append((candidate, extension))

    if not valid:
        return None

    selected, extension = valid[0]
    if len(valid) > 1:
        ignored = ", ".join(path.name for path, _ in valid[1:])
        warn(
            f"Plusieurs couvertures valides ; {selected.name} est utilisée, ignorée(s) : {ignored}.",
            selected.relative_to(root).as_posix(),
        )

    relative = selected.relative_to(root).as_posix()
    return {
        "filename": selected.name,
        "sourcePath": relative,
        "href": relative,
        "format": extension,
    }


def repository_has_git_history(root: Path) -> bool:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0 and result.stdout.strip() == "true"


def addition_date(root: Path, path: Path, git_available: bool) -> AdditionDate:
    if git_available:
        relative = path.relative_to(root).as_posix()
        try:
            result = subprocess.run(
                ["git", "-C", str(root), "log", "--follow", "--format=%aI", "--", relative],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=15,
                check=False,
            )
            lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
            if result.returncode == 0 and lines:
                # git log est antéchronologique : la dernière ligne correspond au premier commit.
                parsed = datetime.fromisoformat(lines[-1].replace("Z", "+00:00"))
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                return AdditionDate(parsed.astimezone(timezone.utc), "git")
        except (OSError, ValueError, subprocess.TimeoutExpired):
            pass

    try:
        modified = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    except OSError:
        modified = datetime(1970, 1, 1, tzinfo=timezone.utc)
    return AdditionDate(modified, "mtime")


def fallback_entry(root: Path, path: Path, slug: str) -> dict[str, object]:
    relative = path.relative_to(root).as_posix()
    return {
        "id": slug,
        "filename": path.name,
        "sourcePath": relative,
        "href": relative,
        "title": humanize_slug(slug),
        "author": None,
        "description": None,
        "tags": [],
        "date": None,
        "datePrecision": None,
        "cover": resolve_cover(root, slug),
    }


def build_book(root: Path, path: Path, slug: str) -> dict[str, object]:
    relative = path.relative_to(root).as_posix()
    parser = scan_metadata(path, relative)

    meta_title = first_scalar(parser.values["book:title"], "book:title", relative)
    author = first_scalar(parser.values["book:author"], "book:author", relative)
    description = first_scalar(parser.values["book:description"], "book:description", relative)
    title = meta_title or (parser.titles[0] if parser.titles else None) or humanize_slug(slug)
    tags = deduplicate_tags(parser.values["book:tags"])
    book_date, date_precision = parse_book_date(parser.values["book:date"], relative)

    warn_long_values(title, author, description, tags, relative)

    if not SLUG_RE.fullmatch(slug):
        warn(
            "Identifiant hors convention ; le catalogue est produit, mais le fichier ou dossier devrait être renommé en kebab-case ASCII.",
            relative,
        )

    return {
        "id": slug,
        "filename": path.name,
        "sourcePath": relative,
        "href": relative,
        "title": title,
        "author": author,
        "description": description,
        "tags": tags,
        "date": book_date,
        "datePrecision": date_precision,
        "cover": resolve_cover(root, slug),
    }


def discover_books(books_dir: Path) -> list[tuple[Path, str]]:
    """Retourne les points d'entrée des livres et leur identifiant stable."""
    if not books_dir.is_dir():
        return []

    discovered: list[tuple[Path, str]] = [
        (path, path.stem)
        for path in sorted(books_dir.glob("*.html"), key=lambda item: item.name)
        if path.is_file()
    ]
    used_slugs = {slug for _, slug in discovered}

    for directory in sorted(
        (path for path in books_dir.iterdir() if path.is_dir()),
        key=lambda item: item.name,
    ):
        slug = directory.name
        candidates = sorted(
            (path for path in directory.glob("*.html") if path.is_file()),
            key=lambda item: item.name,
        )
        preferred = directory / "index.html"

        if preferred.is_file():
            entrypoint = preferred
        elif (directory / f"{slug}.html").is_file():
            entrypoint = directory / f"{slug}.html"
        elif len(candidates) == 1:
            entrypoint = candidates[0]
        elif not candidates:
            warn(
                "Sous-dossier ignoré : aucun point d’entrée HTML trouvé (index.html attendu).",
                directory.relative_to(books_dir.parent).as_posix(),
            )
            continue
        else:
            warn(
                "Sous-dossier ignoré : plusieurs fichiers HTML et aucun index.html ne permettent d’identifier le point d’entrée.",
                directory.relative_to(books_dir.parent).as_posix(),
            )
            continue

        if slug in used_slugs:
            warn(
                f"Sous-dossier ignoré : l’identifiant « {slug} » est déjà utilisé par un livre HTML simple.",
                entrypoint.relative_to(books_dir.parent).as_posix(),
            )
            continue

        used_slugs.add(slug)
        discovered.append((entrypoint, slug))

    return discovered


def load_existing_catalog(output_path: Path) -> dict[str, object] | None:
    try:
        with output_path.open("r", encoding="utf-8") as stream:
            value = json.load(stream)
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None
    return value if isinstance(value, dict) else None


def generated_at(existing: dict[str, object] | None, books: list[dict[str, object]]) -> str:
    if existing and existing.get("schemaVersion") == SCHEMA_VERSION and existing.get("books") == books:
        previous = existing.get("generatedAt")
        if isinstance(previous, str) and previous:
            return previous
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def write_catalog(output_path: Path, payload: dict[str, object]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_name(f".{output_path.name}.{os.getpid()}.tmp")
    serialized = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    try:
        temporary.write_text(serialized, encoding="utf-8")
        os.replace(temporary, output_path)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def generate(root: Path, output_path: Path) -> dict[str, object]:
    books_dir = root / "livres"
    sources = discover_books(books_dir)

    git_available = repository_has_git_history(root)
    sortable: list[tuple[AdditionDate, dict[str, object]]] = []

    for path, slug in sources:
        relative = path.relative_to(root).as_posix()
        added = addition_date(root, path, git_available)
        try:
            entry = build_book(root, path, slug)
        except Exception as error:  # Tolérance volontaire au niveau de chaque livre.
            warn(
                f"Extraction impossible ({type(error).__name__}: {error}) ; utilisation du nom de fichier.",
                relative,
            )
            entry = fallback_entry(root, path, slug)
        sortable.append((added, entry))

    sortable.sort(
        key=lambda item: (
            -item[0].instant.timestamp(),
            comparison_key(str(item[1]["title"])),
            comparison_key(str(item[1]["id"])),
        )
    )
    books = [entry for _, entry in sortable]
    existing = load_existing_catalog(output_path)
    payload: dict[str, object] = {
        "schemaVersion": SCHEMA_VERSION,
        "generatedAt": generated_at(existing, books),
        "bookCount": len(books),
        "books": books,
    }
    write_catalog(output_path, payload)
    return payload


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Génère catalog.json depuis les fichiers et sous-dossiers de livres/."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=default_root,
        help="Racine du dépôt (défaut : parent du dossier scripts).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("catalog.json"),
        help="Chemin de sortie, absolu ou relatif à --root (défaut : catalog.json).",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    output_path = args.output if args.output.is_absolute() else root / args.output
    try:
        payload = generate(root, output_path)
    except Exception as error:
        print(f"::error::{annotation_escape(type(error).__name__ + ': ' + str(error))}", file=sys.stderr)
        return 1

    count = int(payload["bookCount"])
    print(f"Catalogue généré : {count} livre{'s' if count != 1 else ''} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
