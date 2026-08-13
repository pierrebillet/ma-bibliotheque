# VISION.md — vision des rôles Conception & Production

Ce document donne le cap du couple Conception/Production : Production **exécute** des
recettes ([`../../ateliers/`](../../ateliers/README.md)) ; Conception **écrit et fait
évoluer** ces recettes, et porte l'innovation sur le fond et la forme des lectures.
Il pilote la [`ROADMAP.md`](ROADMAP.md) et s'appuie sur le socle éditorial
[`PREFERENCES.md`](PREFERENCES.md).

## Le but

L'objectif majeur d'innovation du projet est **la forme des lectures interactives**.
Le rôle Conception existe pour que cette innovation soit **systématique et
réplicable** : chaque bon résultat obtenu sur un livre doit être transformé en
recette reproductible — un bon résultat non formalisé est un résultat perdu.

Le rôle a un double objet :

1. **Les ateliers** : des recettes versionnées (`ateliers/<nom>/WORKFLOW.md`),
   suffisamment claires pour qu'un agent Production — Claude Code, Codex ou autre,
   de façon indifférenciée — produise le résultat attendu à chaque exécution.
2. **Le socle éditorial** ([`PREFERENCES.md`](PREFERENCES.md)) : les préférences de
   **fond** (contenu, ton, langue) et de **forme** (fonctionnalités des lectures)
   transverses à tous les ateliers, que chaque recette décline.

## La boucle d'amélioration continue

Les recettes ne sont pas figées : elles s'améliorent à chaque itération.

1. **Produire** : un agent Production exécute la recette courante.
2. **Observer** : ce qui a bien marché, ce qui a dévié, ce qui a demandé une
   interprétation (toute interprétation nécessaire est un défaut de la recette).
3. **Formaliser** : un agent Conception intègre l'amélioration dans le
   `WORKFLOW.md` — version +1, entrée au changelog expliquant le pourquoi.
4. **Tracer** : chaque livre enregistre la version de recette qui l'a produit
   (`<meta name="book:workflow" content="<atelier> vN">` + mention dans la PR).
5. **Comparer** : la trace permet de relier la qualité des livres aux versions de
   recette, et donc de savoir si une évolution améliore réellement les résultats.

## Innover sur un nouveau format

Tout nouveau format ou fonctionnalité de lecture — un roman dont on est le héros,
des lectures intégrant des vidéos issues d'une veille YouTube, de l'audio, des
branches narratives… — passe par un agent Conception qui :

1. **prototype** (un premier livrable qui respecte les contraintes de plateforme,
   voir [`creer-un-atelier.md`](creer-un-atelier.md)) ;
2. **formalise** la recette dans un nouvel atelier dès que le résultat est bon,
   pour pouvoir le répliquer à chaque fois ;
3. **inscrit** l'atelier au registre avec son statut (`expérimental` → `stable`).

Jamais d'innovation non capturée dans une recette : c'est la règle qui distingue ce
projet d'une collection de bonnes surprises non reproductibles.

## Les paliers

### P1 (actuel) — recettes exécutées via les interfaces du propriétaire

Pierre pilote la production depuis ses propres interfaces d'agents (Claude Code,
Codex…). L'interface n'apporte rien : **tout ce qui est nécessaire est dans le
dépôt** (`AGENTS.md` + le `WORKFLOW.md` de l'atelier + `PREFERENCES.md`). C'est ce
qui rend les agents interchangeables.

### P2 — « Ma Bibliothèque 2.0 » : génération de bout en bout

Une interface où l'utilisateur renseigne **sa clé API**, remplit un **formulaire**
(paramètres du livre souhaité), et où la génération s'exécute de bout en bout
jusqu'à la **publication dans la bibliothèque de l'utilisateur**.

Principe non négociable : **l'interface n'est qu'un exécutant des recettes
versionnées du dépôt** — aucune logique de génération cachée côté interface. Les
champs du formulaire sont les paramètres explicites de la recette ; un livre généré
par l'interface et un livre généré par un agent piloté à la main suivent le même
`WORKFLOW.md`, à la même version.

Critères d'entrée : paliers comptes/auth de la Bibliothèque atteints
([`../bibliotheque/VISION.md`](../bibliotheque/VISION.md), palier 4) ; recettes
stables dont les paramètres d'entrée sont explicitement définis (le formulaire ne
peut exposer que ce que la recette paramètre).

### P3 — « 2.1 » : budget et génération pour compte de tiers

Extensions du 2.0 : l'utilisateur **fixe un budget avant génération** (estimation de
coût affichée), et peut **payer par carte** pour qu'une génération soit exécutée
pour son compte s'il ne dispose pas de son propre accès API.

## Principes durables

1. **La recette est la source de vérité unique.** Humain-via-agent aujourd'hui,
   interface demain : tous exécutent le même `WORKFLOW.md`.
2. **Agent-agnostique** : une recette ne référence jamais un outil propre à un agent
   donné ; elle doit être exécutable de façon indifférenciée par Claude Code, Codex
   ou tout autre (standard détaillé dans [`creer-un-atelier.md`](creer-un-atelier.md)).
3. **Versionné et tracé** : version en tête + changelog dans chaque `WORKFLOW.md` ;
   chaque livre porte la version qui l'a produit.
4. **Le socle éditorial prime** : un atelier décline
   [`PREFERENCES.md`](PREFERENCES.md), il ne le contredit pas.
