# Illustrations de « La Patience des voleurs »

Manifeste pour l’agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d’images listés plus bas, aux noms **exacts**, dans ce dossier (`livres/la-patience-des-voleurs/`) et dans `couvertures/`. C’est tout.

**Règles impératives** :

1. Tu travailles sur la branche de ce dépôt où se trouve ce fichier (celle de la pull request du livre, `claude/new-fiction-writing-2i392n` à la date de ce manifeste). Tu pousses tes commits sur cette branche, jamais sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l’îlot JSON de `index.html`, ni le texte, ni aucun autre fichier — à une exception près : dans le `<head>` de `livres/la-patience-des-voleurs/index.html`, complète la meta `book:author` en ajoutant ton modèle, sous la forme `content="<valeur existante>, <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de La Patience des voleurs : chapitres 1 à 6 »), plusieurs commits bienvenus.
5. Quand tout est produit : pousse, puis signale ta passe dans la pull request ouverte pour cette branche (outil de génération utilisé, écarts éventuels).

**Contraintes techniques** (pour chaque image, sauf mention contraire dans son entrée) :

- Format **WebP** ; si ta chaîne ne produit pas de WebP, convertis :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou : magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```
- Images de chapitre et de notice : **1600×900**, poids **≤ 150 Ko**.
- Couverture : **800×1200** (ratio 2:3), poids **< 300 Ko**.
- **Couverture : aucun texte autorisé**, sans exception — ni titre, sous-titre, nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre est ajouté par-dessus en HTML dans la bibliothèque.
- Images intérieures : aucun texte lisible incrusté. Registres, plaques, affiches, tableaux noirs : écritures **illisibles**, floues ou hors champ — jamais de lettres ni de faux caractères.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/la-patience-des-voleurs
  ```

## Bible visuelle commune

- **Technique et rendu** : gouache et encre sur papier grenu, touche visible, aplats généreux, contours d’encre fins et un peu irréguliers ; l’esprit des illustrations de livres nordiques anciens, sans pastiche d’un artiste vivant. Même rendu pour toutes les images.
- **Palette** : bleus de glace, du céruléen au bleu de Prusse ; blancs de neige cassés ; gris d’ardoise ; bruns de bois sombre. Deux accents seulement : le rouge vermillon et le blanc des jalons (et de l’écharpe d’Isaure), l’or ambré des lanternes. La mer est noir-sarcelle.
- **Lumière** : basse et latérale — aube, crépuscule, lanternes, lampes à huile. La glace profonde est **lumineuse de l’intérieur**, d’un bleu qui semble venir d’une autre salle. Le chaud (bains, poêles, lanternes) répond toujours au froid.
- **Monde** : Demeure, ville nordique préindustrielle (esprit début XIXᵉ siècle) bâtie sur un glacier qui descend vers un fjord. Maisons de bois sombre à toits bas sur pilotis vissés dans la glace ; quelques palais de pierre ; rues de glace sablée où l’on voit des bandes alternées claires et sombres ; lanternes sur perches ; luges, chiens de trait, chevaux ferrés à crampons ; fourrures, laine, crampons aux bottes. Aucune électricité, aucun objet moderne, aucune machine visible hors des chaudières des bains.
- **Géographie récurrente** : une seule rue droite suit la pente ; les rues transversales se courbent vers l’aval, de plus en plus à mesure qu’on descend (« les rues sourient ») ; un rocher noir perce la glace avec une tour de pierre carrée ; le Bureau des Jalons est scellé à la paroi rocheuse nord ; en bas, la ville finit net au bord d’une falaise de glace de trente toises au-dessus d’un fjord sombre.
- **Personnages** : stylisation modérée, proportions réalistes, visages expressifs mais sobres.
- **Interdits** : aucun texte lisible ni pseudo-texte ; aucune scène macabre — **les morts ne sont jamais montrés**, seulement des cercueils fermés, souvent pris dans la glace ; ni sang ni violence ; aucune créature, aucun effet magique ; aucun logo, signature ou filigrane.

### Personnages et objets récurrents

- **Isaure Sorbier** : 27 ans, mince, taille moyenne, visage pâle et grave, sourcils droits, cheveux sombres noués bas ; manteau de laine gris-bleu ; longue **écharpe à larges bandes rouges et blanches** (sa signature visuelle) ; crampons aux bottes ; souvent un faisceau de jalons rouges et blancs, une masse, un carnet rouge.
- **Constant Mérel** : 68 ans, très maigre et grand, rasé de près, cheveux blancs courts, yeux très clairs et plissés ; manteau sombre démodé, trop grand ; chapeau noir (au dernier chapitre : chapeau de feutre gris neuf) ; gestes lents et précis de charpentier.
- **Pétronille Gaudin** : 63 ans, immense, épaules larges, cheveux gris coupés court ; tablier de cuir sur robe de toile, manches roulées, sabots ; il lui manque l’annulaire et l’auriculaire de la main gauche.
- **Tobie Arnal** : 19 ans, grand, dégingandé, blond, visage doux, oreilles très rouges ; habit de laine grise à capuchon, cordelière blanche à la taille ; cloche de bronze tenue par sa courroie.
- **Firmin Vauclair** : 66 ans, lourd, grand visage fatigué, yeux vifs ; pèlerine de laine qui a été noire ; pipe courte ; à partir du chapitre 10, une plaque de cuivre ovale épinglée sur la pèlerine.
- **Hermine Laroque** : 44 ans, grande, mince, visage calme et fin, cheveux tirés en chignon très serré ; manteau gris sans aucun ornement ; gants gris tenus à la main ; au bal, robe de soie grise très simple sous une cape.
- **Mahaut de Frimas** : 58 ans, petite, visage fin et vif, yeux moqueurs ; toque de fourrure ; robe de chambre de velours râpé ou manteau noir ; souvent un balai.
- **La Couronne de Givre** : bandeau d’or blanc haut de deux doigts, **sans ornement**, serti de sept pierres parfaitement claires, comme de la glace qui ne fond pas.
- **Les Affleureurs** : habits de laine grise à capuchon ; cloches de bronze ; luges basses de bois noir.

## Couverture

- **Fichier** : `couvertures/la-patience-des-voleurs.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : une Jalonneuse plante un jalon au sommet d’une ville bâtie sur un glacier ; sous la surface, dans la glace bleue, dort une couronne.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Composition verticale 2:3 en deux registres. Tiers supérieur : ciel de crépuscule d’hiver, du rose au bleu profond, vide et calme (place implicite du titre). Tiers moyen : vue plongeante sur un glacier entre deux parois de roche sombre ; une longue ville de maisons de bois et de lanternes allumées descend en pente vers une falaise de glace et un fjord noir ; au premier plan, petite, de dos, une jeune femme en manteau gris-bleu et longue écharpe à bandes rouges et blanches enfonce à la masse un piquet rouge et blanc dans la glace. Tiers inférieur : la glace vue en coupe, d’un bleu de plus en plus profond, striée de fines bulles, et, tout au fond, prise dans le bleu, une couronne d’or blanc à sept pierres claires qui brille faiblement. Aucun texte, logo, signature, filigrane ni pseudo-texte.
- **Alt de référence** (déjà dans l’îlot, ne pas le modifier) : « Une jeune femme en écharpe rayée rouge et blanc plante un jalon sur un glacier, au-dessus d’une longue ville de bois et de lanternes qui descend vers la mer au crépuscule ; sous ses pieds, dans la glace bleue, brille une couronne d’or blanc. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Vingt-trois jours
- **Sujet** : Une jeune femme en écharpe rayée rouge et blanc, agenouillée dans la neige derrière une maison de bois sur pilotis, mesure une fente dans la glace avec une réglette.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Plan moyen, légère plongée, aube d’hiver rose et bleue. Au premier plan, Isaure agenouillée de trois quarts dos dans la neige, écharpe à bandes rouges et blanches, réglette de buis plongée dans une fente noire qui traverse la glace. Derrière elle, seule, sa maison de bois sombre à deux étages sur ses pilotis, volet gris. Autour, des carrés de pilotis nus et des tas de chevrons numérotés : les maisons voisines démontées. Au fond, le bord de la falaise de glace, puis le vide, puis la mer noire et lisse semée de petits glaçons, et la paroi rocheuse opposée qui rosit. Silence, froid, beauté exacte.
- **Alt de référence** : « Une jeune femme en écharpe rayée rouge et blanc, agenouillée dans la neige derrière une maison de bois sur pilotis, mesure une fente dans la glace avec une réglette ; au-delà, le bord de la falaise de glace et une mer noire semée de glaçons, à l’aube. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Cinquante-huit, an 571
- **Sujet** : Un vieil homme maigre en manteau trop grand mange une soupe à une table sous des poutres sombres entaillées d’encoches.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur de nuit, lumière chaude d’une lampe à huile et rougeoiement d’un poêle de fonte. Constant, très maigre, cheveux blancs, rasé de près, manteau sombre démodé trop grand, chapeau posé sur les genoux, mange une soupe à une table de bois ; il lève les yeux vers la maîtresse poutre du plafond, où l’on distingue trois encoches. Isaure debout, bras croisés, près du poêle, méfiante. Caisses de déménagement à moitié faites, étagères vides. Ombres profondes, tendresse retenue.
- **Alt de référence** : « Un vieil homme maigre en manteau trop grand mange une soupe à une table sous des poutres sombres entaillées d’encoches ; une jeune femme debout près d’un poêle de fonte le regarde, entre des caisses à moitié faites. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Un pas par jour
- **Sujet** : Seule la nuit dans une grande salle sombre, une jeune femme penchée sur une longue table couverte de registres jaunis et de calques, dans le cercle d’une lampe.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur de nuit, grande salle du Bureau des Jalons aux murs de pierre. Une lampe fait un cercle de lumière sur une longue table couverte de registres ouverts, de colonnes de chiffres illisibles, de calques et d’une règle ; deux pierres grises servent de presse-papiers. Isaure, écharpe rayée sur les épaules, penchée, crayon à la main. Au fond, de hautes fenêtres : en contrebas, la ville de bois et de lanternes descend en longue pente sur le glacier jusqu’à la mer noire. Atmosphère d’obsession paisible, fin de nuit.
- **Alt de référence** : « Seule la nuit dans une grande salle sombre, une jeune femme penchée sur une longue table couverte de registres jaunis et de calques, dans le cercle d’une lampe ; par les fenêtres, la ville illuminée descend en pente vers la mer. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Nul n’arrête un Remis
- **Sujet** : Dans une rue de glace sablée, une procession de quatre silhouettes encapuchonnées de gris tire une luge basse portant un cercueil noirci.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Rue commerçante d’une ville de bois sur la glace, en plein jour gris. Au centre, une petite procession traverse la rue : quatre porteurs en habit de laine grise à capuchon tirent une luge basse de bois noir où repose un cercueil sombre ; l’un tient une cloche de bronze par une courroie ; derrière, une famille en noir. À gauche, un sergent massif à moustache de phoque, descendu d’un grand cheval gris ferré à crampons, tient son casque contre sa poitrine. Marchands, porteurs d’eau, enfants, dames en fourrure : tous figés, tête nue. Un chien de trait attelé attend. Dignité, humour discret.
- **Alt de référence** : « Dans une rue de glace sablée, une procession de quatre silhouettes encapuchonnées de gris tire une luge basse portant un cercueil noirci ; un sergent à moustache, descendu de son cheval gris, tient son casque contre sa poitrine, et tous les passants sont tête nue. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — La glacière basse
- **Sujet** : Dans une longue cave basse taillée dans la glace bleue, une jeune femme lève une lanterne vers un mur où l’on devine, pris dans la glace, un cercueil sombre.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur souterrain : une salle longue et basse creusée au ciseau dans une glace d’un bleu profond, lumineuse de l’intérieur. Jambons et gibiers pendus, tonnelets de beurre, grands blocs de glace pure le long d’un mur. Isaure lève une lanterne vers le mur du fond : à deux pieds dans la glace, net comme une mouche dans l’ambre, un cercueil de bois noirci, légèrement incliné, ferrures aux coins, une petite plaque claire. Derrière elle, Hermine, grande, mince, manteau gris sans ornement, chignon serré, gants à la main. Une vieille femme en fourrures tient une seconde lanterne. Froid, silence, révélation.
- **Alt de référence** : « Dans une longue cave basse taillée dans la glace bleue, une jeune femme lève une lanterne vers un mur où l’on devine, pris dans la glace, un cercueil sombre ; derrière elle, une grande femme en manteau gris observe. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Quarante et un ans
- **Sujet** : La nuit, au milieu d’une place de neige vierge entourée de vieilles façades aux fenêtres éclairées, un vieil homme et une jeune femme se tiennent debout sous une neige fine qui tourne dans la lumière des lanternes.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Nuit d’hiver. Plan large en plongée sur une grande place carrée couverte de neige intacte, bordée de façades de bois de quarante ans, serrées, aux fenêtres jaunes. Une ligne de pas droite mène au centre, où se tiennent Constant (chapeau noir, manteau trop grand) et Isaure (écharpe rayée). Aux coins, des lanternes sur perches ; neige fine qui flotte dans leurs ronds de lumière. Un poteau au coin porte une plaque de cuivre verdie (sans inscription lisible). Mélancolie, confidence, immensité du vide.
- **Alt de référence** : « La nuit, au milieu d’une place de neige vierge entourée de vieilles façades aux fenêtres éclairées, un vieil homme et une jeune femme se tiennent debout sous une neige fine qui tourne dans la lumière des lanternes. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — En attendant la Couronne
- **Sujet** : Dans un bureau blanchi à la chaux, chauffé par un poêle de faïence, une grande femme en gris sert du thé à une jeune femme assise.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur de jour, lumière froide d’une fenêtre haute. Pièce nue blanchie à la chaux : une table, deux chaises, un poêle de faïence blanc. Au mur, une grande carte dessinée de la ville en long ruban sur son glacier, piquée d’épingles à tête de couleur (aucun texte lisible). Hermine, debout, grande, en gris, verse du thé d’une théière dans une tasse, les gants posés parallèles sur la table. Isaure assise, raide, écharpe rayée, mains sur les genoux. Tension feutrée, politesse glaciale.
- **Alt de référence** : « Dans un bureau blanchi à la chaux, chauffé par un poêle de faïence, une grande femme en gris sert du thé à une jeune femme assise ; au mur, une grande carte de la ville piquée d’épingles colorées. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Le moulin
- **Sujet** : Suspendue à une corde dans un puits de glace qui descend en spirale, une jeune femme éclairée par une lanterne à sa ceinture passe devant des couches de glace ancienne où une feuille verte est prise comme dans du verre.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Vue verticale vertigineuse à l’intérieur d’un puits rond creusé par l’eau dans la glace, qui tourne comme une coquille d’escargot. Isaure, baudrier de corde, crampons, barre de fer à la main, lanterne sourde à la ceinture, descend au bout d’une corde tendue. Les parois défilent : bleu clair en haut, bleu nuit, puis noir en bas ; strates de bulles, une fine bande grise de cendre, et, à hauteur de son visage, une feuille de bouleau encore verte prise dans la glace. De l’eau ruisselle. En bas, l’obscurité totale et une brume. Peur, émerveillement.
- **Alt de référence** : « Suspendue à une corde dans un puits de glace qui descend en spirale, une jeune femme éclairée par une lanterne à sa ceinture passe devant des couches de glace ancienne où une feuille verte est prise comme dans du verre. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — La Margravine en attente
- **Sujet** : Dans une bibliothèque froide aux rayonnages blanchis, une petite femme âgée en robe de chambre de velours et toque de fourrure se tient près d’un tableau noir couvert de calculs à la craie pâlie.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur d’un vieux palais, matin gris. Bibliothèque aux rayonnages jusqu’au plafond, livres reliés au dos blanchi, givre sur les vitres. Un poêle de fonte, une table couverte de cartes à jouer étalées en réussite, un vieux domestique endormi sur un tabouret contre les livres. Mahaut, petite, visage fin et vif, toque de fourrure, robe de chambre de velours râpé, touche du bout du doigt un grand tableau noir sur chevalet couvert de calculs à la craie presque effacés (aucun caractère lisible). Isaure, dans un manteau mouillé, la regarde. Émotion contenue, poussière et lumière.
- **Alt de référence** : « Dans une bibliothèque froide aux rayonnages blanchis, une petite femme âgée en robe de chambre de velours et toque de fourrure se tient près d’un tableau noir couvert de calculs à la craie pâlie ; une jeune femme la regarde, près d’un poêle. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — La nuit du Vêlage
- **Sujet** : Dans un tunnel rond de glace bleue éclairé de lanternes, une grande femme dirige un jet d’eau fumante vers la paroi.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur d’un boyau rond creusé dans une glace bleu profond, lumineux, ruisselant, plein de vapeur. Au premier plan, Pétronille, immense, tablier de cuir, manches roulées, tient une longue lance de cuivre emmanchée de bois d’où jaillit un fin jet d’eau chaude ; un jeune homme blond en habit gris actionne une pompe à bras. Au fond du tunnel, dans la vapeur, le flanc d’un cercueil de bois noirci émerge de la glace comme un navire échoué ; Constant, enveloppé de couvertures, à genoux dans l’eau, y pose sa main nue à plat. Isaure tient une lanterne. Tension, recueillement, lumière d’avant la lumière.
- **Alt de référence** : « Dans un tunnel rond de glace bleue éclairé de lanternes, une grande femme dirige un jet d’eau fumante vers la paroi ; au fond, un vieil homme pose la main à plat sur le bois noirci d’un cercueil qui sort de la glace. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — La Glissoire
- **Sujet** : La nuit, une procession traverse une place pleine de monde éclairée de lanternes de papier colorées : un novice encapuchonné tire une luge portant un cercueil et fait sonner une cloche, un vieil homme est assis à la tête du cercueil, une jeune femme marche à côté.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Nuit de fête, plan large. Une grande place carrée se remplit d’une foule silencieuse et tête nue ; lanternes de papier rouges, jaunes et vertes sur des perches, enfants avec des couronnes de papier doré à la main. Au centre, une luge basse de bois noir porte un cercueil ; Tobie, grand, blond, en habit gris à capuchon, la tire et tient une cloche de bronze par sa courroie ; une grande femme en tablier tire à côté de lui. Constant est assis à la tête du cercueil, enveloppé de couvertures, une main sur la plaque. Isaure marche à côté, une main sur le bois. Derrière, d’autres luges et lanternes. Recueillement, émotion collective.
- **Alt de référence** : « La nuit, une procession traverse une place pleine de monde éclairée de lanternes de papier colorées : un novice encapuchonné tire une luge portant un cercueil et fait sonner une cloche, un vieil homme est assis à la tête du cercueil, une jeune femme marche à côté. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — Désormais
- **Sujet** : Au printemps, dans le coin d’une place de neige fondante, un vieil homme au chapeau de feutre gris plante un piquet rouge et blanc à la masse.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Fin d’après-midi de printemps, lumière dorée et douce, neige fondante, rigoles d’eau qui brillent sur la glace. Constant, maigre, chapeau de feutre gris neuf, enfonce à la masse un jalon à bandes rouges et blanches au coin d’un lot marqué de galets alignés. Isaure, écharpe rayée, fil à plomb à la main, le regarde en souriant. À côté, une luge de Remonteur chargée de grosses poutres noircies marquées d’encoches, tirée par une chienne grise. Au fond de la place, des enfants font des glissades autour d’un bonhomme de neige coiffé d’une couronne de papier doré. Au loin, au bout d’une longue rue, la mer. Paix, légèreté, commencement.
- **Alt de référence** : « Au printemps, dans le coin d’une place de neige fondante, un vieil homme au chapeau de feutre gris plante un piquet rouge et blanc à la masse ; une jeune femme le regarde, près d’une luge chargée de vieilles poutres tirée par une chienne grise. »

## Images de notices

### `images/codex-isaure-sorbier.webp`

- **Notice** : Isaure Sorbier (personnage)
- **Sujet** : Portrait d’une jeune femme au visage pâle et grave, cheveux sombres noués bas, écharpe à larges bandes rouges et blanches, un jalon sur l’épaule.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait en buste, extérieur, aube bleue sur la glace. Isaure, vingt-sept ans, visage pâle et attentif, sourcils droits, cheveux sombres noués bas, manteau de laine gris-bleu, écharpe à larges bandes rouges et blanches. Elle porte sur l’épaule un faisceau de jalons peints et tient un carnet rouge. Regard direct, exact, un peu farouche.
- **Alt de référence** : « Portrait d’une jeune femme au visage pâle et grave, cheveux sombres noués bas, écharpe à larges bandes rouges et blanches, un jalon sur l’épaule. »

### `images/codex-constant-merel.webp`

- **Notice** : Constant Mérel (personnage)
- **Sujet** : Portrait d’un vieil homme très maigre, rasé de près, aux yeux clairs plissés, en manteau sombre trop grand, qui pèle une orange.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait en buste, fond d’étuve de bois flou et chaud. Constant, soixante-huit ans, très maigre, cheveux blancs courts, rasé de près, yeux très clairs et plissés comme ceux des gens qui ont regardé la neige au soleil, sourire en coin, manteau sombre démodé trop large aux épaules. Il pèle une orange avec des gestes lents et précis de charpentier. Malice, patience, chagrin caché.
- **Alt de référence** : « Portrait d’un vieil homme très maigre, rasé de près, aux yeux clairs plissés, en manteau sombre trop grand, qui pèle une orange. »

### `images/codex-firmin-vauclair.webp`

- **Notice** : Firmin Vauclair (personnage)
- **Sujet** : Portrait d’un vieil homme lourd au grand visage, en pèlerine usée, qui rallume une pipe courte en protégeant l’allumette de sa main.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait en buste, escalier de pierre dans la pénombre, lanterne scellée dans le roc. Firmin, soixante-six ans, massif, grand visage lourd et fatigué, yeux vifs, pèlerine de laine qui a été noire, une plaque de cuivre ovale épinglée dessus, rallume une pipe courte en protégeant la flamme de sa grosse main. Obstination, ironie, bonté bourrue.
- **Alt de référence** : « Portrait d’un vieil homme lourd au grand visage, en pèlerine usée, qui rallume une pipe courte en protégeant l’allumette de sa main. »

### `images/codex-hermine-laroque.webp`

- **Notice** : Hermine Laroque (personnage)
- **Sujet** : Portrait d’une grande femme mince en manteau gris sans ornement, chignon très serré, qui tient ses gants à la main.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait à mi-corps, bureau blanchi à la chaux, lumière froide. Hermine, quarante-quatre ans, grande, mince, visage calme et fin comme sculpté dans la glace, cheveux tirés en chignon serré, manteau gris sans aucun ornement ; elle tient à la main une paire de gants gris qu’elle ne met pas. Intelligence, maîtrise, une pointe de lassitude.
- **Alt de référence** : « Portrait d’une grande femme mince en manteau gris sans ornement, chignon très serré, qui tient ses gants à la main. »

### `images/codex-mahaut-de-frimas.webp`

- **Notice** : Mahaut de Frimas (personnage)
- **Sujet** : Portrait d’une petite femme âgée au visage vif et ironique, toque de fourrure, robe de velours râpé, un balai tenu comme une crosse.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait en pied, vestibule glacé d’un palais, housses grises sur les meubles, givre aux vitres. Mahaut, cinquante-huit ans, petite, visage fin, yeux moqueurs, toque de fourrure, robe de chambre de velours râpé, tient un balai comme une crosse d’évêque. Derrière elle, des portraits de Margraves dont on ne voit que les mains. Dignité, humour, solitude.
- **Alt de référence** : « Portrait d’une petite femme âgée au visage vif et ironique, toque de fourrure, robe de velours râpé, un balai tenu comme une crosse. »

### `images/codex-petronille-gaudin.webp`

- **Notice** : Pétronille Gaudin (personnage)
- **Sujet** : Portrait d’une femme immense aux cheveux gris courts, tablier de cuir et manches roulées, qui rit.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait à mi-corps, chaufferie d’un établissement de bains, lueur rouge des chaudières. Pétronille, soixante-trois ans, immense, épaules de Fendeuse, cheveux gris coupés court, tablier de cuir sur une robe de toile, manches roulées ; elle rit franchement, sa main gauche, à qui manquent l’annulaire et l’auriculaire, posée sur une longue lance de cuivre. Force, générosité, gouaille.
- **Alt de référence** : « Portrait d’une femme immense aux cheveux gris courts, tablier de cuir et manches roulées, qui rit ; il lui manque deux doigts à la main gauche. »

### `images/codex-tobie-arnal.webp`

- **Notice** : Tobie Arnal (personnage)
- **Sujet** : Portrait d’un grand jeune homme blond aux oreilles rouges, en habit de laine grise à capuchon, qui tient une cloche de bronze par sa courroie.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Portrait à mi-corps, rue de glace au crépuscule, lanternes. Tobie, dix-neuf ans, grand, maigre, blond, visage doux, oreilles rouges de froid, habit de laine grise à capuchon rabattu, cordelière blanche à la taille ; il tient par sa courroie une cloche de bronze grosse comme deux poings. Il chante, les yeux mi-clos. Ferveur, timidité, courage.
- **Alt de référence** : « Portrait d’un grand jeune homme blond aux oreilles rouges, en habit de laine grise à capuchon, qui tient une cloche de bronze par sa courroie. »

### `images/codex-demeure.webp`

- **Notice** : Demeure (lieu)
- **Sujet** : Vue plongeante sur une longue ville de maisons de bois et de palais de pierre bâtie sur un glacier entre deux parois rocheuses, qui descend jusqu’à une falaise de glace au-dessus d’un bras de mer.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Vue panoramique en plongée depuis le haut d’une paroi rocheuse, fin d’après-midi d’hiver. Un glacier large et régulier descend entre deux murailles de roche sombre ; dessus, une ville de trois lieues : maisons de bois sur pilotis, toits bas enneigés, quelques palais de pierre, fumées, lanternes qui s’allument. Une seule rue droite suit la pente au milieu ; les rues transversales se courbent de plus en plus vers le bas, en sourires. Un rocher noir perce la glace avec une tour. Tout en bas, la ville s’arrête net au bord d’une falaise de glace au-dessus d’un fjord sombre où mouillent des voiliers.
- **Alt de référence** : « Vue plongeante sur une longue ville de maisons de bois et de palais de pierre bâtie sur un glacier entre deux parois rocheuses, qui descend jusqu’à une falaise de glace au-dessus d’un bras de mer. »

### `images/codex-la-tour.webp`

- **Notice** : La Tour, le Roc et le Sillage (lieu)
- **Sujet** : Une tour de pierre noire sur un rocher qui perce le glacier.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Plan moyen, lumière grise de midi. Un rocher de granit noir émerge de la glace comme le dos d’une baleine ; dessus, une tour carrée de pierre, massive, à fenêtres étroites, avec un escalier extérieur qui descend vers la glace. En amont, une bande de neige vide ; en aval, le glacier se referme en un chaos de séracs bleus et de crevasses aux ponts de neige. À l’arrière-plan, les toits de la ville qui passe. Une ligne de piquets rouges et blancs traverse le chaos.
- **Alt de référence** : « Une tour de pierre noire sur un rocher qui perce le glacier ; la glace se fend autour de lui et se referme derrière en un chaos de blocs bleus et de crevasses. »

### `images/codex-glaciere-basse.webp`

- **Notice** : La glacière basse (lieu)
- **Sujet** : Une cave basse et longue taillée dans une glace d’un bleu profond, où pendent du gibier et des jambons.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur souterrain vide de personnages, lumière d’une unique lanterne posée sur un tonnelet de beurre. Voûte basse taillée au ciseau dans une glace bleu profond, marques d’outils visibles, fines strates de bulles. Gibier et jambons pendus à des crochets, grands blocs de glace pure alignés. Au fond, dans l’épaisseur du mur, une ombre longue et sombre, légèrement inclinée, aux contours de cercueil, qu’on devine plus qu’on ne la voit. Mystère, froid.
- **Alt de référence** : « Une cave basse et longue taillée dans une glace d’un bleu profond, où pendent du gibier et des jambons ; dans le mur du fond, une ombre allongée prise dans la glace. »

### `images/codex-les-etuves.webp`

- **Notice** : Les Étuves de la Veine (lieu)
- **Sujet** : Sous une verrière embuée, un grand bassin d’eau chaude plein de baigneurs dans la vapeur.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur d’un établissement de bains, soir d’hiver. Grand bassin sous une verrière couverte de buée, colonnes de brique, rigoles de cuivre où coule l’eau, lanternes qui font des lunes dans la vapeur. Des baigneurs de tous âges et de toutes conditions, pudiquement enveloppés de vapeur et de serviettes, rient et chantent. Au fond, Pétronille, immense, cheveux gris courts, tablier de cuir, bras chargés de serviettes. Chaleur, égalité, bonne humeur.
- **Alt de référence** : « Sous une verrière embuée, un grand bassin d’eau chaude plein de baigneurs dans la vapeur ; au fond, une grande femme en tablier de cuir porte des serviettes. »

### `images/codex-carre-d-attente.webp`

- **Notice** : Le Carré d’Attente (lieu)
- **Sujet** : Une grande place carrée de neige vierge au milieu de vieilles maisons serrées.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Matin d’hiver clair. Vue d’ensemble d’une place carrée de cent pas couverte de neige intacte, cernée de façades de bois de quarante ans, serrées comme des vieillards sur un banc, aux volets colorés passés. Dans un coin, quelques enfants en bonnets font des glissades et laissent des traces. Au coin, un poteau de bois porte une plaque de cuivre vert-de-grisée (inscription illisible). Le centre de la place reste parfaitement vide, lumineux.
- **Alt de référence** : « Une grande place carrée de neige vierge au milieu de vieilles maisons serrées ; des enfants font des glissades près d’un poteau portant une plaque de cuivre verdie. »

### `images/codex-hotel-de-frimas.webp`

- **Notice** : L’Hôtel de Frimas (lieu)
- **Sujet** : Un palais de pierre à trois étages, perron à double escalier et blasons rongés par le givre.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Extérieur, matin gris. Façade d’un palais de pierre de taille de trois étages, hautes fenêtres aux volets fermés, blasons ronds usés par le givre, posé sur une plate-forme de chêne noir au-dessus de la glace. Un perron à double escalier. Sur les marches, Mahaut, petite silhouette en toque de fourrure et manteau noir, balaie la neige à grands coups secs. Grandeur passée, solitude, humour.
- **Alt de référence** : « Un palais de pierre à trois étages, perron à double escalier et blasons rongés par le givre ; une petite femme en toque de fourrure balaie les marches. »

### `images/codex-affleurement.webp`

- **Notice** : L’affleurement (glace)
- **Sujet** : Sous le plancher d’une maison, entre des pilotis, trois porteurs encapuchonnés veillent à genoux autour d’un couvercle de cercueil qui affleure dans la glace, à la lueur de deux lanternes.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Intérieur bas et sombre : le vide sous une maison, entre des pilotis de mélèze et un plancher. Trois Affleureurs en habit gris à capuchon, dont un grand jeune homme blond à cordelière blanche, agenouillés autour d’un rectangle de glace plus sombre où l’on voit, à un doigt sous la surface, le couvercle d’un cercueil et sa plaque verdie. Deux lanternes de fer posées sur la glace. Recueillement, patience, lumière chaude contre le froid.
- **Alt de référence** : « Sous le plancher d’une maison, entre des pilotis, trois porteurs encapuchonnés veillent à genoux autour d’un couvercle de cercueil qui affleure dans la glace, à la lueur de deux lanternes. »

### `images/codex-couronne-de-givre.webp`

- **Notice** : La Couronne de Givre (objet)
- **Sujet** : Un simple bandeau d’or blanc serti de sept pierres claires comme de la glace, posé sur un coussin sombre dans la pénombre.
- **Prompt** : Gouache et encre sur papier grenu, touche visible, palette de bleus de glace, blancs cassés, gris d’ardoise et bois sombre, accents rouge vermillon des jalons et or des lanternes ; lumière basse, glace lumineuse de l’intérieur ; ville nordique préindustrielle sur un glacier ; aucun texte lisible ni pseudo-texte. Format paysage 16:9. Nature morte, cadrage serré, fond sombre de velours bleu nuit. Une couronne très simple : un bandeau d’or blanc haut de deux doigts, sans ornement, serti de sept pierres parfaitement claires qui semblent de la glace qui ne fond pas. Elle repose sur un coussin ancien. Une lumière froide de lucarne fait naître sept petites étincelles. Quelques flocons sur le velours. Sobriété, prestige, mystère.
- **Alt de référence** : « Un simple bandeau d’or blanc serti de sept pierres claires comme de la glace, posé sur un coussin sombre dans la pénombre. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/la-patience-des-voleurs.webp` | à produire |
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
| `images/codex-isaure-sorbier.webp` | à produire |
| `images/codex-constant-merel.webp` | à produire |
| `images/codex-firmin-vauclair.webp` | à produire |
| `images/codex-hermine-laroque.webp` | à produire |
| `images/codex-mahaut-de-frimas.webp` | à produire |
| `images/codex-petronille-gaudin.webp` | à produire |
| `images/codex-tobie-arnal.webp` | à produire |
| `images/codex-demeure.webp` | à produire |
| `images/codex-la-tour.webp` | à produire |
| `images/codex-glaciere-basse.webp` | à produire |
| `images/codex-les-etuves.webp` | à produire |
| `images/codex-carre-d-attente.webp` | à produire |
| `images/codex-hotel-de-frimas.webp` | à produire |
| `images/codex-affleurement.webp` | à produire |
| `images/codex-couronne-de-givre.webp` | à produire |

28 fichiers au total : une couverture, 12 images de chapitre, 15 images de notices. Le décompte correspond exactement aux champs `image` de l’îlot et à `cover.catalogImage`.
