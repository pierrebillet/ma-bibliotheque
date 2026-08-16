# AGENTS.md — point d'entrée pour tout agent de code

Ce dépôt est une bibliothèque statique (GitHub Pages) de livres-web HTML autonomes
écrits par des agents IA ; la page d'accueil `index.html` consomme `catalog.json`,
régénéré automatiquement par la CI. Lis ce fichier en entier (~3 minutes), identifie
ton rôle, puis lis **uniquement** la documentation de ce rôle.

## Quel est ton rôle dans cette session ?

| Si ta mission est… | Ton rôle | Ta documentation |
|---|---|---|
| Modifier `index.html`, `scripts/build_catalog.py`, la CI, le traitement des couvertures, la doc technique | **Bibliothèque** | [`docs/bibliotheque/README.md`](docs/bibliotheque/README.md) |
| Inventer un nouveau type de livrable de lecture ou son processus de fabrication | **Conception** | [`docs/conception/README.md`](docs/conception/README.md) |
| Produire un livrable destiné au catalogue (écrire un roman, illustrer…) | **Production** | [`ateliers/README.md`](ateliers/README.md), puis le `WORKFLOW.md` de ton atelier |

En cas de doute sur le rôle ou le périmètre de la mission, poser la question à
Pierre avant de commencer.

## Règles d'or (tous rôles)

1. **Ne jamais éditer `catalog.json`.** Il est régénéré par la CI après chaque merge
   sur `main` ; la CI rejette toute pull request qui le modifie.
2. **Ne jamais éditer le bloc `#demo-catalog` de `index.html`.** Copie de secours du
   catalogue pour l'ouverture en `file://`, régénérée par la CI au même titre que
   `catalog.json` (le reste d'`index.html` reste modifiable normalement, rôle
   Bibliothèque). Ajouter un livre ne demande **aucune** mise à jour du catalogue.
3. **Slug de livre en kebab-case ASCII** : `[a-z0-9]+(-[a-z0-9]+)*`, sans accents ni
   espaces. Un slug invalide fait échouer la CI.
4. **`book:author` crédite le modèle** qui a écrit le texte (`Claude Fable`,
   `GPT 5.5`, `Gemini 3.1 pro`…), jamais un pseudonyme collectif : la traçabilité de
   « quel modèle a écrit quoi » est l'objet même du projet.
5. **Pas de fichiers système** (`.DS_Store`…) ni de **dépendance externe** (CDN,
   fonts distantes) — dans les livres comme dans l'index.
6. **Vérifier avant d'ouvrir la PR** :
   ```bash
   python scripts/build_catalog.py --output /tmp/catalog-verification.json
   ```
   Le script sort en erreur si un identifiant de livre est invalide. La CI exécute
   la même vérification sur chaque pull request.

## Protocole de session (Claude Code, Codex et tout autre agent — sans exception)

Ce protocole harmonise la façon de travailler de tous les agents sur ce dépôt.

1. **Début de session : créer une branche.** Jamais de travail directement sur
   `main`. Nommage : `<role>/<sujet-en-kebab-case>` — ex. `atelier/roman-les-brumes`,
   `bibliotheque/fix-tri-catalogue`, `conception/atelier-nouvelles`.
2. **Pendant la session : commits d'étapes, messages en français, descriptifs.**
   Pour un livre : un commit par étape de fabrication (plan, chapitres, codex,
   relecture) — l'historique de fabrication est une richesse du projet.
3. **Fin de session : ouvrir une pull request, systématiquement.** Même si le
   travail est inachevé (le dire alors explicitement dans la description).
   Description structurée :
   - **Rôle** : Bibliothèque / Conception / Production (+ atelier utilisé) ;
   - **Objectif** de la session ;
   - **Ce qui a été fait** (et ce qui reste à faire) ;
   - **Vérifications passées** (au minimum la commande de la règle d'or n° 6) ;
   - **Points ouverts** ou décisions à prendre par Pierre.
4. **Jamais de push sur `main`.** Le merge est la décision de Pierre, pas de l'agent.
5. **Ne jamais terminer une session avec du travail committé uniquement en local** :
   toute branche avec des commits doit être poussée avant de conclure.

## Carte du dépôt (pour s'orienter)

| Élément | Rôle |
|---|---|
| `livres/`, `couvertures/` | Les livrables publiés et leurs couvertures (`couvertures/<slug>.webp\|avif\|png\|jpg\|jpeg`, ratio 2:3 ; repli possible pour un livre-dossier : `livres/<slug>/cover.*` ou `livres/<slug>/images/cover.*`) |
| `scripts/build_catalog.py` | Découvre les livres, extrait les meta `book:*`, résout les couvertures, génère `catalog.json` |
| `.github/workflows/catalog.yml` | CI : vérification sur PR ; régénération du catalogue après merge sur `main` |
| `index.html` | Page d'accueil autonome (recherche, filtres, tri) |
| `ateliers/` | Workflows de production des livrables (rôle Production) |
| `docs/` | Documentation par rôle, audits, archives |

Détails techniques dans [`docs/bibliotheque/`](docs/bibliotheque/README.md).

## Ce qu'il ne faut PAS faire

- Éditer `catalog.json` ou le bloc `#demo-catalog` (règles d'or 1 et 2).
- Pousser directement sur `main`.
- Renommer un livre publié sans raison forte (le slug est l'identifiant public :
  URL, couverture, clé localStorage des lecteurs).
- Créer une **édition dérivée en doublon** (`-v2`, `-illustree`) : moratoire en
  vigueur jusqu'au schéma de catalogue v2 — voir
  [`docs/audits/2026-08-rapport-etonnement.md`](docs/audits/2026-08-rapport-etonnement.md) §D
  et [`ateliers/roman-atelier/WORKFLOW.md`](ateliers/roman-atelier/WORKFLOW.md).
- Créer `livres/<slug>/` sans `index.html` ou imbriquer à plus d'un niveau (le livre
  serait ignoré silencieusement).
- Ajouter des dépendances externes (CDN, fonts distantes) dans un livre ou l'index.
