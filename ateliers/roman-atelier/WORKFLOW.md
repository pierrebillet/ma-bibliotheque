# Atelier roman-atelier — écrire un roman-web avec la liseuse « Atelier »

- **Version** : 2
- **Statut** : stable
- **Livrable** : un roman-web HTML autonome (récit + liseuse intégrée « Atelier des
  récits explorables » : sommaire, barre de progression, codex à déverrouillage,
  thème sombre, réglage de taille de police), visible au catalogue après merge sans
  aucune intervention manuelle.
- **Exemples publiés** : [`livres/lequation-du-calme/`](../../livres/lequation-du-calme),
  [`livres/la-doublure.html`](../../livres/la-doublure.html).
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md) — le lire
  avant l'étape 1, il fait partie de la recette.

## Changelog

- **v2** (2026-08) — mise au standard de recette
  ([`creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md) §3) : étapes
  au format entrée/travail/sortie/critère de fin/commit, traçabilité
  `book:workflow`, exigences transverses déplacées vers `PREFERENCES.md`.
- **v1** (2026-08) — première formalisation de la pratique observée sur les livres
  d'août (PR #5).

## Avant de commencer

Prérequis de lecture : [`/AGENTS.md`](../../AGENTS.md) (règles d'or + protocole de
session), ce workflow, et [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md).
Rien d'autre n'est supposé connu.

1. **Choisir le slug** : kebab-case ASCII (`les-brumes-du-port`), définitif — URL,
   couverture et clé localStorage en dépendent.
2. **Ouvrir le livre de référence** : le livre le plus récent de la famille
   « Atelier » (aujourd'hui `livres/lequation-du-calme/` et
   `livres/la-doublure.html`). Le moteur de liseuse s'y copie-colle d'un livre à
   l'autre : **repartir du plus récent**, signaler dans la PR toute divergence
   introduite. (La factorisation en template versionné `livres/_template/` est le
   chantier n° 2 de [`docs/conception/ROADMAP.md`](../../docs/conception/ROADMAP.md) ;
   tant qu'il n'est pas fait, cette règle de copie s'applique.)
3. **Créer la branche** : `atelier/roman-<slug>` (protocole de session).

## Étapes de fabrication

### Étape 1 — Plan et synopsis

- **Entrée** : le thème/brief du livre (fourni par Pierre ou choisi), le socle
  `PREFERENCES.md` (§Fond).
- **Travail** : poser l'univers avant d'écrire — synopsis, promesse émotionnelle,
  idée centrale, question thématique, liste des chapitres avec leur rôle narratif,
  personnages et lieux principaux.
- **Sortie** : le fichier du livre créé (structure du §« Structure de fichiers »)
  avec le `<head>` complet (§« Le `<head>` obligatoire ») et l'îlot JSON amorcé :
  bloc `meta` + bloc `world` remplis, chapitres en squelette (titres seuls).
- **Critère de fin** : `python scripts/build_catalog.py --output
  /tmp/catalog-verification.json` passe et le slug apparaît dans le JSON généré.
- **Commit** : « Plan de <titre> : synopsis et structure »

### Étape 2 — Chapitres

- **Entrée** : le plan committé à l'étape 1.
- **Travail** : écrire les chapitres dans l'îlot JSON (blocs de texte), dans l'ordre
  du plan. Un lot cohérent de chapitres par commit.
- **Sortie** : les `chapters[]` de l'îlot remplis.
- **Critère de fin** : le livre s'ouvre en `file://`, chaque chapitre écrit
  s'affiche et la navigation fonctionne, aucune erreur dans la console du
  navigateur.
- **Commit(s)** : « Chapitres 1-3 de <titre> », « Chapitres 4-6 de <titre> »…

### Étape 3 — Codex et annexes

- **Entrée** : les chapitres écrits.
- **Travail** : rédiger les fiches du codex (personnages, lieux, concepts) et leurs
  règles de déverrouillage, en reliant les fiches aux mentions dans le texte.
- **Sortie** : le `codex[]` de l'îlot rempli, liens texte ↔ fiches en place.
- **Critère de fin** : intégrité référentielle parfaite — chaque fiche atteignable
  depuis le texte, aucune fiche orpheline, aucun lien mort (norme des livres
  récents : 0 défaut).
- **Commit** : « Codex de <titre> : personnages, lieux, concepts »

### Étape 4 — Relecture, couverture et finitions

- **Entrée** : le livre complet.
- **Travail** : relecture intégrale (cohérence narrative, orthographe, respect de
  `PREFERENCES.md`), corrections ; création de la couverture
  (§« Images et couverture ») ; passage de la checklist finale.
- **Sortie** : le livre corrigé + `couvertures/<slug>.jpg` (ou `.png`/`.webp`).
- **Critère de fin** : toutes les cases de « Vérifications avant PR » cochées.
- **Commit** : « Relecture de <titre> : corrections et couverture »

Puis : push et **pull request** (protocole de session — description structurée
Rôle : Production / roman-atelier v2, divergences de moteur signalées).

## Structure de fichiers

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
- Toutes les ressources du livre restent **dans son dossier** (la couverture, elle,
  vit dans `couvertures/` ; le livre n'a pas besoin de la référencer).

## Le `<head>` obligatoire

Bloc à copier dans le point d'entrée (les 5 meta `book:*` alimentent le catalogue ;
`book:workflow` trace la recette) :

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

  <!-- Traçabilité : version de la recette utilisée (ignorée par le catalogue) -->
  <meta name="book:workflow" content="roman-atelier v2">

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

## Le moteur de liseuse

- **Données** : le récit vit dans un îlot
  `<script type="application/json" id="book-data">` — structure observable dans les
  livres de référence : `meta` (slug, titre, auteur…), `world` (promesse
  émotionnelle, idée centrale, question thématique), `chapters[]` (blocs de texte,
  images éventuelles), `codex[]` (fiches avec règles de déverrouillage). Reprendre
  la structure du livre de référence à l'identique.
- **Persistance** : clé localStorage **exactement** `<slug>-state-v1` (voir
  `PREFERENCES.md` §Forme — convention violée par 4 livres sur 7 par le passé, ne
  pas reproduire).
- **Fonctionnalités à ne pas régresser** (présentes dans le moteur de référence) :
  sommaire, `role="progressbar"` mis à jour, codex à déverrouillage robuste au
  rechargement, thème sombre, taille de police, piège de focus dans les dialogues,
  région `aria-live` pour les déblocages, `prefers-reduced-motion`, échappement
  HTML systématique des données de l'îlot.
- **Défauts connus du moteur** (audit §B.4) — à corriger si l'occasion se présente,
  en le signalant dans la PR : `function close()` écrase `window.close` ;
  `entry(id)` sans garde (un id de codex manquant bloque tout le rendu) ; précédence
  `||`/`&&` dans la recherche du codex qui masque les fiches verrouillées dès qu'on
  tape.

## Images et couverture

- **Couverture obligatoire** : `couvertures/<slug>.jpg` (ou `.png`/`.webp` — `.webp`
  préféré à terme), ratio **2:3** (ex. 800×1200), poids < 300 Ko visé. Le nom doit
  être **exactement** le slug, sinon elle est ignorée en silence et un placeholder
  est généré.
- **Images de chapitre** : `images/chapter-NN.jpg` (NN sur 2 chiffres) ; poids,
  `loading="lazy"`, `width`/`height` et `alt` : voir `PREFERENCES.md` §Forme.

## Interdits spécifiques

- **Moratoire sur les éditions dérivées en doublon** (`-v2`, `-illustree`) : ne pas
  créer une entrée de catalogue séparée pour une variante d'un livre existant.
  Préférer enrichir le livre existant (images intégrées avec bascule d'affichage) ou
  attendre le schéma de catalogue v2 (`variantOf`) — audit
  [`docs/audits/2026-08-rapport-etonnement.md`](../../docs/audits/2026-08-rapport-etonnement.md) §D.
- Jamais toucher `catalog.json` ni le bloc `#demo-catalog` (règles d'or).
- Aucune ressource distante (CDN, fonts, images externes).

## Vérifications avant PR

- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur et le livre apparaît dans le JSON généré ;
- [ ] le livre s'ouvre et se lit en `file://` (hors ligne, sans erreur console) ;
- [ ] les 5 meta `book:*` sont présentes et exactes (`book:author` = modèle) ;
- [ ] `<meta name="book:workflow" content="roman-atelier v2">` présente ;
- [ ] couverture en place (`couvertures/<slug>.…`, ratio 2:3, nom = slug exact) ;
- [ ] codex : aucune fiche orpheline, aucun lien cassé, aucune image sans `alt` ;
- [ ] clé localStorage `<slug>-state-v1` ;
- [ ] socle [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) respecté
      (fond et forme) ;
- [ ] protocole de session d'`AGENTS.md` : commits d'étapes poussés, PR ouverte
      avec description structurée (Rôle : Production / roman-atelier v2),
      divergences de moteur signalées.
