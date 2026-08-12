# AGENTS.md — contrat de contribution pour agents de code

Ce fichier est le contrat de référence pour tout agent (Claude Code, Codex, Gemini
CLI, etc.) qui contribue à ce dépôt. Il prime sur `SPEC.md`, `CONVENTIONS.md` et
`ROADMAP.md`, partiellement obsolètes (voir l'encart en tête de chacun).

## Le projet en une phrase

Une bibliothèque statique (GitHub Pages) de livres-web HTML autonomes écrits par des
agents IA ; la page d'accueil `index.html` consomme `catalog.json`, régénéré
automatiquement par CI à partir des métadonnées des livres.

## Règles d'or

1. **Ne jamais éditer `catalog.json`.** Il est régénéré par le workflow après chaque
   merge sur `main`. La CI rejette toute pull request qui le modifie.
2. **Ne jamais éditer le bloc `#demo-catalog` de `index.html`.** C'est une copie de
   secours du catalogue pour l'ouverture en `file://` ; sa synchronisation est un
   chantier connu, ne pas l'entretenir à la main.
3. **Tout passe par une branche + pull request.** Jamais de push direct sur `main`,
   y compris pour les éditions illustrées.
4. **Un livre = un commit clair** (ou plusieurs commits d'étapes : plan, chapitres,
   relecture — encore mieux pour l'auditabilité). Message en français, descriptif.
5. **Ne pas committer de fichiers système** (`.DS_Store`, etc.) — le `.gitignore`
   les couvre, ne pas le contourner.
6. **Vérifier avant d'ouvrir la PR** :
   ```bash
   python scripts/build_catalog.py --output /tmp/catalog-verification.json
   ```
   Le script sort en erreur si un identifiant de livre est invalide. La CI exécute
   la même vérification sur chaque pull request.

## Écrire un livre

### Emplacement et nommage

- Slug en **kebab-case ASCII** : `[a-z0-9]+(-[a-z0-9]+)*`, sans accents ni espaces.
  Un slug invalide fait échouer la CI.
- **Livre sans images** : un seul fichier `livres/<slug>.html`.
- **Livre avec images** (recommandé dès qu'il y a des illustrations) :
  ```text
  livres/<slug>/
    index.html          ← point d'entrée (préférer index.html à <slug>.html)
    images/
      chapter-01.jpg    ← numérotation sur 2 chiffres (tri lexicographique correct)
      codex-<slug-entree>.jpg
  ```
- Profondeur maximale : un seul niveau de dossier sous `livres/`.
- Toutes les ressources du livre restent **dans son dossier**. Exception héritée :
  la couverture affichée dans le livre peut référencer `../../couvertures/<slug>.jpg`,
  mais l'autonomie complète du dossier est préférée pour les nouveaux livres.

### Métadonnées obligatoires (`<head>`)

```html
<meta name="book:title" content="Titre du livre">
<meta name="book:author" content="Nom du modèle">
<meta name="book:description" content="Résumé en une ou deux phrases (≤ 600 caractères).">
<meta name="book:tags" content="genre, thème, lieu (1 à 6 tags, séparés par des virgules)">
<meta name="book:date" content="2026-08-12">
```

- **`book:author` crédite le modèle** qui a écrit le texte (`Claude Fable`,
  `GPT 5.5`, `Gemini 3.1 pro`…). Ne pas utiliser de pseudonyme collectif : la
  traçabilité de « quel modèle a écrit quoi » est l'objet même du projet. Pour un
  livre multi-agents, séparer par des virgules (`Claude Fable, GPT 5.5`) et
  détailler les rôles dans le commit.
- `book:date` : `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`.

### Couverture

- Fichier `couvertures/<slug>.jpg` (ou `.png`/`.webp` — `.webp` préféré à terme),
  ratio **2:3** (ex. 800×1200), poids raisonnable (< 300 Ko visé).
- Le nom doit être **exactement** le slug du livre, sinon elle est ignorée en silence
  et un placeholder est généré.

### Qualité attendue

- Fichier **autonome** : CSS et JS inline, aucune ressource distante, lisible hors
  ligne.
- `lang="fr"`, `alt` sur toutes les images, navigation clavier, `prefers-color-scheme`
  et `prefers-reduced-motion` respectés.
- Images : JPEG qualité raisonnable ou WebP, `loading="lazy"` hors première image,
  `width`/`height` déclarés pour éviter les décalages de mise en page.
- Persistance de la position de lecture en `localStorage` **dans le livre** autorisée
  (clé préfixée par le slug : `<slug>-state-v1`). La page d'accueil, elle, n'utilise
  ni localStorage ni cookies.
- Avant de créer un nouveau moteur de liseuse, regarder les livres récents
  (`livres/lequation-du-calme/`, `livres/la-doublure.html`) : un moteur commun
  « Atelier » y est copié-collé. Sa factorisation en template versionné est un
  chantier ouvert — en attendant, repartir du plus récent et signaler dans la PR
  toute divergence introduite.

### Éditions dérivées (illustrée, remaniée…)

État actuel : deux éditions illustrées coexistent avec leur version texte comme des
entrées séparées du catalogue (`-v2`, `-illustree`) — c'est un défaut connu (doublons
indiscernables). **Jusqu'à nouvel ordre : ne pas créer de nouvelle édition dérivée en
doublon.** Préférer enrichir le livre existant (images intégrées avec bascule
d'affichage) ou attendre le schéma de catalogue v2 (`variantOf`) — voir
`audits/2026-08-rapport-etonnement.md` §D.

## Chaîne technique (pour s'orienter)

| Élément | Rôle |
|---|---|
| `scripts/build_catalog.py` | Découvre les livres, extrait les 5 meta `book:*` du `<head>`, résout la couverture, trie par date d'ajout Git. Strict sur les slugs (exit 1). |
| `.github/workflows/catalog.yml` | Job `verification` sur PR (génération à blanc + refus des éditions de `catalog.json`) ; job `catalogue` sur `main` (régénère, commite `[skip ci]`, relance le build Pages). |
| `index.html` | Page d'accueil autonome. Valide chaque entrée du catalogue ; ignore les entrées invalides. |

## Ce qu'il ne faut PAS faire

- Éditer `catalog.json` ou le bloc `#demo-catalog` (voir règles d'or).
- Pousser directement sur `main`.
- Renommer un livre publié sans raison forte (le slug est l'identifiant public :
  URL, couverture, clé localStorage des lecteurs).
- Créer `livres/<slug>/` avec plusieurs fichiers HTML sans `index.html` (le livre
  serait ignoré) ou imbriquer à plus d'un niveau (ignoré silencieusement).
- Ajouter des dépendances externes (CDN, fonts distantes) dans un livre ou l'index.
