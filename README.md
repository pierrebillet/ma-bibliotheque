# Ma Bibliothèque

Une bibliothèque de **livres-web écrits par des agents IA** : chaque livre est une
page HTML autonome (récit + liseuse intégrée), la page d'accueil les référence via un
catalogue généré automatiquement, et le tout est publié par GitHub Pages.

Le projet a une double vocation :

1. **Une bibliothèque vivante** : des modèles différents (Claude, GPT, Gemini…) y
   écrivent des livres, seuls ou à plusieurs (texte + illustrations), et chaque
   contribution passe par une pull request comme dans un vrai projet logiciel.
2. **Un gabarit appropriable** : à terme, n'importe qui doit pouvoir forker ce dépôt,
   y brancher son coding agent préféré et écrire ses propres livres selon ses propres
   références. Les briques (guides, templates, skills) sont ajoutées progressivement.

## Où est la vérité ?

La documentation historique a dérivé de l'implémentation. Hiérarchie de confiance :

| Document | Statut |
|---|---|
| `README.md` (ce fichier) et `AGENTS.md` | **Source de vérité actuelle** |
| `AUTOMATISATION.md` | Fiable — décrit la chaîne de catalogue réelle |
| `FRONTEND.md` | Fiable — décrit `index.html` |
| `audits/2026-08-rapport-etonnement.md` | Audit complet de l'état du projet (août 2026) |
| `SPEC.md`, `CONVENTIONS.md`, `ROADMAP.md` | **Historiques, partiellement obsolètes** — voir l'encart en tête de chacun |
| `dev-mvp/` | Briefs d'exploration, non normatifs |

## Structure du dépôt

```text
index.html            Page d'accueil (recherche, filtres, tri) — autonome, sans framework
catalog.json          Catalogue généré — NE PAS éditer à la main (le bot le régénère)
livres/               Les livres
  mon-livre.html        forme simple : un fichier autonome
  mon-livre/            forme dossier (recommandée si le livre a des images)
    index.html
    images/
couvertures/          Une couverture par livre : <slug>.jpg|png|webp (ratio 2:3)
scripts/build_catalog.py   Générateur du catalogue
.github/workflows/catalog.yml   CI : vérification en PR + régénération sur main
audits/               Audits et rapports d'étonnement
dev-mvp/              Études d'exploration
```

## Ajouter un livre (résumé)

Le contrat détaillé pour les agents est dans [`AGENTS.md`](AGENTS.md). En bref :

1. Créer une branche, puis `livres/<slug>/index.html` (slug en kebab-case ASCII :
   `mon-livre`) avec les 5 métadonnées `book:*` dans le `<head>`.
2. Déposer la couverture dans `couvertures/<slug>.jpg` (ratio 2:3).
3. Vérifier localement : `python scripts/build_catalog.py --output /tmp/catalog.json`
   (le script échoue si le slug est invalide).
4. Ouvrir une pull request. La CI vérifie la génération du catalogue et refuse toute
   modification manuelle de `catalog.json`.
5. Après le merge, le bot régénère `catalog.json` et relance le build GitHub Pages.
   Le livre apparaît sur la page d'accueil sans autre intervention.

## Ce qu'un livre doit respecter

- **Autonome** : un lecteur qui télécharge le fichier/dossier doit pouvoir lire le
  livre hors ligne. Pas de CDN, pas de dépendance externe.
- **Identifié** : les meta `book:title`, `book:author`, `book:description`,
  `book:tags`, `book:date` dans le `<head>`. `book:author` crédite le **modèle**
  qui a écrit le livre (ex. `Claude Fable`, `GPT 5.5`) — la provenance fait partie
  du projet.
- **Accessible** : `lang="fr"`, textes alternatifs, navigation clavier.

## Historique du projet

Le projet a été démarré avec ChatGPT (spec + premiers livres), puis ouvert à d'autres
agents. L'audit d'août 2026 (`audits/2026-08-rapport-etonnement.md`) documente l'état
des lieux complet — workflow, format des livres, bibliothèque — et la liste des
chantiers à venir.
