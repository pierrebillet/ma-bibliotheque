# Ateliers — les workflows de production

Un **atelier** est un workflow de production documenté : un dossier
`ateliers/<nom-atelier>/` dont le `WORKFLOW.md` permet à un agent — Claude Code,
Codex ou autre — de produire de bout en bout un livrable destiné au catalogue de la
bibliothèque. Plusieurs ateliers cohabitent, un par type de livrable.

## Registre des ateliers

| Atelier | Livrable | Version | Statut | Moteur | Exemples publiés |
|---|---|---|---|---|---|
| [`roman-atelier/`](roman-atelier/WORKFLOW.md) | Roman-web autonome **illustré nativement** avec liseuse « Atelier » (sommaire, progression, codex à déverrouillage, illustrations), fabriqué en deux passes tracées : auteur puis illustrateur (brief : [`BRIEF.md`](roman-atelier/BRIEF.md)) ; ancrage dans le monde réel sur option du brief, avec recherche documentaire sourcée en amont de l'écriture ; carte des lieux et graphe de relations sur option du brief | v9 | stable (étapes illustrations pilotées par le livre v3 ; recherche documentaire et modules de lecture en attente de leur pilote à froid) | [`livres/_template/`](../livres/_template/README.md) (`atelier-liseuse v3`) | [`livres/lequation-du-calme/`](../livres/lequation-du-calme), [`livres/la-doublure.html`](../livres/la-doublure.html) (v2, non illustrés), [`livres/la-clause-du-meilleur-ennemi/`](../livres/la-clause-du-meilleur-ennemi) (v3, illustré) |
| [`reportage/`](reportage/WORKFLOW.md) | **Reportage** non romancé : un sujet réel du brief (lieu, personnage historique, métier, événement) documenté par recherche sourcée en amont de l'écriture, restitué en lecture explorable (parcours, notices de codex sourcées) et illustré de **documents du web** crédités de leur source (images, cartes, graphes — règle de pertinence : jamais de décoratif) ; ses livrables sont rangés au catalogue sous `nature: reportage`, dérivée de leur `book:workflow` (brief : [`BRIEF.md`](reportage/BRIEF.md)) ; carte de situation et graphe de relations sourcés sur option du brief | v7 | stable (décision de Pierre, 2026-08-21 — deux livrables publiés, v2 puis v5) | [`livres/_template/`](../livres/_template/README.md) (`atelier-liseuse v3`) | [`livres/la-foret-de-troncais/`](../livres/la-foret-de-troncais) (v2), [`livres/loi-malraux/`](../livres/loi-malraux) (v5) |

Les deux ateliers partagent le moteur [`livres/_template/`](../livres/_template/README.md)
(`atelier-liseuse v3`) : une amélioration du template leur profite à tous les deux
dès leur prochaine production — les **modules optionnels** carte et relations,
comme le mode impression, en viennent (les livres publiés, eux, embarquent la
version du moteur de leur époque et ne sont pas régénérés). Leurs conventions
communes (mise en place, `<head>`, vocabulaires, images, vérification,
interdits) vivent dans [`TRONC-COMMUN.md`](TRONC-COMMUN.md), que chaque
`WORKFLOW.md` référence au lieu de les recopier ; le vérificateur du moteur
vit à côté de lui
([`livres/_template/outils/verifier.py`](../livres/_template/outils/verifier.py)).

Les workflows sont **versionnés** (numéro en tête + changelog) et chaque livre
produit trace la version de recette utilisée
(`<meta name="book:workflow" content="<atelier> vN">` + mention dans la PR) — c'est
aussi de cette meta que `scripts/build_catalog.py` dérive la `nature` du livre,
via sa table `ATELIER_NATURE` (nom d'atelier → `fiction` / `reportage`). Faire
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
