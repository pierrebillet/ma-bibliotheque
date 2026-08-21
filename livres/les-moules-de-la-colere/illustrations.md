# Illustrations de « Les Moules de la colère »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/les-moules-de-la-colere/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Tu travailles sur la branche `claude/roman-mafia-mytiliculteurs-6np9oc` de
   ce dépôt (celle où se trouve ce fichier). Tu pousses tes commits sur cette
   branche, jamais sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON
   de `index.html`, ni le texte, ni aucun autre fichier — à une exception
   près : dans le `<head>` de `livres/les-moules-de-la-colere/index.html`,
   complète la meta `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Fable (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Les Moules de la colère :
   chapitres 1 à 6 »), plusieurs commits bienvenus.
5. Quand tout est produit : pousse, puis signale ta passe dans la pull request
   ouverte pour cette branche (outil de génération utilisé, écarts éventuels).

**Contraintes techniques** (pour chaque image, sauf mention contraire dans son
entrée) :

- Format **WebP** ; si ta chaîne ne produit pas de WebP, convertis :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou : magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```
- Images de chapitre et de notice : **1600×900**, poids **≤ 150 Ko**.
- Couverture : **800×1200** (ratio 2:3), poids **< 300 Ko**.
- **Couverture : aucun texte autorisé**, sans exception — ni titre,
  sous-titre, nom, crédit, logo, signature, filigrane ou pseudo-texte. Le
  titre est ajouté par-dessus en HTML dans la bibliothèque.
- Images intérieures : aucun texte lisible incrusté (le tableau blanc du
  chapitre 8 et les étiquettes du chapitre 4 doivent rester **illisibles** —
  suggérer l'écriture, jamais la rendre déchiffrable).
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/les-moules-de-la-colere
  ```

## Bible visuelle commune

Gouache réaliste sur papier à grain visible, dans l'esprit des affiches
maritimes bretonnes contemporaines : formes simplifiées mais crédibles,
touches franches, aucune photo ni photoréalisme. Palette de l'estuaire de la
Vilaine : gris-vert de vase, ardoise, bleu pétrole, blanc cassé des cirés —
réchauffée par l'ocre doré de la falaise de la Mine d'Or, qui sert d'accent
dans presque toutes les images. Lumières rasantes (aubes, couchants, néons
froids pour les scènes nocturnes de fraude) ; ombres longues ; ciels bretons
à éclaircies dramatiques. Ton général : polar lumineux — la tension vient du
cadrage et de la lumière, jamais de la violence montrée. On ne montre
jamais : sang, cadavre, visage de Job (toujours de dos ou à contre-jour),
marque ou enseigne réelle, texte lisible.

Personnages récurrents (les tenir identiques d'une image à l'autre) :

- **Gwenn Le Dantec** : 34 ans, brune, cheveux mi-longs souvent attachés,
  silhouette vive ; ciré sombre ou pull marin ; souvent un carnet à spirale à
  la main ; bottes (parfois une seule, c'est un gag du livre).
- **Fañch Guégan** : 58 ans, carré comme une armoire, casquette usée vissée,
  ciré orange délavé, visage buriné bienveillant.
- **Bernique** : chienne griffon de taille moyenne, poil gris hirsute « de
  paillasson », collier de corde, digne en toutes circonstances.
- **Louis-Marie Caradec** : 66 ans, grand, cheveux blancs drus, sourcils
  fournis, veste de mer propre ; posture de monument.
- **Yvonne Caradec** : 61 ans, petite, très droite, cheveux d'argent coupés
  net, gilet mauve ; gestes millimétrés.
- **Job Le Dantec** : 65 ans, uniquement de dos ou en silhouette, ciré
  sombre, lampe frontale.

## Couverture

- **Fichier** : `couvertures/les-moules-de-la-colere.webp` (à la racine du
  dépôt) — 800×1200, < 300 Ko
- **Sujet** : les bouchots de l'estuaire à marée basse sous un ciel d'orage
  doré, une silhouette de femme et un chien avançant sur la vasière.
- **Prompt** : Bible visuelle ci-dessus. Composition verticale 2:3 :
  alignements de pieux de bouchots noirs convergeant vers l'horizon sur une
  vasière luisante, à marée basse ; ciel d'orage spectaculaire mêlant ardoise
  et ocre doré (lumière de la Mine d'Or), occupant le tiers supérieur (y
  laisser une zone calme pour le titre HTML) ; au tiers inférieur, de dos, la
  petite silhouette de Gwenn en ciré sombre marchant entre les lignes, la
  chienne griffon à son côté ; reflets du ciel dans les flaques. Aucun texte,
  logo, signature, filigrane ou pseudo-texte.
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) :
  « Alignements de pieux de bouchots découverts à marée basse dans l'estuaire
  de la Vilaine, sous un ciel d'orage doré ; une silhouette de femme et un
  chien avancent sur la vasière. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Fils unique
- **Sujet** : la sortie d'église de l'enterrement de Job.
- **Prompt** : Bible visuelle. Sortie d'église de bourg breton un matin
  venteux : six hommes carrés en cirés sombres portent un cercueil clair sur
  le parvis ; au premier plan, une couronne mortuaire en forme de bouée (sans
  texte lisible sur le ruban) ; clocher de granit, ciel à éclaircies, rideaux
  de fer baissés dans la rue commerçante ; assemblée aux mains énormes et
  missels minuscules.
- **Alt de référence** : « Le cercueil de Job sort de l'église de Pénestin,
  porté par six mytiliculteurs en cirés propres, une couronne de fleurs en
  forme de bouée au premier plan. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — L'inventaire
- **Sujet** : Gwenn découvre les carnets de Job dans l'atelier, le soir.
- **Prompt** : Bible visuelle. Intérieur d'atelier mytilicole le soir :
  bassins de purification à l'eau bleutée brassée par les pompes, calibreuse
  au fond, mur de poches et d'étiquettes (illisibles) ; Gwenn en pull marin
  feuillette un carnet à spirale sous une ampoule nue, une étagère de
  carnets alignés derrière elle ; Bernique dort sur un tas de filets ;
  ambiance chaleureuse et studieuse, clair-obscur doux.
- **Alt de référence** : « Dans l'atelier de purification, Gwenn feuillette un
  carnet à spirale près des bassins éclairés, la chienne couchée sur des
  filets. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Basse mer
- **Sujet** : la première marée de Gwenn, à l'aube, sur le tracteur amphibie.
- **Prompt** : Bible visuelle. Estran de l'estuaire de la Vilaine à l'aube :
  un tracteur amphibie aux roues immenses et à l'échappement en périscope
  avance entre des alignements de pieux coiffés de filets ; Fañch conduit,
  Gwenn se tient à l'arrière, Bernique trône sur le garde-boue ; vasière
  luisante trouée de flaques reflétant un ciel rose et gris ; oiseaux d'eau
  au loin.
- **Alt de référence** : « À l'aube, un tracteur amphibie descend sur l'estran
  entre les lignes de bouchots, deux silhouettes et une chienne à bord. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Les moules parlent espagnol
- **Sujet** : le déchargement nocturne au dépôt, vu de la cachette de Gwenn.
- **Prompt** : Bible visuelle. Scène nocturne de polar : hangar de bardage
  gris entrouvert, quai de déchargement faiblement éclairé aux néons froids,
  semi-remorque frigorifique à cul, hayon baissé ; silhouettes transvasant
  des moules d'une poche à l'autre à la chaîne ; palettes filmées dont les
  étiquettes restent illisibles ; premier plan dans l'ombre derrière des
  casiers empilés (point de vue de témoin caché) ; lune aux trois quarts.
- **Alt de référence** : « De nuit, un semi-remorque frigorifique déchargé au
  quai d'un hangar entrouvert, des silhouettes transvasant des moules entre
  des poches, vues d'une cachette. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — La part du crabe
- **Sujet** : la conversation de Gwenn et Morvan sur le barrage d'Arzal.
- **Prompt** : Bible visuelle. Le barrage d'Arzal vu de la rive : Gwenn en
  ciré et un gendarme en bleu marchent côte à côte sur la digue-promenade,
  le tablier du pont mobile levé au-dessus de l'écluse derrière eux ; en
  amont, des centaines de mâts de voiliers sages sur l'eau douce ; en aval,
  l'estuaire et ses vasières ; vent sensible, ciel dynamique.
- **Alt de référence** : « Gwenn et le gendarme Morvan marchent sur le barrage
  d'Arzal, le pont mobile levé au-dessus de l'écluse derrière eux. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Le phare qui ne dit rien
- **Sujet** : la découverte de la cache dans la maquette du musée.
- **Prompt** : Bible visuelle. Intérieur du petit musée de la Maison de la
  Mytiliculture : lumière chaude, photos sépia aux murs, outils anciens
  accrochés ; au centre, la maquette de l'estran au trentième (lignes de
  bouchots en allumettes, chaland miniature), vitrine de plexiglas
  soulevée ; les mains de Gwenn ouvrent le caisson de contreplaqué où l'on
  devine une pochette plastique scotchée ; en retrait, Denise (78 ans,
  chignon strict) observe, trousseau de clés en main.
- **Alt de référence** : « Dans le musée du vieux phare, des mains ouvrent le
  caisson de la maquette de l'estran, une pochette plastique scotchée à
  l'intérieur. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Byssus et coutumes
- **Sujet** : le dîner du syndicat, la tablée tournée vers Gwenn.
- **Prompt** : Bible visuelle. Arrière-salle de café de port le soir : longue
  tablée d'hommes aux mains épaisses, faitouts fumants de moules, verres de
  muscadet ; Louis-Marie préside en bout de table ; tous les regards
  convergent vers Gwenn, seule au milieu de la tablée ; au fond, discrète, la
  silhouette d'Yvonne (gilet mauve) qui sert le café ; guirlandes de fanions,
  chaleur trouble, sourires ambigus.
- **Alt de référence** : « Le dîner du syndicat au café du port : une longue
  tablée de mytiliculteurs sous les guirlandes, tous les regards tournés vers
  Gwenn. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Gré à gré
- **Sujet** : Gwenn reconstitue le système au tableau blanc, la nuit.
- **Prompt** : Bible visuelle. Scène d'enquête nocturne dans l'atelier :
  Gwenn de dos, marqueur à la main, face à un grand tableau blanc saturé de
  colonnes, de flèches et d'un organigramme dont la case du sommet est
  entourée trois fois (toute écriture illisible — traits et gribouillis
  suggérés) ; lampe d'architecte, bassins éteints en arrière-plan, Bernique
  endormie ; ambiance obsessionnelle et précise.
- **Alt de référence** : « Gwenn de dos face à un grand tableau blanc couvert
  de flèches, de dates et d'un organigramme, la nuit dans l'atelier. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — La visite
- **Sujet** : le face-à-face de Gwenn et d'Yvonne autour du thé.
- **Prompt** : Bible visuelle. Duel domestique dans la lumière d'après-midi
  de l'atelier : deux femmes assises face à face à une table simple ;
  Yvonne, cheveux d'argent et gilet mauve, très droite, sa tasse exactement
  centrée sur la soucoupe ; Gwenn, sur ses gardes, les mains autour de sa
  tasse ; entre elles, un far breton sur un torchon à carreaux rouge et
  blanc ; tension polie, presque cérémonielle ; profondeur vers les bassins.
- **Alt de référence** : « Deux femmes face à face à la table de l'atelier
  autour d'un thé, un far breton sur un torchon à carreaux entre elles. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — Coefficient 108
- **Sujet** : Gwenn piégée par la marée montante près du quad renversé.
- **Prompt** : Bible visuelle. Climax nocturne de grande marée : estran
  argenté par une lune aux trois quarts, un quad renversé enfoncé dans une
  souille, Gwenn trempée creusant à deux mains près de la roue, Bernique
  creusant à son côté ; langues d'eau noire arrivant de partout entre les
  lignes de pieux ; au loin, un point de phare de tracteur ; tension
  maximale, beauté froide, aucun effet gore.
- **Alt de référence** : « De nuit, sous la lune, une femme creuse le sable
  près d'un quad renversé pendant que l'eau de la marée montante l'encercle,
  une chienne creusant à ses côtés. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — L'addition
- **Sujet** : la perquisition du dépôt à l'aube, sous les yeux du village.
- **Prompt** : Bible visuelle. Petit matin gris-doré devant un hangar de
  négoce : fourgons de gendarmerie, ruban de balisage, enquêteurs portant des
  cartons scellés et une étiqueteuse industrielle sur un diable ; au premier
  plan et sur les seuils alentour, des villageois immobiles qui regardent en
  silence, dignité de photo de classe ; aucune inscription lisible.
- **Alt de référence** : « À l'aube, des fourgons de gendarmerie devant le
  dépôt, des enquêteurs emportant des cartons sous les yeux immobiles des
  villageois. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — La saison
- **Sujet** : la Fête de la Moule au port de Tréhiguier, un an après.
- **Prompt** : Bible visuelle. Fête populaire estivale sur le quai de
  Tréhiguier : faitouts hauts comme des chaudières d'où monte la vapeur,
  files joyeuses, fanions multicolores, enfants et chiens (dont Bernique,
  une frite en gueule) ; au stand, Gwenn sert, Fañch officie aux faitouts ;
  au fond du quai, le petit phare blanc éteint ; lumière dorée de fin
  d'après-midi d'août, ambiance de victoire tranquille ; banderoles sans
  texte lisible.
- **Alt de référence** : « La Fête de la Moule au port de Tréhiguier :
  faitouts géants fumants, foule d'été, fanions, le vieux phare au fond du
  quai. »

## Images de notices

### `images/codex-gwenn-le-dantec.webp`

- **Notice** : Gwenn Le Dantec (personnage)
- **Sujet** : portrait de l'auditrice sur le quai au petit matin.
- **Prompt** : Bible visuelle. Portrait en pied de Gwenn (34 ans, brune,
  cheveux attachés), ciré sombre, bottes, carnet à spirale ouvert à la main,
  regard précis ; lumière d'aube froide sur le quai de Tréhiguier ;
  arrière-plan flou de chalands et de poches de moules.
- **Alt de référence** : « Une femme d'une trentaine d'années en ciré, carnet
  à la main, debout sur un quai mytilicole au petit matin. »

### `images/codex-job-le-dantec.webp`

- **Notice** : Job Le Dantec (personnage)
- **Sujet** : Job de dos face à ses lignes, à l'aube.
- **Prompt** : Bible visuelle. Silhouette de dos d'un homme de 65 ans en ciré
  sombre, lampe frontale allumée, carnet dans la poche arrière, face à des
  alignements de pieux à marée basse ; brume d'aube sur l'estuaire ;
  ambiance recueillie, jamais de visage.
- **Alt de référence** : « Un mytiliculteur âgé de dos, lampe frontale
  allumée, face à ses lignes de bouchots dans la lumière du très petit
  matin. »

### `images/codex-fanch-guegan.webp`

- **Notice** : Fañch Guégan (personnage)
- **Sujet** : portrait de Fañch près de son tracteur.
- **Prompt** : Bible visuelle. Portrait de Fañch (58 ans, carré, visage
  buriné bienveillant, casquette usée, ciré orange délavé), adossé à la roue
  immense d'un tracteur amphibie sur la vasière, bras croisés ; lumière
  grise et douce de fin de marée.
- **Alt de référence** : « Un homme trapu en ciré et casquette, debout près
  d'un tracteur amphibie sur l'estran, bras croisés. »

### `images/codex-bernique.webp`

- **Notice** : Bernique (personnage)
- **Sujet** : portrait de la chienne sur le quai.
- **Prompt** : Bible visuelle. Portrait animalier attendrissant et digne :
  chienne griffon au poil gris hirsute « de paillasson », collier de corde,
  assise sur les planches d'un quai, l'air à la fois noble et légèrement
  mouillé ; arrière-plan de poches de moules et de cordages ; lumière chaude
  de fin d'après-midi.
- **Alt de référence** : « Une chienne griffon au poil gris hirsute, assise
  sur un quai, l'air à la fois digne et mouillé. »

### `images/codex-louis-marie-caradec.webp`

- **Notice** : Louis-Marie Caradec (personnage)
- **Sujet** : le patriarche devant ses chalands.
- **Prompt** : Bible visuelle. Portrait imposant de Louis-Marie (66 ans,
  grand, cheveux blancs drus, sourcils fournis, veste de mer propre), bras
  croisés sur le quai devant trois chalands mytilicoles amarrés ; posture de
  monument, mais regard légèrement perdu vers le large ; lumière de fin de
  matinée.
- **Alt de référence** : « Un patriarche breton d'une soixantaine d'années,
  bras croisés sur un quai devant trois chalands, regard au loin. »

### `images/codex-yvonne-caradec.webp`

- **Notice** : Yvonne Caradec (personnage)
- **Sujet** : la Daronne à sa table, tasse centrée au millimètre.
- **Prompt** : Bible visuelle. Portrait d'Yvonne (61 ans, petite, très
  droite, cheveux d'argent coupés net, gilet mauve) assise à une table de
  ferme ; tasse de thé exactement centrée sur la soucoupe, torchon à
  carreaux plié en quatre à angles vifs ; lumière domestique douce ; regard
  d'une intelligence calme et glaciale ; aucun élément menaçant explicite —
  toute la menace est dans l'ordre.
- **Alt de référence** : « Une femme aux cheveux d'argent en gilet mauve,
  assise très droite à une table de cuisine, une tasse de thé exactement
  centrée sur sa soucoupe. »

### `images/codex-maison-de-la-mytiliculture.webp`

- **Notice** : La Maison de la Mytiliculture (lieu)
- **Sujet** : le vieux phare de Tréhiguier à marée basse.
- **Prompt** : Bible visuelle. Le phare de Tréhiguier au bout du quai : tour
  blanche trapue à lanterne éteinte, toit de tuiles, à marée basse ;
  chalands mytilicoles posés sur la vase au premier plan ; ciel breton à
  éclaircies dorées ; sentiment de sentinelle en retraite.
- **Alt de référence** : « Un petit phare blanc à toit de tuiles au bout d'un
  quai, à marée basse, chalands échoués au premier plan. »

### `images/codex-la-mine-d-or.webp`

- **Notice** : La Mine d'Or (lieu)
- **Sujet** : la falaise ocre au couchant, les bouchots en contrebas.
- **Prompt** : Bible visuelle. Vue large de la plage de la Mine d'Or au
  soleil couchant : falaise ocre-doré flamboyante, longue plage humide
  réfléchissant le ciel ; au loin dans la baie, des alignements de pieux de
  bouchots noirs à contre-jour ; quelques minuscules silhouettes de
  promeneurs photographiant la falaise, aucune ne regardant les bouchots.
- **Alt de référence** : « La falaise ocre de la Mine d'Or embrasée par le
  couchant, au-dessus d'une longue plage où la marée basse découvre des
  lignes de bouchots. »

### `images/codex-le-scal.webp`

- **Notice** : Le Scal (lieu)
- **Sujet** : l'estran nu, le quad seul entre les lignes.
- **Prompt** : Bible visuelle. Estran immense et nu à marée basse, lignes de
  bouchots convergeant vers l'horizon ; entre deux lignes, un quad seul, à
  l'arrêt ; ciel gris lourd, flaques réfléchissantes ; sentiment de silence
  et d'exposition ; aucune figure humaine.
- **Alt de référence** : « Alignements de pieux de bouchots sur un estran nu
  à marée basse, un quad à l'arrêt entre deux lignes sous un ciel gris. »

### `images/codex-le-bouchot.webp`

- **Notice** : Le bouchot (concept)
- **Sujet** : gros plan documentaire sur des pieux chargés de moules.
- **Prompt** : Bible visuelle. Gros plan texturé sur trois pieux de bouchots
  couverts de moules bleu-noir serrées, filet catin visible, eau de marée
  descendante autour ; lumière rasante faisant briller les coquilles
  mouillées ; précision quasi naturaliste dans le rendu gouache.
- **Alt de référence** : « Gros plan sur des pieux de bouchots chargés de
  moules, entourés de leur filet, à marée descendante. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/les-moules-de-la-colere.webp` | à produire |
| `images/chapter-01.webp` | à produire |
| `images/chapter-02.webp` | à produire |
| `images/chapter-03.webp` | à produire |
| `images/chapter-04.webp` | à produire |
| `images/chapter-05.webp` | à produire |
| `images/chapter-06.webp` | à produire |
| `images/chapter-07.webp` | à produire |
| `images/chapter-08.webp` | à produire |
| `images/chapter-09.webp` | à produire |
| `images/chapter-10.webp` | à produire |
| `images/chapter-11.webp` | à produire |
| `images/chapter-12.webp` | à produire |
| `images/codex-gwenn-le-dantec.webp` | à produire |
| `images/codex-job-le-dantec.webp` | à produire |
| `images/codex-fanch-guegan.webp` | à produire |
| `images/codex-bernique.webp` | à produire |
| `images/codex-louis-marie-caradec.webp` | à produire |
| `images/codex-yvonne-caradec.webp` | à produire |
| `images/codex-maison-de-la-mytiliculture.webp` | à produire |
| `images/codex-la-mine-d-or.webp` | à produire |
| `images/codex-le-scal.webp` | à produire |
| `images/codex-le-bouchot.webp` | à produire |
