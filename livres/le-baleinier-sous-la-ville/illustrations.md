# Illustrations de « Le Baleinier sous la ville »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/le-baleinier-sous-la-ville/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Tu travailles sur la branche de la pull request de ce livre (celle où se
   trouve ce fichier ; à défaut, une branche dédiée créée depuis `main`, par
   exemple `atelier/illustrations-le-baleinier-sous-la-ville`, avec sa propre pull request). Jamais
   de push sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON de
   `index.html`, ni le texte, ni aucun autre fichier — à une exception près :
   dans le `<head>` de `livres/le-baleinier-sous-la-ville/index.html`, complète la meta
   `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Opus 5.5 (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Le Baleinier sous la ville :
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
- Images intérieures : aucun texte lisible incrusté, aucun logo, aucune marque,
  aucune créature ou personnage sous licence.
- **Personnes réelles jamais reconnaissables** (voir la bible visuelle).
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/le-baleinier-sous-la-ville
  ```

## Bible visuelle commune

Gouache et aquarelle sur papier épais au grain visible, dans l'esprit des grandes planches illustrées de magazine de géographie des années 1970 revues par un peintre contemporain : aplats francs, lavis transparents, contours discrets. Sur chaque image, en surimpression très légère, un réseau de fines courbes de niveau ou de lignes de carte translucides (jamais de texte, jamais de chiffres), comme si une carte était posée sur le monde — c'est la signature du livre. Palette : ivoire de papier, bleu océan profond, ocre de la terre texane, vert tendre, avec pour les scènes nocturnes le bleu froid des écrans et l'orange des réverbères. Lumières basses et rasantes, ciels immenses. Ton : lumineux, tendre, jamais spectaculaire. On ne montre jamais : de logo ou de marque (ni Google, ni Nintendo, ni Pokémon, ni chaîne de télévision), aucune créature Pokémon reconnaissable ni personnage sous licence, aucun texte lisible, aucune scène de violence, de guerre ou de victime.

**Règle impérative sur les personnes réelles** : John Hanke et les autres personnes réelles (Bill Kilday, dirigeants de Google, de Nintendo ou de The Pokémon Company…) ne sont **jamais représentés de face ni reconnaissables** — de dos, en silhouette, de loin, ou par leurs mains seulement. Seuls les personnages inventés (Léna Marchal, Daniel Reyes, Ko Aung) peuvent avoir un visage.

Personnages récurrents (les tenir identiques d'une image à l'autre) :

- **John Hanke** (personne réelle — jamais de face) : grand, légèrement voûté, cheveux châtains courts qui grisonnent avec les années ; chemise à carreaux ou veste simple, mains souvent dans les poches. Enfant (ch. 1) : garçon maigre aux bras trop longs.
- **Léna Marchal** (inventée) : Française, mince, cheveux blond foncé attachés, yeux gris-bleu ; 22 ans en 1995, 43 en 2016 ; pull marin ou pull épais, jamais de tenue d'affaires.
- **Daniel « Dan » Reyes** (inventé) : Louisianais, grand et maigre, cheveux noirs en bataille qui grisonnent à partir de 2013, peau mate, rire qui plisse tout le visage ; veste de pilote en toile.
- **Ko Aung** (inventé) : Birman d'une quarantaine d'années, longyi et chemise blanche ; on ne voit que ses mains.

## Couverture

- **Fichier** : `couvertures/le-baleinier-sous-la-ville.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : le monde en trois couches — la Terre vue d'en haut, les marcheurs dans les rues, le baleinier enseveli dessous.
- **Prompt** : bible visuelle + Composition verticale 2:3 en coupe, de haut en bas : dans le ciel nocturne en haut, une Terre bleue qui tourne, petite et lumineuse ; au milieu, les rues de San Francisco la nuit, trottoirs et façades, où marchent des silhouettes de tous âges penchées sur des téléphones lumineux, reliées par de fines lignes de lumière ; en bas, dans la terre sombre sous la chaussée, la coque d'un vieux baleinier ensablé, faiblement éclairée. Palette bleu nuit, ocre et or. Titre implicite dans le tiers supérieur, autour de la Terre, zone calme. Aucun texte, logo, signature, filigrane ni pseudo-texte.
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) : « Coupe de San Francisco la nuit : au-dessus, les rues éclairées où marchent des silhouettes penchées sur des téléphones lumineux ; en dessous, dans la terre sombre, la coque d’un vieux baleinier ensablé, et plus haut encore, une Terre bleue qui tourne dans le ciel. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Cinq sacs de courses
- **Sujet** : Deux enfants de dos, assis sur le sol d'un salon texan, dépliant une grande carte tirée d'un magazine jaune, entourés de sacs de courses en papier débordant de vieux numéros.
- **Prompt** : bible visuelle + Intérieur d'une maison modeste du Texas central, vers 1979, fin d'après-midi. Un garçon d'une douzaine d'années et sa sœur un peu plus jeune, vus de dos et de trois quarts arrière, assis en tailleur sur un tapis, déplient à deux une grande carte aux couleurs vives tirée d'un National Geographic. Autour d'eux, cinq sacs de courses en papier kraft renversés, des piles de magazines au dos jaune. Lumière dorée et rasante par une fenêtre à moustiquaire ; poussière qui danse. Émerveillement tranquille. Aucun texte lisible sur les couvertures ni sur la carte.
- **Alt de référence** : « Deux enfants de dos, assis sur le sol d'un salon texan, dépliant une grande carte tirée d'un magazine jaune, entourés de sacs de courses en papier débordant de vieux numéros. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Rangoun
- **Sujet** : Sous un auvent de tôle battu par la mousson, la main d'un homme birman dessine au stylo un village sur une serviette en papier, devant deux verres de thé au lait ; au loin, la silhouette dorée d'une pagode dans la pluie.
- **Prompt** : bible visuelle + Rangoun, début des années 1990, après-midi de mousson. Plan rapproché sur une table de maison de thé en plein air, sous un auvent de tôle ruisselant : deux verres de thé au lait, une serviette en papier où une main birmane trace au stylo bleu une rivière, une petite pagode, un grand arbre ; la main d'un jeune Occidental en chemise claire posée à côté. Rideau de pluie serré au premier plan ; au fond, floue, la silhouette dorée de la pagode Shwedagon. Palette verte, grise et or. Aucun texte lisible.
- **Alt de référence** : « Sous un auvent de tôle battu par la mousson, la main d'un homme birman dessine au stylo un village sur une serviette en papier, devant deux verres de thé au lait ; au loin, la silhouette dorée d'une pagode dans la pluie. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Meridian
- **Sujet** : Une jeune femme de dos, la nuit, devant un écran cathodique où s'affiche une rue médiévale rudimentaire éclairée de torches ; le brouillard entre par la fenêtre ouverte.
- **Prompt** : bible visuelle + Chambre d'étudiante à Berkeley, hiver 1995, deux heures du matin. Une jeune femme de vingt-deux ans, vue de trois quarts arrière, cheveux blond foncé attachés, pull épais, assise devant un gros moniteur cathodique beige ; à l'écran, une rue de ville médiévale en 3D primitive, murs de briques pixelisés, torches orange, quelques silhouettes de personnages. Seule lumière : l'écran, bleu et orange. Par la fenêtre à guillotine entrouverte, le brouillard de la baie entre en nappes. Tasse de thé, disquettes. Aucun texte lisible à l'écran.
- **Alt de référence** : « Une jeune femme de dos, la nuit, devant un écran cathodique où s'affiche une rue médiévale rudimentaire éclairée de torches ; le brouillard entre par la fenêtre ouverte. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Le globe dans le Dell
- **Sujet** : Sur une table de salle à manger, une tour d'ordinateur beige et un lourd écran cathodique affichent la Terre bleue qui tourne ; deux hommes, de dos, se penchent vers l'écran.
- **Prompt** : bible visuelle + Printemps 1999, le soir, une salle à manger ordinaire. Sur la table, entre une corbeille de fruits et du courrier, une tour d'ordinateur beige et un écran cathodique massif où tourne une Terre bleue et blanche dans le noir. Deux hommes vus de dos, en tee-shirt et en chemise à carreaux, penchés vers l'écran, l'un le nez presque collé à la vitre. Lumière d'une suspension basse et halo bleu de l'écran. Stupeur et jubilation retenue. Aucun visage de face, aucun logo.
- **Alt de référence** : « Sur une table de salle à manger, une tour d'ordinateur beige et un lourd écran cathodique affichent la Terre bleue qui tourne ; deux hommes, de dos, se penchent vers l'écran. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — L’hiver des pionniers
- **Sujet** : Vue verticale d'un champ de canne à sucre : au centre d'un halo plus clair, la petite ombre en croix d'un avion.
- **Prompt** : bible visuelle + Photographie aérienne verticale peinte, vue exactement d'en haut : un champ de canne à sucre de Louisiane en rangs parallèles, un chemin de terre, un fossé. Au centre, un halo lumineux où les ombres disparaissent, et dedans la petite ombre noire, nette, en forme de croix, d'un avion monomoteur. Lumière de milieu de matinée. Composition presque abstraite, comme une carte. Une fine grille de raccord de dalles, à peine visible, rappelle l'assemblage numérique. Aucun texte.
- **Alt de référence** : « Vue verticale d'un champ de canne à sucre : au centre d'un halo plus clair, la petite ombre en croix d'un avion. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Map Viewer
- **Sujet** : Dans une salle de réunion sombre, une dizaine de silhouettes debout regardent un téléviseur où un globe plonge vers une ville la nuit.
- **Prompt** : bible visuelle + Mars 2003, une salle de réunion de start-up à Mountain View, stores baissés, lumière du soir. Une dizaine de personnes debout, vues de dos et en silhouette, bras croisés ou main sur la bouche, face à un téléviseur fixé au mur où l'on voit un globe terrestre en train de zoomer sur une grande ville fluviale de nuit. À droite, un tableau blanc couvert de marques illisibles. Mélange de joie et de malaise. Aucun logo de chaîne, aucun texte lisible, aucune image de combat.
- **Alt de référence** : « Dans une salle de réunion sombre, une dizaine de silhouettes debout regardent un téléviseur où un globe plonge vers une ville la nuit. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Toute la Terre
- **Sujet** : Vue aérienne à l'aube d'un quartier inondé : l'eau brune monte jusqu'aux gouttières, la couronne sombre d'un magnolia émerge, et l'ombre d'un petit avion passe dessus.
- **Prompt** : bible visuelle + La Nouvelle-Orléans, début septembre 2005, à l'aube. Vue aérienne oblique douce d'un quartier de maisons de bois à un étage, noyées jusqu'aux gouttières dans une eau brune et lisse qui reflète un ciel rose pâle ; des toits comme des radeaux ; au centre, la couronne ronde et sombre d'un grand magnolia qui émerge de l'eau ; sur l'eau, près de l'arbre, la petite ombre en croix d'un avion. Silence, gravité, aucune personne en détresse montrée, aucun corps. Aucun texte.
- **Alt de référence** : « Vue aérienne à l'aube d'un quartier inondé : l'eau brune monte jusqu'aux gouttières, la couronne sombre d'un magnolia émerge, et l'ombre d'un petit avion passe dessus. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — La voiture de Larry
- **Sujet** : La nuit, sous un réverbère, un homme de dos tient un téléphone dont l'écran bleu éclaire sa main ; au bout de la rue, une voiture porte sur son toit un mât hérissé d'objectifs.
- **Prompt** : bible visuelle + Été 2010, une rue résidentielle de la péninsule de San Francisco, la nuit. Un homme grand, légèrement voûté, en chemise à carreaux, vu de dos sous un réverbère orangé, les yeux baissés sur un smartphone dont l'écran bleu, où luit un point bleu sur une carte, éclaire sa main. Au fond de la rue, garée, une voiture sans marque portant sur son toit un mât surmonté d'une boule de caméras. Solitude, réflexion. Aucun logo, aucun visage de face.
- **Alt de référence** : « La nuit, sous un réverbère, un homme de dos tient un téléphone dont l'écran bleu éclaire sa main ; au bout de la rue, une voiture porte sur son toit un mât hérissé d'objectifs. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Le baleinier
- **Sujet** : Sur une petite place de La Nouvelle-Orléans, la nuit, un homme assis sur le rebord d'une fontaine et une femme debout à dix mètres se regardent, chacun éclairé par son téléphone.
- **Prompt** : bible visuelle + Décembre 2013, minuit passé, une petite place pavée du Vieux Carré, balcons de fer forgé, lanternes. Au centre, une fontaine et une statue de bronze. Un homme brun grisonnant en veste de pilote, assis sur le rebord de la fontaine, lève la tête ; à dix mètres, une femme mince aux cheveux blond foncé, debout, téléphone à la main. Les écrans les éclairent l'un de vert, l'autre de bleu ; dans l'air, de très légers filaments lumineux verts et bleus relient la statue au ciel, comme une surimpression. Tension tendre. Aucun texte lisible.
- **Alt de référence** : « Sur une petite place de La Nouvelle-Orléans, la nuit, un homme assis sur le rebord d'une fontaine et une femme debout à dix mètres se regardent, chacun éclairé par son téléphone. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — Poisson d’avril
- **Sujet** : Une salle de réunion au-dessus de Tokyo : deux délégations de part et d'autre d'une table, des interprètes au milieu, la ville immense derrière les vitres.
- **Prompt** : bible visuelle + Mai 2014, Tokyo, une salle de réunion lumineuse en hauteur. Vue large depuis le fond de la salle : une longue table, d'un côté une petite délégation américaine vue de dos, de l'autre des dirigeants japonais en costume sombre, flous et lointains ; deux interprètes au bout de la table. Derrière les baies vitrées, la ville immense sous un ciel de printemps voilé. Posé sur la table, un smartphone dont l'écran montre une carte constellée de points lumineux. Courtoisie, attente. Aucun visage détaillé, aucun logo, aucune créature.
- **Alt de référence** : « Une salle de réunion au-dessus de Tokyo : deux délégations de part et d'autre d'une table, des interprètes au milieu, la ville immense derrière les vitres. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — Six juillet
- **Sujet** : La nuit, sur les quais de San Francisco, une foule de tous âges avance tête baissée, éclairée par des centaines d'écrans ; en retrait, un homme et une femme regardent.
- **Prompt** : bible visuelle + 6-7 juillet 2016, trois heures du matin, l'Embarcadero de San Francisco. Des dizaines de personnes de tous âges — adolescents, couple, père portant un enfant endormi, deux vieilles dames avec un thermos, cuisiniers en tablier, homme en costume qui court — marchent ou s'arrêtent ensemble, visages éclairés par la lueur bleue de leurs téléphones ; au fond, la silhouette de la tour à horloge du Ferry Building (cadran sans chiffres lisibles). Au premier plan, de dos, un homme grand en chemise à carreaux et une femme blonde regardent la foule. Joie nocturne, chaleur humaine. Aucune créature, aucun logo.
- **Alt de référence** : « La nuit, sur les quais de San Francisco, une foule de tous âges avance tête baissée, éclairée par des centaines d'écrans ; en retrait, un homme et une femme regardent. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — À hauteur d’homme
- **Sujet** : Au crépuscule, devant une maison blanche à véranda du Texas, des enfants à vélo penchés sur leurs téléphones ; sur le trottoir, un homme de dos les regarde ; au loin, un feu orange clignote.
- **Prompt** : bible visuelle + Automne 2026, Cross Plains (Texas), fin de journée. Une maison de bois blanche à véranda, pelouse sèche, grands arbres ; sur la pelouse, trois enfants et un adolescent avec leurs vélos, penchés sur des téléphones, riant. Sur le trottoir, au premier plan, un homme d'une soixantaine d'années en chemise à carreaux, vu de dos, mains dans les poches. Au loin, au croisement, un feu de signalisation suspendu, orange. Ciel texan immense, lumière rasante qui étire les ombres des clôtures. Apaisement, retour. Aucun texte, aucun panneau lisible.
- **Alt de référence** : « Au crépuscule, devant une maison blanche à véranda du Texas, des enfants à vélo penchés sur leurs téléphones ; sur le trottoir, un homme de dos les regarde ; au loin, un feu orange clignote. »

## Images de notices

### `images/codex-lena-marchal.webp`

- **Notice** : Léna Marchal (personnage inventé)
- **Sujet** : Portrait à la gouache d'une femme d'une trentaine d'années aux cheveux blond foncé attachés, regard gris-bleu attentif, devant un écran où se raccordent des dalles d'images aériennes.
- **Prompt** : bible visuelle + Portrait de Léna Marchal, personnage inventé, vers 33 ans (2005) : française, visage fin, pommettes hautes, cheveux blond foncé attachés à la va-vite, yeux gris-bleu, cernes légers ; pull marin. De trois quarts, éclairée par un écran où s'assemblent des dalles de photographies aériennes aux couleurs légèrement discordantes. Concentration, douceur obstinée.
- **Alt de référence** : « Portrait à la gouache d'une femme d'une trentaine d'années aux cheveux blond foncé attachés, regard gris-bleu attentif, devant un écran où se raccordent des dalles d'images aériennes. »

### `images/codex-daniel-reyes.webp`

- **Notice** : Daniel Reyes, dit Pélican (personnage inventé)
- **Sujet** : Portrait d'un homme grand et maigre aux cheveux noirs, en veste de pilote, assis dans le cockpit d'un petit avion, souriant avec tout le visage.
- **Prompt** : bible visuelle + Portrait de Daniel Reyes, personnage inventé, vers 35 ans : Louisianais, grand et maigre, cheveux noirs en bataille, peau mate, rire franc qui plisse tout le visage ; veste de pilote en toile, casque audio autour du cou. Assis dans le cockpit d'un monomoteur, porte ouverte, sur un aérodrome de Louisiane ; ciel lavé après l'orage.
- **Alt de référence** : « Portrait d'un homme grand et maigre aux cheveux noirs, en veste de pilote, assis dans le cockpit d'un petit avion, souriant avec tout le visage. »

### `images/codex-ko-aung.webp`

- **Notice** : Ko Aung et la serviette (personnage inventé)
- **Sujet** : Une serviette en papier froissée où l'on devine, à l'encre bleue passée, une rivière, une pagode et un grand arbre.
- **Prompt** : bible visuelle + Nature morte : une serviette en papier pliée en quatre puis dépliée, très usée, douce comme du tissu, posée sur une table de bois ; à l'encre bleue presque effacée, le dessin naïf d'une rivière, d'une petite pagode, d'un grand arbre et d'un minuscule cercle. Lumière latérale douce. Aucun texte.
- **Alt de référence** : « Une serviette en papier froissée où l'on devine, à l'encre bleue passée, une rivière, une pagode et un grand arbre. »

### `images/codex-cross-plains.webp`

- **Notice** : Cross Plains, Texas (lieu)
- **Sujet** : Un croisement désert d'une petite ville du Texas, sous un ciel immense, avec un unique feu orange suspendu au-dessus de la chaussée.
- **Prompt** : bible visuelle + Cross Plains (Texas), vers 1980, matin d'été : rue principale large et vide, façades basses de brique, un château d'eau au loin, et au croisement un unique feu de signalisation suspendu à un câble, allumé orange. Ciel immense bleu pâle, chaleur, un pick-up garé. Aucun texte ni enseigne lisible.
- **Alt de référence** : « Un croisement désert d'une petite ville du Texas, sous un ciel immense, avec un unique feu orange suspendu au-dessus de la chaussée. »

### `images/codex-maison-robert-e-howard.webp`

- **Notice** : La maison de Robert E. Howard (lieu)
- **Sujet** : Une maison de bois blanche à véranda, au bout d'une rue tranquille, sous les arbres.
- **Prompt** : bible visuelle + La maison de Robert E. Howard à Cross Plains : petite maison de bois blanche à un étage avec véranda couverte, fenêtres à guillotine, arbres qui l'ombragent, pelouse ; fin d'après-midi dorée. Calme, modestie, une fenêtre éclairée. Aucun panneau lisible.
- **Alt de référence** : « Une maison de bois blanche à véranda, au bout d'une rue tranquille, sous les arbres. »

### `images/codex-rangoun.webp`

- **Notice** : Rangoun et la Birmanie (lieu)
- **Sujet** : La pagode Shwedagon au crépuscule, son or virant au cuivre au-dessus des arbres de Rangoun.
- **Prompt** : bible visuelle + Rangoun, début des années 1990, au crépuscule : la pagode Shwedagon sur sa colline, dôme doré qui vire au rose puis au cuivre, au-dessus d'une ville basse et verte aux façades coloniales délavées ; ciel de mousson lourd. Aucun texte.
- **Alt de référence** : « La pagode Shwedagon au crépuscule, son or virant au cuivre au-dessus des arbres de Rangoun. »

### `images/codex-gentilly.webp`

- **Notice** : Gentilly, La Nouvelle-Orléans (lieu)
- **Sujet** : Au coin d'une rue de Gentilly, un poteau électrique porte une bande de peinture à hauteur d'épaule ; derrière, une maison de bois à véranda et un grand magnolia.
- **Prompt** : bible visuelle + Gentilly, La Nouvelle-Orléans, été 2016, fin d'après-midi : au coin d'une rue, un poteau électrique en bois marqué d'une bande de peinture horizontale à hauteur d'épaule d'homme (le niveau de l'eau de 2005) ; derrière, une petite maison de bois repeinte, à véranda, et un grand magnolia sombre. Lumière chaude et lourde. Aucun texte lisible.
- **Alt de référence** : « Au coin d'une rue de Gentilly, un poteau électrique porte une bande de peinture à hauteur d'épaule ; derrière, une maison de bois à véranda et un grand magnolia. »

### `images/codex-le-niantic.webp`

- **Notice** : Le baleinier Niantic (lieu)
- **Sujet** : Coupe verticale d'une rue de San Francisco : sous le trottoir et les immeubles, la coque d'un vieux baleinier ensevelie dans le remblai.
- **Prompt** : bible visuelle + Vue en coupe, comme une planche de géologie peinte : en haut, un trottoir du quartier financier de San Francisco avec passants et pied d'immeuble ; en dessous, des couches de sable, de gravats et de terre ; au fond, couchée, la coque en bois d'un trois-mâts baleinier du XIXe siècle, en partie calcinée, avec des bouteilles et des caisses. Lumière douce qui semble venir d'en haut. Aucun texte.
- **Alt de référence** : « Coupe verticale d'une rue de San Francisco : sous le trottoir et les immeubles, la coque d'un vieux baleinier ensevelie dans le remblai. »

### `images/codex-meridian-59.webp`

- **Notice** : Meridian 59 (jeu)
- **Sujet** : Une rue médiévale en trois dimensions primitive, murs de briques pixelisés et torches orange, où se croisent quelques personnages.
- **Prompt** : bible visuelle + Évocation peinte d'un monde de jeu en ligne de 1995 : une rue médiévale en perspective, murs aux textures pixelisées, torches orange qui clignotent, quelques personnages trapus en armure dépareillée, un pont au fond ; rendu volontairement naïf, comme vu sur un écran cathodique, lignes de balayage à peine visibles. Aucun nom flottant lisible, aucun logo.
- **Alt de référence** : « Une rue médiévale en trois dimensions primitive, murs de briques pixelisés et torches orange, où se croisent quelques personnages. »

### `images/codex-keyhole.webp`

- **Notice** : Keyhole (entreprise)
- **Sujet** : Un bureau de start-up presque vide, tables pliantes, écrans, et un tableau blanc en haut duquel quelques mots sont écrits à la main.
- **Prompt** : bible visuelle + Bureaux de Keyhole à Mountain View, 2002, le soir : pièce basse, tables pliantes, écrans cathodiques et plats allumés sur des vues de la Terre, fauteuils vides, une plante verte ; au mur, un grand tableau blanc couvert d'une liste interminable en écriture manuscrite illisible, débordant sur le mur. Lumière de néon et d'écrans. Aucun texte lisible.
- **Alt de référence** : « Un bureau de start-up presque vide, tables pliantes, écrans, et un tableau blanc en haut duquel quelques mots sont écrits à la main. »

### `images/codex-ingress.webp`

- **Notice** : Ingress (jeu)
- **Sujet** : Un petit groupe d'inconnus marche à l'aube vers une chapelle sur une colline, téléphones à la main, sous un ciel strié de filaments verts et bleus.
- **Prompt** : bible visuelle + Aube d'hiver, un chemin qui monte vers une petite chapelle sur une colline : cinq personnes d'âges variés (une grand-mère, un étudiant, un livreur en blouson, un comptable en manteau) marchent ensemble en parlant, téléphones à la main. Dans le ciel pâle, de très légers filaments lumineux verts et bleus relient la chapelle à d'autres points de l'horizon. Aucun texte, aucun logo.
- **Alt de référence** : « Un petit groupe d'inconnus marche à l'aube vers une chapelle sur une colline, téléphones à la main, sous un ciel strié de filaments verts et bleus. »

### `images/codex-national-geographic.webp`

- **Notice** : Les cinq sacs de National Geographic (objet)
- **Sujet** : Cinq sacs de courses en papier kraft débordant de vieux magazines au dos jaune, et une grande carte à moitié dépliée.
- **Prompt** : bible visuelle + Nature morte vers 1979 : sur un tapis, cinq sacs de courses en papier kraft, l'un renversé, d'où glissent des magazines au dos jaune ; au premier plan, une grande carte pliée en huit à moitié dépliée, aux couleurs vives, fonds océaniques en bleus dégradés. Lumière d'après-midi. Aucun texte lisible.
- **Alt de référence** : « Cinq sacs de courses en papier kraft débordant de vieux magazines au dos jaune, et une grande carte à moitié dépliée. »

### `images/codex-point-chaud.webp`

- **Notice** : Le point chaud (concept)
- **Sujet** : Vue verticale d'un champ où, au centre d'un halo sans ombres, se découpe la petite ombre en croix d'un avion.
- **Prompt** : bible visuelle + Vue exactement verticale d'un paysage agricole de Louisiane : rangs de culture, un chemin, une ferme ; toutes les ombres portées tombent vers l'extérieur d'un halo central plus clair où elles disparaissent ; au centre du halo, l'ombre nette et minuscule d'un avion monomoteur en forme de croix. Rendu quasi cartographique.
- **Alt de référence** : « Vue verticale d'un champ où, au centre d'un halo sans ombres, se découpe la petite ombre en croix d'un avion. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/le-baleinier-sous-la-ville.webp` | à produire |
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
| `images/codex-lena-marchal.webp` | à produire |
| `images/codex-daniel-reyes.webp` | à produire |
| `images/codex-ko-aung.webp` | à produire |
| `images/codex-cross-plains.webp` | à produire |
| `images/codex-maison-robert-e-howard.webp` | à produire |
| `images/codex-rangoun.webp` | à produire |
| `images/codex-gentilly.webp` | à produire |
| `images/codex-le-niantic.webp` | à produire |
| `images/codex-meridian-59.webp` | à produire |
| `images/codex-keyhole.webp` | à produire |
| `images/codex-ingress.webp` | à produire |
| `images/codex-national-geographic.webp` | à produire |
| `images/codex-point-chaud.webp` | à produire |
