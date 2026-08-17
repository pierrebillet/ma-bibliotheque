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
- **Les 10 métadonnées** du `<head>` du point d'entrée : `book:title`,
  `book:author`, `book:description`, `book:tags`, `book:date`, plus les cinq
  metas qualitatives à vocabulaire fermé du schéma v2 (`book:genre`,
  `book:format`, `book:tonalite`, `book:exigence`, `book:audience` — valeurs
  admises dans [`../bibliotheque/CATALOGUE.md`](../bibliotheque/CATALOGUE.md)).
  `book:author` = le **modèle** qui écrit (règle d'or d'`AGENTS.md`).
  `book:variant-of` (slug d'un livre existant) est optionnelle et réservée aux
  éditions dérivées.
- **Couverture** : `couvertures/<slug>.jpg|png|webp`, ratio 2:3, nom = slug exact,
  **sans aucun texte dans l'image** (ni titre, sous-titre, nom, crédit, logo,
  signature, filigrane ou pseudo-texte). Le titre et les métadonnées sont
  superposés par l'interface HTML de la bibliothèque ; tout crédit nécessaire
  reste dans le livre ou sa documentation, jamais dans le fichier de couverture.
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

## 3. Le standard de recette

Un `WORKFLOW.md` est une **recette de cuisine** : elle doit produire le résultat
attendu à chaque exécution, par n'importe quel agent (Claude Code, Codex ou autre,
de façon indifférenciée). Concrètement :

- **Exécutable à froid** : la recette ne suppose aucun contexte conversationnel —
  un agent qui n'a lu que `AGENTS.md` et le workflow a tout ce qu'il faut (les
  exigences transverses sont référencées par lien, ex. [`PREFERENCES.md`](PREFERENCES.md),
  jamais supposées connues).
- **Chaque étape est un contrat** : *entrée* (ce dont l'étape a besoin) → *travail*
  → *sortie* (les fichiers produits/modifiés) → *critère de fin* (comment savoir
  que c'est fini) → **commit attendu** (message type en français).
- **Commandes exactes** : toute vérification est une commande copiable-collable ou
  une observation objective (« le fichier X contient Y »), pas un jugement.
- **Agent-agnostique strictement** : aucune référence à un outil, une fonction ou
  une interface propre à un agent donné (« utilise ta fonction X », « ouvre ton
  panneau Y » sont interdits). Uniquement des fichiers, des commandes shell/python
  et des critères observables.
- **Chemins exacts** : chaque fichier mentionné l'est par son chemin complet depuis
  la racine du dépôt.
- **Versionnée** : numéro de version en tête, changelog des évolutions avec leur
  pourquoi ; le livrable produit trace la version utilisée
  (`<meta name="book:workflow" content="<atelier> vN">` — meta **lue par le
  générateur**, qui en tire la `nature` du livre : le nom d'atelier doit être
  celui du dossier `ateliers/<nom-atelier>/`, au caractère près).

Toute interprétation qu'un agent Production a dû faire pendant une exécution est un
**défaut de la recette** : elle doit être remontée dans la PR et corrigée par une
version suivante (boucle d'amélioration de la [`VISION.md`](VISION.md)).

## 4. Critères d'acceptation d'un nouvel atelier

- [ ] Le `WORKFLOW.md` respecte le standard de recette du §3 (test : le faire
      exécuter par un agent à froid, idéalement un agent différent de celui qui
      l'a écrit).
- [ ] L'atelier fournit son **gabarit de brief** `ateliers/<nom-atelier>/BRIEF.md`
      (copié de [`GABARIT-BRIEF.md`](GABARIT-BRIEF.md)) : le document unique
      que Pierre remplit pour lancer une production — identité obligatoire,
      champs optionnels avec leurs défauts, exemple rempli.
- [ ] Il décline le socle éditorial [`PREFERENCES.md`](PREFERENCES.md) sans le
      contredire ni le recopier.
- [ ] Les étapes de fabrication correspondent à des **commits** identifiables
      (protocole de session d'`AGENTS.md`).
- [ ] Un prototype (ou premier livrable) passe
      `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      sans erreur et s'affiche correctement dans `index.html`.
- [ ] Les conventions internes du format (nommage des fichiers, structure des
      données, images) sont écrites dans le workflow, pas implicites.
- [ ] La **nature** de l'atelier est enregistrée dans la table `ATELIER_NATURE`
      de `scripts/build_catalog.py` (§6) — et, si cette nature est inédite, le
      chantier Bibliothèque qui lui crée son onglet d'index est passé avant.
- [ ] La couverture ne contient aucun texte incrusté ; cette vérification est
      visuelle et s'applique aussi aux lettres ou pseudo-lettres produites par
      un générateur d'images.
- [ ] Le poids reste raisonnable (images compressées, WebP ≤ 150 Ko par image
      visé, couverture < 300 Ko).
- [ ] L'atelier est inscrit au registre [`../../ateliers/README.md`](../../ateliers/README.md)
      avec son statut (`expérimental` ou `stable`).

## 5. Procédure

1. **Brancher** : `conception/atelier-<nom>` (protocole de session).
2. **Prototyper** si nécessaire — le prototype suit les contraintes du §1 et passe
   par les mêmes vérifications qu'un livrable de production.
3. **Rédiger** `ateliers/<nom-atelier>/WORKFLOW.md` en copiant
   [`GABARIT-WORKFLOW.md`](GABARIT-WORKFLOW.md) (version 1, changelog
   initialisé) **et** `ateliers/<nom-atelier>/BRIEF.md` en copiant
   [`GABARIT-BRIEF.md`](GABARIT-BRIEF.md) — l'atelier naît avec son gabarit de
   brief, dès la première version.
4. **Inscrire** l'atelier dans le registre `ateliers/README.md` (statut
   `expérimental` tant qu'un second livrable n'a pas confirmé le workflow).
5. **PR** avec description structurée ; signaler explicitement les choix de format
   qui mériteraient l'avis de Pierre.

Pour **faire évoluer** un atelier existant : même protocole, la modification du
`WORKFLOW.md` incrémente la version et documente le pourquoi au changelog.

## 6. Cohabitation des ateliers

Plusieurs ateliers produisent des livrables de formats différents, tous affichés
dans le même catalogue. Trois règles suffisent pour qu'ils cohabitent :

- **Déclaration au catalogue (schéma v2)** : un atelier déclare deux choses, et
  ni l'une ni l'autre ne passe par les tags (dont la gouvernance est le chantier 6
  de la [roadmap Bibliothèque](../bibliotheque/ROADMAP.md)) :
  1. **sa nature** — en enregistrant `<nom-atelier> → nature` dans la table
     `ATELIER_NATURE` de `scripts/build_catalog.py`. Le générateur lit le nom
     d'atelier dans `<meta name="book:workflow">` (suffixe ` vN` retiré) et en
     dérive la `nature` du livre ; un atelier absent de la table retombe sur
     `fiction`. Aucune meta de nature n'est écrite par l'auteur. Si la nature du
     nouvel atelier est **inédite** (ni `fiction` ni `reportage`), elle crée un
     nouvel onglet à l'index : c'est un **chantier Bibliothèque préalable**, dans
     une PR séparée (§1, dernier point), avant que l'atelier ne soit accepté ;
  2. **les vocabulaires fermés que ses livrables renseignent dans le `<head>`** —
     `book:genre`, `book:format`, `book:tonalite`, `book:exigence`,
     `book:audience` (valeurs admises : [`CATALOGUE.md`](../bibliotheque/CATALOGUE.md)).
     Le `WORKFLOW.md` de l'atelier dit lesquelles conviennent à son format et avec
     quel défaut, pour que deux livres du même format soient toujours étiquetés
     pareil ; il ne redéfinit jamais le vocabulaire de son côté.
- **Partage de briques** : le moteur de lecture commun vit dans `livres/_template/`
  ([`ROADMAP.md`](ROADMAP.md), chantier 2) et chaque livre déclare la version
  embarquée par `<meta name="reader-engine">`. Chaque atelier annonce dans le
  registre [`../../ateliers/README.md`](../../ateliers/README.md) le moteur qu'il
  utilise : le template (et sa version) ou un moteur propre. On sait ainsi d'un
  coup d'œil quels ateliers profitent d'une amélioration du template.
- **Nouvel atelier ou nouvelle version ?** Un nouveau *type de livrable* → un
  nouvel atelier ; une amélioration du *même* type de livrable → une version +1 du
  `WORKFLOW.md` existant. Deux ateliers ne produisent jamais le même type de
  livrable (registre : « un par type de livrable »).

Ces règles ne demandent rien au rôle Bibliothèque : quand un format a besoin d'un
champ de catalogue ou d'un comportement d'index nouveau, cela reste un chantier
Bibliothèque préalable (§1, dernier point).
