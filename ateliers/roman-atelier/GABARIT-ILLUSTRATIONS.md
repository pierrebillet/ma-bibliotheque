# GABARIT — manifeste d'illustrations (`livres/<slug>/illustrations.md`)

L'agent auteur copie ce gabarit vers `livres/<slug>/illustrations.md` à l'étape 4
et remplace chaque section. Le manifeste doit être **autoportant** : l'agent
illustrateur qui le reçoit n'a rien lu d'autre du dépôt et n'a pas besoin de
lire le livre — tout ce qu'il doit produire et savoir est ici. Une entrée par
image, dans l'ordre des fichiers ; les prompts se rédigent à partir des champs
`visualDescription` de l'îlot (ils doivent raconter la même image).

Copier à partir d'ici :

---

# Illustrations de « <Titre du livre> »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v<N>`
(reporter la version du WORKFLOW exécuté — celle de la meta `book:workflow`).

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/<slug>/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Tu travailles sur la branche `atelier/roman-<slug>` de ce dépôt (celle où se
   trouve ce fichier). Tu pousses tes commits sur cette branche, jamais sur
   `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON de
   `index.html`, ni le texte, ni aucun autre fichier — à une exception près :
   dans le `<head>` de `livres/<slug>/index.html`, complète la meta
   `book:author` en ajoutant ton modèle, sous la forme :
   `content="<valeur existante>, <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de <titre> : chapitres 1 à 5 »),
   plusieurs commits bienvenus.
5. Quand tout est produit : pousse, puis signale ta passe dans la pull request
   ouverte pour cette branche (outil de génération utilisé, écarts éventuels).

**Contraintes techniques** (pour chaque image, sauf mention contraire dans son
entrée) :

- Format **WebP** ; si ta chaîne ne produit pas de WebP, convertis :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou : magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```
- Images de chapitre et de notice : **1600×900**, poids **≤ 150 Ko**.
- Couverture : **800×1200** (ratio 2:3), poids **< 300 Ko**.
- **Couverture : aucun texte autorisé**, sans exception — ni titre, sous-titre,
  nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre est ajouté
  par-dessus en HTML dans la bibliothèque.
- Images intérieures : aucun texte lisible incrusté (titres, lettrages), sauf si
  une entrée le demande explicitement pour une raison narrative.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/<slug>
  ```

## Bible visuelle commune

<La direction artistique qui unifie toutes les images — à intégrer en tête de
chaque prompt. Technique et rendu (ex. gouache sombre, grain argentique…),
palette dominante, époque et lieu, lumière, ce qu'on ne montre jamais
(interdits), niveau de stylisation des personnages. 5 à 10 lignes.>

<Si des personnages ou lieux reviennent d'une image à l'autre, les décrire ici
une fois pour toutes (silhouette, âge, vêtements, traits distinctifs) afin que
toutes les images restent cohérentes.>

## Couverture

- **Fichier** : `couvertures/<slug>.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : <ce que montre la couverture>
- **Prompt** : <bible visuelle + composition verticale 2:3, point focal, place
  implicite du titre en tiers supérieur ; aucun texte, logo, signature,
  filigrane ou pseudo-texte>
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) : « <cover.alt> »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — <titre du chapitre>
- **Sujet** : <une phrase>
- **Prompt** : <bible visuelle + scène précise : cadrage, sujets, action,
  lumière, ambiance — rédigé depuis `visualDescription`>
- **Alt de référence** : « <alt du chapitre 1> »

### `images/chapter-02.webp`

<idem pour chaque chapitre, sans exception>

## Images de notices

### `images/codex-<id-de-la-notice>.webp`

- **Notice** : <titre de la notice> (<catégorie>)
- **Sujet** : <une phrase>
- **Prompt** : <…>
- **Alt de référence** : « <alt de la notice> »

<idem pour chaque notice illustrée>

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/<slug>.webp` | à produire |
| `images/chapter-01.webp` | à produire |
| … | … |

<Une ligne par fichier — l'illustrateur peut cocher au fil de l'eau ; le
décompte doit correspondre exactement aux champs `image` de l'îlot.>
