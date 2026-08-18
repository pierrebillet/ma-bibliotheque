# Frontend — Ma Bibliothèque HTML

## Fichiers

- `index.html` : page complète, autonome, sans framework ni dépendance externe. Le HTML, le CSS et le JavaScript sont réunis dans ce fichier.
- `favicon.svg`, `og-image.png`, `404.html`, `robots.txt`, `.nojekyll` : hygiène web (chantier 1 de la roadmap). `404.html` est servie par GitHub Pages pour toute URL inexistante ; `og-image.png` (1200 × 630) est l’image de partage social de l’index.
- `a-propos.html` : page « à propos » (chantier 8 de la roadmap) — le récit du projet (quel modèle a écrit quoi, fabrication des livres, contribution). Page statique autonome, sans JavaScript, reliée depuis le pied de page de l’index et référencée dans le sitemap généré.
- `sitemap.xml` : généré par la CI après chaque merge sur `main` (comme `catalog.json`) — ne pas l’éditer à la main, la CI rejette les pull requests qui le modifient.
- `catalog.json` : le catalogue réel du site, conforme au schéma version 3, régénéré automatiquement par le workflow (ne pas l’éditer à la main). Une copie de secours est inlinée dans `index.html` (bloc `#demo-catalog`, utilisé uniquement en `file://`) ; cette copie est régénérée automatiquement par le workflow en même temps que `catalog.json` — ne jamais l’éditer à la main, la CI rejette les pull requests qui la modifient.
- `couvertures/` et `livres/` : ressources facultatives incluses dans le paquet de prévisualisation pour que les images et les liens de démonstration fonctionnent localement.

## Fonctionnement de `index.html`

Au chargement, la page appelle :

```js
fetch("catalog.json", { cache: "no-store" })
```

Le chemin est relatif : le site fonctionne à la racine d’un domaine, dans un sous-répertoire GitHub Pages ou derrière un domaine personnalisé.

Le catalogue est validé légèrement avant affichage : version du schéma, tableau `books`, cohérence de `bookCount`, identifiants, titres et chemins relatifs sûrs. Les contenus sont injectés dans le DOM avec `textContent`, jamais comme HTML.

Les champs qualitatifs des schémas v2 et v3 sont lus **défensivement** : `nature` absente ou
vide vaut `fiction` ; `genre`, `format`, `tonalite`, `exigence` et `audience` doivent
être des chaînes non vides d’au plus 40 caractères, sinon `null` (aucun vocabulaire
n’est imposé côté client, la liste fermée est l’affaire du générateur) ; `variantOf`
doit être un slug de la même forme que `id`, sinon `null` ; `wordCount` et
`readingMinutes` doivent être des entiers strictement positifs, sinon `null` ;
`capabilities` doit être un tableau — ses libellés sont filtrés comme les autres
(chaîne non vide d’au plus 40 caractères), dédupliqués et bornés à huit, sinon le
tableau est vide. Une entrée v2 (champ `capabilities` absent) traverse donc le
validateur sans erreur.

La page fournit :

- recherche insensible à la casse et aux accents, avec logique ET entre les termes ;
- recherche dans le titre, l’auteur, la description, les tags, l’identifiant, ainsi
  que la nature, le genre, la tonalité et les capacités déclarées ;
- onglets de nature construits dynamiquement à partir des natures réellement
  présentes (« Tout » d’abord, puis `fiction`, puis les autres par ordre
  alphabétique), avec compteurs calculés sur le catalogue entier et donc
  indépendants des autres filtres ; le bloc reste masqué tant qu’il n’y a qu’une
  seule nature au catalogue — cas d’une bibliothèque entièrement composée de
  fictions ;
- filtre par genre et filtre par tag ;
- tris par date, titre ou auteur ;
- badges par carte, en deux temps. **Ce que le livre est** : durée de lecture
  (`« 25 min »` en dessous d’une heure, `« ≈ 2 h 30 »` au-delà, reste arrondi aux
  5 minutes), mention `illustré` pour les livres au format illustré, et la nature
  quand elle diffère de `fiction` — la fiction étant la norme du catalogue, on ne
  l’étiquette pas. Puis **ce qu’il fait** : ses capacités interactives déclarées
  (schéma v3 — `codex`, `carte`, `relations`, `choix`, `audio`), dans l’ordre du
  vocabulaire fermé, en trait pointillé (`.badge-capability`) pour les distinguer
  d’un coup d’œil des premiers ; leur `title` est explicite (« Contient : carte »).
  Un livre sans capacité déclarée n’affiche simplement aucun badge de ce type ;
- mention d’édition dérivée (`variantOf`) sous l’auteur : « Autre édition de
  « TITRE » », titre résolu depuis le catalogue chargé (repli : slug humanisé) ;
  texte simple, jamais un lien, pour préserver la règle du lien unique par carte ;
- paramètres partageables `q`, `nature`, `genre`, `tag` et `sort` ; `nature` et
  `genre` sont validés après chargement contre les valeurs réellement présentes,
  comme `tag` : une valeur inconnue est ignorée et retirée de l’URL ;
- couvertures réelles avec remplacement automatique en cas d’erreur ;
- placeholder stable calculé par FNV-1a à partir de `id + "\n" + title` ;
- ouverture des livres dans un nouvel onglet, par un **lien unique par carte** :
  le lien du titre, étendu à toute la surface de la carte par un pseudo-élément
  (le bouton « Lire » est décoratif, le bouton de copie reste un contrôle distinct) ;
- copie de l’URL absolue de chaque livre ;
- selects custom (genre, tag, tri) conformes au motif ARIA listbox : le focus reste
  sur la liste, l’option active est désignée par `aria-activedescendant` ;
- onglets de nature bâtis sur des `input[type=radio]` natifs visuellement masqués
  et leurs `label` stylés en segmented control : l’état, la navigation clavier et
  l’annonce sont ceux du contrôle natif, seul l’habillage change ;
- annonce du nombre de résultats aux lecteurs d’écran (`aria-live` porté par le
  seul décompte, pas par la barre entière) ;
- repli sans JavaScript : le bloc `<noscript>` pointe vers `catalog.json` pour
  retrouver les URL publiques des livres ;
- états de chargement, catalogue vide, aucun résultat et erreur ;
- mode sombre automatique, navigation clavier et réduction des animations.

## Feuille de style

Le CSS d’`index.html` est une **couche unique** depuis le chantier 2 de la roadmap
(2026-08-17) : les quatre refontes empilées (~600 lignes mortes mais téléchargées
et évaluées — audit §C.3.2) ont été remplacées par leur rendu final consolidé.
Pour le faire évoluer : **modifier les règles en place**, jamais rempiler une
nouvelle couche qui surcharge l’ancienne.

**Barre de filtres : quatre colonnes** depuis le chantier 5 (schéma v2) —
recherche, genre, tag, tri. Sous 48 rem la grille passe à deux colonnes : la
recherche prend la première rangée entière, genre et tag se partagent la
deuxième, le tri occupe la troisième plutôt que de laisser une cellule
orpheline ; sous 34 rem tout s’empile en une colonne. Les onglets de nature sont
posés **au-dessus** de la grille, hors de la barre : ils partitionnent le
catalogue là où les selects le filtrent.

**Ratio des cartes : 2:3** (tranché au même chantier, audit §C.3.4). Les cartes de
la galerie adoptent le ratio des couvertures — 2:3, la convention du dépôt
(`AGENTS.md`) — au lieu du 4:5 qui rognait ~17 % de chaque image. Une couverture
produite par un atelier s’affiche donc entière, sans recadrage (`object-fit: cover`
sur des ratios identiques). Si une future direction artistique veut un autre ratio,
c’est le format des couvertures qu’il faudra faire évoluer avec elle, pas l’un sans
l’autre.

## Prévisualisation locale

Les navigateurs bloquent généralement `fetch()` entre fichiers ouverts avec le protocole `file://`. Pour permettre l’ouverture directe de `index.html`, le fichier contient une copie intégrée du catalogue de démonstration, utilisée uniquement lorsque le chargement échoue sous `file://`.

Sur GitHub Pages ou tout serveur HTTP, `catalog.json` reste la source effective. La copie intégrée est ignorée dès que le `fetch()` réussit.

Cette copie est synchronisée automatiquement après chaque merge sur `main` (`scripts/build_catalog.py --sync-demo-catalog`). Son JSON peut différer de `catalog.json` par un seul détail : les séquences `</` y sont échappées en `<\/` pour rester valides dans une balise `<script>` (équivalent strict après `JSON.parse`).

## Format attendu de `catalog.json`

Le fichier suit le schéma version 3, documenté champ par champ dans
[`CATALOGUE.md`](CATALOGUE.md). Exemple minimal :

```json
{
  "schemaVersion": 3,
  "generatedAt": "2026-07-12T09:30:00Z",
  "bookCount": 1,
  "books": [
    {
      "id": "mon-livre",
      "filename": "mon-livre.html",
      "sourcePath": "livres/mon-livre.html",
      "href": "livres/mon-livre.html",
      "title": "Mon livre",
      "author": null,
      "description": null,
      "tags": [],
      "nature": "fiction",
      "genre": null,
      "format": null,
      "tonalite": null,
      "exigence": null,
      "audience": null,
      "date": null,
      "datePrecision": null,
      "variantOf": null,
      "capabilities": [],
      "wordCount": null,
      "readingMinutes": null,
      "cover": null
    }
  ]
}
```

**Versions acceptées : 2 et 3.** L’index refuse toute autre valeur de
`schemaVersion`, mais accepte la version courante *et* la précédente. Ce n’est pas
du confort : entre le merge d’une pull request qui fait évoluer le schéma et le
commit du bot qui régénère `catalog.json` et le bloc `#demo-catalog`, le site sert
une page déjà en v3 avec un catalogue encore en v2. Refuser v2 afficherait une
bibliothèque vide pendant toute cette fenêtre. Sur un catalogue v2, le champ v3
manquant retombe sur sa valeur par défaut (`capabilities` = tableau vide) : aucun
badge de capacité n’apparaît, le reste de la page fonctionne à l’identique.

Corollaire pour la suite : tout champ ajouté en v*N* doit être lu défensivement
tant que la v*N-1* est acceptée, et la liste des versions supportées
(`SCHEMA_VERSIONS` dans `index.html`) glisse d’un cran à chaque incrément — jamais
plus de deux versions à la fois.

Les couvertures utilisent un objet `cover` dont le champ `href` pointe vers `couvertures/<slug>.webp`, `.avif`, `.png`, `.jpg` ou `.jpeg` — ou, pour une couverture embarquée, vers `livres/<slug>/cover.*` ou `livres/<slug>/images/cover.*` (le validateur accepte les préfixes `couvertures/` et `livres/`). En l’absence de couverture, la valeur doit être `null`.

## Évolution

- Ne pas coder de nouvelles cartes directement dans le HTML : faire évoluer le générateur de `catalog.json`.
- Conserver les chemins relatifs, sans slash initial ni domaine codé en dur — **à une exception près** : les métadonnées destinées aux robots et scrapers exigent des URL absolues et portent donc l’URL canonique du site (`https://pierrebillet.github.io/ma-bibliotheque/`). Elle apparaît dans exactement quatre fichiers versionnés : le `<head>` d’`index.html` (canonical + Open Graph/Twitter), le `<head>` d’`a-propos.html` (idem), `robots.txt` (ligne `Sitemap:`) et `404.html` (lien de retour et favicon, la page étant servie à n’importe quelle profondeur d’URL). En cas de fork ou de changement de domaine : `grep -rl "pierrebillet.github.io" --include="*.html" --include="*.txt" .` puis remplacer. Le `sitemap.xml` généré n’est pas concerné : la CI dérive son URL de base du dépôt courant (`GITHUB_REPOSITORY`).
- Le chargement des ressources (fetch du catalogue, couvertures, liens des cartes) reste, lui, strictement relatif.
- Conserver l’injection par API DOM sûres et `textContent`.
- Toute modification incompatible du catalogue exige une nouvelle `schemaVersion` et une mise à jour coordonnée du validateur JavaScript, qui doit continuer d’accepter la version précédente le temps de la fenêtre entre le merge et la régénération par la CI.
- Le catalogue de démonstration intégré peut être régénéré depuis `catalog.json` pour maintenir la prévisualisation locale ; il n’intervient pas dans le fonctionnement publié.
