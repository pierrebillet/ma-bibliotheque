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
   références. Les briques (guides, templates, ateliers) sont ajoutées progressivement.

## Où est la vérité ?

La documentation est organisée par **rôle d'agent**. Point d'entrée unique :
[`AGENTS.md`](AGENTS.md).

| Document | Contenu |
|---|---|
| [`AGENTS.md`](AGENTS.md) | Point d'entrée des agents : routage par rôle, règles d'or, protocole de session |
| [`docs/bibliotheque/`](docs/bibliotheque/README.md) | Rôle Bibliothèque : la plateforme (`index.html`, générateur de catalogue, CI) |
| [`docs/conception/`](docs/conception/README.md) | Rôle Conception : créer un nouveau format de livrable et son atelier |
| [`ateliers/`](ateliers/README.md) | Rôle Production : les workflows de production des livrables |
| [`docs/audits/`](docs/audits) | États des lieux datés (audit d'août 2026) |
| [`docs/archives/`](docs/archives/README.md) | Documents historiques (`SPEC.md`, `CONVENTIONS.md`, `ROADMAP.md`, `dev-mvp/`) — **ne plus suivre** |

## Structure du dépôt

```text
index.html            Page d'accueil (recherche, filtres, tri) — autonome, sans framework
                      (son bloc #demo-catalog est généré — NE PAS l'éditer à la main)
catalog.json          Catalogue généré — NE PAS éditer à la main (le bot le régénère)
livres/               Les livres
  mon-livre.html        forme simple : un fichier autonome
  mon-livre/            forme dossier (recommandée si le livre a des images)
    index.html
    images/
couvertures/          Une couverture par livre : <slug>.jpg|png|webp (ratio 2:3)
scripts/build_catalog.py        Générateur du catalogue
.github/workflows/catalog.yml   CI : vérification en PR + régénération sur main
AGENTS.md             Point d'entrée des agents (routage par rôle + protocole de session)
ateliers/             Workflows de production des livrables
  roman-atelier/        écrire un roman-web avec la liseuse « Atelier »
docs/
  bibliotheque/       Doc de la plateforme (frontend, automatisation, schéma du catalogue)
  conception/         Créer un nouveau format de livrable et son atelier
  audits/             États des lieux datés
  archives/           Docs historiques, conservées pour la traçabilité
```

## Ajouter un livre (résumé)

Le workflow complet est dans
[`ateliers/roman-atelier/WORKFLOW.md`](ateliers/roman-atelier/WORKFLOW.md) ; les
règles communes dans [`AGENTS.md`](AGENTS.md). En bref :

1. Créer une branche, puis `livres/<slug>/index.html` (slug en kebab-case ASCII :
   `mon-livre`) avec les 5 métadonnées `book:*` dans le `<head>`.
2. Déposer la couverture dans `couvertures/<slug>.jpg` (ratio 2:3).
3. Vérifier localement : `python scripts/build_catalog.py --output /tmp/catalog.json`
   (le script échoue si le slug est invalide).
4. Ouvrir une pull request. La CI vérifie la génération du catalogue et refuse toute
   modification manuelle de `catalog.json` ou du bloc `#demo-catalog` de `index.html`.
5. Après le merge, le bot régénère `catalog.json` **et** le bloc `#demo-catalog`
   d'`index.html`, puis relance le build GitHub Pages. Le livre apparaît sur la page
   d'accueil sans autre intervention : ne jamais mettre à jour le catalogue soi-même.

## Ce qu'un livre doit respecter

- **Autonome** : un lecteur qui télécharge le fichier/dossier doit pouvoir lire le
  livre hors ligne. Pas de CDN, pas de dépendance externe.
- **Identifié** : les meta `book:title`, `book:author`, `book:description`,
  `book:tags`, `book:date` dans le `<head>`. `book:author` crédite le **modèle**
  qui a écrit le livre (ex. `Claude Fable`, `GPT 5.5`) — la provenance fait partie
  du projet.
- **Accessible** : `lang="fr"`, textes alternatifs, navigation clavier.

## Licence

- **Le code** (générateur, pages du site, CI, ateliers, gabarits) est sous licence
  [MIT](LICENSE) : forkez, adaptez, réutilisez.
- **Les œuvres** — le contenu de `livres/` et `couvertures/` — sont sous
  [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/deed.fr)
  (CC BY 4.0) : réutilisation libre avec crédit du livre et de son auteur
  (le modèle indiqué par `book:author`).

## Historique du projet

Le projet a été démarré avec ChatGPT (spec + premiers livres), puis ouvert à d'autres
agents. L'audit d'août 2026
([`docs/audits/2026-08-rapport-etonnement.md`](docs/audits/2026-08-rapport-etonnement.md))
documente l'état des lieux complet — workflow, format des livres, bibliothèque — et
la liste des chantiers à venir.
