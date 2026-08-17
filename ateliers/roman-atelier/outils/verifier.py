#!/usr/bin/env python3
"""Vérificateur de livre pour l'atelier roman-atelier (v3).

Usage :
    python ateliers/roman-atelier/outils/verifier.py livres/<slug> [--sans-images]

Contrôle un livre de la famille « Atelier » contre la recette
ateliers/roman-atelier/WORKFLOW.md et la spécification de l'îlot
livres/_template/DONNEES.md : métadonnées du <head>, intégrité du codex
(notices orphelines, liens morts, déverrouillages), densité des mentions,
clé localStorage, correspondance îlot <-> manifeste d'illustrations, et
conformité des fichiers d'images (format, dimensions, poids) et de la
couverture.

Depuis le moteur atelier-liseuse v2, une image peut être un **document du
web** (figure de bloc ou image de notice porteuse d'un objet `source`) : le
crédit `source.label`/`source.url` (http(s)) est alors contrôlé, le champ
`visualDescription` n'est pas exigé et l'image est hors manifeste
d'illustrations (sa traçabilité vit dans recherche.md). Sans `source`,
l'image reste une illustration générée soumise aux règles habituelles.

`--sans-images` : ignore l'existence et la conformité des fichiers d'images
(phase « texte d'abord », avant la passe de l'agent illustrateur).

Sortie : les DÉFAUTS (bloquants, code de sortie 1) puis les AVERTISSEMENTS
(non bloquants). Aucune dépendance hors bibliothèque standard.
"""

from __future__ import annotations

import argparse
import json
import re
import struct
import sys
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}(?:-\d{2}(?:-\d{2})?)?$")
META_RE = re.compile(
    r'<meta\s+name="(book:[a-z]+|reader-engine)"\s+content="([^"]*)"', re.S
)
ISLAND_RE = re.compile(
    r'<script type="application/json" id="book-data">(.*?)</script>', re.S
)
BOOK_METAS = ("book:title", "book:author", "book:description", "book:tags", "book:date")
CHAPTER_IMG_MAX = 150 * 1024
COVER_IMG_MAX = 300 * 1024
FIGURE_IMG_MAX = 300 * 1024  # documents du web : lisibilité avant compression
SOURCE_URL_RE = re.compile(r"^https?://")

defauts: list[str] = []
avert: list[str] = []


def d(msg: str) -> None:
    defauts.append(msg)


def w(msg: str) -> None:
    avert.append(msg)


# ---------------------------------------------------------------- images

def image_dimensions(path: Path) -> tuple[str, int, int] | None:
    """(format, largeur, hauteur) d'après la signature binaire, ou None."""
    data = path.read_bytes()
    if data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) >= 24:
        wd, ht = struct.unpack(">II", data[16:24])
        return ("png", wd, ht)
    if data[:3] == b"\xff\xd8\xff":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            length = struct.unpack(">H", data[i + 2:i + 4])[0]
            if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                ht, wd = struct.unpack(">HH", data[i + 5:i + 9])
                return ("jpeg", wd, ht)
            i += 2 + length
        return ("jpeg", 0, 0)
    if data[:4] == b"RIFF" and data[8:12] == b"WEBP" and len(data) >= 30:
        chunk, payload = data[12:16], data[20:]
        if chunk == b"VP8X" and len(payload) >= 10:
            wd = int.from_bytes(payload[4:7], "little") + 1
            ht = int.from_bytes(payload[7:10], "little") + 1
            return ("webp", wd, ht)
        if chunk == b"VP8 " and len(payload) >= 10 and payload[3:6] == b"\x9d\x01\x2a":
            wd = struct.unpack("<H", payload[6:8])[0] & 0x3FFF
            ht = struct.unpack("<H", payload[8:10])[0] & 0x3FFF
            return ("webp", wd, ht)
        if chunk == b"VP8L" and len(payload) >= 5 and payload[0] == 0x2F:
            bits = int.from_bytes(payload[1:5], "little")
            return ("webp", (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1)
        return ("webp", 0, 0)
    return None


def check_image_file(path: Path, label: str, max_bytes: int, ratio: float | None = None,
                     expect: tuple[int, int] | None = None) -> None:
    if not path.is_file():
        d(f"{label} : fichier manquant ({path})")
        return
    info = image_dimensions(path)
    if info is None:
        d(f"{label} : signature binaire inconnue (ni WebP, ni PNG, ni JPEG)")
        return
    fmt, wd, ht = info
    suffix = path.suffix.lower().lstrip(".").replace("jpg", "jpeg")
    if fmt != suffix:
        d(f"{label} : extension .{path.suffix.lstrip('.')} mais contenu {fmt}")
    if fmt != "webp":
        w(f"{label} : format {fmt} au lieu de WebP (toléré en repli, à signaler dans la PR)")
    size = path.stat().st_size
    if size > max_bytes:
        d(f"{label} : {size // 1024} Ko > {max_bytes // 1024} Ko autorisés")
    if not wd or not ht:
        w(f"{label} : dimensions illisibles")
        return
    if ratio is not None and abs(wd / ht - ratio) > 0.02:
        d(f"{label} : ratio {wd}×{ht} hors 2:3")
    if expect is not None and (wd, ht) != expect:
        w(f"{label} : {wd}×{ht} au lieu de {expect[0]}×{expect[1]} — renseigner "
          "imageWidth/imageHeight dans l'îlot si c'est voulu")


# ---------------------------------------------------------------- contrôles

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("livre", help="dossier livres/<slug> (ou fichier livres/<slug>.html)")
    ap.add_argument("--sans-images", action="store_true",
                    help="ignorer l'existence/conformité des fichiers d'images")
    args = ap.parse_args()

    target = Path(args.livre)
    if target.is_dir():
        book_dir, slug = target, target.name
        entry = next((p for p in (target / "index.html", target / f"{slug}.html") if p.is_file()), None)
        if entry is None:
            htmls = sorted(target.glob("*.html"))
            entry = htmls[0] if len(htmls) == 1 else None
    else:
        book_dir, slug, entry = target.parent, target.stem, target
    if entry is None or not entry.is_file():
        print(f"Point d'entrée HTML introuvable dans {target}", file=sys.stderr)
        return 1

    template = slug == "_template"
    root = entry.resolve()
    for parent in root.parents:
        if (parent / "couvertures").is_dir() or (parent / "scripts" / "build_catalog.py").is_file():
            root = parent
            break
    html = entry.read_text(encoding="utf-8")

    if not template and not SLUG_RE.match(slug):
        d(f"slug « {slug} » hors convention (kebab-case ASCII)")

    # --- métadonnées du <head>
    metas = dict(META_RE.findall(html))
    for name in BOOK_METAS:
        if not metas.get(name, "").strip():
            d(f"meta {name} absente ou vide dans le <head>")
    if not template and metas.get("book:date") and not DATE_RE.match(metas["book:date"]):
        d(f"book:date « {metas['book:date']} » invalide (AAAA[-MM[-JJ]])")
    if "atelier des récits explorables" in metas.get("book:author", "").lower():
        d("book:author = pseudonyme collectif interdit (règle d'or : nom du modèle)")
    if not metas.get("book:workflow", "").strip():
        d("meta book:workflow absente (traçabilité de la recette)")
    if not metas.get("reader-engine", "").strip():
        d("meta reader-engine absente (traçabilité du moteur)")

    # --- îlot JSON
    m = ISLAND_RE.search(html)
    if not m:
        d('îlot <script type="application/json" id="book-data"> introuvable')
        return report()
    try:
        book = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        d(f"îlot JSON invalide : {exc}")
        return report()

    meta = book.get("meta", {})
    if meta.get("slug") != slug:
        d(f"meta.slug « {meta.get('slug')} » ≠ dossier « {slug} »")
    for isle_key, head_key in (("title", "book:title"), ("description", "book:description")):
        if metas.get(head_key) and meta.get(isle_key) and metas[head_key] != meta[isle_key]:
            w(f"meta.{isle_key} de l'îlot ≠ {head_key} du <head>")
    for required in ("world", "entityAudit", "cover"):
        if required not in book:
            d(f"bloc « {required} » absent de l'îlot (spec DONNEES.md)")
    for wkey in ("emotionalPromise", "centralIdea", "thematicQuestion"):
        if not book.get("world", {}).get(wkey, "").strip():
            d(f"world.{wkey} absent ou vide")
    if not str(meta.get("codexVoice", "")).strip():
        d("meta.codexVoice absent ou vide (la voix située du codex)")

    # --- clé localStorage
    if 'const KEY=SLUG+"-state-v1"' in html and 'const SLUG=book.meta.slug' in html:
        pass  # moteur atelier-liseuse v1 : la clé est dérivée du slug
    else:
        km = re.search(r'\bKEY\s*=\s*"([^"]+)"', html)
        if not km:
            w("clé localStorage introuvable dans le script")
        elif km.group(1) != f"{slug}-state-v1":
            d(f"clé localStorage « {km.group(1)} » ≠ « {slug}-state-v1 »")

    # --- chapitres et blocs
    chapters = book.get("chapters", [])
    if not chapters:
        d("chapters[] vide")
        return report()
    all_blocks: list[str] = []
    block_chapter: dict[str, dict] = {}
    block_pos: dict[str, int] = {}
    for ch in chapters:
        for key in ("id", "number", "title", "blocks"):
            if key not in ch:
                d(f"chapitre sans champ « {key} » : {ch.get('id') or ch.get('title')}")
        for i, bl in enumerate(ch.get("blocks", [])):
            bid = bl.get("id", "")
            if bid in block_pos:
                d(f"id de bloc en double : {bid}")
            all_blocks.append(bid)
            block_chapter[bid] = ch
            block_pos[bid] = i + 1
            if "mentions" not in bl:
                d(f"bloc {bid} sans champ mentions (tableau, éventuellement vide)")
    order = {bid: i for i, bid in enumerate(all_blocks)}

    # --- codex : intégrité référentielle
    codex = book.get("codex", [])
    ids = [x.get("id", "") for x in codex]
    dup = {i for i in ids if ids.count(i) > 1}
    for i in sorted(dup):
        d(f"id de notice en double : {i}")
    idset = set(ids)
    mentioned: set[str] = set()
    for ch in chapters:
        for bl in ch.get("blocks", []):
            for ref in bl.get("mentions", []):
                mentioned.add(ref)
                if ref not in idset:
                    d(f"mention « {ref} » (bloc {bl.get('id')}) sans notice correspondante")
    spoiler_fields = ("firstMentionChapter", "firstMentionBlock", "earliestSafeChapter",
                      "earliestSafeBlock", "unlockChapter", "unlockBlock",
                      "unlockPosition", "spoilerRisk", "delayReason", "editorialFunction")
    for x in codex:
        xid = x.get("id", "?")
        for key in ("title", "category", "hook", "text", "links", "unlockBlock"):
            if key not in x:
                d(f"notice {xid} sans champ « {key} »")
        if xid not in mentioned:
            d(f"notice orpheline : « {xid} » n'est mentionnée par aucun bloc")
        for link in x.get("links", []):
            if link not in idset:
                d(f"lien mort : {xid} -> « {link} »")
        ub = x.get("unlockBlock")
        if ub not in block_pos:
            d(f"notice {xid} : unlockBlock « {ub} » inexistant")
        else:
            ch = block_chapter[ub]
            if x.get("unlockChapter") not in (None, ch.get("number")):
                d(f"notice {xid} : unlockChapter={x.get('unlockChapter')} mais "
                  f"« {ub} » est au chapitre {ch.get('number')}")
            if x.get("unlockPosition") not in (None, block_pos[ub]):
                d(f"notice {xid} : unlockPosition={x.get('unlockPosition')} mais "
                  f"« {ub} » est en position {block_pos[ub]}")
        missing = [k for k in spoiler_fields if k not in x]
        if missing:
            d(f"notice {xid} : champs de méthode manquants ({', '.join(missing)})")
        seq = [x.get("firstMentionBlock"), x.get("earliestSafeBlock"), x.get("unlockBlock")]
        known = [order[b] for b in seq if b in order]
        if len(known) == 3 and not (known[0] <= known[1] <= known[2]):
            d(f"notice {xid} : ordre firstMention ≤ earliestSafe ≤ unlock non respecté")

    # --- densité d'exploration
    n_mention_blocks = sum(1 for ch in chapters for bl in ch.get("blocks", []) if bl.get("mentions"))
    density = n_mention_blocks / len(all_blocks) if all_blocks else 0
    words = sum(len(bl.get("text", "").split()) for ch in chapters for bl in ch.get("blocks", []))
    if density < 0.40:
        w(f"densité de mentions {density:.0%} < 40 % visés (socle PREFERENCES.md — "
          "dérogeable par le brief)")

    # --- images : îlot <-> manifeste <-> fichiers
    def is_web_document(holder: dict, label: str) -> bool:
        """True si le porteur déclare un crédit `source` (document du web, v2)
        — en contrôlant sa complétude au passage."""
        src = holder.get("source")
        if src is None:
            return False
        if not isinstance(src, dict) or not str(src.get("label", "")).strip():
            d(f"{label} : source.label absent ou vide (crédit obligatoire)")
        if isinstance(src, dict) and not SOURCE_URL_RE.match(str(src.get("url", ""))):
            d(f"{label} : source.url « {src.get('url', '')} » invalide (http(s):// exigé)")
        return True

    island_images: list[tuple[str, dict, str]] = []  # illustrations générées (chemin, porteur, label)
    web_images: list[tuple[str, dict, str]] = []     # documents du web avec crédit source (v2)
    for ch in chapters:
        if ch.get("image"):
            island_images.append((ch["image"], ch, f"chapitre {ch.get('number')}"))
        exp = f"images/chapter-{int(ch.get('number', 0)):02d}.webp"
        if ch.get("image") and ch["image"] != exp:
            w(f"chapitre {ch.get('number')} : image « {ch['image']} » hors convention « {exp} »")
        for bl in ch.get("blocks", []):
            fig = bl.get("figure")
            if not fig:
                continue
            bid = bl.get("id", "?")
            label = f"figure du bloc {bid}"
            img = str(fig.get("image", ""))
            for key in ("image", "caption"):
                if not str(fig.get(key, "")).strip():
                    d(f"{label} : champ « {key} » absent ou vide")
            if img and ("://" in img or img.startswith("/") or ".." in img):
                d(f"{label} : chemin « {img} » non local (le fichier vit dans livres/<slug>/images/, "
                  "aucune ressource distante)")
            elif img and not img.startswith(f"images/figure-{bid}."):
                w(f"{label} : image « {img} » hors convention « images/figure-{bid}.webp »")
            if not (fig.get("imageWidth") and fig.get("imageHeight")):
                d(f"{label} : imageWidth/imageHeight manquants (dimensions réelles exigées, "
                  "pas de défaut 1600×900 pour les figures)")
            if img:
                (web_images if is_web_document(fig, label) else island_images).append((img, fig, label))
    for x in codex:
        if x.get("image"):
            label = f"notice {x.get('id')}"
            exp = f"images/codex-{x.get('id')}.webp"
            if x["image"] != exp:
                w(f"{label} : image « {x['image']} » hors convention « {exp} »")
            (web_images if is_web_document(x, label) else island_images).append((x["image"], x, label))
    for path, holder, label in island_images:
        if not str(holder.get("alt", "")).strip():
            d(f"{label} : image sans alt")
        if not str(holder.get("visualDescription", "")).strip():
            d(f"{label} : image sans visualDescription (source du prompt du manifeste)")
    for path, holder, label in web_images:
        if not str(holder.get("alt", "")).strip():
            d(f"{label} : image sans alt")

    cover = book.get("cover", {})
    if cover and not str(cover.get("alt", "")).strip():
        d("cover.alt absent ou vide")

    manifest = book_dir / "illustrations.md"
    if not template:
        if manifest.is_file():
            listed = set(re.findall(r"(?:images/[\w.-]+\.(?:webp|jpe?g|png)"
                                    r"|couvertures/[\w.-]+\.(?:webp|jpe?g|png))",
                                    manifest.read_text(encoding="utf-8")))
            island_set = {p for p, _, _ in island_images}
            if cover.get("catalogImage"):
                island_set.add(cover["catalogImage"])
            for p in sorted(island_set - listed):
                d(f"image de l'îlot absente du manifeste illustrations.md : {p}")
            for p in sorted(listed - island_set):
                d(f"image du manifeste absente de l'îlot : {p}")
        elif island_images:
            d("manifeste livres/<slug>/illustrations.md manquant (étape illustrations de la "
              "recette : des images générées sont déclarées dans l'îlot)")
        if not (book_dir / "brief.md").is_file():
            w("brief.md absent du dossier du livre (traçabilité de l'entrée, étape 1)")

    if not args.sans_images and not template:
        for path, holder, label in island_images:
            expect = (holder.get("imageWidth", 1600), holder.get("imageHeight", 900))
            check_image_file(book_dir / path, label, CHAPTER_IMG_MAX, expect=expect)
        for path, holder, label in web_images:
            expect = None
            if holder.get("imageWidth") and holder.get("imageHeight"):
                expect = (holder["imageWidth"], holder["imageHeight"])
            check_image_file(book_dir / path, label, FIGURE_IMG_MAX, expect=expect)
        covers = [p for ext in ("webp", "png", "jpg", "jpeg")
                  for p in [root / "couvertures" / f"{slug}.{ext}"] if p.is_file()]
        if not covers:
            d(f"couverture manquante : couvertures/{slug}.webp (ou .png/.jpg)")
        else:
            check_image_file(covers[0], "couverture", COVER_IMG_MAX, ratio=2 / 3)

    print(f"{slug} : {len(chapters)} chapitres, {len(all_blocks)} blocs, {words} mots, "
          f"{len(codex)} notices, densité de mentions {density:.0%}, "
          f"{len(island_images)} images générées déclarées, "
          f"{len(web_images)} documents du web déclarés")
    return report()


def report() -> int:
    if defauts:
        print(f"\nDÉFAUTS ({len(defauts)}) :")
        for msg in defauts:
            print(f"  ✗ {msg}")
    if avert:
        print(f"\nAVERTISSEMENTS ({len(avert)}) :")
        for msg in avert:
            print(f"  ! {msg}")
    if not defauts:
        print("\nAucun défaut" + (" (avertissements ci-dessus)" if avert else " — livre conforme."))
    return 1 if defauts else 0


if __name__ == "__main__":
    sys.exit(main())
