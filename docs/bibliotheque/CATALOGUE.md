# CATALOGUE.md — le schéma de `catalog.json`

`catalog.json` est le contrat d'interface entre le générateur
(`scripts/build_catalog.py`), la page d'accueil (`index.html`) et les livres. Ce
document fait foi pour le schéma version 2.

## Cycle de vie

- **Généré, jamais édité à la main.** Après chaque merge sur `main`, le job
  `catalogue` de la CI exécute `build_catalog.py --sync-demo-catalog`, commite
  `catalog.json` et le bloc `#demo-catalog` d'`index.html` en tant que
  `github-actions[bot]` (message `[skip ci]`), puis relance le build GitHub Pages.
- La CI **rejette** toute pull request qui modifie `catalog.json` ou le bloc
  `#demo-catalog`.
- `generatedAt` est conservé tel quel si la liste des livres n'a pas changé, pour
  éviter les commits de bruit.

## Schéma version 2

```json
{
  "schemaVersion": 2,
  "generatedAt": "2026-08-17T21:48:12Z",
  "bookCount": 13,
  "books": [
    {
      "id": "mon-livre",
      "filename": "index.html",
      "sourcePath": "livres/mon-livre/index.html",
      "href": "livres/mon-livre/index.html",
      "title": "Mon livre",
      "author": "Claude Fable",
      "description": "Résumé en une ou deux phrases.",
      "tags": ["haute couture", "Paris"],
      "nature": "fiction",
      "genre": "espionnage",
      "format": "texte",
      "tonalite": "ironique",
      "exigence": "accessible",
      "audience": "ados et adultes",
      "date": "2026-08-11",
      "datePrecision": "day",
      "variantOf": null,
      "wordCount": 13974,
      "readingMinutes": 70,
      "cover": {
        "filename": "mon-livre.webp",
        "sourcePath": "couvertures/mon-livre.webp",
        "href": "couvertures/mon-livre.webp",
        "format": "webp"
      }
    }
  ]
}
```

### Champs racine

| Champ | Type | Contenu |
|---|---|---|
| `schemaVersion` | entier | `2`. Toute rupture de compatibilité exige de l'incrémenter et de mettre à jour le validateur JS d'`index.html`. |
| `generatedAt` | chaîne | Horodatage UTC ISO 8601 de la génération. |
| `bookCount` | entier | Nombre d'entrées de `books` (vérifié par l'index). |
| `books` | tableau | Une entrée par livre, triée par date d'ajout Git décroissante, puis titre, puis id (clés insensibles aux accents). |

### Politique de version

Le validateur JS d'`index.html` accepte **la version courante et la précédente**.
Cette tolérance n'est pas du confort : entre le merge d'une pull request qui
incrémente `SCHEMA_VERSION` et le commit du bot qui régénère `catalog.json`, le
site sert un index déjà en v*N* avec un catalogue encore en v*N-1*. Refuser la
version précédente afficherait une bibliothèque vide pendant cette fenêtre.

Un champ ajouté en v*N* doit donc être lu défensivement côté index (absent ⇒ `null`)
tant que la version précédente est acceptée.

### Champs d'un livre

| Champ | Type | Contenu |
|---|---|---|
| `id` | chaîne | Le slug (`[a-z0-9]+(-[a-z0-9]+)*`), identifiant public et stable. Slug invalide = génération en erreur (exit 1). |
| `filename` | chaîne | Nom du fichier d'entrée (`mon-livre.html` ou `index.html`). |
| `sourcePath` / `href` | chaîne | Chemin relatif du point d'entrée depuis la racine du site, sans slash initial. |
| `title` | chaîne | Jamais vide (voir fallbacks ci-dessous). |
| `author` | chaîne ou `null` | Le **modèle** qui a écrit le livre (règle d'or d'`AGENTS.md`). |
| `description` | chaîne ou `null` | Texte brut, ≤ 600 caractères recommandés. |
| `tags` | tableau de chaînes | 2 à 4 **thèmes libres** (thème, lieu, motif, matière du sujet). Dédupliqués (insensible casse/accents), graphie de la première occurrence conservée. Un tag ne redit jamais un champ structuré : voir « Gouvernance des tags » ci-dessous. |
| `nature` | chaîne | **Toujours renseignée** : `fiction` ou `reportage`. Déduite de l'atelier (`book:workflow`), jamais d'un tag. Sépare romans et reportages à l'index. |
| `genre` | chaîne ou `null` | Vocabulaire fermé (voir ci-dessous). `null` si la meta est absente ou hors vocabulaire. |
| `format` | chaîne ou `null` | Vocabulaire fermé : `texte` ou `illustré`. |
| `tonalite` | chaîne ou `null` | Vocabulaire fermé. Couleur dominante du livre. |
| `exigence` | chaîne ou `null` | Vocabulaire fermé. Effort de lecture demandé, pas un jugement de valeur. |
| `audience` | chaîne ou `null` | Vocabulaire fermé. Lectorat visé. |
| `date` | chaîne ou `null` | `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ` ; valeur invalide ignorée avec avertissement. |
| `datePrecision` | chaîne ou `null` | `year`, `month` ou `day` selon la forme de `date`. |
| `variantOf` | chaîne ou `null` | Slug du livre **source** dont cette entrée est une édition dérivée (illustrée, remontée…). Permet de grouper les éditions au lieu de les empiler. `null` pour une œuvre originale. |
| `wordCount` | entier ou `null` | Nombre de mots du texte des chapitres. `null` si indéterminable (voir l'algorithme ci-dessous). |
| `readingMinutes` | entier ou `null` | Durée de lecture estimée, dérivée de `wordCount`. `null` si `wordCount` est `null`. |
| `cover` | objet ou `null` | `filename`, `sourcePath`, `href`, `format` (`webp`/`avif`/`png`/`jpg`/`jpeg`). `href` pointe vers `couvertures/<slug>.*` ou, en repli, vers la couverture embarquée `livres/<slug>/cover.*` ou `livres/<slug>/images/cover.*`. `null` si aucune couverture valide — l'index génère alors un placeholder déterministe (FNV-1a sur `id + "\n" + title`). |

## Vocabulaires fermés

Ce document est la **source de vérité** des cinq listes ci-dessous. Les graphies
sont exactes, accents compris : la comparaison est insensible à la casse et aux
diacritiques, mais c'est toujours la graphie canonique listée ici qui est écrite
dans `catalog.json`.

| Champ | Meta | Valeurs admises |
|---|---|---|
| `genre` | `book:genre` | `science-fiction`, `fantasy`, `fantastique`, `anticipation`, `espionnage`, `policier`, `aventure`, `comédie dramatique`, `drame`, `histoire`, `société`, `sciences`, `portrait` |
| `format` | `book:format` | `texte`, `illustré` |
| `tonalite` | `book:tonalite` | `lumineuse`, `douce-amère`, `contemplative`, `ironique`, `tendue`, `sombre` |
| `exigence` | `book:exigence` | `accessible`, `intermédiaire`, `exigeante` |
| `audience` | `book:audience` | `tout public`, `ados et adultes`, `adultes` |

Une valeur hors vocabulaire n'est **jamais** bloquante : le champ passe à `null` et
un avertissement listant les valeurs admises est émis. Un livre mal étiqueté reste
publié, simplement non filtrable sur ce critère.

**Règle de synchronisation.** Ces listes sont dupliquées à deux endroits :

- `scripts/build_catalog.py` (constantes `GENRES`, `FORMATS`, `TONALITES`,
  `EXIGENCES`, `AUDIENCES`) — ce qui est réellement écrit dans le catalogue ;
- `ateliers/roman-atelier/outils/verifier.py` — ce qui est refusé à l'écriture,
  avant même d'atteindre le catalogue.

Toute modification d'une liste se fait **dans le même commit aux trois endroits**.
Une divergence est silencieuse et coûteuse : le vérificateur laisserait passer une
valeur que le générateur jetterait ensuite sans que personne ne relise
l'avertissement.

## Gouvernance des tags

Les `tags` sont le **seul vocabulaire libre** du catalogue. Depuis le schéma v2, le
classement structuré est porté par `nature`, `genre` et `format` ; les tags n'ont
plus à le répéter. Chantier 6 de la [`ROADMAP.md`](ROADMAP.md).

**La règle, en une phrase** : un tag porte un **thème, un lieu, un motif ou une
matière de sujet** — jamais ce qu'un champ structuré dit déjà, jamais la manière
d'écrire, jamais l'édition.

- **2 à 4 tags par livre.** En dessous, le tag n'apporte rien ; au-dessus, le filtre
  de l'index se transforme en nuage.
- **Interdit : reprendre une valeur de vocabulaire fermé** (`genre`, `format`,
  `tonalite`, `exigence`, `audience`) **ou une nature** (`fiction`, `reportage`).
  Ces valeurs ont leur propre champ et leur propre filtre : `science-fiction`,
  `illustré` ou `reportage` en tag feraient doublon.
- **Interdit aussi : les étiquettes de manière et d'édition** — `récit littéraire`,
  `exploration documentaire`, `édition illustrée`, `récit spéculatif`. La manière
  relève de `tonalite` et `exigence`, l'édition de `format` et `variantOf`.
- **Écrire au singulier**, en minuscules, sauf pour un nom propre (`Paris`,
  `Tronçais`).

**Double contrôle, comme pour les vocabulaires fermés :**

- `scripts/build_catalog.py` (`RESERVED_TAG_VALUES`, `MAX_TAGS`) **écarte** du
  catalogue tout tag qui reprend une valeur structurée, avec un avertissement, et
  avertit au-delà de 4 tags. Non bloquant : le livre reste publié.
- `ateliers/roman-atelier/outils/verifier.py` (`TAGS_RESERVES`, `TAGS_MIN`,
  `TAGS_MAX`) en fait un **défaut bloquant** avant même l'écriture du livre.

L'assainissement des 13 livres publiés a été fait dans le même chantier : 39 tags
distincts ramenés à 28, aucun tag inventé — uniquement des retraits.

## Règles d'extraction (résumé du comportement réel du script)

- **Découverte** : `livres/*.html` de premier niveau + sous-dossiers de premier
  niveau (point d'entrée : `index.html`, sinon `<slug>.html`, sinon l'unique fichier
  HTML — sinon livre ignoré avec avertissement). Les noms commençant par `.` et le
  dossier `_template` sont exclus.
- **Métadonnées** : les 12 meta `book:*` du `<head>`, lues par un vrai parseur HTML
  (lecture bornée à `</head>` ou 4 Mio). Fallbacks du titre : `book:title` →
  `<title>` → nom de fichier humanisé (tirets → espaces, première lettre en
  majuscule). Auteur, description, date : première balise non vide, sinon `null`.
  Les balises génériques (`og:*`, `twitter:*`, JSON-LD…) sont volontairement
  ignorées.
- **Normalisation** : décodage des entités, suppression des caractères de contrôle,
  Unicode NFC, blancs réduits à un espace, trim. Tags découpés sur la virgule
  uniquement.
- **Nature** : lue depuis `book:workflow`, qui nomme l'atelier de production suivi
  d'une version (`roman-atelier v3`, `reportage v2`). Le suffixe ` vN` est retiré,
  puis l'atelier est cherché dans la table `ATELIER_NATURE` :

  | Atelier | `nature` |
  |---|---|
  | `roman-atelier` | `fiction` |
  | `reportage` | `reportage` |

  **Meta absente ⇒ `fiction`, en silence** : c'est le défaut qui a évité de rétrofiter
  les romans publiés avant le schéma v2. **Atelier inconnu ⇒ `fiction` + avertissement**
  nommant l'atelier manquant : un nouvel atelier doit être ajouté à la table, pas
  silencieusement rangé parmi les fictions.
- **`variantOf`** : `book:variant-of` doit être un slug kebab-case ASCII, différent du
  livre lui-même, et **présent dans le catalogue en cours de génération** (les slugs
  connus sont collectés avant la boucle, donc l'ordre de découverte est indifférent).
  Tout écart ⇒ `null` + avertissement : une référence cassée ne doit pas produire un
  groupement fantôme à l'index.
- **`wordCount`** — trois étages, du plus fiable au plus approximatif :
  1. **Îlots de données.** Le script relit le fichier entier (borné à 8 Mio, même
     détection d'encodage que le head) et cherche tous les
     `<script type="application/json">` — identifiant indifférent, attributs dans
     n'importe quel ordre. Dans chaque îlot, il prend la liste `chapters` ou
     `chapitres` et somme les mots de `blocks[].text`, sinon de `texte`/`text`.
     **Seuls les chapitres comptent** : le `codex`, la `carte`, les annexes et
     l'appareil de la liseuse sont exclus — c'est le texte du livre qu'on mesure, pas
     le poids du fichier. Le premier îlot qui produit un total non nul l'emporte.
  2. **Texte visible du body**, si aucun îlot n'aboutit : un parseur HTML collecte ce
     qui suit `</head>` en ignorant `script`, `style`, `template` et `noscript`. Le
     résultat n'est retenu qu'**à partir de 500 mots** ; en deçà, on n'a mesuré que
     les libellés de l'interface de lecture, pas une œuvre.
  3. **`null` + avertissement** sinon. Trois livres sont dans ce cas —
     `archipel-intermittent`, `la-couronne-lente` et `letiage` — parce que leur prose
     vit dans des littéraux JavaScript, illisibles sans exécuter la page. C'est un
     manque assumé, pas une panne : l'index doit traiter `null` comme « durée
     inconnue » et non comme zéro.
- **`readingMinutes`** : `max(1, round(wordCount / 200))`. 200 mots/minute est une
  vitesse de lecture de loisir en français ; le plancher d'une minute évite d'annoncer
  « 0 min » sur un texte court.
- **Couverture** : `couvertures/<slug>.webp`, puis `.avif`, `.png`, `.jpg`, `.jpeg` —
  le premier fichier dont la **signature binaire** correspond au format. Nom ≠ slug
  exact ⇒ couverture ignorée en silence. **Repli embarqué** : si `couvertures/` ne
  fournit rien et que le livre est un dossier, le script cherche
  `livres/<slug>/cover.<ext>` puis `livres/<slug>/images/cover.<ext>` (mêmes
  extensions, même contrôle de signature). `couvertures/` garde toujours la priorité ;
  un livre à plat (`livres/<slug>.html`) n'a pas de repli possible.
- **Date d'ajout** (clé de tri) : `git log --diff-filter=A` sur le point d'entrée,
  sans `--follow` (pour que les éditions dérivées n'héritent pas de la date de leur
  livre source), repli sur la date de modification du fichier.

Le détail exhaustif (avertissements, cas limites) est lisible dans
`scripts/build_catalog.py`, abondamment commenté en français.

## Le bloc `#demo-catalog`

Copie de secours du catalogue inlinée dans `index.html`, utilisée uniquement quand
`fetch()` échoue en `file://`. Régénérée par `--sync-demo-catalog` : JSON identique à
`catalog.json` **à un détail près** — les séquences `</` sont échappées en `<\/` pour
rester valides dans une balise `<script>` (strictement équivalent après
`JSON.parse`). Le script exige exactement une occurrence du bloc, sinon
`DemoBlockError`.

## Suites

Le schéma v2 est posé ; ce qu'on en fait relève des chantiers suivants de
[`ROADMAP.md`](ROADMAP.md). Les chantiers 6 (gouvernance des tags) et 7 (capacités
interactives déclarées) sont faits ; la 1.0 « catalogue public soigné » est atteinte.
La suite relève du palier 2 de [`VISION.md`](VISION.md).
