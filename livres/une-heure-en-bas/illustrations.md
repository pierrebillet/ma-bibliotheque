# Illustrations de « Une heure en bas »

Manifeste pour l’agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d’images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/une-heure-en-bas/`) et dans `couvertures/`. C’est tout.

**Règles impératives** :

1. Tu travailles sur la branche `claude/nouvelle-fiction-libre-yizm6o` de ce dépôt (celle où se
   trouve ce fichier ; elle remplace ici la branche `atelier/roman-une-heure-en-bas` du
   gabarit, imposée par la session d’écriture). Tu pousses tes commits sur cette
   branche, jamais sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l’îlot JSON de
   `index.html`, ni le texte, ni aucun autre fichier — à une exception près :
   dans le `<head>` de `livres/une-heure-en-bas/index.html`, complète la meta
   `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Opus 5.5 (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Une heure en bas : chapitres 1 à 6 »),
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
- **Couverture : aucun texte autorisé**, sans exception — ni titre, sous-titre,
  nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre est ajouté
  par-dessus en HTML dans la bibliothèque.
- Images intérieures : aucun texte lisible incrusté (titres, lettrages). Les
  inscriptions gravées, plaques, cadrans et pages d’écriture qui apparaissent dans
  certaines scènes restent **illisibles** (traits, encoches, points).
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/une-heure-en-bas
  ```

## Bible visuelle commune

**Technique et rendu.** Lavis d’encre et gouache sur papier chaud, à la manière des carnets de voyage illustrés du XIXᵉ siècle : un dessin à la plume fin et sûr, des aplats transparents, des blancs de papier réservés pour la lumière. Pas de rendu photographique, pas de 3D, pas d’effet numérique brillant. Grain de papier visible.

**Palette.** Blancs laiteux et gris perle (le Voile, la bruine), pierre blonde et ocre pâle (Demeure), bleu d’ardoise et gris de plomb (la Pente, la nuit, les uniformes), vert-de-gris des cuivres mouillés, et une seule couleur chaude qui compte : l’ambre du Fanal et des lampes. Noirs d’encre profonds pour l’Ombilic.

**Lumière.** Presque toujours diffuse, laiteuse, sans soleil visible à Demeure (le ciel y est un plafond de lait qui s’éclaire et s’éteint). Sur la Pente, lumière froide de montagne. Les lampes font des halos chauds et petits. Jamais de coucher de soleil spectaculaire.

**Le monde en une phrase.** Une cuvette de calcaire de six lieues où le temps ralentit à mesure qu’on descend : en haut, Surplomb, ville d’hiver à becs de gaz ; en bas, sous une brume laiteuse permanente, Demeure, ville tiède et pluvieuse à arcades, figuiers et toits-jardins ; entre les deux, des paliers, un funiculaire en sections, et une très vieille rampe à lacets presque plats.

**Époque et objets.** Équivalent d’une fin de XIXᵉ siècle inventée : becs de gaz, télégraphe, funiculaire de chêne ferré, montres de gousset, redingotes, capotes de laine, parapluies, robes à tournure (la mode change vite au fond). Pas d’automobile, pas d’électricité domestique (quelques lampes à arc seulement au bord), pas d’avion.

**Interdits.** Aucun texte lisible incrusté (ni titre, ni lettrage, ni pseudo-texte) — à l’exception éventuelle d’une inscription gravée illisible sur la roche quand une entrée le demande. Aucun logo, signature, filigrane. Pas de sang (le mal de cote ne saigne pas). Pas de visages en gros plan larmoyants ; les émotions passent par les postures, les mains, les distances.

**Personnages récurrents (à garder identiques d’une image à l’autre).**
- **Jonas Mérel**, 41 ans, grand, sec, épaules un peu voûtées par le sac ; cheveux bruns courts, grisonnants aux tempes ; barbe de deux jours ; capote de courrier bleu d’ardoise à boutons de laiton, sacoche de cuir en bandoulière, grosse montre d’acier à deux cadrans au bout d’une chaîne ; une cicatrice blanche en travers de la base du pouce gauche.
- **Colombe Mérel**, 6 ans, menue, très pâle, grands yeux sombres, cheveux bruns courts coupés au bol ; chemise de nuit blanche sous un gilet de laine grise trop grand ; souvent en chaussettes ; petites taches violettes sur les avant-bras.
- **Adeline Mérel (Madame Line)**, 35 ans, mince, cheveux châtains relevés en chignon lâche, tablier gris sur robe de laine brune, châle de laine écrue ; mains longues ; une vieille clé de fer au bout d’un cordon, souvent dans la main.
- **Hortense Vaudrey**, 59 ans, très grande et maigre, cheveux gris tirés en arrière, long manteau noir à col droit, insigne de laiton de la Compagnie ; se tient droite.
- **Anatole Pagès**, 29 ans, dégingandé, lunettes rondes épaisses, manchettes tachées d’encre, chronographe et carnet toujours à la main.
- **Ursule Crozes**, 63 ans, petite et nerveuse, visage tanné très ridé, cheveux blancs coupés court, mains d’homme, vieille capote de courrière rapiécée à l’ancienne coupe.
- **Le docteur Salvat**, la cinquantaine, lunettes remontées sur le front, blouse blanche boutonnée de travers.
- **La Doyenne**, 76 ans, robe noire de juge, droite dans un fauteuil haut.

**Cadrage.** Format horizontal 16:9 pour les chapitres et les notices ; composition claire, un sujet principal, profondeur par plans successifs (la Pente s’y prête). La couverture est verticale.

**Ne jamais divulguer par l’image** : chaque image se voit à l’ouverture de son
chapitre ou de sa notice ; ne montre rien de plus que ce que décrit son entrée
(pas de visage pour la lingère du chapitre 2, pas d’allure lisible pour les
Marcheurs du chapitre 6).

## Couverture

- **Fichier** : `couvertures/une-heure-en-bas.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : Jonas au bord du Val, de dos, la double montre ouverte ; tout au fond, le Voile et le point ambré du Fanal.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Composition verticale 2:3. Tiers inférieur : au premier plan, sur le rebord enneigé de la Margelle, un homme grand et sec vu de dos (capote de courrier bleu d’ardoise à boutons de laiton, sacoche de cuir en bandoulière), tête légèrement baissée ; dans sa main gauche ouverte, une grosse montre de gousset d’acier à deux cadrans superposés, sa chaîne pendante (aucun chiffre lisible). Centre et bas de l’image : l’immense cuvette du Val qui plonge en entonnoir, versants de calcaire bleu d’ardoise, une ligne de funiculaire à peine visible et, sur le versant gauche, le fil pâle d’un chemin en lacets presque plats. Tout au fond, petit, un disque de brume laiteuse et lumineuse, et en son centre un minuscule point ambré, la seule couleur chaude de l’image. Tiers supérieur : ciel d’hiver nocturne, gris de plomb qui s’éclaircit vers la vallée, quelques flocons ; espace calme laissé libre pour le titre. Lumière froide de montagne, halo laiteux montant du fond. Mélancolie, vertige, attente. Aucun texte, aucun logo, aucune signature, aucun filigrane, aucun pseudo-texte.
- **Alt de référence** (déjà dans l’îlot, ne pas le modifier) : « Au bord d’un précipice enneigé, de nuit, un homme en capote bleue vu de dos tient ouverte dans sa paume une montre à deux cadrans ; très loin en bas, au fond d’une immense vallée en entonnoir, un disque de brume laiteuse où brille un minuscule point ambré. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Six ans depuis onze ans
- **Sujet** : Dans une longue salle d’hôpital aux fenêtres cintrées emplies de brume blanche, un homme en capote bleue accroupi au chevet d’une petite fille pâle qui lui arrache un cheveu au-dessus de l’oreille.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Intérieur de la salle des Attendants, à la Maison d’Attente de Demeure, sous la lumière laiteuse du Voile à son blanc le plus fort, entrée par trois fenêtres cintrées. Plan moyen : Jonas (41 ans, capote de courrier bleu d’ardoise, sacoche en bandoulière) accroupi de trois quarts dos au bord d’un lit de fer, la tête penchée ; Colombe (6 ans, très pâle, cheveux au bol, chemise de nuit blanche et gilet gris trop grand), assise dans le lit, deux doigts dans les cheveux de son père au-dessus de l’oreille, très concentrée ; sur la couverture, une boîte à pastilles de fer-blanc ouverte et une toupie de fer-blanc. Derrière eux, les rangées de lits à rideaux de toile écrue ; tout au fond, la porte de la lingerie entrebâillée d’un doigt, fente sombre et verticale, sans personne visible. Calme, tendresse retenue.
- **Alt de référence** : « Dans une longue salle d’hôpital aux fenêtres cintrées emplies de brume blanche, un homme en capote bleue accroupi au chevet d’une petite fille pâle qui lui arrache un cheveu au-dessus de l’oreille ; au fond de la salle, une porte entrebâillée d’un doigt. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — La porte de la lingerie
- **Sujet** : Depuis une lingerie sombre aux étagères de draps pliés, par une porte entrebâillée, on aperçoit dans la salle claire un homme de dos assis au bord d’un lit d’enfant.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Contre-champ du chapitre 1, depuis l’intérieur de la lingerie : pièce étroite et blanche, étagères de draps pliés jusqu’au plafond, deux fers sur un réchaud, un tabouret sous une lucarne. Premier plan, un peu flou : la main longue d’une femme posée sur le chant de la porte entrebâillée, une manche de laine brune, un châle écru. Par la fente, lointaine et nette : la salle des Attendants baignée de lait, un homme en capote bleue assis de dos au bord d’un lit, une petite fille assise en face de lui. On ne voit pas le visage de la femme. Silence, secret, attente.
- **Alt de référence** : « Depuis une lingerie sombre aux étagères de draps pliés, par une porte entrebâillée, on aperçoit dans la salle claire un homme de dos assis au bord d’un lit d’enfant ; au premier plan, une main de femme posée sur le chant de la porte. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — On cesse de les porter
- **Sujet** : Dans un bureau austère éclairé au gaz, une très grande femme maigre en manteau noir se tient droite près d’une fenêtre enneigée.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Surplomb, bureau de la directrice de la Compagnie des Paliers, fin d’après-midi d’hiver : lumière jaune du gaz et bleu de la neige par la fenêtre. Hortense Vaudrey (59 ans, très grande et maigre, cheveux gris tirés en arrière, long manteau noir à col droit, insigne de laiton) debout, droite, près de la fenêtre. Au mur face à la fenêtre, le Barème : une grande plaque de laiton gravée de colonnes (chiffres illisibles), usée d’une rainure en son milieu. Premier plan, de trois quarts dos, Jonas en capote bleue, la main posée à plat sur la poche intérieure de sa veste. Pièce nue et trop chauffée : table de bois blanc, deux chaises, encrier et plume, un poêle qui ronfle, une pendule au-dessus de la porte. Tension feutrée.
- **Alt de référence** : « Dans un bureau austère éclairé au gaz, une très grande femme maigre en manteau noir se tient droite près d’une fenêtre enneigée ; au mur, une plaque de laiton gravée de colonnes ; face à elle, un homme en capote bleue, la main posée sur sa veste. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Ce que dit la Doyenne
- **Sujet** : Dans une rue pavée en pente couverte d’une eau lisse, sous la bruine, une femme en tablier avance à plat ventre avec une petite fille cramponnée à son dos.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, quartier des Berges, la rue des Lavoirs qui descend vers le noir de l’Ombilic ; bruine tiède, lumière grise et laiteuse, quelques lanternes. Une nappe d’eau lisse et vitreuse couvre les pavés. Premier plan : Adeline (35 ans, chignon défait, tablier gris sur robe brune trempée) à plat ventre dans l’eau, en appui sur les coudes ; une petite fille d’environ quatre ans (brune, en robe de lavandière d’enfant — ce n’est pas Colombe) cramponnée à son dos, les bras autour de son cou. Au bout de la rue, sur le quai, la silhouette d’un allumeur de réverbères arrêté en plein pas, un pied levé, sa longue perche à la main, d’une immobilité inquiétante. En haut, des gens penchés à l’angle de la rue. Aucun sang.
- **Alt de référence** : « Dans une rue pavée en pente couverte d’une eau lisse, sous la bruine, une femme en tablier avance à plat ventre avec une petite fille cramponnée à son dos ; plus bas, sur un quai, un allumeur de réverbères immobile, un pied levé, sa perche à la main. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — Qui descend remonte
- **Sujet** : La nuit, au bord d’un cimetière enneigé perché sur une falaise, trois silhouettes encordées — une petite femme aux cheveux blancs, un grand homme en capote, un jeune homme à lunettes rondes — s’engagent sur un sentier qui plonge vers une vallée dont le fond luit comme un disque de lait..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Surplomb, nuit d’avril, le vieux cimetière au bord de la Margelle : croix et murets sous des plaques de neige, becs de gaz lointains de la ville en haut de l’image. Trois silhouettes de dos, encordées : Ursule Crozes devant (petite, sèche, cheveux blancs courts, vieille capote rapiécée), une lanterne sourde à la main ; Jonas au milieu (grand, capote bleue, rouleau de corde de chanvre à l’épaule) ; Anatole Pagès derrière (29 ans, dégingandé, lunettes rondes, étui de cuir en bandoulière). Devant eux, un sentier de chèvres qui plonge dans le vide ; très loin en bas, au fond de la cuvette noire, un disque laiteux et pâle. Froid, clandestin, vertige.
- **Alt de référence** : « La nuit, au bord d’un cimetière enneigé perché sur une falaise, trois silhouettes encordées — une petite femme aux cheveux blancs, un grand homme en capote, un jeune homme à lunettes rondes — s’engagent sur un sentier qui plonge vers une vallée dont le fond luit comme un disque de lait. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Les Marcheurs
- **Sujet** : Depuis une terrasse de pierre blonde où des enfants en chemise de nuit ont le menton sur le parapet, on voit en contrebas, au bord d’un gouffre noir bordé de lampes posées au sol, des silhouettes pâles en manteaux de peaux, chargées de ballots, sortir de l’obscurité..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure en plein jour sous le Voile laiteux : la terrasse de la Maison d’Attente, un toit-jardin cerné d’un parapet de pierre blonde, figuiers en caisse. Premier plan, de dos : des enfants en chemises de nuit, le menton sur le parapet ; Colombe (6 ans, gilet gris trop grand) debout sur un tabouret, l’œil à une longue-vue de laiton sur trépied, les mains d’Adeline autour de sa taille ; à côté, le docteur Salvat (la cinquantaine, lunettes remontées sur le front, blouse blanche boutonnée de travers). En contrebas, au-delà des toits-jardins, le bord de l’Ombilic, un creux d’un noir d’encre, bordé d’un cordon de lampes de fête posées à plat ; de ce noir émergent, lointaines, éclairées d’en bas d’une lumière jaune, des silhouettes en manteaux de peaux chargées de ballots. On ne distingue pas leur allure : mystère, stupeur.
- **Alt de référence** : « Depuis une terrasse de pierre blonde où des enfants en chemise de nuit ont le menton sur le parapet, on voit en contrebas, au bord d’un gouffre noir bordé de lampes posées au sol, des silhouettes pâles en manteaux de peaux, chargées de ballots, sortir de l’obscurité. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Le Raide
- **Sujet** : Sous la pluie, au pied d’un haut mur de moellons gris envahi de ronces, une petite femme aux cheveux blancs se glisse à plat ventre par un trou à ras de terre, pendant qu’un grand homme en capote bleue tient une dalle pivotée et qu’un jeune homme à lunettes attend, couché, un étui contre lui..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Sur le versant sous l’Octroi, pluie froide, lumière de montagne grise. Un mur de la Compagnie en moellons gris jointoyés, haut de deux hommes, barre un chemin en lacet accroché à la paroi ; les ronces l’ont pris jusqu’aux épaules ; une plaque de fonte scellée (inscription illisible). Au pied du mur, côté roche, une dalle a pivoté sur une broche de fer et découvre un trou à ras de terre : Ursule Crozes (63 ans, petite, cheveux blancs courts, capote rapiécée) s’y glisse sur le ventre. Jonas (grand, capote bleue trempée) agenouillé tient la dalle ; Anatole Pagès (lunettes rondes embuées) allongé dans la boue, un étui de cuir serré contre lui. Au-delà du mur, le ciel gris semble clignoter. Clandestinité, effort, humidité.
- **Alt de référence** : « Sous la pluie, au pied d’un haut mur de moellons gris envahi de ronces, une petite femme aux cheveux blancs se glisse à plat ventre par un trou à ras de terre, pendant qu’un grand homme en capote bleue tient une dalle pivotée et qu’un jeune homme à lunettes attend, couché, un étui contre lui. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Le trentième jour
- **Sujet** : Dans deux banquettes de pierre creusées côte à côte dans le roc, un homme couché tient une petite fille au creux de son bras, et une femme est allongée dans la banquette voisine.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Le Raide, sur la vieille Rampe des Premiers : un tournant de lacet taillé dans le roc, pénombre, lueur chaude de deux lampes posées sur une arête de pierre basse. Vue plongeante et rapprochée : deux banquettes creusées côte à côte, de la longueur d’un corps, polies par les siècles. Dans celle de droite, Jonas couché sur le dos, barbe grise, terre dans la barbe, Colombe (gilet gris, chaussettes) blottie au creux de son bras, une boîte à pastilles serrée dans le poing ; dans celle de gauche, Adeline (35 ans, châle écru, manches usées) allongée, la joue tournée vers la paroi. Au-dessus d’eux, dans la roche, une inscription gravée (illisible). Aucun des trois ne se touche. Recueillement, gravité, même heure.
- **Alt de référence** : « Dans deux banquettes de pierre creusées côte à côte dans le roc, un homme couché tient une petite fille au creux de son bras, et une femme est allongée dans la banquette voisine ; deux lampes brûlent sur l’arête qui les sépare, sous des lettres gravées dans la paroi. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Douze heures
- **Sujet** : Dans une grande salle de pierre blonde aux bancs de chêne noir, un homme en capote bleue se tient à la barre face à une longue table de juges en robes noires, au centre de laquelle siège une vieille femme très droite.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, grande salle de la Haute Chambre, lampes de cuivre, lumière laiteuse par de hautes fenêtres. Au fond, sur une estrade, la longue table des juges en robes noires à rabats d’une coupe ancienne ; au centre, la Doyenne (76 ans, petite, très droite, les mains à plat sur la table). Au premier plan, de dos, Jonas à la barre des témoins, en capote bleue, la main à plat sur la barre ; un pas derrière lui, Pagès (lunettes rondes). Aux premiers rangs, des rentiers élégants, dont un homme en fauteuil à roues aux jambes emmaillotées et une dame coiffée d’un petit chapeau de paille noire relevé d’un côté, à nœud de velours cerise. Au fond, contre les piliers, des engagées en tablier et des tanneurs se lèvent un à un, dont une femme qui tient encore son torchon. Solennité, basculement silencieux.
- **Alt de référence** : « Dans une grande salle de pierre blonde aux bancs de chêne noir, un homme en capote bleue se tient à la barre face à une longue table de juges en robes noires, au centre de laquelle siège une vieille femme très droite ; au fond de la salle, des domestiques se lèvent un à un. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — À tout à l’heure
- **Sujet** : La nuit, dans une cour de tannerie sous la bruine, une femme assise sur un banc tient une enfant couchée en travers de ses genoux.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, la dernière cour des tanneries, le soir, bruine et lumière de lampes. Sous des arcades, sur un banc de tanneur poli, Adeline (35 ans, blouse de médecin boutonnée par-dessus sa robe, châle) tient Colombe couchée à plat en travers de ses genoux, la tête au creux de son bras. Autour, des gens assis par paquets sur des planches qui couvrent les fosses, des enfants endormis. Au-delà d’une arche creusée dans le roc, la falaise, et sur elle un chemin en lacets presque plats où monte une longue file de lampes : les plus basses brûlent calmes et jaunes, les plus hautes, prises dans la brume laiteuse, brillent de plus en plus vives et tremblées, comme accélérées. Sur la première, en tête, une silhouette d’homme qui ne se retourne pas. Séparation, beauté, vertige du temps.
- **Alt de référence** : « La nuit, dans une cour de tannerie sous la bruine, une femme assise sur un banc tient une enfant couchée en travers de ses genoux ; au-dessus, sur la falaise, une file de lampes monte un chemin en lacets, les plus hautes vives et tremblantes. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — À plat ventre
- **Sujet** : Sur une falaise noyée de brume laiteuse, des lacets de pierre presque plats où rampe à plat ventre une longue file de gens portant des enfants noués sur le dos, chacun poussant une lampe devant soi le long d’une corde tendue d’anneau en anneau..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. La vieille Rampe dans le Raide, la nuit : vue plongeante depuis un tournant sur plusieurs lacets superposés accrochés à la falaise de calcaire, qui s’enfoncent plus bas dans la brume laiteuse du Voile. Sur chaque lacet, une file de gens couchés à plat ventre, en appui sur les coudes : laveuses aux bras rouges, tanneurs, engagées, chacun avec un enfant noué sur le dos par une bande de drap croisée ; le long de chaque lacet, une corde faite de cordes à linge et de cordes à peaux nouées bout à bout, tendue d’anneau de fer en anneau. Une lampe par corps, poussée devant soi : sur les lacets du haut, les flammes sont vives et tremblées ; sur ceux du bas, elles s’allongent, grasses et immobiles. Premier plan : une couchette taillée dans le roc ; Jonas (capote bleue couverte de terre) couché le long du rebord, un cahier d’écolier bleu ouvert sous la main, un crayon ; à côté, Pagès allongé, un chronomètre posé à sa tête, un autre à ses pieds. Effort collectif, silence, vertige.
- **Alt de référence** : « Sur une falaise noyée de brume laiteuse, des lacets de pierre presque plats où rampe à plat ventre une longue file de gens portant des enfants noués sur le dos, chacun poussant une lampe devant soi le long d’une corde tendue d’anneau en anneau. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — Une heure en bas
- **Sujet** : Dans une grande salle de pierre aux bancs repoussés contre les murs, des gens sont couchés en rangées sur les dalles mouillées.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, grande salle de la Haute Chambre, la nuit de la fermeture. Les bancs de chêne noir poussés contre les murs ; sur les dalles, entre les piliers, des dizaines de gens couchés par rangées sur des matelas, des manteaux, des tapis roulés : rentiers et domestiques côte à côte, une dame sur une pelisse avec un petit garçon et, posé droit à côté d’elle, un chapeau noir à nœud cerise. Au premier plan, Colombe (6 ans, gilet gris) couchée sur le dos sans oreiller, une boîte à pastilles dans le poing, les yeux grands ouverts vers les fenêtres ; à côté d’elle un garçon de neuf ans, la main sur un carton à chapeau ; entre eux, une petite lampe à mèche basse fait un rond jaune ; Adeline allongée près d’eux, la joue sur la dalle. Une lame d’eau mince entre sous la porte. Sur l’estrade, derrière la longue table, les juges couchés en robes, et la Doyenne seule assise, très droite. Aux hautes fenêtres, une lumière grise, épaisse et tremblée, comme de la corne. Attente, veille, gravité.
- **Alt de référence** : « Dans une grande salle de pierre aux bancs repoussés contre les murs, des gens sont couchés en rangées sur les dalles mouillées ; une petite lampe jaune brûle entre deux enfants allongés, et sur l’estrade une vieille juge est restée assise, très droite, sous de hautes fenêtres d’un gris trouble. »

## Images de notices

### `images/codex-jonas-merel.webp`

- **Notice** : Jonas Mérel (personne)
- **Sujet** : Portrait d’un homme d’une quarantaine d’années, grand et sec, en capote bleue à boutons de laiton, qui regarde une grosse montre d’acier à deux cadrans ouverte dans sa paume.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Portrait en buste, trois quarts, sur fond de quai de gare noyé de brume. Jonas Mérel (41 ans, grand, sec, épaules un peu voûtées, cheveux bruns courts grisonnants aux tempes, barbe de deux jours), capote de courrier bleu d’ardoise, sacoche de cuir en bandoulière. Il baisse les yeux sur la double montre ouverte dans sa main gauche (deux cadrans superposés, aucun chiffre lisible) ; cicatrice blanche en travers de la base du pouce gauche. Expression fermée, exacte, lasse.
- **Alt de référence** : « Portrait d’un homme d’une quarantaine d’années, grand et sec, en capote bleue à boutons de laiton, qui regarde une grosse montre d’acier à deux cadrans ouverte dans sa paume ; une cicatrice blanche barre la base de son pouce. »

### `images/codex-colombe-merel.webp`

- **Notice** : Colombe Mérel (personne)
- **Sujet** : Une petite fille très pâle aux cheveux bruns coupés au bol, en chemise de nuit et gilet gris trop grand, debout sur son lit, qui range un jouet au bout d’une rangée de jouets alignés sur une étagère..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Au-dessus d’un lit de fer de la salle des Attendants, une étagère de bois où sont alignés, dans l’ordre, des jouets d’époques successives : une toupie de bois, un pantin, une poupée de chiffon, un cheval à roulettes, un petit train de fer peint, une toupie de fer-blanc. Colombe (6 ans, très pâle, grands yeux sombres, cheveux au bol, chemise de nuit blanche, gilet de laine grise trop grand, en chaussettes) debout sur le matelas, pose un jouet au bout de la rangée avec une application sérieuse. Lumière laiteuse d’une fenêtre cintrée.
- **Alt de référence** : « Une petite fille très pâle aux cheveux bruns coupés au bol, en chemise de nuit et gilet gris trop grand, debout sur son lit, qui range un jouet au bout d’une rangée de jouets alignés sur une étagère. »

### `images/codex-madame-line.webp`

- **Notice** : Madame Line (personne)
- **Sujet** : Une lingère en tablier gris et châle écru, vue de dos, plie un drap devant des étagères de linge blanc.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Intérieur de la lingerie de la Maison d’Attente : étagères de draps pliés jusqu’au plafond, lucarne, réchaud et fers. Une femme mince (35 ans, cheveux châtains relevés en chignon lâche, tablier gris sur robe de laine brune, châle écru) vue de dos ou de profil perdu, plie un grand drap blanc les bras écartés ; une longue clé de fer noir pend à un cordon. Son visage n’est pas visible. Douceur, effacement.
- **Alt de référence** : « Une lingère en tablier gris et châle écru, vue de dos, plie un drap devant des étagères de linge blanc ; une vieille clé de fer pend à un cordon à sa taille. »

### `images/codex-maison-d-attente.webp`

- **Notice** : La Maison d’Attente (lieu)
- **Sujet** : Une grande maison de pierre blonde à arcades, percée au deuxième étage de trois hautes fenêtres cintrées, sous un ciel de brume laiteuse, à côté d’une tour blanche élancée..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, ville haute : façade d’une grande maison de pierre blonde, arcades au rez-de-chaussée, gouttières de cuivre vert-de-gris, toit-jardin avec un figuier ; au deuxième étage, trois grandes fenêtres cintrées. À côté, la Tour du Fanal, blanche et élancée, qui se perd dans le Voile. Bruine fine, passants sous des parapluies, lumière laiteuse sans soleil. Calme, lenteur.
- **Alt de référence** : « Une grande maison de pierre blonde à arcades, percée au deuxième étage de trois hautes fenêtres cintrées, sous un ciel de brume laiteuse, à côté d’une tour blanche élancée. »

### `images/codex-double-montre.webp`

- **Notice** : La double montre (objet)
- **Sujet** : Une grosse montre de gousset d’acier à deux cadrans superposés, ouverte dans une paume calleuse, sa chaîne pendante.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Gros plan : une paume d’homme calleuse, cicatrice blanche à la base du pouce, tient ouverte une montre de gousset d’acier à deux cadrans superposés, l’un au-dessus de l’autre, marqués de points et non de chiffres ; l’aiguille du cadran du haut est nette, celle du cadran du bas est un flou circulaire. Chaîne d’acier qui pend. Fond de capote bleue. Reflet laiteux sur le verre.
- **Alt de référence** : « Une grosse montre de gousset d’acier à deux cadrans superposés, ouverte dans une paume calleuse, sa chaîne pendante ; l’aiguille du cadran du bas est floue de vitesse. »

### `images/codex-les-bennes.webp`

- **Notice** : Les Bennes (institution)
- **Sujet** : Une caisse de funiculaire en chêne ferré, à banquettes en gradins, descend sur un câble le long d’un versant rocheux vers une mer de brume.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Le versant nord du Val, calcaire bleu d’ardoise, lumière froide de montagne. Une benne de chêne ferré à fenêtres, en gradins comme un escalier, descend sur un câble tendu, droit comme une règle ; quelques voyageurs assis en redingote et capote. Plus bas, une gare de transbordement de pierre accrochée au versant, et encore plus bas, le fond du Val noyé d’une brume laiteuse. Sensation de profondeur et de plans successifs.
- **Alt de référence** : « Une caisse de funiculaire en chêne ferré, à banquettes en gradins, descend sur un câble le long d’un versant rocheux vers une mer de brume ; en contrebas, une petite gare de transbordement. »

### `images/codex-demeure.webp`

- **Notice** : Demeure (lieu)
- **Sujet** : Une rue à arcades de pierre blonde sous une bruine tiède, avec des gouttières de cuivre, des figuiers sur des toits-jardins et des passants sous des parapluies, sous un plafond de brume laiteuse..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Demeure, rue de la ville haute : arcades de pierre blonde de part et d’autre, gouttières de cuivre vert-de-gris, treilles et figuiers qui débordent des toits plats, bruine fine et tiède, pavés luisants. Passants en redingotes et robes à tournure de modes légèrement dépareillées, sous des parapluies. Pas de soleil : un plafond de lait lumineux. Douceur, climat de serre, lenteur.
- **Alt de référence** : « Une rue à arcades de pierre blonde sous une bruine tiède, avec des gouttières de cuivre, des figuiers sur des toits-jardins et des passants sous des parapluies, sous un plafond de brume laiteuse. »

### `images/codex-le-fanal.webp`

- **Notice** : Le Fanal (objet)
- **Sujet** : La nuit, vu par une fenêtre de cuisine aux vitres givrées, au fond d’une immense vallée noire, un disque de brume pâle où luit un minuscule point ambré..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Surplomb, intérieur d’une cuisine modeste la nuit : rebord de fenêtre avec un pot, vitres à petits carreaux givrées sur les bords. Par la fenêtre, l’immense cuvette du Val, noire, et tout au fond un disque de brume pâle, laiteuse, où luit un minuscule point ambré, pâle comme une braise sous la cendre. Seule couleur chaude de l’image : ce point. Attente, veille.
- **Alt de référence** : « La nuit, vu par une fenêtre de cuisine aux vitres givrées, au fond d’une immense vallée noire, un disque de brume pâle où luit un minuscule point ambré. »

### `images/codex-les-marcheurs.webp`

- **Notice** : Les Marcheurs (personne)
- **Sujet** : Sept silhouettes en manteaux de peaux, chargées de ballots, un pied levé, se devinent au bord d’un creux d’un noir d’encre, éclairées d’en bas par une lueur jaune..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Le bord de l’Ombilic, un creux d’un noir d’encre profond. Sept silhouettes humaines en manteaux de peaux, ballots sur le dos, un pied levé, à peine sorties de l’obscurité, éclairées d’en bas par une lumière jaune et franche de lampes posées au sol hors champ. Figures archaïques, sans visage distinct, figées. Mystère, ancienneté.
- **Alt de référence** : « Sept silhouettes en manteaux de peaux, chargées de ballots, un pied levé, se devinent au bord d’un creux d’un noir d’encre, éclairées d’en bas par une lueur jaune. »

### `images/codex-hortense-vaudrey.webp`

- **Notice** : Hortense Vaudrey (personne)
- **Sujet** : Une très grande femme maigre aux cheveux gris tirés, en long manteau noir à col droit orné d’un insigne de laiton, se tient droite, les mains derrière le dos, sur un quai de gare enneigé..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Portrait en pied, légèrement en contre-plongée : Hortense Vaudrey (59 ans, très grande et maigre, cheveux gris tirés en arrière, long manteau noir à col droit, insigne de laiton de la Compagnie), droite, les mains derrière le dos, sur le quai de la gare des Bennes de Surplomb, neige tassée, becs de gaz, une benne à quai derrière elle. Regard qui porte loin. Intégrité, dureté, solitude.
- **Alt de référence** : « Une très grande femme maigre aux cheveux gris tirés, en long manteau noir à col droit orné d’un insigne de laiton, se tient droite, les mains derrière le dos, sur un quai de gare enneigé. »

### `images/codex-ursule-crozes.webp`

- **Notice** : Ursule Crozes, dite la Centenaire (personne)
- **Sujet** : Une petite vieille femme sèche aux cheveux blancs coupés court, au visage tanné, dans une capote de courrière rapiécée, assise sur un banc, ses mains d’homme posées sur les genoux..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. L’Asile des courriers, longue maison basse au bout de la Margelle, tournée vers le Val : une salle commune pauvre et propre, poêle, banc de bois sous une fenêtre. Ursule Crozes (63 ans, petite et nerveuse, visage tanné très ridé, cheveux blancs coupés court, mains larges d’homme, vieille capote de courrière rapiécée à l’ancienne coupe) assise, droite, les mains sur les genoux, regard vif et ironique. Lumière d’hiver par une fenêtre.
- **Alt de référence** : « Une petite vieille femme sèche aux cheveux blancs coupés court, au visage tanné, dans une capote de courrière rapiécée, assise sur un banc, ses mains d’homme posées sur les genoux. »

### `images/codex-carnet-des-battements.webp`

- **Notice** : Le carnet des battements (objet)
- **Sujet** : Un cahier d’écolier à couverture de carton bleu, ouvert sur une table de cuisine, chaque page partagée par un trait vertical, à côté d’une pile d’enveloppes cachetées et d’une boîte à souliers.
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Nature morte, lumière d’une lampe à pétrole : sur une table de cuisine en bois, un cahier d’écolier à couverture de carton bleu, cousu, aux coins mangés, ouvert ; chaque page est partagée par un trait vertical tiré à la règle, lignes d’écriture d’enfant illisibles. À côté, une pile d’enveloppes cachetées qui tient debout toute seule, une vieille boîte à souliers de carton gris, un crayon. Derrière, une fenêtre sur la nuit du Val. Intimité, mémoire.
- **Alt de référence** : « Un cahier d’écolier à couverture de carton bleu, ouvert sur une table de cuisine, chaque page partagée par un trait vertical, à côté d’une pile d’enveloppes cachetées et d’une boîte à souliers ; la fenêtre donne sur une vallée de nuit. »

### `images/codex-la-rampe.webp`

- **Notice** : La Rampe des Premiers (lieu)
- **Sujet** : Un chemin de pierre en lacets presque plats accroché à une falaise, avec, à un tournant, deux banquettes creusées côte à côte dans le roc et des anneaux de fer rouillés scellés dans la paroi..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. Le versant ouest du Val, falaise de calcaire, ronces. Un chemin de pierre étroit, large comme un lit, en lacets presque horizontaux qui vont et viennent sur la paroi. Au premier plan, un tournant : deux banquettes de la longueur d’un corps creusées côte à côte dans le roc, séparées par une arête basse, avec un bourrelet poli pour la nuque ; anneaux de fer rouillés scellés dans la paroi à hauteur d’homme couché ; au-dessus, une inscription gravée illisible. En contrebas, la brume laiteuse du fond. Ancienneté, patience.
- **Alt de référence** : « Un chemin de pierre en lacets presque plats accroché à une falaise, avec, à un tournant, deux banquettes creusées côte à côte dans le roc et des anneaux de fer rouillés scellés dans la paroi. »

### `images/codex-la-vanne.webp`

- **Notice** : La Vanne des Premiers (objet)
- **Sujet** : Dans une cour de pierre au bord d’un ravin, au-dessus d’un canal où coule une eau épaisse et vitreuse, une immense roue de fer rouillée, haute comme deux hommes, sur laquelle sèche une capote bleue..
- **Prompt** : Bible visuelle commune (lavis d’encre et gouache, carnet de voyage XIXᵉ, palette laiteuse, ardoise et ambre, aucun texte lisible). Format horizontal 16:9. L’Octroi, cour de la douane en terrasse au-dessus d’un ravin, pluie. Au premier plan, la grande roue de fer rouillée de la Vanne des Premiers, haute comme deux hommes, à rayons et crémaillère, dressée au-dessus d’un canal de pierre où coule une eau épaisse, lente et vitreuse, bombée comme du verre gris. Une capote bleue de préposé pend à un rayon. Derrière, le porche de la douane (devise gravée illisible). Poids, attente, geste à venir.
- **Alt de référence** : « Dans une cour de pierre au bord d’un ravin, au-dessus d’un canal où coule une eau épaisse et vitreuse, une immense roue de fer rouillée, haute comme deux hommes, sur laquelle sèche une capote bleue. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/une-heure-en-bas.webp` | à produire |
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
| `images/codex-jonas-merel.webp` | à produire |
| `images/codex-colombe-merel.webp` | à produire |
| `images/codex-madame-line.webp` | à produire |
| `images/codex-maison-d-attente.webp` | à produire |
| `images/codex-double-montre.webp` | à produire |
| `images/codex-les-bennes.webp` | à produire |
| `images/codex-demeure.webp` | à produire |
| `images/codex-le-fanal.webp` | à produire |
| `images/codex-les-marcheurs.webp` | à produire |
| `images/codex-hortense-vaudrey.webp` | à produire |
| `images/codex-ursule-crozes.webp` | à produire |
| `images/codex-carnet-des-battements.webp` | à produire |
| `images/codex-la-rampe.webp` | à produire |
| `images/codex-la-vanne.webp` | à produire |

27 fichiers : 1 couverture, 12 images de chapitre, 14 images de notice.
