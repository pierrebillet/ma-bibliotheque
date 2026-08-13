# CLAUDE.md

Le point d'entrée des agents est [`AGENTS.md`](AGENTS.md) — le lire avant toute
modification : il route vers la documentation de chaque rôle (Bibliothèque,
Conception, Production). Rappels critiques :

- **Ne jamais éditer `catalog.json`** ni le bloc `#demo-catalog` de `index.html` :
  les deux sont régénérés par la CI après chaque merge sur `main`, et la CI rejette
  toute pull request qui les modifie.
- **Protocole de session** (détaillé dans `AGENTS.md`) : branche dédiée dès le début,
  commits d'étapes en français, **pull request systématique en fin de session**,
  jamais de push sur `main`.
- Slug de livre en kebab-case ASCII ; vérification locale :
  `python scripts/build_catalog.py --output /tmp/catalog-verification.json`.
- `book:author` = nom du modèle qui écrit (ex. `Claude Fable`), pas de pseudonyme
  collectif.
- Docs : `AGENTS.md` route par rôle ; les anciennes `SPEC.md`/`CONVENTIONS.md`/
  `ROADMAP.md` sont archivées dans `docs/archives/` — ne plus les suivre.
