# Illustrations de « Quatre jours par heure »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/quatre-jours-par-heure/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Tu travailles sur la branche `claude/nouvelle-fiction-libre-xxd43x` de ce dépôt (celle où se trouve ce
   fichier). Tu pousses tes commits sur cette branche, jamais sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON
   de `index.html`, ni le texte, ni aucun autre fichier — à une exception
   près : dans le `<head>` de `livres/quatre-jours-par-heure/index.html`, complète la meta
   `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Opus 5.5 (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Quatre jours par heure : chapitres 1 à 5 »),
   plusieurs commits bienvenus.
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
- Images intérieures : aucun texte lisible incrusté. Les cadrans de montre et
  d'horloge restent **sans chiffres lisibles** ; l'inscription du linteau de
  l'Écluse, les étiquettes du Greffe et les registres restent suggérés,
  jamais déchiffrables.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/quatre-jours-par-heure
  ```

## Bible visuelle commune

Gouache et encre sur papier à grain visible, dans l'esprit des affiches de montagne de l'entre-deux-guerres revisitées par l'illustration contemporaine : aplats francs, contours simplifiés mais crédibles, aucun photoréalisme. Palette dominante froide — neige, ardoise, bleu de glacier, gris des veilleuses — avec **un seul accent chaud par image** : le laiton des montres, la flamme d'une lampe, le manteau rouge de Capucine. Monde technique des années 1930 en bas (tramways à perche, réverbères, postes de radio), plus ancien à mesure qu'on monte (XVIIIe siècle à l'Hospice).

**La règle du monde doit se voir** : le temps ralentit avec l'altitude. Ce qui est plus bas que le point de vue se représente avec des traînées, des superpositions, des mouvements trop rapides ; ce qui est plus haut, figé, lissé, comme du verre. Au-dessus du Pas de l'Écluse, le ciel « bat » : on le figure par des bandes alternées claires et sombres, ou par des traits de lumière qui passent par les fentes des volets. Aux Terrasses, une lumière grise, égale, sans source.

Ton : aventure tendue et tendre ; la tension vient du cadrage, de l'échelle (montagne immense, personnages petits) et de la lumière, jamais de la violence. On ne montre jamais : sang, blessure, aiguille plantée dans la peau en gros plan, visage d'enfant souffrant de façon insistante, texte lisible, logo, marque réelle.

### Personnages et lieux récurrents

- **Lou Ferrand** — 39 ans, horlogère ; cheveux châtains courts attachés, visage fin, petite ride verticale entre les sourcils ; manteau de montagne brun, pantalon de toile, sac à dos ; au poignet gauche, une grosse montre de laiton à deux cadrans côte à côte.
- **Nine Ferrand** — sa fille ; 14 ans au chapitre 1 (cheveux coupés très court et de travers), 16 ans au chapitre 10 (cheveux aux épaules) ; blouson d'homme trop grand, même ride naissante que sa mère.
- **Orso Lebreuil** — passeur, 53 ans d'apparence ; moustache grise soignée, manteau de drap sombre, chapeau d'un autre siècle, pipe de terre ; barbe grise de deux semaines au seul chapitre 8.
- **Capucine Rigal** — 9 ans, manteau rouge boutonné jusqu'au menton, regard frondeur, un roman d'aventures à couverture d'aéroplane.
- **Hélène Ferrand** — 32 ans, plus petite que Lou, cheveux noirs en chignon défait, taches de rousseur, robe de laine grise de veilleuse et tablier.
- **Tobie Ferrand** — 7 ans, très maigre, cheveux collés, grands yeux, cheval de bois.
- **Anselme Lestang** — 60 ans, grand, cheveux blancs courts, habit noir boutonné jusqu'au menton, longues mains propres.
- **Adrienne Coquard** — 62 ans, chignon gris tiré, loupe d'horloger dans l'orbite gauche, manchettes de lustrine noire.
- **Le Tardif** — montagne solitaire au-dessus d'une plaine ; une longue cascade blanche (la Pendule) sur son flanc ; l'Hospice, forteresse grise à galeries de bois, collée à une falaise vers le tiers supérieur ; au-dessus, une brume grise lumineuse.

## Couverture

- **Fichier** : `couvertures/quatre-jours-par-heure.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : l'ascension vers l'Hospice sous un ciel coupé entre le jour et la nuit.
- **Prompt** : bible visuelle + composition verticale 2:3 ; en bas, minuscule, une femme en manteau brun (Lou) sur un sentier en lacets ; la falaise monte sur toute la hauteur, avec la cascade figée comme du verre ; au tiers supérieur, l'Hospice gris accroché à la roche, une seule fenêtre chaude ; le ciel, derrière, partagé en bandes verticales ou diagonales alternant jour pâle et nuit étoilée, comme un battement ; laisser respirer le tiers supérieur (le titre HTML s'y posera) ; aucun texte, logo, signature, filigrane ou pseudo-texte.
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) : « Une femme en manteau de montagne gravit un sentier en lacets vers un hospice accroché à une falaise, sous un ciel coupé en deux entre le jour et la nuit. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Les deux cadrans
- **Sujet** : Avant l’aube, rue des Cadrans, une femme en manteau de montagne regarde sa montre sous un réverbère ; au fond, la montagne noire, et tout en haut une seule fenêtre éclairée.
- **Prompt** : bible visuelle + Rue pavée d'une petite ville de vallée, juste avant l'aube, ciel encore noir ; Lou, 39 ans, sac de montagne au dos, sous un réverbère à gaz, regarde la grosse montre de laiton à son poignet ; enseigne d'horloger en tôle au-dessus d'une boutique au rideau de fer baissé (lettrage illisible) ; au fond, la masse immense du Tardif, et très haut contre la falaise, une seule petite fenêtre allumée.
- **Alt de référence** : « Avant l’aube, rue des Cadrans, une femme en manteau de montagne regarde sa montre sous un réverbère ; au fond, la montagne noire, et tout en haut une seule fenêtre éclairée. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — La cascade arrêtée
- **Sujet** : Trois marcheurs, dont une fillette en manteau rouge, montent un sentier en lacets le long d’une cascade vive en bas et figée comme du verre en haut.
- **Prompt** : bible visuelle + Sentier en lacets entre des murets de pierres sèches, prés en pente ; Orso (moustache grise, manteau de drap, chapeau) devant, Capucine (9 ans, manteau rouge) au milieu la main en visière, Lou derrière ; à côté d'eux, la Pendule : en bas l'eau bouillonne et éclabousse, au milieu elle s'étire, tout en haut elle paraît immobile, un ruban de verre ; lumière de matinée qui glisse trop vite, ombres déjà longues.
- **Alt de référence** : « Trois marcheurs, dont une fillette en manteau rouge, montent un sentier en lacets le long d’une cascade vive en bas et figée comme du verre en haut. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Le musée de ce qui n’est pas monté
- **Sujet** : À la lueur d’une bougie, une femme accroupie ouvre une montre de laiton dans une longue voûte encombrée d’objets anciens étiquetés.
- **Prompt** : bible visuelle + Intérieur du Greffe des Saisies, voûte de rocher en perspective profonde ; au premier plan, Lou accroupie près d'une porte cloutée, une bougie posée au sol, dévisse le fond de sa montre et découvre une petite fiole trouble dans du coton ; derrière elle, étagères jusqu'au plafond : vélocipède à grande roue pendu, phonographe, postes de radio, lampes à huile ; par la fente de la porte, le ciel commence à pâlir.
- **Alt de référence** : « À la lueur d’une bougie, une femme accroupie ouvre une montre de laiton dans une longue voûte encombrée d’objets anciens étiquetés. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Le ciel qui bat
- **Sujet** : Trois silhouettes encordées avancent sur une crête étroite pendant qu’un mur de neige avale la plaine et que le ciel alterne bandes de jour et de nuit.
- **Prompt** : bible visuelle + Plan large sur une crête rocheuse étroite munie de chaînes ; trois silhouettes encordées, dont une petite en rouge ; à l'ouest, une barre de tempête grise qui roule sur la plaine en avalant les villages ; au-dessus, un ciel strié de bandes alternées claires et sombres, comme si le jour et la nuit se succédaient trop vite ; mélèzes rouille qui perdent leurs aiguilles dans le vent.
- **Alt de référence** : « Trois silhouettes encordées avancent sur une crête étroite pendant qu’un mur de neige avale la plaine et que le ciel alterne bandes de jour et de nuit. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — La Longue Veille
- **Sujet** : Dans une chambre blanchie à la chaux éclairée d’une lampe à pétrole, une jeune femme en robe grise entre avec une cuvette et découvre une femme plus âgée près d’un petit garçon alité.
- **Prompt** : bible visuelle + Chambre étroite à la chaux, lit de fer, poêle de faïence, lampe à pétrole au verre fêlé ; Tobie (7 ans, maigre, cheval de bois) assis dans le lit, yeux ronds ; Lou debout près du lit ; dans l'encadrement de la porte, Hélène (32 ans, robe grise, tablier, taches de rousseur) tient une cuvette d'eau fumante et fixe Lou sans la reconnaître ; volet plein à fente horizontale, trait de lumière froide sur le mur.
- **Alt de référence** : « Dans une chambre blanchie à la chaux éclairée d’une lampe à pétrole, une jeune femme en robe grise entre avec une cuvette et découvre une femme plus âgée près d’un petit garçon alité. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Une nuit de vingt-deux ans
- **Sujet** : Une femme est assise la nuit sur un banc de galerie devant une porte close ; un trait de lumière venu d’une fente de volet barre le mur en face.
- **Prompt** : bible visuelle + Galerie de bois de l'Hospice, la nuit ; Lou assise sur un banc, une couverture sur les épaules, une feuille de papier gris et une plume sur les genoux ; à côté d'elle une porte fermée sous laquelle filtre la lueur d'une lampe ; sur le mur d'en face, un trait de lumière horizontal venu d'une fente de volet, capté à l'instant où il s'allume ; atmosphère d'attente, silence.
- **Alt de référence** : « Une femme est assise la nuit sur un banc de galerie devant une porte close ; un trait de lumière venu d’une fente de volet barre le mur en face. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — La chambre haute
- **Sujet** : Dans une cellule taillée dans la roche, une femme trace des bâtons au clou sur la paroi près d’une meurtrière qui clignote.
- **Prompt** : bible visuelle + Cellule minuscule creusée dans le rocher, paillasse, cruche, grille au fond ; Lou de profil, un clou rouillé à la main, trace des bâtons groupés par cinq sur la paroi ; à côté, une meurtrière large comme une main par laquelle on voit le vide et un ciel qui passe du clair au sombre ; lumière dure, intermittente.
- **Alt de référence** : « Dans une cellule taillée dans la roche, une femme trace des bâtons au clou sur la paroi près d’une meurtrière qui clignote. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Le puits des vendanges
- **Sujet** : À l’aube, sur une terrasse au-dessus du vide, des dizaines d’enfants en chemise de nuit tenant des bougies regardent un homme barbu sortir d’un puits dans un panier.
- **Prompt** : bible visuelle + Terrasse de pierre sous un auvent de poutres noircies, aube grise ; un grand treuil à tambour de chêne tourné par un homme massif et des femmes en robe grise ; du puits rond et noir émerge un panier d'osier cerclé de fer où se tient Orso, barbe grise de deux semaines, lanterne à la main, bidons de cuivre à ses pieds ; derrière, une foule d'enfants pâles en chemise de nuit, pieds nus, bougies à la main ; un homme en habit noir immobile au milieu d'eux.
- **Alt de référence** : « À l’aube, sur une terrasse au-dessus du vide, des dizaines d’enfants en chemise de nuit tenant des bougies regardent un homme barbu sortir d’un puits dans un panier. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Le temps de tout le monde
- **Sujet** : Par la fente d’un volet ouvert, une femme regarde la plaine d’en bas où l’on voit en même temps l’aube, le plein jour et le crépuscule.
- **Prompt** : bible visuelle + Vue depuis l'intérieur d'une galerie de l'Hospice : Lou de dos, penchée à un volet entrouvert, une montre d'argent ouverte dans la main ; dehors, loin en bas, une plaine d'hiver et une petite ville, représentées comme une superposition de moments de la même journée — aube rose à gauche, midi blanc au centre, crépuscule et réverbères à droite ; un trait de vapeur de train traverse la vallée.
- **Alt de référence** : « Par la fente d’un volet ouvert, une femme regarde la plaine d’en bas où l’on voit en même temps l’aube, le plein jour et le crépuscule. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — Un seul cadran
- **Sujet** : Sur le quai d’une petite gare au pied de la montagne, une adolescente debout sous l’horloge fait face à une femme qui arrive, sac au dos.
- **Prompt** : bible visuelle + Quai d'une petite gare terminus de tramway, fin de journée de mai ; un tramway électrique à perche arrêté ; sous l'horloge du quai (cadran sans chiffres lisibles), Nine, 16 ans, cheveux aux épaules, blouson trop grand, un livre fermé à la main, debout ; face à elle, Lou qui arrive, sac de montagne, couverture de laine serrée contre le ventre ; derrière, la montagne et, tout en haut, la cascade figée.
- **Alt de référence** : « Sur le quai d’une petite gare au pied de la montagne, une adolescente debout sous l’horloge fait face à une femme qui arrive, sac au dos. »

## Images de notices

### `images/codex-tobie-ferrand.webp`

- **Notice** : Tobie Ferrand (personnage)
- **Sujet** : Un petit garçon maigre de sept ans, dans un lit de fer trop grand, serre un cheval de bois contre sa joue à la lueur d’une lampe à pétrole.
- **Prompt** : bible visuelle + Portrait intime à la lampe à pétrole dans une chambre blanchie à la chaux ; garçon de sept ans aux cheveux collés par la fièvre, lèvres un peu bleues, grands yeux sombres grands ouverts ; un cheval de bois usé contre la joue ; un volet plein percé d’une fente horizontale par où passe un trait de lumière froide sur le mur.
- **Alt de référence** : « Un petit garçon maigre de sept ans, dans un lit de fer trop grand, serre un cheval de bois contre sa joue à la lueur d’une lampe à pétrole. »

### `images/codex-helene-ferrand.webp`

- **Notice** : Hélène Ferrand (personnage)
- **Sujet** : Une jeune femme de trente-deux ans en robe grise de veilleuse, taches de rousseur, tient à deux mains une photographie dans une galerie où passe un trait de lumière.
- **Prompt** : bible visuelle + Portrait en buste dans une galerie de bois sombre ; femme de 32 ans, cheveux noirs en chignon défait, taches de rousseur, yeux gonflés de larmes et de fatigue, robe de laine grise et tablier ; elle tient à deux mains une petite photographie qu'on ne voit que de dos ; un trait de lumière horizontal, venu d'une fente de volet, lui barre le visage.
- **Alt de référence** : « Une jeune femme de trente-deux ans en robe grise de veilleuse, taches de rousseur, tient à deux mains une photographie dans une galerie où passe un trait de lumière. »

### `images/codex-orso-lebreuil.webp`

- **Notice** : Orso Lebreuil (personnage)
- **Sujet** : Un homme d’une cinquantaine d’années à moustache grise, manteau de drap et chapeau démodé, fume une pipe de terre au bord d’un sentier de montagne.
- **Prompt** : bible visuelle + Portrait en pied au bord d'un sentier en lacets, lumière d'altitude ; homme de 53 ans, moustache grise soignée, manteau de drap sombre trop chaud, chapeau d'un autre siècle, pipe de terre ; derrière lui, flou, un long trait de cascade blanche qui semble figé contre la falaise.
- **Alt de référence** : « Un homme d’une cinquantaine d’années à moustache grise, manteau de drap et chapeau démodé, fume une pipe de terre au bord d’un sentier de montagne. »

### `images/codex-capucine-rigal.webp`

- **Notice** : Capucine Rigal (personnage)
- **Sujet** : Une fillette de neuf ans en manteau rouge boutonné jusqu’au menton, assise sur sa valise, un livre illustré serré contre elle.
- **Prompt** : bible visuelle + Portrait d'une fillette de 9 ans assise sur une valise de carton au pied d'une borne de pierre, manteau rouge boutonné jusqu'au menton, regard frondeur, joues pâles ; elle serre contre elle un roman d'aventures à couverture illustrée d'un aéroplane (image floue, aucun texte lisible) ; derrière, les premiers prés en pente et une montagne immense.
- **Alt de référence** : « Une fillette de neuf ans en manteau rouge boutonné jusqu’au menton, assise sur sa valise, un livre illustré serré contre elle. »

### `images/codex-anselme-lestang.webp`

- **Notice** : Anselme Lestang (personnage)
- **Sujet** : Un homme de soixante ans aux cheveux blancs courts, en habit noir boutonné haut, écrit à la plume d’oie dans un grand registre sur un bureau d’acajou.
- **Prompt** : bible visuelle + Portrait à la lampe dans un bureau lambrissé ; homme de 60 ans, grand, cheveux blancs coupés court, habit noir boutonné jusqu'au menton, longues mains très propres tenant une plume d'oie au-dessus d'un registre ouvert (écriture illisible) ; un sablier d'encre, un encrier ; derrière lui un volet plein fermé, sa fente traçant un trait de lumière.
- **Alt de référence** : « Un homme de soixante ans aux cheveux blancs courts, en habit noir boutonné haut, écrit à la plume d’oie dans un grand registre sur un bureau d’acajou. »

### `images/codex-adrienne-coquard.webp`

- **Notice** : Adrienne Coquard (personnage)
- **Sujet** : Une femme de soixante ans au chignon gris serré, une loupe d’horloger vissée dans l’œil, examine une montre de laiton à son pupitre.
- **Prompt** : bible visuelle + Portrait serré à un pupitre de bois sous une fenêtre étroite ; femme de 62 ans, chignon gris tiré, loupe d'horloger dans l'orbite gauche, manchettes de lustrine noire, regard baissé vers ses mains qui tiennent une montre de laiton à deux cadrans ; derrière elle, un panier d'osier plein d'objets étiquetés.
- **Alt de référence** : « Une femme de soixante ans au chignon gris serré, une loupe d’horloger vissée dans l’œil, examine une montre de laiton à son pupitre. »

### `images/codex-la-pendule.webp`

- **Notice** : La Pendule (lieu)
- **Sujet** : Une longue cascade blanche tombe d’une falaise ; en bas l’eau bouillonne, en haut elle semble figée comme du verre.
- **Prompt** : bible visuelle + Vue verticale d'une haute cascade le long d'une falaise grise ; dans la vasque du bas, l'eau blanche et furieuse, écume et embruns ; plus haut, le flot s'étire et se lisse ; tout en haut, il paraît immobile, un ruban de verre posé contre la roche ; sentier en lacets et murets de pierres sèches au premier plan.
- **Alt de référence** : « Une longue cascade blanche tombe d’une falaise ; en bas l’eau bouillonne, en haut elle semble figée comme du verre. »

### `images/codex-pas-de-lecluse.webp`

- **Notice** : Le Pas de l'Écluse (lieu)
- **Sujet** : Un énorme mur de granit ferme une gorge étroite ; une seule porte le traverse, au pied de laquelle attend une file de voyageurs.
- **Prompt** : bible visuelle + Plan d'ensemble au fond d'une gorge étroite aux parois vertigineuses ; un mur de blocs de granit gros comme des armoires ferme la gorge d'une paroi à l'autre, percé d'une seule porte voûtée au linteau gravé (inscription suggérée, illisible) ; une file de voyageurs assis sur leurs bagages ; l'ombre portée d'une borne s'étire, lumière rasante et pressée.
- **Alt de référence** : « Un énorme mur de granit ferme une gorge étroite ; une seule porte le traverse, au pied de laquelle attend une file de voyageurs. »

### `images/codex-greffe-des-saisies.webp`

- **Notice** : Le Greffe des Saisies (lieu)
- **Sujet** : Une longue salle voûtée creusée dans la roche, aux étagères chargées d’objets anciens étiquetés, éclairée par une seule bougie.
- **Prompt** : bible visuelle + Intérieur d'une salle voûtée creusée dans le rocher, en perspective profonde, à la lueur d'une seule bougie ; étagères jusqu'au plafond chargées d'objets de toutes époques : rouet, lampes à huile, vélocipède à grande roue pendu à deux crochets, phonographe à pavillon, postes de radio ; au premier plan, un casier de petites fioles claires ; étiquettes suggérées, illisibles.
- **Alt de référence** : « Une longue salle voûtée creusée dans la roche, aux étagères chargées d’objets anciens étiquetés, éclairée par une seule bougie. »

### `images/codex-hospice-longue-veille.webp`

- **Notice** : L'Hospice de la Longue Veille (lieu)
- **Sujet** : Une forteresse grise aux galeries de bois accrochée à une falaise, avec un escalier taillé en zigzag et une seule fenêtre éclairée.
- **Prompt** : bible visuelle + Vue en contre-plongée depuis le pied de la falaise, crépuscule ; une forteresse de pierre grise sur trois étages de galeries de bois accrochées à la roche, volets pleins fermés ; un escalier taillé en zigzag monte vers la porte ; une seule fenêtre éclairée au troisième palier ; au-dessus, une brume grise, égale, lumineuse, ni jour ni nuit ; ciel partagé entre clair et sombre.
- **Alt de référence** : « Une forteresse grise aux galeries de bois accrochée à une falaise, avec un escalier taillé en zigzag et une seule fenêtre éclairée. »

### `images/codex-puits-des-vendanges.webp`

- **Notice** : Le Puits des vendanges (lieu)
- **Sujet** : Sous un auvent de bois noirci, un grand treuil à tambour de chêne surplombe un trou rond et noir dans la roche, éclairé par une lanterne.
- **Prompt** : bible visuelle + Nuit sur une terrasse de pierre au-dessus du vide ; sous un auvent de grosses poutres noircies, un treuil ancien : tambour de chêne cerclé de fer, roue dentée, manivelle double, frein à sabot ; deux câbles plongent dans un puits rond et noir d'où monte une vapeur tiède ; une lanterne posée au sol, une petite clochette de cuivre pendue à une poutre.
- **Alt de référence** : « Sous un auvent de bois noirci, un grand treuil à tambour de chêne surplombe un trou rond et noir dans la roche, éclairé par une lanterne. »

### `images/codex-les-terrasses.webp`

- **Notice** : Les Terrasses (lieu)
- **Sujet** : Des gradins de roche montent vers une brume grise lumineuse, sans ombre ni soleil, où l’on devine des silhouettes immobiles.
- **Prompt** : bible visuelle + Paysage de haute montagne : une suite de gradins de roche et un escalier taillé qui montent vers une lumière grise, égale, sans source ni ombres, comme une aube figée ; quelques bâtiments bas à peine devinés ; silhouettes humaines immobiles ; aucune indication de jour ou de nuit.
- **Alt de référence** : « Des gradins de roche montent vers une brume grise lumineuse, sans ombre ni soleil, où l’on devine des silhouettes immobiles. »

### `images/codex-double-montre.webp`

- **Notice** : La double montre (objet)
- **Sujet** : Une grosse montre de laiton à deux cadrans côte à côte, boîtier ouvert, posée sur un établi d’horloger près d’une loupe.
- **Prompt** : bible visuelle + Nature morte sur un établi d'horloger, lumière de verrière ; une grosse montre de gousset en laiton à deux cadrans côte à côte, un petit et un grand, aiguilles fines, sans chiffres lisibles ; le fond dévissé révèle un mouvement délicat et une cavité vide garnie de coton ; à côté, une loupe, des brucelles, une burette d'huile.
- **Alt de référence** : « Une grosse montre de laiton à deux cadrans côte à côte, boîtier ouvert, posée sur un établi d’horloger près d’une loupe. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/quatre-jours-par-heure.webp` | à produire |
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
| `images/codex-tobie-ferrand.webp` | à produire |
| `images/codex-helene-ferrand.webp` | à produire |
| `images/codex-orso-lebreuil.webp` | à produire |
| `images/codex-capucine-rigal.webp` | à produire |
| `images/codex-anselme-lestang.webp` | à produire |
| `images/codex-adrienne-coquard.webp` | à produire |
| `images/codex-la-pendule.webp` | à produire |
| `images/codex-pas-de-lecluse.webp` | à produire |
| `images/codex-greffe-des-saisies.webp` | à produire |
| `images/codex-hospice-longue-veille.webp` | à produire |
| `images/codex-puits-des-vendanges.webp` | à produire |
| `images/codex-les-terrasses.webp` | à produire |
| `images/codex-double-montre.webp` | à produire |

Total : 24 fichiers (1 couverture, 10 chapitres, 13 notices).
