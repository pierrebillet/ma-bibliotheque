# Illustrations de « Les Mots donnés »

Manifeste pour l’agent illustrateur — atelier `roman-atelier v9`.

## Ta mission

Produire les fichiers d’images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/les-mots-donnes/`) et dans `couvertures/`. C’est tout.

**Règles impératives** :

1. Tu travailles sur la branche `claude/roman-heroic-fantasy-ya-3fl1d0` de ce
   dépôt (celle où se trouve ce fichier — la session auteur a été configurée
   sur cette branche par l’orchestrateur, elle remplace la convention
   `atelier/roman-<slug>`). Tu pousses tes commits sur cette branche, jamais
   sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l’îlot JSON
   de `index.html`, ni le texte, ni aucun autre fichier — à une exception
   près : dans le `<head>` de `livres/les-mots-donnes/index.html`, complète la
   meta `book:author` en ajoutant ton modèle, sous la forme :
   `content="Claude Fable 5.1 (texte), <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de Les Mots donnés : chapitres 1
   à 6 »), plusieurs commits bienvenus.
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
- Images intérieures : aucun texte lisible incrusté (titres, lettrages), ni
  signature ni filigrane. Le Registre du chapitre 11 se voit de loin : des
  colonnes suggérées, pas de lettres lisibles.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python livres/_template/outils/verifier.py livres/les-mots-donnes
  ```

## Bible visuelle commune

**Technique et rendu.** Gouache et encre sur papier à grain, rehauts de
crayon de couleur ; le registre de l’illustration d’album jeunes adultes de
qualité — peint, précis dans les silhouettes, simple et constant dans les
visages. Ni photoréalisme, ni rendu 3D, ni manga, ni cartoon. On montre le
souffle épique par la précision des gestes et des lieux, pas par les effets.

**Palette.** Chanvre blond pâle (les fils, les cheveux d’Aube, les
cordelettes neuves), gris d’étain (le lac, les lauzes, la pierre), vert-bleu
d’eau de montagne (la Tende), noir de goudron (les grosses cordes, les cols de
manteau), brun de feutre et de laine ; un **seul accent chaud, safran/or
terni**, réservé à ce qui tient : la lueur des lanternes et des lampes à huile,
un rehaut sur un nœud ou une cordelette au moment où il compte. Pas d’autre
couleur vive.

**Monde et époque.** Monde secondaire d’inspiration montagnarde et
préindustrielle (pierre, chanvre, cuir, bois, lauzes, goudron) ; aucune
architecture ni costume identifiable d’un pays réel, aucune arme, aucune
machine. La magie ne se voit jamais : un nœud qui tient ressemble à un nœud.

**Lumière.** Petit jour, crépuscule, brouillard, nuit aux lanternes, pluie
fine ; jamais de plein midi dur.

**Interdits.** Aucun texte lisible, aucun logo, aucune signature ou
filigrane ; pas de lueur magique, pas d’effets de particules ; pas de sang
visible ; pas de caricature.

**Préfixe de style à placer en tête de chaque prompt** (les prompts ci-dessous
sont rédigés en anglais pour les générateurs ; ce préfixe s’y colle tel quel) :

> Gouache and ink illustration on grainy paper with colored-pencil highlights,
> high-end young-adult fantasy book illustration, painterly, precise
> silhouettes, simple and consistent faces, no photorealism, no 3D render, no
> manga. Palette: pale hemp blond, pewter grey, blue-green mountain water,
> black tar, brown felt and wool, with a single warm saffron-gold accent
> reserved for lanterns, oil lamps and the knot or cord that matters.
> Pre-industrial secondary world of stone, hemp rope, leather and slate; no
> real-world architecture, no weapons, no machines, no visible magic glow. Soft
> dawn, dusk, fog or lantern light. No text, no lettering, no logo, no
> watermark, no signature.

### Personnages récurrents (à tenir identiques d’une image à l’autre)

- **Aube** — 17 ans, petite, mince, mains fortes ; cheveux blond cendré
  « couleur chanvre peigné » attachés sur la nuque par un bout de ficelle ;
  yeux gris attentifs ; chemise de toile grise, pantalon de chanvre, pieds
  nus ou sabots ; **cordelette au poignet gauche** (grise à trois nœuds aux
  chapitres 1–4, grise et inégale au chapitre 5–6, blonde ensuite) ; une
  marque de brûlure dans la paume gauche. Expression : concentrée, jamais
  suppliante. *English descriptor: a small slender 17-year-old girl with ash-blond hemp-colored hair tied back with a piece of string, grey eyes, grey linen shirt, hemp trousers, bare feet or wooden clogs, a thin cord tied around her left wrist.*
- **Hersende** — 71 ans, minuscule, très ridée ; robe de laine brune, châle
  gris, cheveux blancs tirés ; mains noueuses posées à plat sur les genoux.
  *English: a tiny very old woman, brown wool dress, grey shawl, white hair pulled back, gnarled hands resting flat on her knees.*
- **Maître Aymon** — 56 ans, grand, barbe grise coupée ras, yeux très clairs
  presque sans couleur ; tablier de cuir sombre sur chemise de toile ; une
  grande clé de fer au cou sur un cordon. *English: a tall 56-year-old man with a close-cropped grey beard, very pale eyes, dark leather apron over a linen shirt, a large iron key hanging at his chest on a cord.*
- **Séverin** — 23 ans, mince, cheveux noirs courts ; manteau de laine gris au
  col noirci de goudron ; gestes exacts, visage fermé sans dureté. *English: a lean 23-year-old man with short black hair, grey wool coat with a tar-blackened collar, precise and composed.*
- **Bastien Dautry** — 18 ans, grand, blond, visage régulier ; veste et
  manteau de voyage en drap gris fin, **trop neufs** au début (chap. 2–3),
  tachés et déchirés ensuite ; bottes de cuir couvertes de boue ; sac neuf.
  *English: a tall 18-year-old fair-haired young man in a fine grey wool travelling coat that is too new, then muddy and torn, leather boots.*
- **Garance Malaurie** — 38 ans, courte et carrée, visage franc ; manteau de
  feutre brun, foulard sur des cheveux châtains courts, bâton de marche.
  *English: a short, stocky 38-year-old woman in a brown felt coat, a scarf over short chestnut hair, a walking stick, talking.*
- **Vergogne** — mule grise robuste, oreilles rabattues, sonnaille de laiton au
  cou, bât de cuir rouge délavé ; air d’offense digne. *English: a sturdy grey mule with a brass bell at the neck and a faded red leather pack-saddle, a dignified offended expression.*
- **Aurèle Malaurie** — 44 ans, grand et maigre, visage long et creusé (les
  traits de Garance en plus long) ; manteau de laine brune, chapeau à large
  bord, une dizaine de ficelles nouées pendues à la ceinture ; sourit. *English: a tall gaunt 44-year-old man in a brown wool coat and a wide-brimmed hat, a dozen knotted strings hanging from his belt, smiling silently.*
- **Dame Ysabeau Dautry** — 50 ans, grande, grise, droite ; robe de drap fin
  gris-bleu ; cordelette serrée au poignet. *English: a tall, straight-backed grey-haired woman of 50 in a fine grey-blue wool dress.*
- **Mère Ancelle** — 80 ans, petite, châle, mains comme des racines de
  prunier, yeux clairs.

### Lieux récurrents

- **Tressaille** — ville de six mille âmes au pied d’une digue ; la Haute sur
  un éperon rocheux à l’est (portes peintes), la Basse en bas le long d’un
  canal entre quais de pierre noire ; toits de lauzes gris, fumées de
  châtaignier.
- **La Levée** — digue de pierre grise moussue, six cents pas de long,
  quarante de haut, droite, coupant le ciel ; une bande sombre luisante sous
  la crête (la marque) ; sur la crête, une rigole de pierre à hauteur de genou
  où repose la **Maîtresse-Corde**, grise, goudronnée, grosse comme un tronc
  de jeune frêne, avec de loin en loin une bosse de la taille d’une tête (un
  nœud) ; aux deux bouts, une grosse **Pierre d’Ancre** où la corde entre dans
  le roc ; à l’extrémité ouest, un escalier de cent soixante marches taillé
  dans la digue, sans rampe.
- **La Retenue** — lac de montagne long et étroit, gris d’étain, lisse,
  reflétant des aiguilles rocheuses ; rives de galets gris et saules.
- **La Salle des Cordes** — corderie longue et basse (deux cent vingt pas),
  terre battue, hautes fenêtres grises, écheveaux de chanvre suspendus,
  grand rouet au fond, bat-flanc de bois.
- **Pont-Sauvage et la Grande Traversée** — vingt maisons de pierre grise à
  toits de lauzes au bord d’une gorge étroite et très profonde ; un pont de
  cordes de quatre cents pas : deux câbles goudronnés gros comme des cuisses,
  tablier de planches, centaines de cordes verticales de plus en plus fines
  vers le milieu, deux rampes ; anneaux de fer forgé aux ancrages.
- **Sombreval** — ruines sous un éboulis de blocs gris, pignons debout,
  pruniers en fleur blanche partout, château ruiné sur un piton ; anneaux de
  fer rouillés dans les murs.
- **La benne de Malebosse** — gorge sombre, câble tendu entre deux piliers de
  roche, nacelle de vannerie et de cuir suspendue par deux poulies de bois,
  cabestan à quatre bras sous un appentis de lauzes.
- **Le col de la Déliée** — selle de pierre nue entre deux épaules
  rocheuses ; des dizaines de cordes tendues de pilier en pilier à toutes les
  hauteurs, givrées ; brouillard, puis mer de nuages et aiguilles roses au
  lever du soleil.
- **Haut-Charme** — hameau de trente toits de lauzes sur une butte dans une
  prairie de sources (linaigrettes blanches) ; un carré de terre noire bêchée
  devant chaque maison ; grande grange ; petit pont de cordes bas dont la
  corde maîtresse est couverte de cordelettes nouées ; brebis.

## Couverture

- **Fichier** : `couvertures/les-mots-donnes.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : Aube debout sur la crête de la Levée au petit jour, la main posée sur la Maîtresse-Corde, le lac derrière elle, la ville en bas.
- **Prompt** : [préfixe de style] Vertical 2:3 composition. A small slender 17-year-old girl with ash-blond hemp-colored hair tied back with a piece of string, grey linen shirt, hemp trousers, bare feet, a thin grey cord knotted around her left wrist, stands in the lower-middle of the frame on the crest of a long straight stone dam, seen from slightly below and to the side; her right hand rests on a huge tar-black rope as thick as a young tree trunk lying in a stone channel that runs away toward the horizon with a knot-shaped bulge visible farther along. Behind and below her to one side, a vast still mountain lake the color of pewter at first light, mirroring pink rocky peaks; on the other side, far below, the slate roofs of a town with thin chimney smoke. Dawn sky, pale gold on the horizon, cool grey above; a single warm saffron highlight on the cord under her hand. Upper third of the image left calm and uncluttered (sky) for a title to be overlaid later. No text, no lettering, no logo, no watermark, no signature.
- **Alt de référence** (déjà dans l’îlot, ne pas le modifier) : « Une jeune fille aux cheveux couleur de chanvre, une cordelette nouée au poignet, debout sur la crête d’une digue de pierre au-dessus d’une ville, la main posée sur une corde épaisse tendue vers l’horizon ; derrière elle, un lac de montagne au petit jour. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — À reculons
- **Sujet** : la Salle des Cordes à l’aube, trente fileuses reculant en rangs, Aube au premier plan.
- **Prompt** : [préfixe de style] Wide shot with deep perspective inside a long, low rope-walk hall: packed-earth floor, tall grey windows letting in flat early-morning light, skeins of hemp hanging from the beams, a large wooden spinning wheel far at the back. Thirty barefoot young women in grey linen walk backwards side by side in rows, each drawing a pale blond thread that runs taut toward the wheel. In the right foreground, Aube, a small 17-year-old girl with ash-blond hemp-colored hair tied with string, a hemp bundle at her belt, twists a strand between thumb and forefinger while stepping backward, eyes on the thread. Hemp dust in the light, dark tar vats along the wall. Grey-blond palette, no gold accent except a faint warmth on her thread. No text.
- **Alt de référence** : « Trente fileuses reculent en rangs dans la longue Salle des Cordes à l’aube, chacune tirant un fil pâle tendu vers le fond ; au premier plan, Aube, une mèche de chanvre entre les doigts. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Douze mots
- **Sujet** : la nuit dans le dortoir, Hersende noue une lettre à la lampe à huile, Aube la regarde.
- **Prompt** : [préfixe de style] Intimate night interior with a single light source: an oil lamp set on a packed-earth floor lights from below a tiny, very old woman in a brown wool dress and grey shawl, white hair pulled back, gnarled hands knotting a long grey string into small tight knots. Beside her on a low wooden sleeping bench sits Aube, a small 17-year-old girl with ash-blond hair tied with string, knees drawn up, watching intently. Above them, hanging skeins of hemp fade into blue darkness. Close framing, warm saffron lamplight against deep blue night, texture of wool and rope. No text.
- **Alt de référence** : « La nuit dans le dortoir des fileuses : Hersende, très vieille, assise au bord d’un bat-flanc, noue une ficelle à la lumière d’une lampe à huile posée au sol, tandis qu’Aube la regarde. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — La corde qui chante
- **Sujet** : la Grande Traversée au crépuscule, vue du chemin ; Séverin assis sur la pierre d’ancrage de l’autre rive.
- **Prompt** : [préfixe de style] Very wide dusk landscape: a rope bridge four hundred paces long spans a narrow, dizzyingly deep gorge — two thick tar-black cables, a plank walkway, and hundreds of vertical cords growing thinner toward the middle, all vibrating in the wind. On the left, the small village of Pont-Sauvage: grey stone houses with slate roofs clinging to the cliff edge, an inn lantern already lit, villagers on a tiny square looking up. Two children run across the middle of the bridge. On the far right anchor stone, facing us, the small figure of a lean young man in a grey coat sits with his legs dangling, eating a pear. In the foreground, backlit silhouettes: a small girl, a loaded grey mule with a bell, a short stocky woman with a staff, a tall young man. Orange and grey sky, white mist deep in the gorge. No text.
- **Alt de référence** : « Au crépuscule, la Grande Traversée de Pont-Sauvage tendue au-dessus de la gorge, ses centaines de cordes verticales prises dans le vent ; sur la pierre d’ancrage de l’autre rive, une silhouette assise mange une poire. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Nœud d’amarre
- **Sujet** : sous la pluie, Aube à genoux noue sa cordelette autour du câble du pont à l’anneau d’ancrage.
- **Prompt** : [préfixe de style] Close shot from slightly above in fine rain: Aube, a small 17-year-old girl with wet ash-blond hair tied with string and a soaked grey linen shirt, kneels on wet stone and tightens with both hands a thin grey cord around a tar-black cable as thick as a thigh where it enters a heavy wrought-iron ring set in the rock; her mouth is almost touching the knot. Behind her, out of focus, the plank walkway of a rope bridge tilts to the left with six mules loaded with hemp bales and men in felt capes frozen in place; villagers on the square stand still. Grey rain palette, black tar, one warm saffron highlight on the small cord in her hands. No text.
- **Alt de référence** : « Sous la pluie, Aube à genoux devant l’anneau de fer de l’ancrage noue sa cordelette autour du gros câble noir du pont, qui penche derrière elle avec des mules chargées dessus. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — Les anneaux de Sombreval
- **Sujet** : dans les ruines en fleurs, Bastien montre un petit anneau à chaîne sous un grand anneau ; Aube et Séverin regardent.
- **Prompt** : [préfixe de style] Ruins of a mountain village half-buried under a rockslide of huge grey boulders, gable walls still standing, and everywhere plum trees in white blossom in fine rain, petals on the stones. In the foreground, a stone wall with a large rusted iron ring at chest height and, below it, a small ring at hip height with three links of chain hanging from it. Bastien, a tall fair-haired 18-year-old in a soaked grey wool coat, bends and points at the small ring; Aube, a small girl with ash-blond hair tied with string, and Séverin, a lean young man in a grey coat with a tar-black collar, stand beside him, grave. Upper right, a ruined castle on a rocky spur. Muted grey-green palette, white blossom. No text.
- **Alt de référence** : « Dans les ruines de Sombreval, sous des pruniers en fleur et la pluie, Bastien penché montre un petit anneau de fer avec un bout de chaîne scellé dans un mur, sous un anneau plus grand ; Aube et Séverin regardent. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — La benne
- **Sujet** : la nacelle au milieu du vide, la mule pendue de travers dessous, Aube et Séverin penchés sur la corde.
- **Prompt** : [préfixe de style] Wide frontal view inside a narrow gorge with dark rock walls, a brown roaring river far below. At the center, a wicker-and-leather basket hangs from a cable stretched between two rock pillars. Aube, a small girl with ash-blond hair tied with string, and Séverin, a lean young man in a grey coat with a tar-black collar, lie flat over the basket's edge, both gripping a short rope together. Below the basket, a grey mule hangs askew in leather slings, one strap ridden up on its flank, legs stiff, a brass bell at its neck. On the right cliff edge, tiny, an old man at a four-armed capstan under a slate shelter. High white sky, taut lines, one saffron highlight on the rope in their hands. No text.
- **Alt de référence** : « Une nacelle de vannerie suspendue à un câble au milieu d’une gorge profonde ; en dessous, une mule pend de travers dans ses sangles, et deux jeunes gens penchés hors de la nacelle tiennent la corde. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — La harpe du col
- **Sujet** : l’aube au-dessus d’une mer de nuages sur le col, les cordes givrées, Aurèle à sa clé de bois, les voyageurs sortant du brouillard.
- **Prompt** : [préfixe de style] Luminous wide landscape: a bare stone saddle of a mountain pass rises above a sea of white cloud that fills the whole valley below, out to pink rocky needle-peaks; the sun is just rising between two summits. Everywhere across the pass, stretched from rock pillar to rock pillar at every height, dozens of frost-covered cords glitter, from hair-thin to arm-thick. At the foot of a tall pillar, a tall gaunt man in a brown wool coat and a wide-brimmed hat held against the wind turns a wooden key set in the stone at the base of one cord, head tilted, listening. On the left, emerging from the fog: a grey mule with a brass bell, a short stocky woman with a staff, a small girl with ash-blond hair, a tall fair young man, a lean young man in a grey coat. Cold gold light. No text.
- **Alt de référence** : « À l’aube, au-dessus d’une mer de nuages, des dizaines de cordes givrées tendues entre des piliers de roche sur le col ; un homme au chapeau à large bord tourne une clé de bois au pied d’un pilier, et les voyageurs sortent du brouillard. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — La veillée
- **Sujet** : la veillée nocturne aux torches sur le Pont de Charme ; les villageois nouent leurs cordelettes, Bastien à genoux, Aube file à l’écart.
- **Prompt** : [préfixe de style] Night scene lit by resin torches: a short, low rope bridge crosses a network of small streams in a wet mountain meadow; its main rope, as thick as an arm, is covered almost end to end with small cords knotted side by side like fur. A line of elderly villagers, each holding a cord, waits; an old woman kneels and knots hers onto the main rope, her mouth close to the knot; a tall gaunt man in a wide-brimmed hat checks the knot with his fingers. Bastien, a tall fair-haired young man in a ruined grey coat, kneels in the mud. Set apart on the bank, Aube, a small girl with ash-blond hair, sits spinning a string between thumb and forefinger. In the background, a dozen people simply hold torches; slate roofs in the dark. Warm saffron torchlight against blue night. No text.
- **Alt de référence** : « La nuit, à la lumière des torches, les habitants de Haut-Charme agenouillés au bord d’un petit pont de cordes nouent leurs cordelettes sur la corde maîtresse ; Bastien est à genoux dans la boue, et Aube, assise à l’écart, file. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Grandes eaux
- **Sujet** : nuit sur le lac plein, la gabare à la perche entre les saules noyés ; au fond, la Levée et la file de lanternes sur l’escalier.
- **Prompt** : [préfixe de style] Wide night landscape over a perfectly still mountain lake, a sheet of silver under a nearly full moon. A flat-bottomed barge moves through the middle, a boatman with a long pole, a slack sail, and on board a grey mule standing stiffly, a short stocky woman, a tall man in a wide-brimmed hat, a small girl, a tall fair young man, a lean young man in grey. On both sides, willows stand drowned to mid-trunk, the roofs of fishermen's huts barely above the water. In the background, cutting straight across sky and lake, the long black wall of a stone dam; at its left end a stairway carved into the dam with a file of hundreds of tiny lantern lights climbing it; a faint glow of a town above the dam. Cold silver and black, warm pinpoints of lantern gold. No text.
- **Alt de référence** : « Nuit sur le lac plein : une gabare avance à la perche sous une lune presque pleine, entre des saules noyés jusqu’à mi-tronc ; au fond, la longue crête noire de la Levée et, sur son escalier, une file de petites lumières qui montent. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — Le registre
- **Sujet** : la Salle inondée ; les fileuses avec des lampes autour d’Aube, qui délie la cordelette de Hersende près du corps couvert.
- **Prompt** : [préfixe de style] Night interior: the long rope-walk hall has water on its floor with planks laid across it; thirty young women in grey linen stand or sit on wooden benches holding oil lamps, silent, grave. At the center, on a low bench, a very small form under a hemp blanket, one thin wrist showing. Aube, a small girl with ash-blond hair tied with string, sits beside it, head bowed, holding a long grey cord and undoing one of its knots. Skeins of hemp hang above. Warm lamplight, reflections in black water, deep blue shadows. Restrained, tender, no visible face of the dead. No text.
- **Alt de référence** : « Dans la Salle des Cordes inondée, sur des planches, trente fileuses tiennent des lampes en silence autour d’Aube, assise près d’une forme couverte d’une couverture de chanvre, qui délie une cordelette nœud après nœud. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — Mille demi-clés
- **Sujet** : la nuit de la pleine lune sur la crête de la Levée, la ville à genoux le long de la corde avec des lanternes ; Aube debout à la Pierre d’Ancre, Aymon à son Registre.
- **Prompt** : [préfixe de style] Very wide night scene on the crest of a long straight stone dam: on the left, the black lake brimming and licking the stone; far below on the right, the lantern-lit roofs of a town; a full moon rising over rocky needle-peaks at the back. Along a stone channel holding a rope as thick as a tree trunk, hundreds of people kneel with iron and copper lanterns, mouths close to the rope, and the rope is already covered with small knotted cords. In the foreground, Aube, a small girl with ash-blond hair, stands beside a large anchor stone, one hand on the rope. Next to her, a tall bearded man in a leather apron with an iron key at his chest writes in a large book laid on a plank, a lantern beside him (columns suggested, no readable letters). A tall gaunt man in a wide-brimmed hat bends over a knot. Lantern gold on the faces, silver moon, black water. No text.
- **Alt de référence** : « La nuit de la pleine lune sur la crête de la Levée : des centaines de gens agenouillés le long de la rigole avec des lanternes nouent leurs cordelettes sur la grosse corde ; Aube, debout à la pierre d’ancrage, regarde ; à une planche, Maître Aymon écrit dans un grand livre. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — Les manquants
- **Sujet** : au petit jour, la Maîtresse-Corde couverte de cordelettes comme une fourrure ; Aube à genoux y pose la main ; en bas, la mule et deux silhouettes attendent à la porte de la ville.
- **Prompt** : [préfixe de style] Wide shot at sunrise in pink and gold light: the crest of a grey stone dam runs diagonally across the frame, and in its stone channel lies a rope as thick as a tree trunk entirely covered, end to end, with small grey, brown and blond cords knotted side by side like a pelt. Aube, a small girl with ash-blond hair tied with string, kneels beside a large anchor stone with her hand resting on the rope, a new pale-blond cord around her left wrist. Behind her the lake is calm again, smooth pewter, mirroring the mountains. Far below on the right, tiny: a loaded grey mule, a short stocky woman with a staff and a tall man in a wide-brimmed hat waiting before a gap in an old town wall. Quiet, luminous, hopeful. No text.
- **Alt de référence** : « Au petit jour sur la crête de la Levée, la grande corde est couverte d’un bout à l’autre de cordelettes nouées comme une fourrure ; Aube, à genoux, y pose la main ; tout en bas, à la porte de la ville, une mule chargée et deux silhouettes attendent. »

## Images de notices

### `images/codex-aube.webp`

- **Notice** : Aube (personnage)
- **Sujet** : portrait d’Aube, une mèche de chanvre entre les doigts, la cordelette au poignet.
- **Prompt** : [préfixe de style] Three-quarter portrait of a small slender 17-year-old girl, ash-blond hemp-colored hair tied at the nape with a piece of string, attentive grey eyes, thin face, grey linen shirt; her strong hands twist a strand of blond hemp between thumb and forefinger; around her left wrist a thin grey cord with three small knots; a faint burn scar on her left palm. Soft background of taut blond threads in a grey hall. Calm, concentrated expression, not smiling, not pleading. No text.
- **Alt de référence** : « Portrait d’Aube, dix-sept ans, cheveux couleur chanvre attachés d’une ficelle, yeux gris, chemise de toile grise, une cordelette au poignet gauche, une mèche de chanvre entre les doigts. »

### `images/codex-hersende.webp`

- **Notice** : Hersende (personnage)
- **Sujet** : Hersende assise sur le banc des vieilles, la tête penchée pour écouter.
- **Prompt** : [préfixe de style] Seated portrait of a tiny woman well over seventy, deeply wrinkled, brown wool dress, grey shawl, white hair pulled back, gnarled hands resting flat on her knees like tools put away; her head tilts slightly, eyes half-closed, as if listening to a distant sound. Behind her a stone wall and hanging skeins of hemp; flat grey light from a high window. Great gentleness and economy in the pose. No text.
- **Alt de référence** : « Hersende, très vieille et très petite, assise sur un banc de bois contre un mur, châle gris, mains noueuses posées sur les genoux, la tête un peu penchée comme pour écouter. »

### `images/codex-maitre-aymon.webp`

- **Notice** : Maître Aymon (personnage)
- **Sujet** : le Maître de la Corderie, la main posée sur la Maîtresse-Corde, le lac derrière lui.
- **Prompt** : [préfixe de style] Three-quarter portrait of a tall 56-year-old man with a close-cropped grey beard and very pale, almost colorless eyes, dark leather apron over a linen shirt, a large iron key hanging at his chest on a cord; his palm rests on a tar-grey rope as thick as a tree trunk lying in a stone channel. Behind him a pewter-grey lake and mountains under a soft sky. Tired, attentive, without harshness. No text.
- **Alt de référence** : « Maître Aymon, cinquante-six ans, barbe grise coupée ras, tablier de cuir sur une chemise de toile, une grande clé de fer au cou sur un cordon, debout, une main posée sur une grosse corde goudronnée. »

### `images/codex-severin.webp`

- **Notice** : Séverin (personnage)
- **Sujet** : Séverin assis sur la pierre d’ancrage du pont, une poire à la main.
- **Prompt** : [préfixe de style] Portrait of a lean 23-year-old man with short black hair, grey wool coat with a tar-blackened collar, sitting on a large anchor stone where two thick tar-black cables enter the rock, legs dangling over a misty void; he eats a pear with care and looks straight at the viewer, neither hostile nor curious. Behind him twisted pines on a shadowed cliff; dusk light. No text.
- **Alt de référence** : « Séverin, vingt-trois ans, cheveux noirs, manteau gris au col noirci de goudron, assis sur une grosse pierre d’ancrage au bord d’une gorge, jambes pendantes, une poire à la main. »

### `images/codex-bastien-dautry.webp`

- **Notice** : Bastien Dautry (personnage)
- **Sujet** : Bastien en manteau trop neuf et bottes boueuses sur un chemin de corniche.
- **Prompt** : [préfixe de style] Full-length portrait of a tall fair-haired 18-year-old young man with a regular, earnest face, wearing a fine grey wool jacket and travelling coat that are visibly new and already stained, a new pack on one shoulder and a peddler's bundle on the other, leather boots muddy to the knee; he stands straight on a narrow cliff path above a white river, looking like someone with blisters who won't mention them. Rainy morning light. No text.
- **Alt de référence** : « Bastien Dautry, dix-huit ans, grand et blond, un manteau de voyage en drap gris trop neuf, un sac sur l’épaule, des bottes couvertes de boue, debout sur un chemin de montagne. »

### `images/codex-garance-malaurie.webp`

- **Notice** : Garance Malaurie (personnage)
- **Sujet** : la colporteuse au bâton, une main sur le bât de sa mule, au bord du lac à l’aube.
- **Prompt** : [préfixe de style] Full-length portrait of a short, stocky 38-year-old woman in a brown felt coat, a scarf knotted over short chestnut hair, a walking staff in one hand, a frank face caught mid-sentence, her other hand resting on the pack-saddle of a grey mule loaded like a walking house, the mule's brass bell stuffed with a rag. Behind them a shore of grey pebbles and a pewter lake at dawn. Lively, slightly mocking tone. No text.
- **Alt de référence** : « Garance Malaurie, trente-huit ans, courte et carrée, manteau de feutre brun, un bâton à la main, un foulard sur des cheveux châtains courts, debout à côté d’une mule grise chargée à la sonnaille bourrée de chiffon. »

### `images/codex-vergogne.webp`

- **Notice** : Vergogne (bête)
- **Sujet** : la mule grise chargée, mâchant un nouet, l’air offensé.
- **Prompt** : [préfixe de style] Portrait of a sturdy grey mule with ears laid back, loaded with a faded red leather pack-saddle carrying bundles of salt and cloth, a brass bell at its neck; it chews a small fried knot-shaped pastry glazed with honey and looks at the viewer with an expression of deep and dignified offense. Behind it a mountain path and a misty drop. Affectionate, gently humorous rendering. No text.
- **Alt de référence** : « Une mule grise de douze ans, chargée d’un bât rouge délavé, une sonnaille au cou, qui mâche une pâtisserie en forme de nœud avec un air d’offense profonde. »

### `images/codex-aurele-malaurie.webp`

- **Notice** : Aurèle Malaurie (personnage)
- **Sujet** : le veilleur du col à sa clé de bois, au pied d’une corde givrée, au-dessus des nuages.
- **Prompt** : [préfixe de style] Full-length portrait of a tall gaunt 44-year-old man with a long hollowed face, brown wool coat, a wide-brimmed hat held against the wind with one hand, a dozen knotted strings hanging from his belt; with his other hand he turns a wooden key set into a rock pillar at the base of a frost-covered cord that rises into the sky; he smiles, head tilted as if listening to the note. Behind him a sea of white clouds and pink summits at dawn. No text.
- **Alt de référence** : « Aurèle Malaurie, grand et maigre, manteau de laine brune, chapeau à large bord, des ficelles nouées pendues à la ceinture, tourne une clé de bois plantée dans la pierre au pied d’une corde tendue, et sourit sans rien dire. »

### `images/codex-la-levee.webp`

- **Notice** : La Levée (lieu)
- **Sujet** : la digue vue du lac, la marque sous la crête, la corde et ses nœuds dans la rigole.
- **Prompt** : [préfixe de style] View from the lake, slightly from below, of a long straight dam of grey moss-glazed stone, six hundred paces long, cutting across the sky; a dark glossy band runs just under the crest; on the crest, in a stone channel, lies a tar-grey rope as thick as a young tree trunk with, every so often, a bulge the size of a head. At one end a stairway carved into the dam descends out of frame. Smooth pewter water in the foreground mirrors the dam; clear morning sky. No human figures. No text.
- **Alt de référence** : « La Levée vue depuis le lac : une longue digue de pierre grise moussue coupant l’horizon, une ligne sombre sous sa crête, et sur la crête la grosse corde goudronnée dans sa rigole avec ses nœuds espacés. »

### `images/codex-pont-sauvage.webp`

- **Notice** : Pont-Sauvage et la Grande Traversée (lieu)
- **Sujet** : le village au bord de la gorge et le pont qui s’élance depuis sa place.
- **Prompt** : [préfixe de style] Gentle high-angle view of a mountain village: about twenty grey stone houses with slate roofs, washing lines, an inn with a lantern, clinging to the lip of a very narrow and deep gorge; from the small square a rope bridge four hundred paces long leaps out over the void — two cables as thick as thighs, a plank walkway, hundreds of vertical cords growing thinner toward the middle. Villagers on the square look up, listening to the bridge. Late afternoon, white mist deep in the gorge, twisted pines on the opposite cliff. No text.
- **Alt de référence** : « Le village de Pont-Sauvage, vingt maisons de pierre grise à toits de lauzes accrochées au bord d’une gorge, et la Grande Traversée qui s’élance depuis sa place au-dessus du vide, avec ses centaines de cordes verticales. »

### `images/codex-le-col-de-la-deliee.webp`

- **Notice** : Le col de la Déliée (lieu)
- **Sujet** : la harpe du col dans le brouillard, une mule seule qui avance vers une corde.
- **Prompt** : [préfixe de style] High mountain landscape in dense, luminous fog: a bare stone saddle between two rocky shoulders and, everywhere, stretched from pillar to pillar at every height, dozens of frost-covered cords, some hair-thin, some arm-thick, glinting faintly in the grey. At the center a loaded grey mule with a brass bell walks alone toward the nearest cord as if toward a door; far behind it, three blurred figures. The fog brightens from above with a golden white. No text.
- **Alt de référence** : « Le col de la Déliée dans le brouillard : des cordes givrées tendues de pilier de roche en pilier de roche à toutes les hauteurs, brillant faiblement dans le gris, et une mule grise qui avance seule vers l’une d’elles. »

### `images/codex-haut-charme.webp`

- **Notice** : Haut-Charme (lieu)
- **Sujet** : le hameau sur sa butte, les carrés de chanvre, la grange, le pont bas, les brebis.
- **Prompt** : [préfixe de style] Wide view of a high mountain hamlet in spring: a knoll in the middle of a wet meadow where a hundred small streams rise among tufts of white cotton-grass; about thirty stone houses with grey slate roofs, a large barn taller than everything else, a low short rope bridge over the streams; in front of every house a freshly dug square of black earth the size of a blanket; sheep, a few bent figures working the squares, children running; pink summits in the background. Clear, cold late-morning light. No text.
- **Alt de référence** : « Le hameau de Haut-Charme : trente toits de lauzes sur une butte au milieu d’une prairie de sources, un carré de terre noire fraîchement bêché devant chaque maison, une grande grange, un pont de cordes bas, et des brebis. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/les-mots-donnes.webp` | à produire |
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
| `images/codex-aube.webp` | à produire |
| `images/codex-hersende.webp` | à produire |
| `images/codex-maitre-aymon.webp` | à produire |
| `images/codex-severin.webp` | à produire |
| `images/codex-bastien-dautry.webp` | à produire |
| `images/codex-garance-malaurie.webp` | à produire |
| `images/codex-vergogne.webp` | à produire |
| `images/codex-aurele-malaurie.webp` | à produire |
| `images/codex-la-levee.webp` | à produire |
| `images/codex-pont-sauvage.webp` | à produire |
| `images/codex-le-col-de-la-deliee.webp` | à produire |
| `images/codex-haut-charme.webp` | à produire |

Vingt-cinq fichiers : une couverture, douze images de chapitre, douze images
de notice. Le décompte correspond aux champs `image` de l’îlot et au bloc
`cover` de `index.html`.
