# TRONC-COMMUN.md — le tronc commun des ateliers du moteur « Atelier »

Référence partagée par tous les ateliers qui produisent leurs livres avec le
moteur [`livres/_template/`](../livres/_template/README.md) (aujourd'hui :
`roman-atelier`, `reportage`). Chaque `WORKFLOW.md` concerné **référence ce
document au lieu de le recopier** — même principe que le socle éditorial
[`PREFERENCES.md`](../docs/conception/PREFERENCES.md) — et ne le contredit
jamais ; une évolution du tronc commun s'applique à tous ces ateliers dès leur
prochaine production.

Ce document ne décrit **aucune étape de fabrication** : les étapes, leurs
critères de fin et leurs commits restent dans la recette de chaque atelier. Il
rassemble ce qui est identique d'un atelier à l'autre : la mise en place, les
conventions de fichiers, le `<head>`, les vocabulaires, le moteur, les images
générées, la vérification outillée et les interdits communs.

## Mise en place (début de session Production)

1. **Recevoir le brief** : le message de lancement contient le `BRIEF.md` de
   l'atelier, rempli. S'il manque, le demander ; s'il est incomplet, les
   défauts indiqués champ par champ dans le gabarit s'appliquent (ils viennent
   du `WORKFLOW.md` de l'atelier et du socle `PREFERENCES.md`).
2. **Choisir le slug** : celui du brief, ou à défaut le proposer — kebab-case
   ASCII (`les-brumes-du-port`), définitif : URL, couverture et clé
   localStorage en dépendent.
3. **Copier le moteur** :
   ```bash
   mkdir -p livres/<slug>/images
   cp livres/_template/index.html livres/<slug>/index.html
   ```
   Ne copier ni `README.md` ni `DONNEES.md`. Le `<script>` du moteur ne se
   modifie pas (toute divergence est signalée dans la PR) ; la palette CSS
   (variables de `:root` et `[data-theme="dark"]`) peut être adaptée à
   l'univers du livre.
4. **Créer la branche** : `atelier/<nom-court>-<slug>` selon la convention du
   `WORKFLOW.md` de l'atelier (ex. `atelier/roman-<slug>`,
   `atelier/reportage-<slug>`) — protocole de session d'`AGENTS.md`.
5. **Traçabilité de l'entrée** : le brief reçu est recopié **tel quel** en
   `livres/<slug>/brief.md` à la première étape de la recette.

## Structure de fichiers

Un livre du moteur « Atelier » est **toujours un dossier** :

```text
livres/<slug>/
  index.html          ← point d'entrée (obligatoirement index.html)
  brief.md            ← le brief d'entrée, recopié tel quel
  recherche.md        ← le dossier documentaire sourcé (si la recette de
                        l'atelier le prévoit)
  illustrations.md    ← le manifeste pour l'agent illustrateur (si la recette
                        prévoit une passe d'illustrations générées)
  images/             ← les images du livre (générées et/ou documents du web)
```

- Profondeur maximale : **un seul niveau** de dossier sous `livres/`.
- Toutes les ressources du livre restent **dans son dossier** ; la couverture,
  elle, vit dans `couvertures/<slug>.webp`.

## Le `<head>` obligatoire

Le template en contient un gabarit prêt à remplacer. Pour référence (les 11
meta `book:*` alimentent le catalogue ; `reader-engine` trace le moteur) :

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Métadonnées utilisées par Ma Bibliothèque -->
  <meta name="book:title" content="Titre complet du livre">
  <meta name="book:author" content="Claude Fable">
  <meta
    name="book:description"
    content="Résumé en une ou deux phrases (≤ 600 caractères), destiné à la carte du catalogue."
  >
  <meta name="book:tags" content="thème, lieu, motif (2 à 4 tags, séparés par des virgules)">
  <meta name="book:date" content="2026-08-21">

  <!-- Metas qualitatives (vocabulaires fermés, voir ci-dessous) -->
  <meta name="book:genre" content="anticipation">
  <meta name="book:format" content="illustré">
  <meta name="book:tonalite" content="douce-amère">
  <meta name="book:exigence" content="intermédiaire">
  <meta name="book:audience" content="ados et adultes">

  <!-- Capacités interactives réellement offertes (vocabulaire fermé, liste) -->
  <meta name="book:capacites" content="codex">

  <!-- Recette (lue par le générateur : elle en dérive la nature) et moteur -->
  <meta name="book:workflow" content="<nom-atelier> v<N>">
  <meta name="reader-engine" content="atelier-liseuse v3">

  <!-- Utilisé par l'onglet du navigateur et comme fallback de titre -->
  <title>Titre complet du livre</title>
</head>
```

- **`book:author` = le nom du ou des modèles** (`Claude Fable`, `GPT 5.5`,
  `Gemini 3.1 pro`…). **Pas de pseudonyme collectif** — cette dérive a effacé
  la provenance de la moitié du catalogue (audit §B.6). Pour un livre
  multi-agents, le champ liste les rôles : « <modèle auteur> (texte),
  <modèle illustrateur> (images) » — chacun écrit sa part pendant sa passe.
- `book:date` : `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`.

## Les cinq metas qualitatives et les capacités (vocabulaires fermés)

Elles sont **obligatoires** et n'acceptent que les valeurs ci-dessous, à la
graphie exacte (accents compris). Source de vérité :
[`docs/bibliotheque/CATALOGUE.md`](../docs/bibliotheque/CATALOGUE.md) — s'y
reporter en cas de doute, et n'inventer aucune valeur : une valeur hors
vocabulaire est un défaut bloquant du vérificateur. Un seul terme par meta,
celui qui décrit le mieux le livre dans son ensemble.

| Meta | Valeurs admises |
|---|---|
| `book:genre` | `science-fiction`, `fantasy`, `fantastique`, `anticipation`, `espionnage`, `policier`, `aventure`, `comédie dramatique`, `drame`, `histoire`, `société`, `sciences`, `portrait` |
| `book:format` | `texte`, `illustré` |
| `book:tonalite` | `lumineuse`, `douce-amère`, `contemplative`, `ironique`, `tendue`, `sombre` |
| `book:exigence` | `accessible`, `intermédiaire`, `exigeante` |
| `book:audience` | `tout public`, `ados et adultes`, `adultes` |
| `book:capacites` | `codex`, `carte`, `relations`, `choix`, `audio` — **liste** séparée par des virgules |

- `book:capacites` déclare **ce que le livre fait** en plus de dérouler son
  texte. Un livre du moteur « Atelier » a toujours un codex : `codex` au
  minimum (le vérificateur en fait un défaut bloquant si l'îlot porte un codex
  non déclaré). Ajouter `carte`, `relations`, `choix` ou `audio` **seulement
  si le livre les offre réellement** — une capacité annoncée et absente est
  pire qu'un badge manquant. Le vérificateur exige la capacité dès que l'îlot
  porte le module correspondant. Les illustrations et documents ne sont pas
  une capacité : `book:format` le dit déjà.
- Les `book:tags` restent **libres et complémentaires** (thème, lieu, motif)
  mais gouvernés : **2 à 4 tags**, jamais une valeur de vocabulaire fermé
  (`genre`, `format`, `tonalite`, `exigence`, `audience`) ni une nature
  (`fiction`, `reportage`), jamais une étiquette de manière (`récit
  littéraire`, `exploration documentaire`) ou d'édition (`édition illustrée`).
  Le vérificateur en fait un défaut bloquant et le générateur écarte le tag
  fautif. Règle complète :
  [`docs/bibliotheque/CATALOGUE.md`](../docs/bibliotheque/CATALOGUE.md)
  §Gouvernance des tags.
- Rien à renseigner pour la longueur : `wordCount` et le temps de lecture sont
  **calculés** par `scripts/build_catalog.py` à partir de l'îlot JSON.

## La nature du livre : dérivée, jamais déclarée

Le catalogue range les livres par `nature` (`fiction` ou `reportage`), mais
**aucune meta ne la porte** : `scripts/build_catalog.py` la déduit du nom
d'atelier lu dans `book:workflow` (le contenu sans son suffixe ` vN`) via sa
table `ATELIER_NATURE`. Renseigner
`<meta name="book:workflow" content="<nom-atelier> v<N>">` suffit donc à
ranger le livre du bon côté — et c'est aussi ce qui trace la version de
recette utilisée (la PR de production la mentionne aussi). Une meta absente ou
un atelier inconnu de la table retombent sur `fiction`.

## `book:variant-of` (optionnelle, cas rare)

Réservée aux **éditions dérivées** : un livre qui est une autre édition d'un
livre déjà publié déclare le slug de ce livre source
(`<meta name="book:variant-of" content="lequation-du-calme">`), ce qui permet
au catalogue de les regrouper au lieu de les afficher en doublon. Le slug doit
exister sous `livres/` (`<slug>.html` ou dossier `<slug>/`) et ne peut pas
être celui du livre lui-même. **Ne pas l'utiliser pour créer un doublon** : le
moratoire sur les éditions dérivées (§« Interdits communs ») reste en vigueur.
Un livre ordinaire n'a pas cette meta.

## Le moteur de liseuse

- **Source unique** : [`livres/_template/index.html`](../livres/_template/index.html)
  (`atelier-liseuse v3`), copié tel quel — plus jamais depuis le dernier livre
  publié. Les trois défauts historiques du moteur (audit §B.4 : `close()`
  écrasé, `entry()` sans garde, recherche du codex) y sont corrigés — ne pas
  les réintroduire en copiant un ancien livre.
- **Données** : le récit vit dans l'îlot
  `<script type="application/json" id="book-data">`, dont la structure est
  spécifiée champ par champ dans
  [`livres/_template/DONNEES.md`](../livres/_template/DONNEES.md).
- **Persistance** : la clé localStorage `<slug>-state-v1` est dérivée de
  `meta.slug` par le moteur — renseigner `meta.slug` correctement suffit.
- **Modules optionnels** (v3) : les blocs `map` et `relations` de l'îlot
  ajoutent une carte des lieux et un graphe de relations, avec leur bouton de
  barre, leur entrée de sommaire et leur équivalent textuel (étape
  conditionnelle de chaque recette). Absents de l'îlot, ils n'existent pas
  pour le lecteur : c'est le défaut — **supprimer les blocs `map` et
  `relations` hérités de l'îlot d'exemple du template** quand le brief ne les
  demande pas.
- **Impression** (v3) : la vue affichée s'imprime sans le mobilier de la
  liseuse — rien à faire, mais ne pas casser la feuille `@media print` en
  adaptant la palette.
- **Fonctionnalités à ne pas régresser** : sommaire, `role="progressbar"` mis
  à jour, codex à déverrouillage robuste au rechargement, thème sombre, taille
  de police, piège de focus dans les dialogues, région `aria-live` pour les
  déblocages, `prefers-reduced-motion`, échappement HTML systématique des
  données de l'îlot, visionneuse d'images, dégradation propre des images
  manquantes, impression propre, et — si le brief les demande — carte et
  graphe de relations à révélation progressive.

## Images générées et couverture

(Les **documents du web** — images sourcées du réel — ont leurs propres
règles dans la recette de l'atelier qui les autorise.)

- **Format** : **WebP** pour tout (chapitres, notices, couverture). JPEG
  toléré en repli si la chaîne de l'illustrateur ne produit pas de WebP — le
  signaler dans la PR.
- **Couverture obligatoire** : `couvertures/<slug>.webp`, ratio **2:3**
  (cible : 800×1200), poids **< 300 Ko**. Le nom doit être **exactement** le
  slug, sinon elle est ignorée en silence et un placeholder est généré. Son
  image ne contient **aucun texte**, sans exception : ni titre, sous-titre,
  nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre et les
  métadonnées sont ajoutés par-dessus en HTML dans la bibliothèque.
- **Images de chapitre** : `livres/<slug>/images/chapter-NN.webp` (NN = numéro
  du chapitre sur 2 chiffres), **1600×900**, poids **≤ 150 Ko**.
- **Images de notice** : `livres/<slug>/images/codex-<id>.webp` (id = id exact
  de la notice), **1600×900**, poids **≤ 150 Ko**.
- Le moteur pose `width`/`height` (1600×900 par défaut) et `loading="lazy"`
  hors première image ; si une image déroge aux dimensions, renseigner
  `imageWidth`/`imageHeight` dans l'îlot.
- Les `alt` sont écrits par l'**auteur** et vivent dans l'îlot — pas par
  l'illustrateur.
- Conversion/compression (commandes de référence, reprises dans le manifeste
  d'illustrations) :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou, si seul ImageMagick est disponible :
  magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```

## Vérification outillée

Deux outils, à lancer depuis la racine du dépôt :

- **Le vérificateur du moteur** —
  [`livres/_template/outils/verifier.py`](../livres/_template/outils/verifier.py) :
  ```bash
  python livres/_template/outils/verifier.py livres/<slug> [--sans-images]
  ```
  Il contrôle le `<head>` (11 metas, vocabulaires fermés, gouvernance des
  tags), l'intégrité du codex, la clé localStorage, les modules, la
  correspondance îlot ↔ manifeste et la conformité des images. `--sans-images`
  tolère les fichiers d'images pas encore produits (phase « texte d'abord »).
  Sortie : les **DÉFAUTS** (bloquants) puis les **AVERTISSEMENTS**.
- **Le générateur de catalogue** (règle d'or n° 6, exécuté à l'identique par
  la CI) :
  ```bash
  python scripts/build_catalog.py --output /tmp/catalog-verification.json
  ```

## Interdits communs

- **Moratoire sur les éditions dérivées en doublon** (`-v2`, `-illustree`) :
  ne pas créer une entrée de catalogue séparée pour une variante d'un livre
  existant — audit
  [`docs/audits/2026-08-rapport-etonnement.md`](../docs/audits/2026-08-rapport-etonnement.md) §D.
- Jamais toucher `catalog.json` ni le bloc `#demo-catalog` de l'`index.html`
  racine (règles d'or d'`AGENTS.md`).
- Aucune ressource distante (CDN, fonts, images externes) : l'autonomie du
  livre est une règle d'or.
- Le `<script>` du moteur copié ne se modifie pas ; seule la palette CSS
  s'adapte.
