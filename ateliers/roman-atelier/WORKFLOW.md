# Atelier roman-atelier — écrire un roman-web avec la liseuse « Atelier »

- **Statut** : stable
- **Livrable** : un roman-web HTML autonome (récit + liseuse intégrée « Atelier des
  récits explorables » : sommaire, barre de progression, codex à déverrouillage,
  thème sombre, réglage de taille de police), visible au catalogue après merge sans
  aucune intervention manuelle.
- **Exemples publiés** : [`livres/lequation-du-calme/`](../../livres/lequation-du-calme),
  [`livres/la-doublure.html`](../../livres/la-doublure.html).

## 1. Avant de commencer

- Avoir lu [`/AGENTS.md`](../../AGENTS.md) : règles d'or et protocole de session
  (branche `atelier/roman-<sujet>`, commits d'étapes, PR systématique).
- **Ouvrir le livre le plus récent de la famille « Atelier » comme référence de
  moteur** — aujourd'hui `livres/lequation-du-calme/` et `livres/la-doublure.html`.
  Le moteur de liseuse y est copié-collé d'un livre à l'autre : repartir du plus
  récent, et **signaler dans la PR toute divergence introduite**. Sa factorisation
  en template versionné (`livres/_template/`, emplacement déjà exclu du catalogue
  par le script) est un chantier ouvert — voir l'audit
  [`docs/audits/2026-08-rapport-etonnement.md`](../../docs/audits/2026-08-rapport-etonnement.md) §D.3.1.
- Choisir le slug : kebab-case ASCII (`les-brumes-du-port`), définitif (URL,
  couverture et clé localStorage en dépendent).

## 2. Étapes de fabrication = commits

Chaque étape se conclut par un commit, message en français, descriptif.
L'historique de fabrication est une richesse du projet, pas un déchet.

### Étape 1 — Plan et synopsis (commit : « Plan de <titre> : synopsis et structure »)

Poser l'intention du livre : synopsis, promesse émotionnelle, question thématique,
liste des chapitres avec leur rôle narratif, personnages et lieux principaux. Ce
matériau alimente le bloc `world` de l'îlot JSON (§4) — le committer (dans le HTML
naissant ou en commentaire de l'îlot), il fait partie de l'auditabilité.

### Étape 2 — Chapitres (un ou plusieurs commits : « Chapitres 1-3 de <titre> »)

Écrire les chapitres dans l'îlot JSON. Un commit par lot cohérent de chapitres.

### Étape 3 — Codex et annexes (commit : « Codex de <titre> : personnages, lieux, concepts »)

Rédiger les fiches du codex (personnages, lieux, concepts) et leurs règles de
déverrouillage. Veiller à l'intégrité référentielle : chaque fiche atteignable
depuis le texte, aucun lien orphelin (les 4 livres récents sont à 0 défaut — s'y
tenir).

### Étape 4 — Relecture et corrections (commit : « Relecture de <titre> : corrections »)

Relecture complète : cohérence narrative, orthographe, métadonnées, accessibilité,
vérifications du §7. Puis couverture et PR.

## 3. Structure de fichiers

- **Livre sans images** : un seul fichier `livres/<slug>.html`.
- **Livre avec images** (recommandé dès qu'il y a des illustrations) :
  ```text
  livres/<slug>/
    index.html          ← point d'entrée (obligatoirement index.html)
    images/
      chapter-01.jpg    ← numérotation sur 2 chiffres (tri lexicographique correct)
      codex-<slug-entree>.jpg
  ```
- Profondeur maximale : **un seul niveau** de dossier sous `livres/`.
- Toutes les ressources du livre restent **dans son dossier** (aucune référence
  vers l'extérieur, couverture comprise : elle vit dans `couvertures/`, le livre
  n'a pas besoin de la référencer).

## 4. Le `<head>` obligatoire

Bloc à copier dans le point d'entrée (les 5 meta `book:*` alimentent le catalogue) :

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
  <meta name="book:tags" content="genre, thème, lieu (1 à 6 tags, séparés par des virgules)">
  <meta name="book:date" content="2026-08-13">

  <!-- Utilisé par l'onglet du navigateur et comme fallback de titre -->
  <title>Titre complet du livre</title>
</head>
```

- **`book:author` = le nom du modèle qui écrit** (`Claude Fable`, `GPT 5.5`,
  `Gemini 3.1 pro`…). **Pas de pseudonyme collectif** type « Atelier des récits
  explorables » — cette dérive a effacé la provenance de la moitié du catalogue
  (audit §B.6). Livre multi-agents : tous les modèles séparés par des virgules, et
  les rôles (auteur / illustrateur / relecteur) détaillés dans la PR.
- `book:date` : `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`.

## 5. Le moteur de liseuse

- **Données** : le récit vit dans un îlot
  `<script type="application/json" id="book-data">` — structure observable dans les
  livres de référence : `meta` (slug, titre, auteur…), `world` (promesse
  émotionnelle, idée centrale, question thématique), `chapters[]` (blocs de texte,
  images éventuelles), `codex[]` (fiches avec règles de déverrouillage). Reprendre
  la structure du livre de référence à l'identique.
- **Persistance** : position de lecture en localStorage autorisée **dans le livre**,
  clé **exactement** `<slug>-state-v1` — convention à respecter strictement (elle a
  été violée par 4 livres sur 7 : suffixes `-v2`/`-v3`, slug tronqué ; ne pas
  reproduire).
- **Fonctionnalités attendues** (présentes dans le moteur de référence, à ne pas
  régresser) : sommaire, `role="progressbar"` mis à jour, codex à déverrouillage
  robuste au rechargement, thème sombre (`prefers-color-scheme`), taille de police,
  piège de focus dans les dialogues, région `aria-live` pour les déblocages,
  `prefers-reduced-motion`, échappement HTML systématique des données de l'îlot.
- **Défauts connus du moteur** (audit §B.4) — à corriger si l'occasion se présente,
  en le signalant dans la PR : `function close()` écrase `window.close` ;
  `entry(id)` sans garde (un id de codex manquant bloque tout le rendu) ; précédence
  `||`/`&&` dans la recherche du codex qui masque les fiches verrouillées dès qu'on
  tape.

## 6. Images et couverture

- **Couverture obligatoire** : `couvertures/<slug>.jpg` (ou `.png`/`.webp` — `.webp`
  préféré à terme), ratio **2:3** (ex. 800×1200), poids < 300 Ko visé. Le nom doit
  être **exactement** le slug, sinon elle est ignorée en silence et un placeholder
  est généré.
- **Images de chapitre** : `images/chapter-NN.jpg` (NN sur 2 chiffres), WebP ≤ 150 Ko
  par image visé ; `loading="lazy"` hors première image ; `width`/`height` déclarés
  pour éviter les décalages de mise en page ; `alt` sur toutes les images.

## 7. Interdits spécifiques

- **Moratoire sur les éditions dérivées en doublon** (`-v2`, `-illustree`) : ne pas
  créer une entrée de catalogue séparée pour une variante d'un livre existant.
  Préférer enrichir le livre existant (images intégrées avec bascule d'affichage) ou
  attendre le schéma de catalogue v2 (`variantOf`) — audit §D.
- Jamais toucher `catalog.json` ni le bloc `#demo-catalog` (règles d'or).
- Aucune ressource distante (CDN, fonts, images externes).

## 8. Vérifications avant PR

- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur et le livre apparaît dans le JSON généré ;
- [ ] le livre s'ouvre et se lit en `file://` (hors ligne, sans console d'erreurs) ;
- [ ] les 5 meta `book:*` sont présentes et exactes (`book:author` = modèle) ;
- [ ] couverture en place (`couvertures/<slug>.…`, ratio 2:3, nom = slug exact) ;
- [ ] codex : aucune fiche orpheline, aucun lien cassé, aucune image sans `alt` ;
- [ ] clé localStorage `<slug>-state-v1` ;
- [ ] protocole de session d'`AGENTS.md` : commits d'étapes poussés, PR ouverte avec
      description structurée (Rôle : Production / roman-atelier), divergences de
      moteur signalées.
