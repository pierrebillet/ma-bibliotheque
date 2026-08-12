# CLAUDE.md

Le contrat de contribution complet est dans [`AGENTS.md`](AGENTS.md) — le lire avant
toute modification. Rappels critiques :

- **Ne jamais éditer `catalog.json`** ni le bloc `#demo-catalog` de `index.html` :
  le catalogue est régénéré par CI après merge sur `main`.
- **Tout passe par branche + pull request**, y compris les éditions illustrées.
- Slug de livre en kebab-case ASCII ; vérification locale :
  `python scripts/build_catalog.py --output /tmp/catalog-verification.json`.
- `book:author` = nom du modèle qui écrit (ex. `Claude Fable`), pas de pseudonyme
  collectif.
- Docs : `README.md` et `AGENTS.md` font foi ; `SPEC.md`/`CONVENTIONS.md`/`ROADMAP.md`
  sont partiellement obsolètes (encarts en tête).
