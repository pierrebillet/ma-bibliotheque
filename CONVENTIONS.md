# Conventions — Ma Bibliothèque HTML

Version : 1.0  
Statut : source normative complémentaire à `SPEC.md`

## 1. Principe général

Un livre publiable est un fichier HTML autonome placé directement dans `livres/`.

Le seul élément obligatoire est le fichier lui-même. Toutes les métadonnées et la couverture sont optionnelles.

Exemple minimal valide :

```text
livres/mon-livre.html
```

Exemple enrichi :

```text
livres/mon-livre.html
couvertures/mon-livre.webp
```

## 2. Convention de nommage des livres

### 2.1 Forme obligatoire

Le nom complet doit correspondre à l’expression régulière :

```regex
^[a-z0-9]+(?:-[a-z0-9]+)*\.html$
```

Le nom de base, sans `.html`, est le `slug` et devient l’identifiant stable du livre dans le catalogue.

Contraintes :

- lettres ASCII minuscules `a` à `z` ;
- chiffres `0` à `9` ;
- mots séparés par un seul tiret `-` ;
- aucun espace ;
- aucun underscore ;
- aucun accent ;
- aucune apostrophe ;
- aucun point dans le nom de base ;
- aucun tiret initial ou final ;
- aucun double tiret ;
- extension exactement `.html` en minuscules ;
- longueur recommandée du slug : 3 à 80 caractères ;
- fichier placé directement dans `livres/`, sans sous-dossier.

### 2.2 Exemples valides

```text
mon-livre.html
livre-2.html
chroniques-du-seuil.html
2026-journal-de-bord.html
l-ile-des-brumes.html
```

### 2.3 Exemples invalides

```text
Mon-Livre.html          # majuscules
mon livre.html          # espace
mon_livre.html          # underscore
mon-livre.HTML          # extension en majuscules
mon--livre.html          # double tiret
-mon-livre.html          # tiret initial
mon-livre-.html          # tiret final
mon.livre.html           # point dans le nom de base
île-des-brumes.html      # caractère accentué
livres/serie/tome-1.html # sous-dossier non pris en charge
```

### 2.4 Stabilité des URLs

Le slug fait partie de l’URL publique :

```text
livres/chroniques-du-seuil.html
```

Renommer le fichier modifie son URL et son `id`. Aucun mécanisme de redirection automatique n’est prévu.

Le nom doit donc être choisi comme un identifiant durable, indépendamment du titre éditorial qui peut évoluer dans les métadonnées.

## 3. Encodage et structure HTML recommandés

### 3.1 Encodage

UTF-8 est obligatoire pour tout nouveau livre.

Le document DEVRAIT contenir, le plus tôt possible dans `<head>` :

```html
<meta charset="utf-8">
```

Le générateur possède des fallbacks d’encodage, mais ils servent uniquement à préserver la robustesse face à des fichiers existants.

### 3.2 Autonomie

Un livre DEVRAIT être un fichier réellement autonome :

- CSS intégré dans `<style>` ;
- JavaScript intégré dans `<script>` ;
- données intégrées dans le HTML ou le JavaScript ;
- images intégrées sous forme de `data:` ou de SVG inline lorsque cela est nécessaire ;
- absence de dépendance à un serveur applicatif.

Les ressources externes sont techniquement possibles, mais leur disponibilité, leur politique CORS et leur pérennité ne sont pas garanties par la bibliothèque.

### 3.3 Structure libre

La bibliothèque accepte un HTML libre. Les éléments suivants ne sont pas obligatoires pour être catalogué :

- `<!doctype html>` ;
- `<html>` ;
- `<head>` ;
- `<body>` ;
- `<title>` ;
- métadonnées `book:*`.

Une structure HTML5 valide reste recommandée pour le comportement du livre dans les navigateurs.

## 4. Métadonnées optionnelles

### 4.1 Noms reconnus

Les seules métadonnées spécifiques reconnues en version 1 sont :

```text
book:title
book:author
book:description
book:tags
book:date
```

Elles utilisent la forme :

```html
<meta name="book:title" content="Titre du livre">
```

Le nom de l’attribut `name` est comparé sans tenir compte de la casse et après suppression des espaces externes. Les valeurs `BOOK:TITLE`, `Book:Title` et `book:title` sont donc équivalentes.

Le contenu de `content` est une chaîne. Une balise sans attribut `content`, ou dont le contenu est vide après normalisation, est ignorée.

### 4.2 Métadonnées volontairement non reconnues

Pour garantir un comportement prévisible, le générateur n’utilise pas :

- `<meta name="title">` ;
- `<meta name="author">` ;
- `<meta name="description">` ;
- `og:title`, `og:description`, `og:image` ;
- `twitter:*` ;
- JSON-LD ;
- microdonnées schema.org ;
- noms de fichiers de couverture déclarés dans le HTML.

Ces balises peuvent rester présentes pour d’autres usages, mais elles n’influencent pas `catalog.json`.

## 5. Ordre précis d’extraction

### 5.1 Titre

Le titre est résolu dans cet ordre strict :

1. première balise `<meta name="book:title">` non vide dans l’ordre du document ;
2. première balise `<title>` dont le texte normalisé est non vide ;
3. nom de fichier humanisé.

Exemple :

```html
<meta name="book:title" content="Titre catalogue">
<title>Titre navigateur</title>
```

Résultat :

```json
"title": "Titre catalogue"
```

Si plusieurs `book:title` non vides existent, la première valeur est utilisée et les suivantes produisent un avertissement.

Si plusieurs `<title>` existent et qu’aucun `book:title` n’est exploitable, le premier `<title>` non vide est utilisé.

### 5.2 Humanisation du nom de fichier

Pour `fragment-sans-titre.html` :

1. retirer `.html` ;
2. remplacer chaque tiret par un espace ;
3. réduire les espaces multiples ;
4. mettre en majuscule le premier caractère de la chaîne ;
5. laisser les autres caractères inchangés.

Résultat :

```text
Fragment sans titre
```

Cette règle est un fallback technique, pas une règle typographique éditoriale. Pour un titre avec apostrophe, accents ou capitalisation spécifique, utiliser `book:title`.

### 5.3 Auteur

Priorité unique :

1. première balise `<meta name="book:author">` non vide ;
2. sinon `null`.

Plusieurs auteurs peuvent être écrits dans la même valeur, par exemple :

```html
<meta name="book:author" content="Ariane Valmont et Noé Sorel">
```

Le format n’impose pas de structure interne ni de séparation normalisée des auteurs.

### 5.4 Description

Priorité unique :

1. première balise `<meta name="book:description">` non vide ;
2. sinon `null`.

La description doit être du texte brut. Le HTML placé dans `content` est traité comme du texte après décodage des entités, jamais comme du balisage.

Longueur éditoriale recommandée : 80 à 240 caractères. L’interface limite visuellement la description à quatre lignes, sans modifier la valeur stockée dans le catalogue.

### 5.5 Tags

Le générateur lit toutes les balises `book:tags` non vides dans l’ordre du document.

Chaque valeur est découpée uniquement sur la virgule `,`.

Exemple :

```html
<meta name="book:tags" content="fantasy, interactif, mystère">
<meta name="book:tags" content="court, Fantasy">
```

Étapes :

1. concaténation des deux listes ;
2. suppression des espaces externes de chaque tag ;
3. suppression des tags vides ;
4. normalisation Unicode NFC ;
5. déduplication insensible à la casse et aux accents ;
6. conservation de la graphie de la première occurrence.

Résultat :

```json
"tags": [
  "fantasy",
  "interactif",
  "mystère",
  "court"
]
```

Règles éditoriales recommandées :

- 1 à 6 tags ;
- noms courts ;
- singulier plutôt que pluriel ;
- minuscules sauf nom propre ;
- pas de `#` ;
- pas de hiérarchie implicite ;
- éviter les synonymes redondants.

Une valeur `science-fiction; interactif` n’est pas séparée sur le point-virgule et devient un seul tag. Utiliser des virgules.

### 5.6 Date

Priorité unique :

1. première balise `<meta name="book:date">` non vide et valide ;
2. sinon `null`.

Formats acceptés :

```text
YYYY
YYYY-MM
YYYY-MM-DD
```

Exemples valides :

```html
<meta name="book:date" content="2026">
<meta name="book:date" content="2026-07">
<meta name="book:date" content="2026-07-12">
```

Exemples invalides :

```text
12/07/2026
2026/07/12
2026-7-12
12 juillet 2026
2026-02-30
```

La précision est écrite séparément dans le catalogue :

| Valeur | `datePrecision` |
|---|---|
| `2026` | `year` |
| `2026-07` | `month` |
| `2026-07-12` | `day` |
| valeur absente ou invalide | `null` |

Une date invalide n’empêche pas la publication ; elle est ignorée avec avertissement.

## 6. Normalisation textuelle

Toutes les valeurs extraites suivent le même pipeline :

1. décodage des entités HTML, par exemple `&amp;` vers `&` ;
2. suppression des caractères de contrôle non imprimables ;
3. normalisation Unicode NFC ;
4. remplacement de toute suite de blancs Unicode par un espace ASCII simple ;
5. suppression des espaces au début et à la fin.

Une valeur composée uniquement d’espaces devient absente.

Les valeurs restent du texte brut. Le générateur ne transforme pas les guillemets, apostrophes, tirets typographiques ou majuscules.

## 7. Limites de présentation et avertissements

Le catalogue conserve les valeurs normalisées sans troncature destructive. Le workflow émet toutefois un avertissement au-delà des seuils suivants :

| Champ | Seuil d’avertissement |
|---|---:|
| titre | 160 caractères |
| auteur | 120 caractères |
| description | 600 caractères |
| un tag | 40 caractères |
| nombre de tags | 20 |

L’interface applique ses propres limites visuelles par CSS, mais le texte complet reste disponible dans le DOM ou via l’attribut `title` lorsque pertinent.

## 8. Conventions des couvertures

### 8.1 Nom de fichier

La couverture doit reprendre exactement le slug du livre :

```text
livres/mon-livre.html
couvertures/mon-livre.webp
```

Le nom de base doit donc respecter la même convention que le livre.

### 8.2 Formats acceptés

Extensions reconnues, en minuscules :

```text
.webp
.png
.jpg
```

Formats ignorés :

```text
.jpeg
.svg
.gif
.avif
.heic
.pdf
.PNG
.JPG
.WEBP
```

### 8.3 Priorité en cas de doublon

Si plusieurs couvertures existent pour le même slug :

1. `.webp` ;
2. `.png` ;
3. `.jpg`.

Le premier fichier valide est utilisé. Les autres sont ignorés avec avertissement.

Il est recommandé de ne conserver qu’un seul fichier de couverture par livre.

### 8.4 Dimensions recommandées

Ratio cible : **2:3**.

Recommandation principale :

```text
1200 × 1800 px
```

Minimum conseillé :

```text
600 × 900 px
```

Autres recommandations :

- orientation portrait ;
- espace colorimétrique sRGB ;
- poids inférieur à 2 Mio ;
- texte essentiel placé loin des bords ;
- contraste suffisant pour une vignette de petite taille ;
- absence de transparence indispensable, car le fond de carte peut varier ;
- ne pas intégrer de données personnelles ou de contenu non publiable.

L’interface recadre avec `object-fit: cover` dans un cadre 2:3. Une image d’un autre ratio peut donc être coupée.

### 8.5 Couverture absente

Aucune action n’est requise. Le site génère une couverture de remplacement déterministe à partir du slug et du titre.

## 9. Bloc `<head>` optionnel à copier

Ce bloc enrichit le catalogue mais ne constitue pas une dépendance. Il peut être adapté ou supprimé sans empêcher la publication.

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Métadonnées utilisées par Ma Bibliothèque HTML -->
  <meta name="book:title" content="Titre complet du livre">
  <meta name="book:author" content="Nom de l’auteur ou des auteurs">
  <meta
    name="book:description"
    content="Description courte destinée à la carte du catalogue."
  >
  <meta name="book:tags" content="fiction, interactif, aventure">
  <meta name="book:date" content="2026-07-12">

  <!-- Utilisé par l’onglet du navigateur et comme fallback de titre -->
  <title>Titre complet du livre</title>
</head>
```

### 9.1 Version minimale avec métadonnées

```html
<head>
  <meta charset="utf-8">
  <meta name="book:title" content="Titre du livre">
  <title>Titre du livre</title>
</head>
```

### 9.2 Version sans métadonnées spécifiques

```html
<head>
  <meta charset="utf-8">
  <title>Titre du livre</title>
</head>
```

Dans ce dernier cas, seul le titre est extrait. Auteur, description, tags et date restent absents.

## 10. Cas limites et résolution déterministe

### 10.1 Métadonnée vide

```html
<meta name="book:title" content="   ">
<title>Le vrai titre</title>
```

Résultat : `Le vrai titre`.

### 10.2 Métadonnée dupliquée

```html
<meta name="book:author" content="Premier auteur">
<meta name="book:author" content="Second auteur">
```

Résultat : `Premier auteur`, avec avertissement.

### 10.3 Balise `<title>` comportant des retours à la ligne

```html
<title>
  Le livre
  des seuils
</title>
```

Résultat : `Le livre des seuils`.

### 10.4 Document sans `<head>`

```html
<meta name="book:title" content="Titre hors head">
<div>Contenu</div>
```

Résultat : `Titre hors head`.

Le générateur recherche les métadonnées dans tout le document afin de rester tolérant.

### 10.5 HTML vide

Fichier :

```text
livres/carnet-vide.html
```

Résultat :

```json
{
  "id": "carnet-vide",
  "title": "Carnet vide",
  "author": null,
  "description": null,
  "tags": [],
  "date": null,
  "datePrecision": null,
  "cover": null
}
```

### 10.6 Caractères HTML dans une description

```html
<meta
  name="book:description"
  content="Une enquête &amp; un récit &lt;interactif&gt;."
>
```

Résultat textuel :

```text
Une enquête & un récit <interactif>.
```

L’interface l’affiche comme texte et non comme balise.

## 11. Règles pratiques de contribution via GitHub

Pour l’ajout courant d’un livre :

1. ne modifier aucun fichier technique ;
2. déposer le fichier directement dans `livres/` ;
3. vérifier son nom avant de valider ;
4. utiliser un message de commit explicite, par exemple `Ajoute chroniques-du-seuil` ;
5. attendre la réussite de l’action GitHub Pages ;
6. ouvrir l’URL publique du livre pour vérifier son fonctionnement.

Pour une couverture :

1. déposer l’image directement dans `couvertures/` ;
2. reprendre exactement le slug ;
3. utiliser une extension acceptée en minuscules ;
4. ne pas créer ou modifier manuellement `catalog.json`.

## 12. Règles de non-intervention

L’utilisateur ne doit jamais avoir à :

- lancer Python ;
- lancer un build ;
- exécuter une commande Git ;
- installer Node.js ;
- éditer `catalog.json` ;
- référencer manuellement un livre dans `index.html` ;
- renseigner un chemin de couverture ;
- modifier le workflow pour un ajout normal.
