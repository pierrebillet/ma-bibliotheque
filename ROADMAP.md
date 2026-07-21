# Roadmap — Ma Bibliothèque HTML

Version : 1.0  
Point de départ : étape 1 terminée par la production de `SPEC.md`, `CONVENTIONS.md` et `ROADMAP.md`.

Chaque étape suivante doit utiliser les fichiers existants comme sources normatives. Aucun choix d’architecture ne doit être réouvert sans contradiction technique démontrée.

## Étape 2 — Site bibliothèque statique

### Objectif

Produire l’interface publique de la bibliothèque en HTML, CSS et JavaScript natifs. À ce stade, le site peut être testé avec un `catalog.json` temporaire, mais ce fichier temporaire ne fait pas partie du livrable final de l’étape.

### Fichiers exacts à produire

```text
.nojekyll
404.html
index.html
assets/css/library.css
assets/icons/favicon.svg
assets/js/library.js
couvertures/.gitkeep
livres/.gitkeep
```

### Contenu attendu

#### `.nojekyll`

Fichier vide désactivant Jekyll sur GitHub Pages.

#### `index.html`

Doit contenir :

- structure HTML5 sémantique ;
- titre et description de la bibliothèque ;
- champ de recherche ;
- sélecteur de tag ;
- sélecteur de tri ;
- compteur de résultats ;
- zone de grille ;
- états chargement, vide, aucun résultat et erreur ;
- bloc `<noscript>` ;
- lien vers la feuille de style ;
- script JavaScript chargé avec `defer` ;
- aucun livre codé en dur ;
- aucun chemin absolu dépendant du propriétaire ou du dépôt.

#### `assets/css/library.css`

Doit définir :

- variables CSS de thème ;
- layout responsive ;
- grille de cartes ;
- cadre de couverture au ratio 2:3 ;
- placeholder par gradient et motif SVG ;
- troncatures visuelles ;
- focus visible ;
- états de chargement et d’erreur ;
- styles adaptés au clavier et au tactile ;
- support `prefers-reduced-motion` ;
- contraste WCAG AA.

#### `assets/js/library.js`

Doit implémenter :

- chargement relatif de `catalog.json` avec `cache: "no-store"` ;
- validation légère du payload ;
- rendu sûr par DOM et `textContent` ;
- cartes et liens directs ;
- couverture réelle avec fallback sur erreur ;
- placeholder déterministe FNV-1a ;
- recherche insensible à la casse et aux accents ;
- filtre par tag ;
- trois tris normatifs ;
- paramètres `q`, `tag`, `sort` dans l’URL ;
- compteur et états vides ;
- absence de stockage local.

#### `404.html`

Doit :

- expliquer que la page demandée n’existe pas ;
- proposer un lien relatif vers la bibliothèque ;
- rester autonome et sans JavaScript obligatoire.

#### `assets/icons/favicon.svg`

Doit être :

- un SVG original ;
- lisible à petite taille ;
- sans police distante ;
- sans dépendance externe.

#### `livres/.gitkeep` et `couvertures/.gitkeep`

Maintiennent les dossiers vides dans Git avant l’ajout des premiers contenus.

### Vérifications de fin d’étape

- l’index fonctionne sous un chemin racine et sous un sous-chemin de type `/nom-du-depot/` ;
- le HTML, CSS et JavaScript ne comportent aucune dépendance externe obligatoire ;
- les liens livres sont des ancres directes ;
- le placeholder est stable pour une même graine ;
- les états d’erreur ne produisent jamais une page blanche ;
- le site reste utilisable à 320 px de largeur.

## Étape 3 — Automatisation GitHub Action

### Objectif

Produire la chaîne complète de validation, génération du catalogue, construction de l’artefact Pages et déploiement automatique.

### Fichiers exacts à produire

```text
.github/workflows/deploy-pages.yml
.gitignore
catalog.schema.json
scripts/build_site.py
scripts/generate_catalog.py
scripts/validate_project.py
tests/test_generate_catalog.py
```

### Contenu attendu

#### `.github/workflows/deploy-pages.yml`

Doit :

- se déclencher sur `push` vers `main` ;
- se déclencher sur `pull_request` vers `main` pour validation sans déploiement ;
- accepter `workflow_dispatch` ;
- utiliser Python 3.12 ;
- exécuter les tests unitaires ;
- exécuter `scripts/build_site.py` ;
- téléverser `_site/` avec l’action officielle Pages ;
- déployer uniquement hors pull request ;
- utiliser les permissions minimales `contents: read`, `pages: write`, `id-token: write` ;
- utiliser une concurrence de groupe `pages` avec annulation des déploiements obsolètes ;
- ne jamais committer `catalog.json` dans le dépôt.

#### `.gitignore`

Doit ignorer exactement les artefacts locaux ou CI non versionnés :

```text
_site/
__pycache__/
*.py[cod]
.DS_Store
```

#### `catalog.schema.json`

Doit formaliser le schéma version 1 décrit dans `SPEC.md` avec :

- `additionalProperties: false` à la racine et dans les objets ;
- types, enums et motifs de chemins ;
- cohérence des champs nullable ;
- motif du slug ;
- formats de date autorisés.

La validation JSON Schema peut être effectuée par le validateur interne du projet sans dépendance externe, sur le sous-ensemble de règles utilisé.

#### `scripts/generate_catalog.py`

Doit :

- utiliser uniquement la bibliothèque standard ;
- accepter au minimum `--root` et `--output` ;
- parcourir seulement `livres/*.html` au premier niveau ;
- appliquer toutes les règles d’encodage et d’extraction ;
- résoudre les couvertures ;
- produire des avertissements GitHub Actions ;
- trier les entrées de façon déterministe ;
- écrire le JSON UTF-8 indenté ;
- retourner un code non nul uniquement pour les erreurs bloquantes.

#### `scripts/validate_project.py`

Doit :

- contrôler la présence des fichiers indispensables ;
- valider les slugs et collisions ;
- détecter les couvertures orphelines et concurrentes ;
- vérifier les signatures d’images ;
- valider la structure de `catalog.json` ;
- vérifier `bookCount` ;
- vérifier que tous les chemins restent relatifs et sûrs ;
- produire des annotations lisibles dans GitHub Actions.

#### `scripts/build_site.py`

Doit :

- supprimer puis recréer `_site/` ;
- copier uniquement la liste blanche publique définie dans `SPEC.md` ;
- préserver les livres et couvertures octet pour octet ;
- appeler le générateur vers `_site/catalog.json` ;
- appeler le validateur sur le résultat ;
- échouer si un fichier public obligatoire manque ;
- ne jamais copier `.github/`, `scripts/`, `tests/`, les guides ou les spécifications.

#### `tests/test_generate_catalog.py`

Doit couvrir au minimum :

1. priorité `book:title` sur `<title>` ;
2. fallback `<title>` ;
3. fallback nom de fichier ;
4. fichier vide ;
5. HTML mal formé ;
6. métadonnées dupliquées ;
7. tags multiples et déduplication ;
8. dates aux trois précisions ;
9. date invalide ;
10. détection UTF-8 BOM ;
11. fallback Windows-1252 ;
12. priorité de couverture `webp`, `png`, `jpg` ;
13. couverture invalide ;
14. couverture orpheline ;
15. ordre déterministe des livres ;
16. rejet d’un slug invalide ;
17. sérialisation Unicode et saut de ligne final.

Les tests créent leurs fichiers temporaires pendant l’exécution et ne nécessitent aucun fixture binaire versionné.

### Vérifications de fin d’étape

- un push avec uniquement `livres/nouveau-livre.html` produit un nouveau déploiement ;
- le site publié contient `catalog.json` alors que le dépôt ne le versionne pas ;
- un pull request invalide échoue sans déployer ;
- une erreur de build laisse en ligne la dernière version valide ;
- les fichiers HTML copiés ont le même hash avant et après construction ;
- aucun paquet externe n’est installé.

## Étape 4 — Guides utilisateur

### Objectif

Documenter l’usage du projet uniquement par l’interface web GitHub, ainsi que la configuration initiale et les procédures de diagnostic.

### Fichiers exacts à produire

```text
README.md
guides/AJOUTER-UN-LIVRE.md
guides/AJOUTER-UNE-COUVERTURE.md
guides/DEPANNAGE.md
guides/METADONNEES.md
guides/PUBLIER-ET-PARTAGER.md
```

### Contenu attendu

#### `README.md`

Doit contenir :

- description synthétique du projet ;
- prérequis GitHub ;
- lien vers chaque guide ;
- procédure d’ajout en cinq étapes maximum ;
- rappel qu’un livre est un fichier HTML autonome ;
- rappel de ne jamais éditer `catalog.json` ;
- schéma bref du workflow ;
- emplacement des spécifications normatives.

#### `guides/AJOUTER-UN-LIVRE.md`

Doit expliquer, captures textuelles des boutons comprises :

- comment ouvrir `livres/` ;
- comment téléverser un fichier ;
- comment nommer le fichier ;
- comment committer sur `main` ;
- comment suivre l’action ;
- comment trouver l’URL publique ;
- comment remplacer ou supprimer un livre.

Aucune commande de terminal ne doit être proposée comme procédure principale ou alternative nécessaire.

#### `guides/AJOUTER-UNE-COUVERTURE.md`

Doit expliquer :

- correspondance exacte des noms ;
- formats acceptés ;
- priorité en cas de doublon ;
- ratio et dimensions ;
- fallback automatique ;
- remplacement et suppression.

#### `guides/METADONNEES.md`

Doit reprendre de façon opérationnelle :

- le bloc `<head>` copiable ;
- la priorité des titres ;
- le format des tags ;
- les formats de date ;
- les cas sans métadonnées ;
- des exemples avant/après dans `catalog.json`.

#### `guides/PUBLIER-ET-PARTAGER.md`

Doit couvrir :

- activation de GitHub Pages avec source GitHub Actions ;
- première exécution manuelle ;
- URL de site de projet ;
- URL de site utilisateur ;
- URL directe d’un livre ;
- domaine personnalisé comme option non requise ;
- délai de propagation et cache navigateur ;
- vérification du statut de déploiement.

#### `guides/DEPANNAGE.md`

Doit fournir un tableau symptômes → causes → corrections pour :

- livre absent du catalogue ;
- action rouge ;
- nom invalide ;
- couverture absente ;
- couverture non actualisée ;
- livre qui fonctionne localement mais pas sur Pages ;
- ressource externe bloquée ;
- `catalog.json` introuvable ;
- page 404 ;
- caractères mal encodés ;
- ancien contenu visible à cause du cache.

### Vérifications de fin d’étape

- une personne ne connaissant pas Git peut ajouter un livre via l’interface web ;
- tous les chemins et noms correspondent à l’arborescence réelle ;
- aucune étape ne demande un build local ;
- les guides ne contredisent ni `SPEC.md` ni `CONVENTIONS.md`.

## Étape 5 — Livre d’exemple et recette finale

### Objectif

Fournir un exemple réel, autonome et interactif, puis exécuter une recette d’acceptation complète du projet.

### Fichiers exacts à produire

```text
RECETTE.md
couvertures/livre-exemple.webp
livres/livre-exemple.html
```

### Contenu attendu

#### `livres/livre-exemple.html`

Doit être un fichier HTML autonome démontrant :

- structure HTML5 valide ;
- métadonnées `book:*` complètes ;
- titre navigateur ;
- CSS inline ;
- JavaScript inline ;
- lecture en plusieurs sections ou chapitres ;
- une interaction simple fonctionnant sans serveur ;
- navigation clavier ;
- responsive mobile ;
- absence de ressource externe ;
- absence de `localStorage` ;
- taille raisonnable permettant une inspection manuelle.

Le contenu doit être original et librement publiable.

#### `couvertures/livre-exemple.webp`

Doit :

- porter exactement le même slug ;
- être au ratio 2:3 ;
- mesurer idéalement 1200 × 1800 px ;
- être en sRGB ;
- peser moins de 2 Mio ;
- rester lisible sous forme de vignette.

#### `RECETTE.md`

Doit contenir une checklist exécutable couvrant :

1. configuration GitHub Pages ;
2. déploiement initial ;
3. présence du livre d’exemple ;
4. ouverture directe du livre ;
5. fonctionnement de son interaction ;
6. extraction de toutes les métadonnées ;
7. chargement de sa couverture ;
8. recherche par titre, auteur, description et tag ;
9. tris ;
10. paramètres d’URL de l’index ;
11. affichage mobile ;
12. navigation clavier ;
13. test d’un fichier sans `<title>` ;
14. test d’un HTML mal formé ;
15. test d’un livre sans couverture ;
16. test du fallback sur image cassée ;
17. test d’un slug invalide et vérification de l’échec du workflow ;
18. test d’une date invalide non bloquante ;
19. test d’une couverture orpheline ;
20. test d’une URL de projet avec sous-chemin ;
21. vérification que le dépôt ne contient ni `_site/` ni `catalog.json` versionné ;
22. vérification qu’un échec ne remplace pas le dernier déploiement valide.

Chaque ligne de recette doit comporter :

- précondition ;
- action ;
- résultat attendu ;
- emplacement de preuve ;
- case de validation.

### Critère de clôture du projet

L’étape 5 est terminée lorsque :

- tous les tests automatisés sont verts ;
- tous les cas obligatoires de `RECETTE.md` sont validés ;
- l’ajout d’un nouveau livre depuis l’interface GitHub ne nécessite que le dépôt d’un fichier HTML dans `livres/` ;
- le livre est publiquement accessible par une URL directe ;
- le catalogue est régénéré et déployé sans intervention manuelle.
