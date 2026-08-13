# Ateliers — les workflows de production

Un **atelier** est un workflow de production documenté : un dossier
`ateliers/<nom-atelier>/` dont le `WORKFLOW.md` permet à un agent — Claude Code,
Codex ou autre — de produire de bout en bout un livrable destiné au catalogue de la
bibliothèque. Plusieurs ateliers cohabitent, un par type de livrable.

## Registre des ateliers

| Atelier | Livrable | Statut | Exemples publiés |
|---|---|---|---|
| [`roman-atelier/`](roman-atelier/WORKFLOW.md) | Roman-web autonome avec liseuse « Atelier » (sommaire, progression, codex à déverrouillage) | stable | [`livres/lequation-du-calme/`](../livres/lequation-du-calme), [`livres/la-doublure.html`](../livres/la-doublure.html) |

## Exécuter un atelier (rôle Production)

1. Lire [`AGENTS.md`](../AGENTS.md) à la racine — règles d'or et **protocole de
   session** (branche `atelier/<sujet>`, commits d'étapes, PR systématique en fin de
   session) ;
2. Lire le `WORKFLOW.md` de l'atelier choisi et le suivre étape par étape ;
3. Avant la PR : `python scripts/build_catalog.py --output /tmp/catalog-verification.json`.

Aucune autre lecture n'est nécessaire pour produire un livrable.

## Créer un nouvel atelier (rôle Conception)

Guide, critères d'acceptation et gabarit dans
[`docs/conception/`](../docs/conception/README.md). Tout nouvel atelier s'inscrit
dans le registre ci-dessus avec son statut (`expérimental` puis `stable`).
