"""Tests du générateur de catalogue (bibliothèque standard uniquement).

Deux familles :
- tests unitaires sur une mini-bibliothèque synthétique (tmpdir) ;
- test d'or sur le dépôt réel : la régénération doit reproduire le
  catalog.json committé (l'ordre n'est vérifié que si l'historique git est
  complet — un clone shallow fausse les dates d'ajout, voir catalog.yml).

Lancement : python -m unittest discover -s tests
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_catalog  # noqa: E402  (import après l'ajustement de sys.path)

# Ordre des clés du schéma v3 — le contrat documenté dans
# docs/bibliotheque/CATALOGUE.md, que catalog_entry doit figer.
EXPECTED_KEY_ORDER = [
    "id",
    "filename",
    "sourcePath",
    "href",
    "title",
    "author",
    "description",
    "tags",
    "nature",
    "genre",
    "format",
    "tonalite",
    "exigence",
    "audience",
    "date",
    "datePrecision",
    "variantOf",
    "capabilities",
    "wordCount",
    "readingMinutes",
    "cover",
]

# Signature WebP minimale acceptée par cover_signature_is_valid.
WEBP_BYTES = b"RIFF\x00\x00\x00\x00WEBPVP8 "


def book_html(metas: dict[str, str] | None = None, title_tag: str | None = None, body: str = "") -> str:
    meta_lines = "".join(
        f'<meta name="{name}" content="{content}">\n' for name, content in (metas or {}).items()
    )
    title_line = f"<title>{title_tag}</title>\n" if title_tag else ""
    return (
        "<!doctype html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        f"{title_line}{meta_lines}</head>\n<body>\n{body}\n</body>\n</html>\n"
    )


@contextlib.contextmanager
def captured_stderr():
    buffer = io.StringIO()
    with contextlib.redirect_stderr(buffer):
        yield buffer


class LibraryFixture(unittest.TestCase):
    """Socle commun : une racine de bibliothèque jetable."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        (self.root / "livres").mkdir()
        (self.root / "couvertures").mkdir()

    def add_book(self, slug: str, content: str, *, as_dir: bool = False, mtime: float | None = None) -> Path:
        if as_dir:
            directory = self.root / "livres" / slug
            directory.mkdir()
            path = directory / "index.html"
        else:
            path = self.root / "livres" / f"{slug}.html"
        path.write_text(content, encoding="utf-8")
        if mtime is not None:
            os.utime(path, (mtime, mtime))
        return path

    def generate(self) -> dict[str, object]:
        output = self.root / "catalog.json"
        with captured_stderr():
            return build_catalog.generate(self.root, output)


class TestDecouverteEtSlug(LibraryFixture):
    def test_slug_invalide_bloque_la_generation(self) -> None:
        self.add_book("mon-livre", book_html())
        (self.root / "livres" / "Mauvais_Slug.html").write_text(book_html(), encoding="utf-8")
        with captured_stderr():
            with self.assertRaises(build_catalog.InvalidSlugError):
                build_catalog.generate(self.root, self.root / "catalog.json")

    def test_dossier_et_fichier_plat_sont_decouverts(self) -> None:
        self.add_book("livre-plat", book_html())
        self.add_book("livre-dossier", book_html(), as_dir=True)
        payload = self.generate()
        ids = sorted(book["id"] for book in payload["books"])
        self.assertEqual(ids, ["livre-dossier", "livre-plat"])
        self.assertEqual(payload["bookCount"], 2)

    def test_template_et_fichiers_caches_sont_ignores(self) -> None:
        self.add_book("visible", book_html())
        self.add_book("_template", book_html(), as_dir=True)
        (self.root / "livres" / ".cache.html").write_text(book_html(), encoding="utf-8")
        payload = self.generate()
        self.assertEqual([book["id"] for book in payload["books"]], ["visible"])


class TestMetadonnees(LibraryFixture):
    def test_fallbacks_du_titre(self) -> None:
        self.add_book("sans-rien", book_html())
        self.add_book("avec-title", book_html(title_tag="Titre balise"))
        self.add_book("avec-meta", book_html({"book:title": "Titre meta"}, title_tag="Titre balise"))
        by_id = {book["id"]: book for book in self.generate()["books"]}
        self.assertEqual(by_id["sans-rien"]["title"], "Sans rien")
        self.assertEqual(by_id["avec-title"]["title"], "Titre balise")
        self.assertEqual(by_id["avec-meta"]["title"], "Titre meta")

    def test_ordre_des_cles_identique_entre_entree_et_repli(self) -> None:
        self.add_book("complet", book_html({"book:title": "Complet"}))
        entry = self.generate()["books"][0]
        self.assertEqual(list(entry.keys()), EXPECTED_KEY_ORDER)
        fallback = build_catalog.fallback_entry(self.root, self.root / "livres" / "complet.html", "complet")
        self.assertEqual(list(fallback.keys()), EXPECTED_KEY_ORDER)

    def test_vocabulaire_ferme_insensible_casse_et_accents(self) -> None:
        self.add_book(
            "bien-etiquete",
            book_html({"book:genre": "Science-Fiction", "book:exigence": "EXIGEANTE"}),
        )
        book = self.generate()["books"][0]
        # La graphie canonique du vocabulaire est écrite, pas celle de la meta.
        self.assertEqual(book["genre"], "science-fiction")
        self.assertEqual(book["exigence"], "exigeante")

    def test_valeur_hors_vocabulaire_donne_null_et_avertit(self) -> None:
        self.add_book("mal-etiquete", book_html({"book:genre": "polar noir"}))
        output = self.root / "catalog.json"
        with captured_stderr() as stderr:
            payload = build_catalog.generate(self.root, output)
        self.assertIsNone(payload["books"][0]["genre"])
        self.assertIn("hors vocabulaire", stderr.getvalue())

    def test_tags_dedoublonnes_et_tags_reserves_ecartes(self) -> None:
        self.add_book(
            "taggue",
            book_html({"book:tags": "Paris, paris, fantasy, mémoire, MÉMOIRE"}),
        )
        book = self.generate()["books"][0]
        # « fantasy » reprend un genre : écarté. Doublons insensibles casse/accents.
        self.assertEqual(book["tags"], ["Paris", "mémoire"])

    def test_variant_of_valide_et_references_cassees(self) -> None:
        self.add_book("original", book_html())
        self.add_book("edition-bis", book_html({"book:variant-of": "original"}))
        self.add_book("orphelin", book_html({"book:variant-of": "livre-fantome"}))
        self.add_book("narcisse", book_html({"book:variant-of": "narcisse"}))
        by_id = {book["id"]: book for book in self.generate()["books"]}
        self.assertEqual(by_id["edition-bis"]["variantOf"], "original")
        self.assertIsNone(by_id["orphelin"]["variantOf"])
        self.assertIsNone(by_id["narcisse"]["variantOf"])

    def test_nature_deduite_de_l_atelier(self) -> None:
        self.add_book("roman", book_html({"book:workflow": "roman-atelier v9"}))
        self.add_book("enquete", book_html({"book:workflow": "reportage v7"}))
        self.add_book("inconnu", book_html({"book:workflow": "atelier-mystere v1"}))
        self.add_book("muet", book_html())
        by_id = {book["id"]: book for book in self.generate()["books"]}
        self.assertEqual(by_id["roman"]["nature"], "fiction")
        self.assertEqual(by_id["enquete"]["nature"], "reportage")
        self.assertEqual(by_id["inconnu"]["nature"], "fiction")
        self.assertEqual(by_id["muet"]["nature"], "fiction")

    def test_capacites_dans_l_ordre_du_vocabulaire(self) -> None:
        self.add_book("interactif", book_html({"book:capacites": "carte, codex, hologramme"}))
        with captured_stderr() as stderr:
            payload = build_catalog.generate(self.root, self.root / "catalog.json")
        # L'ordre est celui de CAPACITES, pas celui de la meta ; l'inconnue est écartée.
        self.assertEqual(payload["books"][0]["capabilities"], ["codex", "carte"])
        self.assertIn("hologramme", stderr.getvalue())

    def test_date_invalide_ignoree(self) -> None:
        self.add_book("date-ok", book_html({"book:date": "2026-08"}))
        self.add_book("date-ko", book_html({"book:date": "2026-13-40"}))
        by_id = {book["id"]: book for book in self.generate()["books"]}
        self.assertEqual((by_id["date-ok"]["date"], by_id["date-ok"]["datePrecision"]), ("2026-08", "month"))
        self.assertEqual((by_id["date-ko"]["date"], by_id["date-ko"]["datePrecision"]), (None, None))


class TestComptageEtCouvertures(LibraryFixture):
    def test_word_count_depuis_l_ilot_json(self) -> None:
        island = json.dumps(
            {
                "chapters": [
                    {"blocks": [{"text": "un deux trois"}, {"text": "quatre cinq"}]},
                    {"texte": "six sept"},
                ],
                "codex": [{"text": "jamais compté " * 100}],
            }
        )
        body = f'<script type="application/json" id="book-data">{island}</script>'
        self.add_book("mesurable", book_html(body=body))
        book = self.generate()["books"][0]
        self.assertEqual(book["wordCount"], 7)
        self.assertEqual(book["readingMinutes"], 1)  # plancher d'une minute

    def test_word_count_null_sans_texte_substantiel(self) -> None:
        self.add_book("immesurable", book_html(body="<p>trop court</p>"))
        book = self.generate()["books"][0]
        self.assertIsNone(book["wordCount"])
        self.assertIsNone(book["readingMinutes"])

    def test_reading_minutes(self) -> None:
        self.assertIsNone(build_catalog.reading_minutes(None))
        self.assertEqual(build_catalog.reading_minutes(100), 1)
        self.assertEqual(build_catalog.reading_minutes(13974), 70)

    def test_couverture_signature_controlee(self) -> None:
        self.add_book("couvert", book_html())
        self.add_book("decouvert", book_html())
        (self.root / "couvertures" / "couvert.webp").write_bytes(WEBP_BYTES)
        # Extension webp mais contenu PNG : signature incompatible, ignorée.
        (self.root / "couvertures" / "decouvert.webp").write_bytes(b"\x89PNG\r\n\x1a\nxxxx")
        by_id = {book["id"]: book for book in self.generate()["books"]}
        self.assertEqual(by_id["couvert"]["cover"]["href"], "couvertures/couvert.webp")
        self.assertEqual(by_id["couvert"]["cover"]["format"], "webp")
        self.assertIsNone(by_id["decouvert"]["cover"])

    def test_couverture_embarquee_en_repli_pour_un_dossier(self) -> None:
        directory_book = self.add_book("embarque", book_html(), as_dir=True)
        (directory_book.parent / "cover.webp").write_bytes(WEBP_BYTES)
        book = self.generate()["books"][0]
        self.assertEqual(book["cover"]["href"], "livres/embarque/cover.webp")


class TestSorties(LibraryFixture):
    def test_generated_at_conserve_si_la_liste_ne_change_pas(self) -> None:
        self.add_book("stable", book_html(), mtime=1_700_000_000)
        first = self.generate()
        second = self.generate()
        self.assertEqual(first["generatedAt"], second["generatedAt"])

    def test_bloc_demo_synchronise_et_echappe(self) -> None:
        index_path = self.root / "index.html"
        index_path.write_text(
            '<html><body><script id="demo-catalog" type="application/json">{}</script></body></html>',
            encoding="utf-8",
        )
        payload = {"schemaVersion": 3, "books": [{"description": "avec </script> dedans"}]}
        self.assertTrue(build_catalog.sync_demo_catalog(index_path, payload))
        content = index_path.read_text(encoding="utf-8")
        self.assertIn("<\\/script> dedans", content)
        self.assertNotIn("</script> dedans", content)
        # Le JSON échappé reste strictement équivalent après parse.
        body = content.split('type="application/json">', 1)[1].split("</script>", 1)[0]
        self.assertEqual(json.loads(body), payload)
        # Une resynchronisation à l'identique ne réécrit pas le fichier.
        self.assertFalse(build_catalog.sync_demo_catalog(index_path, payload))

    def test_bloc_demo_absent_ou_duplique_refuse(self) -> None:
        index_path = self.root / "index.html"
        index_path.write_text("<html><body></body></html>", encoding="utf-8")
        with self.assertRaises(build_catalog.DemoBlockError):
            build_catalog.sync_demo_catalog(index_path, {})
        index_path.write_text(
            '<script id="demo-catalog" type="application/json">{}</script>'
            '<script id="demo-catalog" type="application/json">{}</script>',
            encoding="utf-8",
        )
        with self.assertRaises(build_catalog.DemoBlockError):
            build_catalog.sync_demo_catalog(index_path, {})

    def test_sitemap_deterministe(self) -> None:
        payload = {"books": [{"href": "livres/un.html"}, {"href": "livres/deux/index.html"}]}
        expected = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            "  <url><loc>https://exemple.test/</loc></url>\n"
            "  <url><loc>https://exemple.test/a-propos.html</loc></url>\n"
            "  <url><loc>https://exemple.test/livres/un.html</loc></url>\n"
            "  <url><loc>https://exemple.test/livres/deux/index.html</loc></url>\n"
            "</urlset>\n"
        )
        self.assertEqual(build_catalog.render_sitemap(payload, "https://exemple.test/"), expected)
        # Idempotent vis-à-vis du slash final de --base-url.
        self.assertEqual(build_catalog.render_sitemap(payload, "https://exemple.test"), expected)

    def test_tri_antichronologique_puis_titre(self) -> None:
        self.add_book("ancien", book_html({"book:title": "Zèbre"}), mtime=1_700_000_000)
        self.add_book("recent", book_html({"book:title": "Autruche"}), mtime=1_800_000_000)
        self.add_book("jumeau", book_html({"book:title": "Élan"}), mtime=1_700_000_000)
        payload = self.generate()
        # Le plus récent d'abord ; à date égale, tri par titre insensible aux accents.
        self.assertEqual([book["id"] for book in payload["books"]], ["recent", "jumeau", "ancien"])


class TestOr(unittest.TestCase):
    """Test d'or : le script reproduit le catalog.json committé du dépôt réel."""

    def test_regeneration_reproduit_le_catalogue_committe(self) -> None:
        committed_path = ROOT / "catalog.json"
        if not committed_path.is_file():
            self.skipTest("catalog.json absent (dépôt incomplet)")
        committed = json.loads(committed_path.read_text(encoding="utf-8"))

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "catalog.json"
            # Copie préalable : generated_at conserve l'horodatage si la liste
            # des livres n'a pas changé — c'est aussi ce que fait la CI.
            output.write_text(committed_path.read_text(encoding="utf-8"), encoding="utf-8")
            with captured_stderr():
                payload = build_catalog.generate(ROOT, output)

        # Un clone shallow tronque les dates d'ajout git et fausse l'ordre :
        # dans ce cas on ne compare que le contenu, pas l'ordre.
        shallow = (ROOT / ".git" / "shallow").is_file()
        sort_key = (lambda books: sorted(books, key=lambda book: book["id"])) if shallow else (lambda books: books)
        self.assertEqual(payload["schemaVersion"], committed["schemaVersion"])
        self.assertEqual(payload["bookCount"], committed["bookCount"])
        self.assertEqual(sort_key(payload["books"]), sort_key(committed["books"]))
        if not shallow:
            self.assertEqual(payload["generatedAt"], committed["generatedAt"])


if __name__ == "__main__":
    unittest.main()
