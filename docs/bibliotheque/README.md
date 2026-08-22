# Rôle Bibliothèque — design & développement de la plateforme

Tu conçois et développes la **plateforme** qui héberge et affiche les livres.
Prérequis : avoir lu [`AGENTS.md`](../../AGENTS.md) (règles d'or + protocole de
session). Le cap du rôle — vision produit, paliers, chantiers priorisés — vit dans
[`VISION.md`](VISION.md) et [`ROADMAP.md`](ROADMAP.md) : tout chantier de plateforme
s'y rattache.

## Périmètre du rôle

- `index.html` — la page d'accueil (catalogue, recherche, filtres, tri) ;
- `scripts/build_catalog.py` — le générateur de `catalog.json` ;
- `.github/workflows/catalog.yml` — la CI (vérification en PR, régénération sur `main`) ;
- le traitement des couvertures (résolution, formats, placeholder) ;
- cette documentation.

**Hors périmètre** : le contenu de `livres/` — écrire ou modifier un livre relève du
rôle Production ([`ateliers/`](../../ateliers/README.md)) ; inventer un nouveau
format relève du rôle Conception ([`docs/conception/`](../conception/README.md)).

## Invariants (à ne jamais casser)

- **Autonomie d'`index.html`** : zéro dépendance externe (CDN, fonts distantes),
  HTML + CSS + JS dans le fichier unique.
- **Chemins relatifs** partout, sans slash initial ni domaine codé en dur (le site
  doit fonctionner à la racine d'un domaine comme dans un sous-répertoire Pages).
  Exception documentée : les métadonnées destinées aux robots et scrapers portent
  l'URL canonique absolue — voir [`FRONTEND.md`](FRONTEND.md) §Évolution pour la
  liste des fichiers concernés.
- **Injection DOM sûre** : `textContent` uniquement, jamais de HTML construit depuis
  les données du catalogue.
- **Une seule balise** `<script id="demo-catalog" type="application/json">` dans
  `index.html` — le script de génération échoue (`DemoBlockError`) s'il en trouve
  zéro ou plusieurs.
- **Contrat de sortie du générateur** : le schéma de `catalog.json` est documenté
  dans [`CATALOGUE.md`](CATALOGUE.md) ; l'index valide chaque entrée et ignore les
  entrées invalides.
- **Interface CLI du script** : les options `--root`, `--output`,
  `--sync-demo-catalog`, `--index`, `--sitemap`, `--base-url` sont utilisées par
  la CI — ne pas les casser.
- **Déclencheurs de `catalog.yml`** : les chemins surveillés (`livres/**`,
  `couvertures/**`, `scripts/**`, `index.html`, `catalog.json`, plus `tests/**`
  et `sitemap.xml` côté pull request) conditionnent tout le fonctionnement
  automatique.

## Interdits spécifiques

- Ne jamais committer une régénération de `catalog.json` ou du bloc `#demo-catalog` :
  c'est le travail du bot après merge (règles d'or 1 et 2 d'`AGENTS.md`).
- Toute modification **incompatible** du schéma du catalogue exige d'incrémenter
  `schemaVersion` et de mettre à jour de façon coordonnée le validateur JavaScript
  d'`index.html` (voir [`FRONTEND.md`](FRONTEND.md) §Évolution).
- Ne pas coder de cartes de livres en dur dans le HTML : faire évoluer le générateur.

## Comment tester

Prérequis : Python ≥ 3.10 (syntaxe du script), 3.12 en CI. Aucune dépendance
externe — bibliothèque standard uniquement, pour les scripts comme pour les tests.

1. **Tests unitaires du générateur** (la CI les exécute sur chaque pull request) :
   ```bash
   python -m unittest discover -s tests
   ```
2. **Génération à blanc** (obligatoire avant PR) :
   ```bash
   python scripts/build_catalog.py --output /tmp/catalog-verification.json
   ```
   Pour tester aussi la synchronisation du bloc demo et le sitemap sans toucher
   aux fichiers réels :
   ```bash
   cp index.html /tmp/index-verification.html
   python scripts/build_catalog.py --output /tmp/catalog-verification.json \
     --sync-demo-catalog --index /tmp/index-verification.html \
     --sitemap /tmp/sitemap-verification.xml \
     --base-url "https://pierrebillet.github.io/ma-bibliotheque/"
   ```
3. **Prévisualisation** : ouvrir `index.html` en `file://` (utilise le bloc
   `#demo-catalog`) puis via un serveur HTTP local (`python -m http.server`, utilise
   `catalog.json`) — les deux chemins de chargement doivent fonctionner.
4. **CI** : sur la PR, relire les annotations du job `verification`.

## Sommaire du dossier

| Document | Contenu |
|---|---|
| [`VISION.md`](VISION.md) | Vision produit : but, hiérarchie des directions, principes durables, paliers (1.0 → 1.x → PWA → comptes) avec critères de passage |
| [`ROADMAP.md`](ROADMAP.md) | Chantiers priorisés vers la 1.0 et au-delà, avec niveau d'architecture et statut |
| [`FRONTEND.md`](FRONTEND.md) | Fonctionnement d'`index.html` : chargement, validation, fonctionnalités, règles d'évolution |
| [`AUTOMATISATION.md`](AUTOMATISATION.md) | La chaîne CI de bout en bout : déclencheurs, déroulé d'un run, diagnostic des 4 pannes types |
| [`CATALOGUE.md`](CATALOGUE.md) | Le schéma de `catalog.json` champ par champ, les règles d'extraction, le bloc `#demo-catalog` |
