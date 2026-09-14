# Illustrations de « Le Fleuve et la Citadelle »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/le-fleuve-et-la-citadelle/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Le brief de ce livre prévoit que l'illustration a lieu **après merge** de la
   version texte : tu travailles donc sur une branche dédiée créée depuis
   `main` (ex. `atelier/illustrations-le-fleuve-et-la-citadelle`), et tu ouvres une pull request
   pour elle ; jamais de push sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON de
   `index.html`, ni le texte, ni aucun autre fichier — à une exception près :
   dans le `<head>` de `livres/le-fleuve-et-la-citadelle/index.html`, complète la meta
   `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Fable (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Le Fleuve et la Citadelle :
   chapitres 1 à 6 »), plusieurs commits bienvenus.
5. Quand tout est produit : pousse, puis signale ta passe dans la pull request
   (outil de génération utilisé, écarts éventuels).

**Contraintes techniques** (pour chaque image, sauf mention contraire dans son
entrée) :

- Format **WebP** ; si ta chaîne ne produit pas de WebP, convertis :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou : magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```
- Images de chapitre et de notice : **1600×900**, poids **≤ 150 Ko**.
- Couverture : **800×1200** (ratio 2:3), poids **< 300 Ko**.
- **Couverture : aucun texte autorisé**, sans exception — ni titre, sous-titre,
  nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre est ajouté
  par-dessus en HTML dans la bibliothèque.
- Images intérieures : aucun texte lisible incrusté — les tablettes de cire,
  la tessère du mot d'ordre et les papyrus portent des signes **illisibles**
  (suggérer l'écriture, jamais la rendre déchiffrable) ; aucune inscription
  latine ou grecque lisible sur les monuments.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/le-fleuve-et-la-citadelle
  ```

## Bible visuelle commune

Peinture à l'huile sur toile à grain visible, dans l'esprit des grands paysagistes et des peintres d'histoire du XIXᵉ siècle (Alma-Tadema pour les intérieurs, les paysages d'hiver des peintres du Danube pour le fleuve), sans photoréalisme ni rendu numérique lisse : touches franches, matière, lumière naturelle. Palette de la Pannonie et du camp : gris de glace, brun de cuir et de boue, blanc cassé des tuniques, ocre des tentes et des murs de brique, bronze des casques — réchauffée par deux accents qui reviennent partout : l'or des lampes à huile et le rouge éteint de la pourpre impériale, jamais vif. Lumières basses et rasantes : aubes de neige, crépuscules sur l'eau, lampes sous la tente ; ciels immenses. Ton général : gravité sans emphase — la tension vient du cadrage, des mains et des visages, jamais du sang. On ne montre jamais : sang, cadavres, la tête de Cassius, un visage de mort en gros plan, le rite d'Éleusis lui-même, texte lisible, marques ou reconstitutions de péplum (pas de cuirasses rutilantes de cinéma). Personnages traités avec réalisme et retenue, sans idéalisation ; les Romains ont des visages méditerranéens et pannoniens variés ; les barbares ne sont jamais caricaturés.

Personnages récurrents (les tenir identiques d'une image à l'autre) :

- **Marc Aurèle** : cinquante ans au début, cinquante-huit à la fin ; barbe pleine et bouclée qui grisonne puis blanchit, cheveux bouclés courts, paupières lourdes, regard baissé ou levé, visage fatigué et bienveillant, d'après la statue équestre du Capitole et les bustes du dernier type ; en campagne, tunique et manteau de pourpre passée agrafé à l'épaule droite (paludamentum), jamais de cuirasse ; à Rome, toge. Il a souvent froid : couverture ou manteau serré.
- **Nikias** : vingt-deux à trente-trois ans ; brun, cheveux courts, visage aigu et concentré, mince ; tunique de lin écru courte, ceinture, sandales ; un stylet d'os derrière l'oreille ; une tablette de cire à quatre volets ou un coffre de cuir toujours à portée.
- **Faustine** : quarante-cinq ans ; visage grave, coiffure à bandeaux ondulés relevés en chignon bas (d'après ses portraits), palla bleu jacinthe.
- **Commode** : treize à dix-huit ans ; blond bouclé, visage plein, large d'épaules, beau ; toge blanche ou tunique brodée ; toujours un peu trop bien dressé.
- **Pompeianus** : cinquante-cinq ans ; visage osseux tanné, cheveux gris ras, barbe rase, cuirasse de cuir à lanières, manteau sombre.
- **Galien** : quarante ans ; barbe noire soignée, sourcils arqués, tunique grecque, mains fines.
- **Hérode Atticus** : soixante-quinze ans ; cheveux et barbe blancs abondants, manteau grec, long bâton.
- **Avidius Cassius** : cinquante-cinq ans ; grand, sec, cheveux gris ras, visage dur ; cuirasse d'apparat, manteau rouge.
- **Soldats** : cottes de mailles ou cuirasses segmentées, casques de bronze, boucliers ovales ou rectangulaires, bottes fermées et braies en hiver, manteaux de laine à capuche (paenula) sous la pluie ; les cavaliers sarmates en armures d'écailles, longues lances à deux mains.

## Couverture

- **Fichier** : `couvertures/le-fleuve-et-la-citadelle.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : l'empereur écrivant sous la tente, le fleuve derrière lui.
- **Prompt** : bible visuelle + composition verticale 2:3 : au premier plan, de trois quarts, un homme d'une cinquantaine d'années à la barbe bouclée grisonnante, manteau militaire de pourpre passée sur une tunique, assis sur un tabouret pliant devant l'ouverture d'une tente de cuir, écrivant au stylet sur une tablette de cire posée sur ses genoux, à la lueur d'une lampe à huile ; derrière lui, par l'ouverture de la tente, un grand fleuve gris sous la neige et, sur l'autre rive, une plaine blanche sans limite ; point focal sur la main et la tablette ; tiers supérieur du cadre laissé calme (ciel de neige, haut de la tente) pour le titre qui sera superposé en HTML ; aucun texte, logo, signature, filigrane ou pseudo-texte.
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) : « Un homme barbu en manteau militaire, assis sur un tabouret devant une tente, écrit sur une tablette de cire à la lueur d’une lampe ; derrière lui, un grand fleuve gris sous la neige. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — La voiture d’Altinum
- **Sujet** : Une voiture de voyage arrêtée dans le brouillard d’une lagune d’hiver ; un homme en manteau soutient la tête d’un autre, affaissé contre la portière ouverte.
- **Prompt** : bible visuelle + Plan moyen sur une lourde voiture de voyage à quatre roues arrêtée sur une route de lagune noyée de brouillard, janvier ; la portière est ouverte ; à l’intérieur, un homme barbu en manteau de pourpre passée soutient la tête d’un homme blond affaissé, la bouche entrouverte ; une coupe renversée sur le marchepied ; cavaliers de l’escorte flous dans la brume, roseaux ; lumière blanche et sourde.
- **Alt de référence** : « Une voiture de voyage arrêtée dans le brouillard d’une lagune d’hiver ; un homme en manteau soutient la tête d’un autre, affaissé contre la portière ouverte. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Deux mois au forum de Trajan
- **Sujet** : Une lance plantée devant une basilique à colonnes ; on présente sur des perches des robes de soie à une foule silencieuse, tandis qu’un homme en toge lit, assis en retrait.
- **Prompt** : bible visuelle + Vue large du forum de Trajan au printemps, la basilique Ulpia et ses colonnes de granit ; une lance fichée en terre devant l’estrade ; des serviteurs présentent sur des perches des robes de soie et une palla bleue à une foule dense et silencieuse ; en retrait, sur un siège de bois sans coussin, un homme barbu en toge sombre lit un rouleau ; au pied d’une colonne, un jeune homme brun écrit sur une tablette ; lumière de midi, ombres nettes.
- **Alt de référence** : « Une lance plantée devant une basilique à colonnes ; on présente sur des perches des robes de soie à une foule silencieuse, tandis qu’un homme en toge lit, assis en retrait. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — La première neige
- **Sujet** : Un empereur emmitouflé dans un manteau, debout devant un brasero dans une salle de pierre, écoute des officiers penchés sur une table de sable ; dehors, la neige.
- **Prompt** : bible visuelle + Intérieur de la basilique des principia d’un camp légionnaire, murs de pierre, deux braseros qui fument ; autour d’une table couverte de sable où l’on a tracé un fleuve, quatre officiers en cuirasse de cuir discutent ; un peu à l’écart, un homme barbu serré dans un manteau de pourpre passée, les mains tendues vers le brasero, écoute ; par une porte ouverte, la cour du camp sous la première neige ; lumière froide d’hiver et rougeoiement des braises.
- **Alt de référence** : « Un empereur emmitouflé dans un manteau, debout devant un brasero dans une salle de pierre, écoute des officiers penchés sur une table de sable ; dehors, la neige. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Écrit chez les Quades
- **Sujet** : Sous une pluie d’orage soudaine, des légionnaires assoiffés tendent leurs casques et leurs boucliers retournés vers le ciel ; un centurion à genoux fait boire un blessé dans son casque.
- **Prompt** : bible visuelle + Scène de bataille sous un orage : dans un vallon d’herbes hautes, des légionnaires épuisés, casques et boucliers retournés levés vers un ciel de plomb, boivent la pluie qui tombe drue ; au premier plan, un centurion à genoux fait boire un blessé dans son casque ; sur la crête, des cavaliers barbares chargent dans le rideau de pluie, un éclair frappe la pente ; lumière verte et violette d’orage, eau partout.
- **Alt de référence** : « Sous une pluie d’orage soudaine, des légionnaires assoiffés tendent leurs casques et leurs boucliers retournés vers le ciel ; un centurion à genoux fait boire un blessé dans son casque. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — Le fleuve gelé
- **Sujet** : Sur le Danube gelé, un carré de légionnaires, le pied posé sur leurs boucliers couchés, reçoit une charge de cavaliers en armures d’écailles dont les chevaux glissent ; un homme à cheval regarde depuis la rive.
- **Prompt** : bible visuelle + Vue depuis la rive enneigée d’un grand fleuve gelé : un carré de légionnaires, chacun un pied posé sur son bouclier couché sur la glace, reçoit la charge de cavaliers sarmates en armures d’écailles dont les chevaux glissent et se couchent ; corps à corps confus ; au premier plan, de dos, un homme à cheval, le manteau de pourpre remonté jusqu’aux yeux, regarde ; ciel bas et gris, souffle des hommes et des bêtes.
- **Alt de référence** : « Sur le Danube gelé, un carré de légionnaires, le pied posé sur leurs boucliers couchés, reçoit une charge de cavaliers en armures d’écailles dont les chevaux glissent ; un homme à cheval regarde depuis la rive. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Le mot d’ordre
- **Sujet** : Un empereur lit un discours depuis un tribunal de terre battue devant des rangs de légionnaires immobiles ; au pied de l’estrade, un jeune homme écrit sur une tablette.
- **Prompt** : bible visuelle + Champ de manœuvre en plaine, été ; sur un tribunal de terre battue, un homme barbu en manteau de pourpre passée lit un rouleau devant des milliers de légionnaires en rangs, immobiles, casques au bras ; sur le côté, des cavaliers barbares en armures d’écailles regardent ; au pied de l’estrade, un jeune homme brun écrit sur une tablette ; lumière blanche de fin de matinée, poussière.
- **Alt de référence** : « Un empereur lit un discours depuis un tribunal de terre battue devant des rangs de légionnaires immobiles ; au pied de l’estrade, un jeune homme écrit sur une tablette. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Les lettres
- **Sujet** : Un homme en toge, seul, la main posée sur le couvercle d’un coffre de cèdre cerclé de bronze, dans une salle de pierre vide ; un brasero éteint à côté.
- **Prompt** : bible visuelle + Intérieur d’une salle de conseil aux murs de pierre, vide ; au centre, sur une table, un coffre de cèdre cerclé de bronze au sceau intact ; un homme barbu en toge, debout, seul, la main droite posée à plat sur le couvercle, la tête baissée ; un brasero de bronze non allumé près de la table, une fenêtre ouverte sur une cour ensoleillée ; lumière d’été oblique, poussière dans le rai ; silence.
- **Alt de référence** : « Un homme en toge, seul, la main posée sur le couvercle d’un coffre de cèdre cerclé de bronze, dans une salle de pierre vide ; un brasero éteint à côté. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Halala
- **Sujet** : Dans une petite maison de pierre au pied de montagnes, un homme assis sur un tabouret veille une femme couchée, vêtue d’une palla bleue ; par la porte, des feux de cavaliers dans la cour.
- **Prompt** : bible visuelle + Intérieur d’une maison de relais en pierre grise, chambre basse éclairée d’une lampe ; sur un lit, une femme aux cheveux relevés, vêtue d’une palla bleu jacinthe, les mains croisées ; à côté, sur un tabouret, un homme barbu voûté, le visage grave, ne pleure pas ; par la porte ouverte, une cour nocturne où des cavaliers ont allumé des feux, et la masse sombre des montagnes ; lumière chaude de lampe contre bleu de nuit.
- **Alt de référence** : « Dans une petite maison de pierre au pied de montagnes, un homme assis sur un tabouret veille une femme couchée, vêtue d’une palla bleue ; par la porte, des feux de cavaliers dans la cour. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Éleusis
- **Sujet** : Un homme seul assis sur une pierre au sommet d’une colline, la nuit, regarde une baie éclairée par la lune ; en contrebas, des milliers de torches devant un sanctuaire.
- **Prompt** : bible visuelle + Vue nocturne depuis une colline rocheuse : au premier plan, de dos, un homme en tunique de lin assis sur une pierre, seul ; en contrebas, les toits d’un sanctuaire à colonnes et une foule de torches minuscules ; au-delà, une baie d’argent sous la lune avec une île sombre ; ciel étoilé immense ; lumière bleue et or.
- **Alt de référence** : « Un homme seul assis sur une pierre au sommet d’une colline, la nuit, regarde une baie éclairée par la lune ; en contrebas, des milliers de torches devant un sanctuaire. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — Les épées émoussées
- **Sujet** : Dans la loge d’un amphithéâtre, un vieil homme en toge lit des rapports pendant que deux gladiateurs se battent avec des épées sans fil ; à côté de lui, un jeune homme blond se penche en avant, fasciné.
- **Prompt** : bible visuelle + Loge impériale d’un amphithéâtre, vue de trois quarts : un homme âgé barbu en toge lit un rouleau, un tachygraphe à côté de lui ; à sa droite, un adolescent blond couronné se penche en avant, la bouche entrouverte, les yeux sur l’arène où deux gladiateurs se battent avec des épées émoussées, l’un posant sa lame sur la gorge de l’autre à terre ; foule floue dans les gradins ; lumière de juin, velum ocre.
- **Alt de référence** : « Dans la loge d’un amphithéâtre, un vieil homme en toge lit des rapports pendant que deux gladiateurs se battent avec des épées sans fil ; à côté de lui, un jeune homme blond se penche en avant, fasciné. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — Le soleil levant
- **Sujet** : Un jeune tribun, sa petite tablette de bois à la main, se tient au pied du lit d’un vieil homme couché sous une couverture de laine, dans une chambre de camp au crépuscule.
- **Prompt** : bible visuelle + Chambre austère d’un prétoire de camp, murs chaulés, brasero, une lampe ; sur un lit étroit, un vieil homme à la barbe blanche couché, la couverture remontée jusqu’au menton, les yeux ouverts ; au pied du lit, très droit, un jeune tribun en cuirasse tient une petite tablette de bois vierge ; par une fenêtre haute, le dernier rayon d’un soleil couchant ; lumière rouge et ombre.
- **Alt de référence** : « Un jeune tribun, sa petite tablette de bois à la main, se tient au pied du lit d’un vieil homme couché sous une couverture de laine, dans une chambre de camp au crépuscule. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — Le fleuve
- **Sujet** : Un homme d’une trentaine d’années, assis sur la berge d’un grand fleuve brun en crue, une tablette sur les genoux ; derrière lui, les murs et les tours d’un camp de pierre ; on démonte un pont de bateaux.
- **Prompt** : bible visuelle + Vue large d’une berge herbeuse au printemps : un homme brun de trente-trois ans, tunique de lin, assis sur l’herbe, une tablette de cire sur les genoux, regarde un grand fleuve brun en crue ; à droite, des soldats démontent un pont de bateaux ; en arrière-plan sur sa terrasse, les murs gris et les tours carrées d’un camp légionnaire ; ciel de mai, lumière claire, vent.
- **Alt de référence** : « Un homme d’une trentaine d’années, assis sur la berge d’un grand fleuve brun en crue, une tablette sur les genoux ; derrière lui, les murs et les tours d’un camp de pierre ; on démonte un pont de bateaux. »

## Images de notices

### `images/codex-marc-aurele.webp`

- **Notice** : Marc Aurèle (personnage)
- **Sujet** : Un homme d’une cinquantaine d’années, barbe frisée grisonnante, manteau militaire jeté sur une tunique, assis sur un tabouret pliant, une tablette de cire sur les genoux.
- **Prompt** : bible visuelle + Portrait aux trois quarts d’un homme de cinquante ans à la barbe bouclée grisonnante et aux paupières lourdes, d’après les bustes du dernier type ; il est assis sur un tabouret pliant sous une tente de cuir, un manteau de pourpre passée sur les épaules, une tablette de cire à trois volets sur les genoux, un stylet à la main ; lampe à huile, lumière chaude et basse, fond de toile brune.
- **Alt de référence** : « Un homme d’une cinquantaine d’années, barbe frisée grisonnante, manteau militaire jeté sur une tunique, assis sur un tabouret pliant, une tablette de cire sur les genoux. »

### `images/codex-nikias.webp`

- **Notice** : Nikias (personnage)
- **Sujet** : Un jeune homme brun d’une vingtaine d’années, tunique courte, un stylet d’os derrière l’oreille, écrit vite sur une tablette de cire à quatre volets.
- **Prompt** : bible visuelle + Jeune homme brun de vingt-cinq ans, cheveux courts, visage aigu et concentré, tunique de lin écru, assis en tailleur sur un coffre de cuir dans un coin de tente ; il écrit des signes serrés sur une tablette de cire à quatre volets, un stylet d’os derrière l’oreille ; une lampe à huile, une feuille de papyrus roulée à côté de lui.
- **Alt de référence** : « Un jeune homme brun d’une vingtaine d’années, tunique courte, un stylet d’os derrière l’oreille, écrit vite sur une tablette de cire à quatre volets. »

### `images/codex-faustine.webp`

- **Notice** : Faustine la Jeune (personnage)
- **Sujet** : Une femme de quarante-quatre ans, coiffure à bandeaux ondulés et chignon bas, palla couleur de jacinthe, debout sur une terrasse au-dessus d’une rivière.
- **Prompt** : bible visuelle + Femme de quarante-cinq ans au visage grave, coiffure à bandeaux ondulés relevés en chignon bas d’après ses portraits, palla bleu jacinthe sur une tunique claire, debout sur une terrasse de pierre au crépuscule, au-dessus d’une rivière rapide ; une petite fille de trois ans endormie contre elle ; lumière rasante dorée, ciel pannonien.
- **Alt de référence** : « Une femme de quarante-quatre ans, coiffure à bandeaux ondulés et chignon bas, palla couleur de jacinthe, debout sur une terrasse au-dessus d’une rivière. »

### `images/codex-commode.webp`

- **Notice** : Commode (personnage)
- **Sujet** : Un adolescent blond et large d’épaules, toge d’homme neuve, salue une foule de soldats depuis une estrade de terre battue.
- **Prompt** : bible visuelle + Adolescent de treize ans, blond bouclé, visage plein, large d’épaules, en toge virile blanche trop neuve, debout sur un tribunal de terre battue devant des rangs de légionnaires en cotte de mailles ; il lève le bras droit avec une raideur apprise ; à côté, de dos, un homme âgé en manteau de pourpre ; plaine de Pannonie, ciel d’été.
- **Alt de référence** : « Un adolescent blond et large d’épaules, toge d’homme neuve, salue une foule de soldats depuis une estrade de terre battue. »

### `images/codex-galien.webp`

- **Notice** : Galien (personnage)
- **Sujet** : Un homme de quarante ans, barbe noire soignée, penché sur un pot d’étain, pèse des ingrédients sur une petite balance.
- **Prompt** : bible visuelle + Homme de quarante ans à la barbe noire bien taillée et aux sourcils arqués, tunique grecque, dans un cabinet encombré de pots d’étain, de fioles et de rouleaux ; il pèse sur une petite balance de bronze une pincée d’herbe au-dessus d’un mortier ; une vipère desséchée sur la table ; lumière de fenêtre, Rome.
- **Alt de référence** : « Un homme de quarante ans, barbe noire soignée, penché sur un pot d’étain, pèse des ingrédients sur une petite balance. »

### `images/codex-pompeianus.webp`

- **Notice** : Claudius Pompeianus (personnage)
- **Sujet** : Un officier de cinquante ans, visage tanné et impassible, cuirasse de cuir et manteau sombre, debout devant une carte posée sur une table.
- **Prompt** : bible visuelle + Officier romain d’une cinquantaine d’années, visage osseux et tanné, cheveux courts gris, barbe rase, cuirasse de cuir aux lanières et manteau sombre, debout les mains posées sur une table où une carte de peau est déroulée ; deux braseros fumants derrière lui dans une grande salle de pierre ; lumière d’hiver.
- **Alt de référence** : « Un officier de cinquante ans, visage tanné et impassible, cuirasse de cuir et manteau sombre, debout devant une carte posée sur une table. »

### `images/codex-avidius-cassius.webp`

- **Notice** : Avidius Cassius (personnage)
- **Sujet** : Un officier de haute taille, cheveux gris coupés court, cuirasse d’apparat, se tient devant un rempart de brique sous un ciel de Syrie.
- **Prompt** : bible visuelle + Homme de cinquante-cinq ans, grand, sec, cheveux gris coupés ras, visage dur et intelligent, cuirasse musclée d’apparat et manteau rouge, debout sur un rempart de brique crue au-dessus d’une ville blanche au bord d’un fleuve ; soldats en rangs plus bas ; lumière blanche de midi, Syrie.
- **Alt de référence** : « Un officier de haute taille, cheveux gris coupés court, cuirasse d’apparat, se tient devant un rempart de brique sous un ciel de Syrie. »

### `images/codex-herode-atticus.webp`

- **Notice** : Hérode Atticus (personnage)
- **Sujet** : Un vieil homme aux cheveux blancs, appuyé sur un bâton, manteau grec, debout devant une porte de pierre fermée, une torche à la main dans la nuit.
- **Prompt** : bible visuelle + Vieillard de soixante-quinze ans aux cheveux blancs abondants, barbe blanche, manteau grec drapé, appuyé sur un long bâton, debout seul devant les grandes portes fermées d’une salle de pierre à colonnes, une torche à la main, dans une nuit pleine de lueurs lointaines ; visage fermé, digne ; Éleusis.
- **Alt de référence** : « Un vieil homme aux cheveux blancs, appuyé sur un bâton, manteau grec, debout devant une porte de pierre fermée, une torche à la main dans la nuit. »

### `images/codex-carnuntum.webp`

- **Notice** : Carnuntum (lieu)
- **Sujet** : Un camp romain de pierre sur une terrasse au-dessus d’un grand fleuve gelé, sous la neige, avec ses tours et sa porte ; fumées des braseros.
- **Prompt** : bible visuelle + Vue plongeante d’un camp légionnaire rectangulaire aux murs de pierre grise et aux tours carrées, sur une terrasse dominant un grand fleuve gris pris par la glace, sous une neige fraîche ; fumées bleues montant des baraquements, sentinelles minuscules sur le rempart, au loin l’autre rive plate et blanche sans limite ; lumière d’aube d’hiver.
- **Alt de référence** : « Un camp romain de pierre sur une terrasse au-dessus d’un grand fleuve gelé, sous la neige, avec ses tours et sa porte ; fumées des braseros. »

### `images/codex-le-danube.webp`

- **Notice** : Le Danube (lieu)
- **Sujet** : Des légionnaires en carré sur un fleuve gelé, le pied posé sur leur bouclier couché, reçoivent une charge de cavaliers en armures d’écailles qui glissent.
- **Prompt** : bible visuelle + Scène de bataille sur un fleuve gelé sous un ciel bas : un carré de légionnaires, chacun un pied posé sur son bouclier couché sur la glace, reçoit une charge de cavaliers sarmates en armures d’écailles et longues lances dont les chevaux glissent et se couchent ; corps à corps au premier plan, rives enneigées au loin ; lumière grise, souffle des hommes visible.
- **Alt de référence** : « Des légionnaires en carré sur un fleuve gelé, le pied posé sur leur bouclier couché, reçoivent une charge de cavaliers en armures d’écailles qui glissent. »

### `images/codex-la-granua.webp`

- **Notice** : La Granua (lieu)
- **Sujet** : Une colonne romaine avance dans un vallon d’herbes hautes le long d’une rivière verte, des cavaliers immobiles sur les crêtes.
- **Prompt** : bible visuelle + Paysage de collines rondes couvertes d’herbes plus hautes qu’un homme, une rivière étroite et verte au fond du vallon, une longue colonne de légionnaires et de mulets qui la remonte dans la poussière ; sur les crêtes, en silhouette, des cavaliers immobiles aux longues lances ; ciel blanc de grande chaleur.
- **Alt de référence** : « Une colonne romaine avance dans un vallon d’herbes hautes le long d’une rivière verte, des cavaliers immobiles sur les crêtes. »

### `images/codex-sirmium.webp`

- **Notice** : Sirmium (lieu)
- **Sujet** : Une terrasse de pierre au-dessus d’une rivière rapide au crépuscule, un homme en toge assis près d’une femme, un garçon fait tourner une fronde plus loin.
- **Prompt** : bible visuelle + Terrasse de pierre d’une maison romaine dominant une rivière rapide et brune, au crépuscule d’été ; un homme barbu en toge assis sur un banc, une femme à la palla bleue à côté de lui, une petite fille endormie contre elle ; plus loin, un adolescent blond fait tourner une fronde sans viser ; cyprès, murs de brique, ciel orangé.
- **Alt de référence** : « Une terrasse de pierre au-dessus d’une rivière rapide au crépuscule, un homme en toge assis près d’une femme, un garçon fait tourner une fronde plus loin. »

### `images/codex-halala.webp`

- **Notice** : Halala (lieu)
- **Sujet** : Quelques maisons de pierre grise au pied de hautes montagnes, un relais de poste, une source ; des cavaliers ont allumé des feux dans une cour au crépuscule.
- **Prompt** : bible visuelle + Petit bourg de maisons basses en pierre grise et toits plats, serré au pied d’une chaîne de montagnes enneigées, avec une cour de relais où des cavaliers ont allumé des feux au crépuscule ; une source coule dans un abreuvoir de pierre ; ciel violet, premières étoiles ; Cappadoce.
- **Alt de référence** : « Quelques maisons de pierre grise au pied de hautes montagnes, un relais de poste, une source ; des cavaliers ont allumé des feux dans une cour au crépuscule. »

### `images/codex-eleusis.webp`

- **Notice** : Éleusis et Athènes (lieu)
- **Sujet** : Une foule portant des torches devant les portes fermées d’une grande salle à colonnes, la nuit, avec la baie de Salamine au loin.
- **Prompt** : bible visuelle + Nuit d’automne sur un sanctuaire grec : une foule dense portant des torches attend devant les grandes portes closes d’une salle carrée à colonnes, sur une terrasse au-dessus d’une baie où brille la mer ; au premier plan, de dos, un homme en tunique de lin et un vieillard au bâton ; fumée des torches, ciel étoilé, île sombre au large.
- **Alt de référence** : « Une foule portant des torches devant les portes fermées d’une grande salle à colonnes, la nuit, avec la baie de Salamine au loin. »

### `images/codex-vindobona.webp`

- **Notice** : Vindobona (lieu)
- **Sujet** : Une chambre de camp aux murs de pierre, un lit étroit, un homme couché sous une couverture de laine, un tribun debout au pied du lit avec une petite tablette de bois.
- **Prompt** : bible visuelle + Chambre austère d’un prétoire de camp, murs de pierre chaulée, brasero, une lampe ; sur un lit étroit, un vieil homme barbu couché, la couverture de laine remontée jusqu’au menton ; au pied du lit, un jeune tribun en cuirasse se tient très droit, une petite tablette de bois vierge à la main ; lumière de fin de jour par une fenêtre haute.
- **Alt de référence** : « Une chambre de camp aux murs de pierre, un lit étroit, un homme couché sous une couverture de laine, un tribun debout au pied du lit avec une petite tablette de bois. »

### `images/codex-le-mot-d-ordre.webp`

- **Notice** : Le mot d’ordre (objet)
- **Sujet** : Une petite tablette de bois rectangulaire posée dans une main de soldat, avec un mot gravé qu’on ne peut pas lire, à la lueur d’un feu de veille.
- **Prompt** : bible visuelle + Gros plan sur la main calleuse d’un soldat tenant une petite tablette de bois rectangulaire où un mot est gravé, illisible ; derrière, flou, un feu de veille, une palissade et la silhouette d’une sentinelle ; nuit, lumière orange et bleue.
- **Alt de référence** : « Une petite tablette de bois rectangulaire posée dans une main de soldat, avec un mot gravé qu’on ne peut pas lire, à la lueur d’un feu de veille. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/le-fleuve-et-la-citadelle.webp` | à produire |
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
| `images/codex-marc-aurele.webp` | à produire |
| `images/codex-nikias.webp` | à produire |
| `images/codex-faustine.webp` | à produire |
| `images/codex-commode.webp` | à produire |
| `images/codex-galien.webp` | à produire |
| `images/codex-pompeianus.webp` | à produire |
| `images/codex-avidius-cassius.webp` | à produire |
| `images/codex-herode-atticus.webp` | à produire |
| `images/codex-carnuntum.webp` | à produire |
| `images/codex-le-danube.webp` | à produire |
| `images/codex-la-granua.webp` | à produire |
| `images/codex-sirmium.webp` | à produire |
| `images/codex-halala.webp` | à produire |
| `images/codex-eleusis.webp` | à produire |
| `images/codex-vindobona.webp` | à produire |
| `images/codex-le-mot-d-ordre.webp` | à produire |

29 fichiers — le décompte correspond exactement aux champs `image` de l'îlot.
