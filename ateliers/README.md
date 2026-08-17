# Ateliers — les workflows de production

Un **atelier** est un workflow de production documenté : un dossier
`ateliers/<nom-atelier>/` dont le `WORKFLOW.md` permet à un agent — Claude Code,
Codex ou autre — de produire de bout en bout un livrable destiné au catalogue de la
bibliothèque. Plusieurs ateliers cohabitent, un par type de livrable.

## Registre des ateliers

| Atelier | Livrable | Version | Statut | Moteur | Exemples publiés |
|---|---|---|---|---|---|
| [`roman-atelier/`](roman-atelier/WORKFLOW.md) | Roman-web autonome **illustré nativement** avec liseuse « Atelier » (sommaire, progression, codex à déverrouillage, illustrations), fabriqué en deux passes tracées : auteur puis illustrateur (brief : [`BRIEF.md`](roman-atelier/BRIEF.md)) ; ancrage dans le monde réel sur option du brief, avec recherche documentaire sourcée en amont de l'écriture | v4 | stable (étapes illustrations et recherche documentaire en attente de leur pilote à froid) | [`livres/_template/`](../livres/_template/README.md) (`atelier-liseuse v1`) | [`livres/lequation-du-calme/`](../livres/lequation-du-calme), [`livres/la-doublure.html`](../livres/la-doublure.html) (v2, non illustrés) |
| [`reportage/`](reportage/WORKFLOW.md) | **Reportage** non romancé : un sujet réel du brief (lieu, personnage historique, métier, événement) documenté par recherche sourcée en amont de l'écriture, restitué en lecture explorable (parcours, notices de codex sourcées) et illustré de **documents du web** crédités de leur source (images, cartes, graphes — règle de pertinence : jamais de décoratif) ; ses livrables se signalent par le premier tag `reportage` (brief : [`BRIEF.md`](reportage/BRIEF.md)) | v2 | expérimental (pilote à froid à programmer) | [`livres/_template/`](../livres/_template/README.md) (`atelier-liseuse v2`) | aucun encore |

Les workflows sont **versionnés** (numéro en tête + changelog) et chaque livre
produit trace la version de recette utilisée
(`<meta name="book:workflow" content="<atelier> vN">` + mention dans la PR). Faire
évoluer une recette relève du rôle Conception
([`docs/conception/VISION.md`](../docs/conception/VISION.md)).

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
