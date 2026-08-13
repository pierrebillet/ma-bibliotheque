# VISION.md — vision produit de la Bibliothèque

Ce document donne le cap du rôle Bibliothèque : ce que la plateforme cherche à être,
dans quel ordre, et les critères qui déclenchent chaque étape. Il complète la doc
technique du dossier ([`README.md`](README.md)) et pilote la
[`ROADMAP.md`](ROADMAP.md).

## Le but

Rendre le **catalogue de lectures** de Pierre disponible en ligne, **facilement
explorable et beau**, et porter les **fonctionnalités transverses** voulues pour
toutes les lectures (aujourd'hui des romans, demain des catégories de contenus plus
variées). La plateforme est *au service* des lectures : l'objectif majeur
d'innovation du projet est **la forme des lectures interactives elles-mêmes** — la
Bibliothèque doit donc rester la plus simple possible à déployer et maintenir, pour
que l'énergie aille aux livres.

## Proposition principale et hiérarchie produit

L'étude archivée du champ des possibles
([`../archives/dev-mvp/ETUDE-CHAMP-DES-POSSIBLES-MVP.md`](../archives/dev-mvp/ETUDE-CHAMP-DES-POSSIBLES-MVP.md))
définissait cinq directions produit sans les trancher. C'est tranché :

| Direction | Statut |
|---|---|
| **C — Plateforme d'expériences de lecture** (démontrer des formes de lecture interactive) | **Proposition principale** |
| **A — Bibliothèque personnelle du lecteur** (reprise, favoris, préférences) | Service au lecteur, au service de C |
| **D — Liseuse installable et hors ligne** (PWA) | Mode de distribution, palier post-1.0 |
| **B — Catalogue éditorial exploratoire** (collections, parcours, découverte) | Intégrée aux versions proches de 1.0 / 1.x |
| **E — Laboratoire mesurable** (mesure d'usage sobre) | Intégrée en 1.x, pas de mesure avant la 1.0 |

**Utilisateur visé à terme : un public large.** La bibliothèque est une vitrine
ouverte ; n'importe quel lecteur doit pouvoir découvrir, lire, et à terme retrouver
ses lectures. Cela dimensionne les paliers PWA et authentification comme un vrai
service multi-utilisateurs — mais ne les avance pas dans le temps.

## Principes durables

Test de recevabilité de toute proposition d'évolution — une proposition qui casse un
de ces principes doit prouver une valeur nettement supérieure :

1. **Publier un livre = déposer un HTML dans `livres/`.** Jamais de geste plus
   lourd, quel que soit le palier.
2. **Robustesse statique** : URL directe et stable par livre, livres autonomes et
   libres dans leur forme — la couche commune ne limite pas la créativité des
   livres.
3. **Toute couche ajoutée échoue sans empêcher la lecture** : état local, mesure,
   service worker… tout est optionnel et non bloquant.
4. **Zéro dépendance externe et zéro build jusqu'à la 1.0 incluse** : un
   `index.html` autonome, un script Python stdlib, GitHub Pages sans étape de build.
5. **Classer chaque chantier sur la grille des 5 niveaux d'architecture** :
   ① navigateur statique seul → ② + stockage local → ③ + génération par la CI →
   ④ + service externe facultatif → ⑤ backend réellement requis.
   **Le niveau le plus bas qui suffit gagne.**
6. **Critère directeur** (hérité de l'étude et confirmé) : la bonne évolution
   augmente la valeur de la bibliothèque *en conservant* sa simplicité éditoriale,
   sa robustesse statique et la liberté des livres autonomes.

## Les paliers

Chaque palier dit ce qu'il apporte, ce qu'il ne doit pas casser, et les critères de
passage au suivant. On ne saute pas de palier.

### Palier 0 — le prérequis transverse (hors rôle Bibliothèque)

**Le moteur de liseuse unifié et versionné** (`livres/_template/` +
`<meta name="reader-engine">`) — chantier des rôles Conception/Production, décrit
dans l'audit
([`../audits/2026-08-rapport-etonnement.md`](../audits/2026-08-rapport-etonnement.md) §D.3.1)
et dans [`../../ateliers/roman-atelier/WORKFLOW.md`](../../ateliers/roman-atelier/WORKFLOW.md).

Il est nommé ici parce qu'il **conditionne toutes les fonctionnalités transverses**
de la plateforme : sans contrat commun de chapitres/progression dans les livres, pas
de « reprendre ma lecture » fiable, pas de hors-ligne par livre, pas de comptes qui
synchronisent quoi que ce soit. Le dépôt compte aujourd'hui deux familles de moteurs
et six implémentations localStorage divergentes : toute fonctionnalité transverse
construite avant l'unification serait bâtie sur du sable.

### Palier 1 — du MVP à la **1.0 « catalogue public soigné »** (palier actuel)

Ce que c'est : la bibliothèque GitHub Pages actuelle, amenée à un niveau de finition
publique — belle, explorable, accessible, partageable, au schéma de catalogue
extensible.

Discipline : **zéro build, zéro dépendance externe, aucune donnée utilisateur côté
index**. Niveaux d'architecture ① et ③ uniquement.

**Critères de sortie (= la 1.0 est atteinte)** : les chantiers « vers la 1.0 » de la
[`ROADMAP.md`](ROADMAP.md) sont tous faits — hygiène web (favicon, 404, Open
Graph…), CSS purgé, accessibilité de l'index, couvertures optimisées, **schéma de
catalogue v2** (`format`, `variantOf`, durée de lecture, `genre`), tags gouvernés,
catégories déclaratives affichées, page « à propos ».

### Palier 2 — **1.x « exploration et bibliothèque du lecteur »**

Ce que c'est : la 1.0 enrichie des directions B, A et E, dans cet ordre de valeur :

- **B — exploration éditoriale** : collections, parcours de lecture, mises en avant
  calculées depuis le schéma v2 (badges de durée, format, capacités interactives
  déclarées). Le catalogue devient un objet éditorial, pas une grille.
- **A — bibliothèque personnelle, locale d'abord** : reprendre ma lecture, favoris,
  export/import de son état (lots 1 → 4 de
  [`../archives/dev-mvp/ETUDE-FONCTIONNALITES-LOCALES.md`](../archives/dev-mvp/ETUDE-FONCTIONNALITES-LOCALES.md),
  en gardant son ordre délibéré : **portabilité avant visibilité** — l'export existe
  avant la page « Ma liste »). Vocabulaire d'interface : « données enregistrées sur
  cet appareil », jamais « compte », jamais d'avatar — on ne suggère pas une
  persistance serveur qui n'existe pas.
- **E — mesure sobre** : uniquement pour répondre à des questions produit précises
  (quelles formes de lecture fonctionnent ?), avec les principes hérités de l'étude
  analytics : taxonomie d'événements versionnée, **l'usage oui, le contenu non**,
  strictement non bloquant, l'outil n'est pas choisi d'avance (Umami self-hosté
  n'est pas un acquis).

**Critères d'entrée** : 1.0 atteinte ; **palier 0 fait** (moteur unifié) ; `variantOf`
disponible dans le schéma v2 — sinon l'état local indexé par slug recrée le bug
connu « le lecteur qui passe à l'édition illustrée repart de zéro ».

**Préparation du palier 4 à coût quasi nul, dès ce palier** : modèle d'état local
isomorphe au futur modèle distant, identifiants stables, `updatedAt` partout, règles
de fusion définies avant toute synchronisation, séparation préférences locales /
données synchronisables.

### Palier 3 — **PWA « liseuse installable »**

Ce que c'est : la bibliothèque devient installable (écran d'accueil, standalone) et
utilisable hors ligne, cross-plateforme.

Cahier des charges (repris de l'étude, §7) : mise en cache **sélective par livre**
(un bouton « disponible hors ligne », pas tout le catalogue d'office), gestion et
purge du stockage utilisé, bannière de nouvelle version, page hors-ligne explicite,
manifeste PWA généré par la CI (niveau ③), bibliothèque et livres servis depuis la
**même origine** (condition d'un état partagé).

**Le risque à traiter avant tout** : le service worker est le premier composant du
projet capable de **casser durablement** le site pour un visiteur (version obsolète
servie indéfiniment). Une procédure de retour arrière testée (kill-switch du SW) est
un **prérequis d'activation**, pas une amélioration ultérieure. Réserves connues à
instruire : limites iOS, cycles de mise à jour du SW, quotas de stockage.

**Critères d'entrée** : 1.x stable ; moteur unifié en usage réel ; un usage mesuré
(palier 2, direction E) qui justifie l'installation hors ligne — *mesurer avant de
décider*, pas de PWA « parce que c'est la cible ».

### Palier 4 — **comptes utilisateur**

Ce que c'est : authentification et fonctionnalités par utilisateur (synchronisation
multi-appareils, listes partagées, éventuellement contenu privé).

**Déclencheurs objectifs** (conditions d'entrée — au moins un besoin réel constaté,
pas une intention) : demande avérée de synchronisation multi-appareils, récupération
d'identité, listes partagées modifiables, contenu privé ou à droits, notifications
individualisées.

**Arbitrage d'architecture posé dès maintenant** : *l'authentification seule ne
justifie pas de quitter GitHub Pages*. Un backend d'auth/données (type Supabase)
peut servir un frontend statique inchangé ; une web app (rendu serveur, routes,
fonctions) ne se justifie que par des besoins supplémentaires démontrés. La
simplicité de déploiement reste le juge de paix jusqu'au bout.

## Ce qui a été écarté

Issues des études archivées ([`../archives/dev-mvp/`](../archives/dev-mvp)), ces
pistes sont écartées — les rouvrir exige un argument nouveau :

- **Injection au build / retour d'un artefact `_site/`** : contredit le déploiement
  direct depuis `main` et l'autonomie des livres. Seule survit la variante opt-in
  par métadonnée déclarée dans le livre.
- **Umami/Cloudron comme hypothèse par défaut** (et la périphérie n8n) : une
  infrastructure à héberger et maintenir, contraire au focus du projet. Les actifs
  conceptuels de l'étude (taxonomie, funnel, RGPD) restent réutilisables le jour venu.
- **« Fonctions intelligentes »** (embeddings, recherche sémantique, Q&A) :
  disproportionnées pour ce catalogue, coût de build et opacité non justifiés.
- **Profils locaux multiples** sur un appareil partagé : la complexité d'un système
  de comptes sans aucune de ses garanties.
- **Notes textuelles libres** dans l'état local : vie privée et surface de risque,
  écartées par l'étude elle-même.
- **Gamification des statistiques de lecture** : détourne de la lecture, précision
  illusoire.
