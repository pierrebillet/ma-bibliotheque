# Concours d'écriture — heroic fantasy jeunes adultes (septembre 2026)

Prompt de lancement commun à plusieurs modèles frontier (Claude Fable, Astra…).
Chaque modèle reçoit **le même message**, dans sa propre session ouverte sur ce
dépôt, et fabrique son roman seul. Le concours s'arrête à la fin de la passe
auteur de `roman-atelier` v9 : pull request ouverte, manifeste d'illustrations
committé, **aucune image produite**. La passe illustrateur viendra après, sur le
ou les livres retenus.

Pierre juge les livres dans la liseuse ; la grille est annoncée aux concurrents
(§« Ce qui est jugé ») pour qu'ils sachent où porter l'effort.

## Message de lancement (à coller tel quel dans chaque session)

```markdown
Tu es un agent Production du dépôt `ma-bibliotheque`. Tu participes à un
concours d'écriture : plusieurs modèles frontier reçoivent ce même message et
écrivent chacun un roman à partir du brief ci-dessous. Les livres seront lus de
bout en bout dans la liseuse et comparés. Tu es seul sur ton livre : personne ne
relira ni ne corrigera derrière toi.

## Cadre de travail

- **Recette** : `ateliers/roman-atelier/WORKFLOW.md` (v9), **passe auteur
  uniquement** — étapes 1 à 5b, étape 4 comprise (champs d'images renseignés
  dans l'îlot + manifeste `livres/<slug>/illustrations.md` rédigé depuis
  `ateliers/roman-atelier/GABARIT-ILLUSTRATIONS.md`). Le manifeste fait
  partie des livrables attendus : il sera exécuté tel quel par un agent
  illustrateur lancé ensuite. Tu ne produis **aucune image** : le concours
  s'arrête à la pull request de fin de passe auteur.
- **À lire avant d'écrire une ligne**, dans cet ordre : `AGENTS.md`,
  `ateliers/roman-atelier/WORKFLOW.md`, `ateliers/TRONC-COMMUN.md`,
  `docs/conception/PREFERENCES.md`, `livres/_template/DONNEES.md`,
  `ateliers/roman-atelier/GABARIT-ILLUSTRATIONS.md`. Rien d'autre n'est
  supposé connu ; ne copie jamais le moteur depuis un livre publié, seulement
  depuis `livres/_template/`.
- **Effort** : si ton environnement permet de régler ton niveau de
  raisonnement, utilise le maximum disponible (xhigh) pour toute la session,
  y compris pour les sub-agents que tu délègues (même modèle que toi).
- **Titre et slug** : à toi de les choisir. Slug kebab-case ASCII, unique —
  vérifie qu'il n'existe pas déjà dans `livres/`. Branche `atelier/roman-<slug>`.
- **`book:author`** : le nom exact de ton modèle et de sa version, sous la forme
  « <Modèle> (texte) ». C'est l'objet même du concours : pas de pseudonyme,
  pas d'approximation.
- **Aucune question à Pierre** : tout ce que le brief ne fixe pas est ton choix
  d'auteur. Tu le documentes dans `livres/<slug>/brief.md` (le brief recopié
  tel quel, suivi d'une section « Lecture du brief par l'auteur ») et dans la PR.
- **Fin de session** : PR ouverte selon le protocole d'`AGENTS.md`
  (Rôle : Production / roman-atelier v9), portant la mention
  « Concours heroic fantasy YA — septembre 2026 » et
  « En attente de la passe illustrateur — `livres/<slug>/illustrations.md` ».
  Tu ne merges rien.
- **Interdits** : jamais `catalog.json` ni le bloc `#demo-catalog`, jamais de
  push sur `main`, aucune ressource distante, aucune édition dérivée.

## Ce qui est jugé

1. **Le plaisir de lecture** — l'incipit fait sa promesse dès la première page,
   la voix est reconnaissable, le point de vue et le temps du récit tiennent
   de bout en bout, chaque fin de chapitre donne envie d'ouvrir le suivant.
2. **La construction** — une bascule par chapitre, une chute qui paie la
   promesse émotionnelle et répond, même obliquement, à la question
   thématique ; un monde cohérent, sans contradiction entre le récit et le
   codex.
3. **La langue** — registre littéraire soigné et vivant, dialogues qui
   sonnent, montrer plutôt qu'expliquer, typographie française uniforme, zéro
   coquille.
4. **L'exploration** — un codex qui récompense la curiosité sans jamais être
   nécessaire, des mentions posées là où elles servent, une carte et un graphe
   qui se révèlent au bon moment.
5. **Le relai illustrateur** — un manifeste autoportant : bible visuelle qui
   décrit une fois pour toutes les personnages et lieux récurrents, une entrée
   par image, prompts précis et cohérents avec les `visualDescription`.
6. **La discipline** — `verifier.py --sans-images` et `build_catalog.py`
   verts, commits d'étapes en français, écarts au plan resynchronisés dans le
   même commit, checklist auteur intégralement cochée.

Éliminatoire : livre inachevé, manifeste `illustrations.md` absent ou
incomplet (une image de l'îlot sans entrée, ou l'inverse), vérificateur en
défaut, `book:author` inexact, contenu hors public.

## Brief

# Brief — Concours heroic fantasy jeunes adultes

## Identité (obligatoire)
- **Pitch** : un roman d'heroic fantasy pour jeunes adultes, en français, dans
  un monde secondaire entièrement inventé. L'histoire est la tienne ; elle
  contient nécessairement :
  - un monde qui tient debout — institutions, métiers, géographie, nourriture,
    droit, croyances — et dont la magie (ou le savoir qui en tient lieu) obéit
    à des règles et a un prix ;
  - une héroïne ou un héros de seize à vingt ans qui part d'une position de
    faiblesse ou de marge et grandit par ses choix, pas par ce qu'on lui a
    prédit ;
  - un voyage ou une quête concrète, avec des compagnons dont chacun a sa
    propre raison d'être là et sa propre trajectoire ;
  - un antagoniste qui a raison de son point de vue ;
  - de l'aventure véritable : des dangers, des décisions irréversibles, des
    pertes, des victoires payées.
  L'idée centrale, la question thématique et la promesse émotionnelle sont à
  toi ; elles figurent dans le bloc `world` et le livre les tient.
- **Slug proposé** : au choix de l'auteur.

## Cadrage éditorial (optionnel)
- **Genre** : heroic fantasy — `book:genre` = `fantasy`.
- **Ton** : élan et lumière. Tension retenue plutôt que spectaculaire ; le
  souffle épique se gagne par la précision des gestes et des lieux, pas par
  les adjectifs. L'humour fin est bienvenu s'il sert la voix. `book:tonalite`
  au choix, sauf `sombre`.
- **Longueur** : libre — l'auteur dimensionne chapitres et notices à la
  pertinence, sans jamais écrire pour remplir (socle §« Quantités »).
- **Public** : jeunes adultes — `book:audience` = `ados et adultes` ;
  `book:exigence` = `accessible` ou `intermédiaire`. Violence possible mais
  jamais graphique ; romance possible mais pudique.
- **Codex** : 20 à 35 notices, dans une voix incarnée — un document du monde
  (chronique, bestiaire, carnet de route, registre d'une guilde, manuel d'un
  métier…), pas une encyclopédie neutre. Exploration dense (repère ≥ 40 % des
  blocs porteurs d'une mention, sans sur-lier).

## Ancrage réel (optionnel)
- Aucun : monde secondaire, pas d'étape 0. En revanche l'onomastique et la
  toponymie doivent **sonner en français** — pas de noms anglo-saxons ni de
  suffixes génériques de fantasy — et la texture du réel vient des métiers,
  des objets, des gestes et de la cuisine du monde inventé.

## Illustrations (optionnel)
- **Volume** : défaut de la recette — 1 image par chapitre + couverture +
  environ un tiers des notices (personnages, lieux, créatures ; pas les
  concepts abstraits).
- **Direction artistique** : proposée par l'auteur dans la bible visuelle du
  manifeste. Le manifeste est autoportant (l'illustrateur n'aura pas lu le
  livre) ; les prompts d'images peuvent être rédigés en anglais si tu juges
  que cela sert les générateurs, tout le reste du manifeste en français ;
  couverture strictement sans texte.

## Modules de lecture (optionnel)
- **Carte des lieux** : oui — le territoire du voyage, 6 à 12 lieux, fond
  schématique dessiné dans l'îlot.
- **Graphe de relations** : oui — personnages et factions ; au moins un lien
  dont l'existence est elle-même une révélation (`unlockBlock`).

## Divers (optionnel)
- **Effet recherché sur le lecteur** : qu'il veuille lire le chapitre suivant
  à chaque fin de chapitre ; qu'il admire le protagoniste pour ce qu'il a
  choisi, pas pour ce qu'il a reçu ; qu'il referme le livre avec l'envie de
  repartir dans ce monde — et que la fin ne soit pas une défaite.
- **Fonctionnalités hors socle** : aucune.
- **Contraintes et envies** :
  - **Interdits** : l'élu et la prophétie ; le seigneur des ténèbres sans
    mobile ; l'école de magie ; l'exposition du monde en premier chapitre ;
    la fin ouverte qui promet une suite — l'histoire tient en un tome.
  - **Envies** : une magie (ou un savoir) qui coûte à qui s'en sert ; des
    adultes ni absents ni idiots ; au moins un moment de pur émerveillement
    par tiers de livre ; un objet du quotidien du monde qui devient central
    au récit ; des titres de chapitres qui évoquent sans divulgâcher.
```

## Après le concours

- Lecture et classement par Pierre dans la liseuse (grille ci-dessus).
- Passe illustrateur sur le ou les livres retenus : message de relai du
  `WORKFLOW.md` §« Le relai illustrateur », manifeste `illustrations.md` de la
  branche du livre.
- Les livres non retenus restent sur leur branche (PR non mergée) : la trace
  « quel modèle a écrit quoi » est l'objet du projet.
