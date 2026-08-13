# Créer un nouvel atelier (workflow de production)

Un **atelier** est un workflow de production documenté dans
`ateliers/<nom-atelier>/WORKFLOW.md`, exécutable de bout en bout par un agent seul.
Ce guide fixe ce qu'un nouveau format de livrable doit respecter, ce qu'il peut
inventer, et comment l'atelier est accepté.

## 1. Ce que la plateforme impose (non négociable, quel que soit le format)

Tout livrable destiné au catalogue est soumis aux mêmes contraintes techniques,
vérifiées par `scripts/build_catalog.py` et la CI :

- **Emplacement** : `livres/<slug>.html` (fichier unique) ou `livres/<slug>/` avec
  `index.html` comme point d'entrée. **Un seul niveau** de dossier sous `livres/` ;
  toutes les ressources du livrable restent dans son dossier.
- **Slug** : kebab-case ASCII `[a-z0-9]+(-[a-z0-9]+)*` — slug invalide = CI rouge.
  Le slug est l'identifiant public et stable (URL, couverture, localStorage).
- **Les 5 métadonnées** `book:title`, `book:author`, `book:description`,
  `book:tags`, `book:date` dans le `<head>` du point d'entrée. `book:author` = le
  **modèle** qui écrit (règle d'or d'`AGENTS.md`).
- **Couverture** : `couvertures/<slug>.jpg|png|webp`, ratio 2:3, nom = slug exact.
- **Autonomie** : HTML/CSS/JS inline, aucune ressource distante, lisible hors ligne.
- **Accessibilité** : `lang="fr"`, `alt` sur toutes les images, navigation clavier,
  `prefers-color-scheme` et `prefers-reduced-motion` respectés.
- **Compatibilité catalogue** : le livrable doit être découvert par
  `build_catalog.py` et affiché par `index.html` **sans modification de la
  plateforme**. Sinon, la modification de plateforme est un chantier du rôle
  Bibliothèque, dans une PR séparée et préalable.

Le schéma complet du catalogue est dans
[`../bibliotheque/CATALOGUE.md`](../bibliotheque/CATALOGUE.md).

## 2. Ce qui est libre

Tout le reste : le moteur de lecture (liseuse, navigation, interactions), la
structure interne du HTML, les données embarquées (îlot JSON ou autre), l'usage du
localStorage **dans le livrable** (clé préfixée par le slug : `<slug>-state-v1`),
l'esthétique, le ton, la langue du contenu, le processus de fabrication lui-même
(nombre d'étapes, rôles multi-agents, outils).

## 3. Critères d'acceptation d'un nouvel atelier

- [ ] Le `WORKFLOW.md` est exécutable de bout en bout par un agent qui n'a lu que
      `AGENTS.md` et ce workflow (test : le faire exécuter par un agent à froid).
- [ ] Les étapes de fabrication correspondent à des **commits** identifiables
      (protocole de session d'`AGENTS.md`).
- [ ] Un prototype (ou premier livrable) passe
      `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      sans erreur et s'affiche correctement dans `index.html`.
- [ ] Les conventions internes du format (nommage des fichiers, structure des
      données, images) sont écrites dans le workflow, pas implicites.
- [ ] Le poids reste raisonnable (images compressées, WebP ≤ 150 Ko par image
      visé, couverture < 300 Ko).
- [ ] L'atelier est inscrit au registre [`../../ateliers/README.md`](../../ateliers/README.md)
      avec son statut (`expérimental` ou `stable`).

## 4. Procédure

1. **Brancher** : `conception/atelier-<nom>` (protocole de session).
2. **Prototyper** si nécessaire — le prototype suit les contraintes du §1 et passe
   par les mêmes vérifications qu'un livrable de production.
3. **Rédiger** `ateliers/<nom-atelier>/WORKFLOW.md` en copiant
   [`GABARIT-WORKFLOW.md`](GABARIT-WORKFLOW.md).
4. **Inscrire** l'atelier dans le registre `ateliers/README.md` (statut
   `expérimental` tant qu'un second livrable n'a pas confirmé le workflow).
5. **PR** avec description structurée ; signaler explicitement les choix de format
   qui mériteraient l'avis de Pierre.
