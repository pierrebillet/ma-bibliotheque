# Illustrations de « La Clause du meilleur ennemi »

Manifeste pour l'agent illustrateur — atelier `roman-atelier v3`.

## Ta mission

Produire les fichiers d'images listés plus bas, aux noms **exacts**, dans ce
dossier (`livres/la-clause-du-meilleur-ennemi/`) et dans `couvertures/`. C'est tout.

**Règles impératives** :

1. Tu travailles sur la branche `claude/roman-illustre-workflow-ptcfws` de ce
   dépôt (celle où se trouve ce fichier — la session auteur a été configurée sur
   cette branche, qui remplace la convention `atelier/roman-<slug>`). Tu pousses
   tes commits sur cette branche, jamais sur `main`.
2. Tu ne crées **que** les fichiers listés ici. Tu ne modifies ni l'îlot JSON de
   `index.html`, ni le texte, ni aucun autre fichier — à une exception près :
   dans le `<head>` de `livres/la-clause-du-meilleur-ennemi/index.html`, complète
   la meta `book:author` en ajoutant ton modèle, sous la forme :
   `content="<valeur existante>, <ton modèle> (images)"`.
3. Interdits absolus du dépôt : ne jamais toucher `catalog.json` ni le bloc
   `#demo-catalog` de `index.html` à la racine ; aucune ressource distante.
4. Commits en français (ex. « Illustrations de La Clause du meilleur ennemi :
   chapitres 1 à 5 »), plusieurs commits bienvenus.
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
- Aucun texte lisible incrusté dans les images (titres, lettrages) sauf si une
  entrée le demande explicitement.
- Vérification finale (depuis la racine du dépôt) :
  ```bash
  python ateliers/roman-atelier/outils/verifier.py livres/la-clause-du-meilleur-ennemi
  ```

## Bible visuelle commune

Gouache et encre sur papier à grain, rehauts de crayon gras ; le registre de
l'illustration de presse littéraire — ni photoréalisme, ni cartoon, ni rendu
3D. Palette : zinc parisien (gris-bleu), bleu nuit, ivoire du papier laissé
visible, et un seul accent chaud cuivre/or terni — l'or marque toujours ce qui
relie les deux rivaux (sablier, sonnette, écharpe, ruban jaune, bougie).
Époque : Paris réel, 2005-2026 (Sentier, rue Réaumur, palais Brongniart, haut
Marais). Lumière de fin de journée ou de nuit électrique, jamais de plein midi.
Interdits : aucun texte lisible (enseignes floues, écritures suggérées), aucun
logo ou marque réels, aucune caricature de personne réelle. Stylisation des
personnages : silhouettes précises, visages esquissés mais constants d'une
image à l'autre.

Personnages récurrents (à tenir identiques partout, vieillissement compris) :

- **Octave Brossard** : homme solide et élégant, costume marine impeccable en
  toute circonstance, cheveux bruns (25 ans en 2005) puis gris aux tempes
  (années 2020), écharpe grise en extérieur, souvent un petit sablier ou un
  stylo plume à portée de main.
- **Salomé Vidal** : femme mince et très droite, cheveux noirs coupés court
  puis grisonnants après 2018, vêtements techniques sobres au début puis
  manteau droit gris-bleu, souvent un objet mécanique en main (sonnette de
  vélo chromée, clé à rayons).
- **Anselme Rueff** : grand vieil homme sec, costume trois-pièces à gilet,
  sourcils broussailleux, carnet noir.
- **Marguerite Lin** : tailleur sombre, lunettes rondes, chignon strict,
  dossier ou papier plié à la main.

## Couverture

- **Fichier** : `couvertures/la-clause-du-meilleur-ennemi.webp` (à la racine du dépôt) — 800×1200, < 300 Ko
- **Sujet** : deux rivaux dos à dos sur un toit de Paris, reliés par une même écharpe dorée.
- **Prompt** : bible visuelle + composition verticale 2:3 : sur un toit en zinc
  de Paris au crépuscule, un homme en costume marine et une femme en manteau
  droit se tournent le dos, à trois pas l'un de l'autre, chacun regardant son
  propre horizon de cheminées ; une longue écharpe dorée portée par le vent
  passe de l'épaule de l'un à l'épaule de l'autre et les relie d'un seul trait
  de cuivre ; ciel bleu nuit dégradé vers l'ivoire au ras des toits ; point
  focal sur l'écharpe au tiers inférieur, tiers supérieur du ciel laissé calme
  pour la place implicite du titre (sans lettrage).
- **Alt de référence** (déjà dans l'îlot, ne pas le modifier) : « Sur un toit en zinc de Paris au crépuscule, un homme et une femme en manteau se tournent le dos, reliés par le long fil doré d'une même écharpe emportée par le vent. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Ex æquo
- **Sujet** : la poignée de main ratée de la remise du prix, sous la verrière.
- **Prompt** : bible visuelle + plan moyen sous la charpente vitrée d'un
  atelier 1900 la nuit, guirlandes d'ampoules ; un jeune homme en costume
  marine (Octave, 25 ans) ouvre les deux bras pour une accolade de vainqueur
  face à une jeune femme droite (Salomé, 24 ans) qui lui tend une main ferme à
  distance réglementaire ; petit public flou et amusé en arrière-plan, reflets
  de pluie sur les carreaux ; lumière chaude cuivrée au centre, bleu nuit sur
  les bords.
- **Alt de référence** : « Sous la verrière illuminée, un jeune homme en costume marine ouvre les bras pour une accolade tandis qu'une jeune femme lui tend une main ferme à distance. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Le premier tour
- **Sujet** : la diagonale d'Octave vers Gabriel Atlan, à la soirée des anciens.
- **Prompt** : bible visuelle + vue légèrement plongeante d'une salle de fête
  sous verrière, foule en grappes de conversations ; au centre, Octave en
  costume marine fend la foule selon une diagonale parfaite, un verre dans
  chaque main, cap sur un jeune ingénieur timide à lunettes (Gabriel) adossé à
  un babyfoot ; une traînée d'espace vide se dessine dans son sillage, comme un
  sillage de navire ; lumière de guirlandes, zinc et cuivre.
- **Alt de référence** : « Dans une fête d'anciens élèves, un homme en costume marine traverse la salle en diagonale avec deux verres, vers un ingénieur timide adossé au babyfoot. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Sept minutes
- **Sujet** : Octave seul au dernier étage, le 31 décembre 2011, sablier en main, face aux fenêtres du 128.
- **Prompt** : bible visuelle + intérieur nuit d'un étage de bureaux éteint ;
  Octave en costume marine, de trois quarts dos, retourne un petit sablier
  devant la vitre ; par la fenêtre, en fond de cour à deux cents mètres, les
  plateaux éclairés d'une ancienne imprimerie aux colonnes de fonte, où passe
  une silhouette féminine affairée ; bleu nuit dominant, deux foyers de lumière
  cuivrée : le sablier au premier plan, les fenêtres au fond.
- **Alt de référence** : « De nuit, seul à une fenêtre de bureau, un homme retourne un sablier ; au fond de la cour, les fenêtres éclairées d'une ancienne imprimerie. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — La keynote des couteaux
- **Sujet** : le duel au micro du palais Brongniart, sonnette contre badge.
- **Prompt** : bible visuelle + plan large de la scène circulaire du palais
  Brongniart, colonnade et écrans géants sans texte lisible ; Salomé au
  pupitre, bras levé tenant une petite sonnette de vélo chromée ; au premier
  rang, Octave debout brandit son badge de conférencier comme un carton
  d'arbitre ; salle comble hilare, faisceaux de projecteurs dorés sur la pierre
  gris-bleu.
- **Alt de référence** : « Sur la scène circulaire d'un ancien palais boursier, une femme au pupitre lève une sonnette de vélo ; au premier rang, un homme brandit son badge comme un carton d'arbitre. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — Chasse à la licorne
- **Sujet** : l'annonce du milliard au 128, Octave sur sa caisse parmi les gilets réfléchissants.
- **Prompt** : bible visuelle + intérieur jour d'un dépôt de vélos-cargos,
  colonnes de fonte, racks de roues ; Salomé debout annonce ses chiffres
  simplement devant des rangées d'employés en gilets réfléchissants ; au
  premier rang, légèrement décalé, Octave en costume marine assis très droit
  sur une caisse en bois de pièces détachées, comme sur un fauteuil de
  cérémonie ; lumière d'atelier froide trouée d'un rai doré qui tombe sur la
  caisse.
- **Alt de référence** : « Entre les colonnes de fonte d'un atelier, une femme annonce ses chiffres devant son personnel en gilets réfléchissants ; un homme en costume marine écoute, assis sur une caisse de pièces détachées. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — L'année des orages
- **Sujet** : la défense publique de Salomé à Convergence 2019.
- **Prompt** : bible visuelle + plan rapproché en légère contre-plongée :
  Salomé (cheveux grisonnants aux tempes) au micro d'une grande conférence,
  main tendue vers la salle, sonnette de vélo posée sur le pupitre ; au premier
  rang flou, Octave tête baissée, un sourire à peine visible ; ambiance d'orage
  retenu, fond bleu nuit, visage éclairé cuivre.
- **Alt de référence** : « Une femme au micro d'une grande conférence désigne la salle, sonnette posée sur le pupitre ; au premier rang, un homme écoute tête baissée, un léger sourire aux lèvres. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Les vélos de mars
- **Sujet** : la coursière « Line » dans Paris confiné, au petit matin.
- **Prompt** : bible visuelle + plan large d'une rue de Paris totalement vide
  au petit matin de printemps 2020, rideaux de fer baissés, chaussée luisante ;
  une seule figure mobile : une coursière d'âge mûr en gilet réfléchissant sur
  un vélo-cargo chargé de caisses de pharmacie ; perspective profonde, ciel
  ivoire pâle, la bande réfléchissante du gilet comme unique accent cuivré.
- **Alt de référence** : « Au petit matin dans un Paris confiné et vide, une coursière d'âge mûr en gilet réfléchissant remonte à vélo-cargo une rue déserte aux rideaux de fer baissés. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Une affaire d'enchères
- **Sujet** : la vente à la bougie de l'hôtel de Vaudreuil, Marguerite debout au fond.
- **Prompt** : bible visuelle + intérieur solennel d'une salle des criées de la
  chambre des notaires : boiseries, rangées d'enchérisseurs de dos, un notaire
  en tribune penché sur deux petites bougies dont l'une fume encore ; au
  dernier rang, Marguerite Lin en tailleur sombre, debout, téléphone à la
  main ; clair-obscur à la bougie, ors ternis, bleu nuit.
- **Alt de référence** : « Dans la salle des criées de la chambre des notaires, deux petites bougies brûlent devant le pupitre du notaire ; au fond, une avocate en tailleur se lève, téléphone en main. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Le jury
- **Sujet** : la première vraie conversation, de nuit, sur le toit de la Verrière.
- **Prompt** : bible visuelle + plan large de nuit sur un toit-terrasse moderne
  au-dessus des toits en zinc du Sentier ; deux silhouettes d'une cinquantaine
  d'années au garde-corps — Octave dont l'écharpe grise claque au vent, Salomé
  droite en manteau ; en contrebas, la rue du Caire éclairée et la charpente
  vitrée illuminée de l'incubateur ; ciel bleu nuit, lignes de zinc, accent
  doré discret sur l'écharpe.
- **Alt de référence** : « De nuit sur le toit-terrasse d'un incubateur, deux silhouettes d'une cinquantaine d'années conversent au garde-corps au-dessus des toits du Sentier, une écharpe flottant au vent. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — La clause du meilleur ennemi
- **Sujet** : Odile lit le dos de la nappe devant les sept convives.
- **Prompt** : bible visuelle + intérieur chaleureux d'un couscous de la rue
  Saint-Denis, tables poussées, plats fumants ; une très vieille dame debout,
  lunettes empruntées, lit le verso d'un set de table en papier jauni tenu à
  deux mains ; sept convives suspendus à sa lecture — costume marine, manteau
  droit, tailleur à lunettes rondes, gilet trois-pièces ; lumière d'applique
  dorée, vapeur des plats, bleu nuit aux fenêtres ; l'écriture sur le papier
  reste suggérée, illisible.
- **Alt de référence** : « Autour d'une table de restaurant aux plats de couscous, une très vieille dame lit le dos d'un set de table jauni que sept convives regardent en silence. »

## Images de notices

### `images/codex-octave-brossard.webp`

- **Notice** : Octave Brossard (personnage)
- **Sujet** : portrait au sablier.
- **Prompt** : bible visuelle + portrait aux trois quarts d'Octave à cinquante
  ans : cheveux gris aux tempes, costume marine impeccable, assis à un bureau
  sobre ; devant lui, un petit sablier de verre ; regard amusé et exact ; fond
  de bibliothèque estompé bleu nuit, rehaut cuivré sur le sablier.
- **Alt de référence** : « Portrait d'un homme d'une cinquantaine d'années en costume marine, assis à son bureau, un petit sablier posé devant lui. »

### `images/codex-salome-vidal.webp`

- **Notice** : Salomé Vidal (personnage)
- **Sujet** : portrait à la sonnette, dans l'atelier.
- **Prompt** : bible visuelle + portrait en pied court de Salomé à cinquante
  ans : mince, très droite, cheveux noirs courts grisonnants, manteau
  gris-bleu, debout entre colonnes de fonte et racks de roues ; dans sa main
  ouverte, une petite sonnette de vélo chromée ; regard direct, sourire
  retenu ; lumière d'atelier froide, accent cuivré sur la sonnette.
- **Alt de référence** : « Portrait d'une femme d'une cinquantaine d'années en manteau droit, debout dans un atelier de vélos-cargos, une sonnette de vélo dans la main ouverte. »

### `images/codex-anselme-rueff.webp`

- **Notice** : Anselme Rueff (personnage)
- **Sujet** : le mémorialiste au carnet.
- **Prompt** : bible visuelle + portrait assis d'un grand vieil homme sec,
  sourcils broussailleux, costume trois-pièces à gilet, fauteuil de cuir
  patiné ; carnet noir ouvert sur les genoux, stylo suspendu, l'air d'avoir
  déjà noté la phrase qu'on n'a pas encore dite ; boiseries et dossiers en
  fond, clair-obscur doré.
- **Alt de référence** : « Portrait d'un grand vieil homme sec en costume trois-pièces, carnet noir ouvert sur les genoux, assis dans un fauteuil de bureau ancien. »

### `images/codex-marguerite-lin.webp`

- **Notice** : Marguerite Lin (personnage)
- **Sujet** : la gardienne de la nappe.
- **Prompt** : bible visuelle + portrait à mi-corps d'une femme d'une
  soixantaine d'années, tailleur sombre, lunettes rondes, chignon strict,
  malice contenue ; elle tient contre elle une chemise cartonnée de coffre d'où
  dépasse le coin d'un set de table en papier jauni ; fond de bibliothèque
  juridique estompé, lumière latérale cuivrée.
- **Alt de référence** : « Portrait d'une avocate en tailleur sombre et lunettes rondes, tenant contre elle une chemise de coffre d'où dépasse un set de table en papier jauni. »

### `images/codex-la-verriere.webp`

- **Notice** : La Verrière (lieu)
- **Sujet** : la charpente vitrée et la ligne jaune sous verre.
- **Prompt** : bible visuelle + intérieur jour d'un atelier 1900 réhabilité :
  grande charpente vitrée, poutrelles rivetées, bureaux dépareillés, babyfoot
  au fond ; au premier plan, l'angle d'un bureau où une ligne de ruban adhésif
  jaune traverse le parquet sous une plaque de verre munie d'un petit cartel
  (texte suggéré, illisible) ; lumière zénithale ivoire, touches cuivrées.
- **Alt de référence** : « Intérieur d'un incubateur sous une grande charpente vitrée 1900 ; au sol d'un bureau d'angle, une ligne de ruban adhésif jaune protégée par une plaque de verre. »

### `images/codex-chez-odile.webp`

- **Notice** : Chez Odile (lieu)
- **Sujet** : la salle, les tables poussées, la patronne au comptoir.
- **Prompt** : bible visuelle + intérieur nuit d'un couscous populaire de la
  rue Saint-Denis : trois tables poussées bout à bout, sets en papier, plats de
  semoule fumants, carafes ; au comptoir, une patronne âgée essuie un verre en
  jaugeant la salle ; vitrine embuée sur la rue éclairée ; dorures modestes,
  bleu nuit dehors, chaleur cuivrée dedans.
- **Alt de référence** : « Salle d'un petit restaurant de couscous la nuit : tables poussées bout à bout, sets en papier, plats fumants, et une patronne âgée qui observe depuis le comptoir. »

### `images/codex-le-palais-brongniart.webp`

- **Notice** : Le palais Brongniart (lieu)
- **Sujet** : la colonnade au crépuscule, un soir de conférence.
- **Prompt** : bible visuelle + vue frontale légèrement décadrée du palais
  Brongniart au crépuscule : colonnade corinthienne monumentale, parvis où se
  croisent des silhouettes à badges, oriflammes unies sans aucun texte entre
  les colonnes ; ciel cuivre et bleu nuit, pierre gris-bleu, longues ombres.
- **Alt de référence** : « La colonnade du palais Brongniart au crépuscule, parvis animé de participants à une conférence, bannières sans texte entre les colonnes. »

### `images/codex-l-hotel-de-vaudreuil.webp`

- **Notice** : L'hôtel de Vaudreuil (lieu)
- **Sujet** : la cour, le jardin et l'orangerie au couchant.
- **Prompt** : bible visuelle + vue depuis le porche d'une cour pavée d'hôtel
  particulier du dix-septième siècle : façade de pierre blonde, hautes
  fenêtres, jardin débordant à droite, et au fond une orangerie du
  dix-huitième aux verrières dorées par le couchant ; grille en fer forgé
  entrouverte au premier plan ; ivoire et cuivre sur bleu d'ombre.
- **Alt de référence** : « Cour pavée d'un hôtel particulier du Marais en fin de journée, orangerie vitrée au fond du jardin, grille entrouverte au premier plan. »

### `images/codex-la-clause-du-meilleur-ennemi.webp`

- **Notice** : La clause du meilleur ennemi (document)
- **Sujet** : la nappe elle-même, en nature morte.
- **Prompt** : bible visuelle + nature morte en plongée : un set de table en
  papier jauni, plié en quatre puis déplié sur une nappe, couvert de lignes
  manuscrites numérotées **volontairement illisibles** (écriture suggérée,
  aucun mot déchiffrable — c'est l'exception d'écriture prévue par les
  contraintes, elle reste non lisible) ; deux signatures d'encres différentes,
  une croix et un cœur dans l'angle, une tache de thé ; à côté, un verre à thé
  et un stylo plume ; lumière chaude rasante, papier ivoire, encre bleu nuit.
- **Alt de référence** : « Sur une nappe de restaurant, un set de table en papier jauni couvert d'articles manuscrits illisibles, avec deux signatures, une croix et un cœur, une tache de thé dans l'angle. »

## Récapitulatif

| Fichier | Statut |
|---|---|
| `couvertures/la-clause-du-meilleur-ennemi.webp` | à produire |
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
| `images/codex-octave-brossard.webp` | à produire |
| `images/codex-salome-vidal.webp` | à produire |
| `images/codex-anselme-rueff.webp` | à produire |
| `images/codex-marguerite-lin.webp` | à produire |
| `images/codex-la-verriere.webp` | à produire |
| `images/codex-chez-odile.webp` | à produire |
| `images/codex-le-palais-brongniart.webp` | à produire |
| `images/codex-l-hotel-de-vaudreuil.webp` | à produire |
| `images/codex-la-clause-du-meilleur-ennemi.webp` | à produire |
