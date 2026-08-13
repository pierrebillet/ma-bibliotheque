# Rôle Conception — nouveaux formats et workflows de production

Tu inventes de **nouveaux types de livrables de lecture** (nouvelle forme de livre,
recueil, fiction interactive à branches, livre audio, mode illustré…), tu documentes
leur **processus de fabrication reproductible** (les « recettes » exécutées par le
rôle Production) et tu **fais évoluer** les recettes existantes. Prérequis : avoir
lu [`AGENTS.md`](../../AGENTS.md) (règles d'or + protocole de session). Le cap du
rôle — boucle d'amélioration continue, socle éditorial, vision « génération de bout
en bout » (Ma Bibliothèque 2.0) — vit dans [`VISION.md`](VISION.md) et
[`ROADMAP.md`](ROADMAP.md).

## Le livrable de ce rôle est double

1. **Éventuellement un prototype** : un premier livre du nouveau format, publié dans
   `livres/` comme n'importe quel livre (il valide le format en conditions réelles).
2. **Toujours un atelier** : un dossier `ateliers/<nom-atelier>/` contenant un
   `WORKFLOW.md` suffisamment complet pour qu'un agent de production — Claude Code,
   Codex ou autre — puisse produire un livrable du format **sans autre contexte** que
   `AGENTS.md` et ce workflow.

Un format sans atelier n'est pas terminé : c'est l'atelier qui permet la
diversification des livrables, pas le prototype.

## Démarche

1. Lire [`creer-un-atelier.md`](creer-un-atelier.md) : ce que la plateforme impose,
   ce qui est libre, et les critères d'acceptation d'un nouvel atelier.
2. S'inspirer de l'atelier de référence :
   [`../../ateliers/roman-atelier/WORKFLOW.md`](../../ateliers/roman-atelier/WORKFLOW.md).
3. Rédiger le workflow en copiant [`GABARIT-WORKFLOW.md`](GABARIT-WORKFLOW.md) vers
   `ateliers/<nom-atelier>/WORKFLOW.md`.
4. Inscrire le nouvel atelier dans le registre
   [`../../ateliers/README.md`](../../ateliers/README.md).
5. Ouvrir la PR (protocole de session d'`AGENTS.md`) en décrivant le format, les
   choix faits et ce qui reste expérimental.

## Si le format exige de modifier la plateforme

Un livrable doit être découvert par `build_catalog.py` et affiché par `index.html`
**sans modification de la plateforme**. Si le format en exige une (nouveau champ de
catalogue, nouveau comportement de l'index…), c'est un chantier du rôle
**Bibliothèque** à traiter dans une PR séparée, en amont — voir
[`../bibliotheque/`](../bibliotheque/README.md).

## Sommaire du dossier

| Document | Contenu |
|---|---|
| [`VISION.md`](VISION.md) | Vision des rôles Conception & Production : boucle d'amélioration des recettes, paliers (P1 interfaces du propriétaire → 2.0 génération via clé API → 2.1 budget/paiement) |
| [`ROADMAP.md`](ROADMAP.md) | Chantiers priorisés : template de moteur versionné (palier 0), ateliers candidats, spécification 2.0 |
| [`IDEES.md`](IDEES.md) | Vivier d'idées (fonctionnalités de lecture, variété de contenus) : les pistes non engagées, d'où se piochent les prochains ateliers |
| [`PREFERENCES.md`](PREFERENCES.md) | Socle éditorial commun (fond et forme) que chaque atelier décline |
| [`creer-un-atelier.md`](creer-un-atelier.md) | Contraintes de plateforme, libertés, **standard de recette agent-agnostique**, critères d'acceptation, procédure |
| [`GABARIT-WORKFLOW.md`](GABARIT-WORKFLOW.md) | Squelette de `WORKFLOW.md` à copier pour tout nouvel atelier (versionné, étapes-contrats) |
