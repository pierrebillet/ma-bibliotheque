# Illustrations de « La Part du vent »

Manifeste pour l’agent illustrateur — atelier `roman-atelier v9`.
Concours heroic fantasy YA — septembre 2026.

## Ta mission

Produire les **21 fichiers** listés ici : une couverture, douze images de chapitre et huit images de notice. Les chemins intérieurs sont relatifs à `livres/la-part-du-vent/` ; la couverture est à la racine du dépôt. Le roman et ses champs sont achevés. Ce document suffit à exécuter la passe : aucune lecture du récit n’est nécessaire.

**Règles impératives** :

1. Travailler sur `atelier/roman-la-part-du-vent`, pousser sur cette branche, jamais sur `main`.
2. Ne créer que les fichiers listés. Ne modifier ni texte, ni îlot JSON, ni métadonnées éditoriales, ni ce manifeste. Seule exception : dans le `<head>` de `livres/la-part-du-vent/index.html`, compléter `book:author`, actuellement `gpt-6-astra (texte)`, par `, <nom exact de ton modèle> (images)`. Ne pas modifier `meta.author` dans l’îlot : cette limitation est celle du protocole de relai.
3. Ne jamais toucher `catalog.json` ni le bloc `#demo-catalog` de l’accueil. Aucune ressource distante dans le livre.
4. Commits en français, par lots cohérents, sur cette même branche ; ne pas créer une édition dérivée. Utiliser l’identité de commit Pierre <billet.pierre@gmail.com> et tracer honnêtement l’assistance du modèle dans un trailer `Assisted-by`.
5. Pousser les commits, puis signaler la passe dans la PR existante, en indiquant modèle, générateur d’images et écarts éventuels. Ne pas merger.

**Contraintes techniques** :

- Toutes les images sont en **WebP**. Chapitres et notices : **1600×900**, **≤ 150 Ko** chacun. Couverture : **800×1200**, ratio **2:3**, **< 300 Ko**.
- Aucun texte dans aucune image : ni titre, sous-titre, crédit, nom, chiffre, logo, signature, filigrane, pseudo-texte. Les cartes, plans et documents restent des tracés muets. Le titre de couverture est ajouté par l’interface.
- Générer une illustration cohérente par entrée, puis ajuster le cadrage et compresser. Ne jamais réduire la lisibilité du sujet pour remplir le cadre. Exemple de conversion pour une image intérieure réellement listée :

```bash
cwebp -q 82 -resize 1600 900 source.png -o livres/la-part-du-vent/images/chapter-01.webp
```

- Vérifier dimensions, poids, lisibilité, identités et correspondance aux alt avant de pousser. Ne pas changer l’îlot pour accommoder une image qui s’en écarte.
- Vérifications finales depuis la racine :

```bash
python livres/_template/outils/verifier.py livres/la-part-du-vent
python scripts/build_catalog.py --output /tmp/catalog-verification.json
```

## Bible visuelle commune

Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte.

### Personnages récurrents

- **Aubine** : 17 ans, silhouette mince et nerveuse, peau brune chaude, cheveux châtain foncé en une tresse simple, manteau rouille rapiécé à deux tons, tunique écrue, tablier bleu grisé, chaussures brunes usées. Aucun bijou, aucune arme. Mains valides, sans mutilation visible : la perte magique est une perte de savoir gestuel, jamais une amputation.
- **Mado** : 43 ans, mère d’Aubine, peau brune chaude, visage large, cheveux noirs ondulés attachés bas, manches écrues retroussées, jupe vert mousse et tablier beige, mains de travailleuse. Présence ferme et attentive.
- **Sabine** : 55 ans, grande et large d’épaules, peau claire hâlée, cheveux gris courts et bouclés, manteau de travail olive à grandes poches, deux crayons de bois aux oreilles, pantalon brun, bottes solides. Sans chapeau ni arme ; sacoche d’outils en cuir sombre.
- **Colas** : 19 ans, peau brune cuivrée, cheveux noirs courts, épaules solides, visage encore juvénile, veste bleu pétrole sur chemise écrue, pantalon brun, chaussures cousues au fil de voile. Après le chapitre 8 : chemise prêtée beige aux manches trop courtes, pantalon brun prêté. Aucun chapeau.
- **Bertille** : 18 ans, peau olive claire, courtes boucles noires aux tempes, manteau bleu moyen avec capuche, bottes brunes, sacoche blanche en bandoulière, petite planche à écrire. La sangle peut être serrée par une pince de bois à partir du chapitre 3, absente à la fin du 5 et au 6, remise au 7. Aucun insigne textuel.
- **Orane** : 46 ans, peau claire hâlée, visage long et ferme, cheveux bruns mêlés de gris coupés au menton, manteau gris avec une simple agrafe de cuivre, manches retroussées. Aucun diadème, aucune robe royale, aucune armure ; posture de responsable de chantier.

### Lieux, objets et continuité

- **Rivebasse et lavoir** : maisons modestes de pierre claire au bord de l’eau, linge sur perches et cordes, dalles et bassins de lavage. La chambre de Mado et d’Aubine est juste au-dessus. Avant le chapitre 8, lavoir entier ; au chapitre 12, lavoir neuf plus court, marque d’eau sous la fenêtre. Ne pas montrer la destruction dans un bandeau antérieur à sa révélation.
- **Maison des mesures** : bâtiment administratif sobre en pierre, tables encombrées de plans et poids, marmite et bols. Aucun palais. La chambre des mesures aux moulins est une annexe située au-dessus d’engrenages, avec un flotteur et une règle muette.
- **Vallée** : roche crayeuse claire, rivière encaissée, terrasses cultivées, ponts et passerelles de bois ; le lac est en amont de la ville haute, Rivebasse plus bas. Les moulins sont dans une gorge latérale ; l’ancien chenal traverse leur gorge vers les Fosses. Pas de château ni montagne enneigée ajoutés par réflexe.
- **Vergers** : poiriers sur étroites terrasses, branches dans le vide et filets de fibres sous les fruits. Les veilleuses sont de minuscules insectes vert lumineux qui éclairent de l’intérieur les poires percées ; pas de fées humanoïdes. Seules les scènes expressément nocturnes peuvent les montrer lumineuses.
- **Fosses** : carrières en gradins devenues bassins verts, escaliers noyés, potagers sur limon, petites maisons au-dessus de l’eau.
- **Forge des Échos** : atelier abandonné de pierre, toit incomplet, four froid, ancien canal à roue envahi d’herbes, outillage conservé dans la graisse et la toile. Gobelet rempli de terre avec une petite fleur blanche sur l’établi. Le bruit est une barre suspendue, pas un occupant caché.
- **Retenue et vanne** : barrage artisanal imposant entre deux falaises, arches de pierre claire, grosses poutres et liaisons de terre cuite ; petite cour de travail, chambre de vanne étroite, grand axe horizontal en fer, battant de bois épais et treuil à barres. Aucun mécanisme moderne, aucune vapeur industrielle.
- **Étrier** : lourd U de fer forgé, pieds recourbés adaptés à des logements de pierre ; manutention sur perches et sangles. Outil de réparation, pas une arme. Il porte provisoirement l’axe pendant le remplacement de ses appuis.
- **Semelles mobiles** : pièces de bois dur au dos arrondi, placées sous l’axe, capables de rouler très légèrement sans le laisser tomber. Le modèle de forge tient sur un tonneau. Ne pas représenter la pince comme une pince géante qui retient le barrage.
- **Pinces** : chacune taillée d’un seul morceau de frêne blond, tête épaisse et deux longues mâchoires séparées par une fente. Aucun ressort métallique. Aubine en transporte trois ; la première pince de lavoir est cassée d’un côté.
- **Tenues** : anneaux de céramique ocre ou jaune qui immobilisent deux pièces en contact. Une fissure est une fissure matérielle, pas une aura maléfique. Le don fait perdre un geste précis et ne laisse aucune mutilation visible ; jamais de main absente ou de doigts blessés pour le symboliser.
- **Barque de Colas** : petite barque de travail en bois, voile sobre, bordages réparés. Aucune inscription : plaque retournée jusqu’à la révélation du chapitre 8, de toute manière aucun lettrage dans les images.

### Application des prompts

Chaque prompt ci-dessous contient le socle stylistique et la scène issue de `visualDescription`. Y appliquer les identités et lieux définis ci-dessus, sans varier les visages entre les images. Les bandeaux précèdent la lecture : les interdits de divulgâchage de chaque entrée sont impératifs. Les alt sont déjà fixés dans l’îlot ; ils doivent rester identiques.

## Couverture

- **Fichier** : `couvertures/la-part-du-vent.webp` — 800×1200, < 300 Ko.
- **Sujet** : Aubine et sa pince devant les passages de la vallée.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Composition verticale 2:3. Aubine de trois quarts dos au premier plan, manteau rouille, main ouverte tenant une simple pince de frêne à deux mâchoires. Devant elle, vallée inventée de roche claire, ponts de bois suspendus, eau bleue et filets des vergers au loin. Vent visible dans son manteau et un drap sur une corde latérale. Grandes masses lumineuses sobres dans le tiers supérieur, image seule sans titre ni aucun signe. Aucun barrage brisé, aucune blessure, aucune couronne, aucune arme.
- **Alt de référence** : « Aubine, un manteau couleur de rouille sur les épaules, tient une pince de bois devant des ponts suspendus au-dessus d’une vallée lumineuse. »

## Images de chapitre

### `images/chapter-01.webp`

- **Chapitre** : 1 — Le linge qui reste.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Un drap gonflé de vent claque au bord d’un lavoir de pierre au-dessus d’une rivière en crue.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan large horizontal, hauteur humaine depuis les dalles du lavoir. Aubine de trois quarts, au bord gauche, retient un grand drap écru qui se gonfle vers la rivière ; perches, cordes et pinces de frêne au premier plan. Mado est près d’une perche derrière elle. Matin clair après pluie, eau brune vive, maisons modestes étagées. Aucun enfant en danger visible : instant qui précède le sauvetage, sans en montrer l’issue.
- **Alt de référence** : « Un drap gonflé de vent claque au bord d’un lavoir de pierre au-dessus d’une rivière en crue. »

### `images/chapter-02.webp`

- **Chapitre** : 2 — Une place sur la charrette.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Aubine et Sabine attendent devant une porte ouverte de la Maison des mesures, des feuilles et une pince à la main.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan moyen dans un corridor de pierre claire, Aubine tenant une pince cassée et Sabine portant un dessin roulé aux traits indéchiffrables. À travers la porte ouverte, une table chargée de cartes muettes et une marmite plus loin. Matin doux, lumière latérale, gestes d’attente ; aucune scène de confrontation et aucun texte dans les papiers.
- **Alt de référence** : « Aubine et Sabine attendent devant une porte ouverte de la Maison des mesures, des feuilles et une pince à la main. »

### `images/chapter-03.webp`

- **Chapitre** : 3 — Les fruits de la nuit.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Des poiriers débordent de terrasses de pierre au-dessus de filets tendus dans le vide.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Vue panoramique des vergers suspendus au couchant, branches de poiriers chargées de fruits vert doré dépassant des terrasses très étroites, grands filets en fibres tendus dessous. Aubine, Sabine et Bertille petites silhouettes avec paniers vides sur le dos le long du chemin ; Colas absent car il mène la barque. Fleuve loin en bas, lumière dorée, profondeur lisible. Pas de pont en ruine, pas de sacrifice ; montrer l’approche du verger.
- **Alt de référence** : « Des poiriers débordent de terrasses de pierre au-dessus de filets tendus dans le vide. »

### `images/chapter-04.webp`

- **Chapitre** : 4 — Le fond des choses.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Une barque de bois longe les marches noyées d’anciennes carrières bordées de jardins.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan large horizontal sur les Fosses, anciennes carrières à gradins de craie, bassins verts et escaliers noyés, maisons sur les marches hautes, potagers et céréales attachées par poignées. Colas pousse sa barque au premier plan, Aubine tient un cordage, Sabine et Bertille assises à bord. Après-midi chaud, eau calme dans les bassins, aucune avarie. La plaque de nom du bateau est retournée, aucun lettrage.
- **Alt de référence** : « Une barque de bois longe les marches noyées d’anciennes carrières bordées de jardins. »

### `images/chapter-05.webp`

- **Chapitre** : 5 — La chambre des mesures.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Cinq grandes roues de moulin occupent une gorge étroite sous des greniers de bois.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Vue au pied des moulins de la ville haute, cinq roues à aubes successives dans une entaille de roche, bâtiments de pierre claire et greniers en bois au-dessus d’un passage muré. Aubine et ses trois compagnons arrivent à pied ; leurs visages ne montrent aucune dispute. Aube pâle, poussière de farine et eau scintillante. Ne pas représenter les démolitions futures ni le cahier ouvert de Bertille.
- **Alt de référence** : « Cinq grandes roues de moulin occupent une gorge étroite sous des greniers de bois. »

### `images/chapter-06.webp`

- **Chapitre** : 6 — Ce qui porte encore.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Une lumière de jour colore les cristaux d’une voûte où trois voyageuses se tiennent en silence.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Vue intérieure large du chenal sec, sol sableux et voûte basse couverte de cristaux fins portant des gouttes. Lumière du jour entrant par une brèche latérale, reflets délicats bleus et roses, pas de lumière artificielle surnaturelle. Aubine de profil lève la main ; Sabine debout observe le plafond ; Bertille accroupie tient une lampe éteinte. Colas absent, dehors avec les sacs. Pas d’éboulement montré, atmosphère d’émerveillement tranquille.
- **Alt de référence** : « Une lumière de jour colore les cristaux d’une voûte où trois voyageuses se tiennent en silence. »

### `images/chapter-07.webp`

- **Chapitre** : 7 — Le fer au soleil.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Dans une forge vide, une petite fleur pousse dans un gobelet posé sur l’établi.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan rapproché large de l’établi d’une forge abandonnée, gobelet d’argile rempli de terre avec une petite fleur blanche. Au second plan, Sabine à la porte arrête une barre pendue à une chaîne ; Aubine et Bertille restent sur le seuil, Colas derrière. Toit incomplet, vieux four froid, outils sombres, soleil d’après-midi. Ne pas montrer l’étrier encore recherché, ni des flammes ni un forgeron vivant.
- **Alt de référence** : « Dans une forge vide, une petite fleur pousse dans un gobelet posé sur l’établi. »

### `images/chapter-08.webp`

- **Chapitre** : 8 — Les lumières sur la rive.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Quatre silhouettes portent un étrier de fer sur des perches au-dessus de moulins éclairés dans la nuit.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan large depuis le chemin de crête, de nuit bleue, Aubine, Sabine, Bertille et Colas portent ensemble un lourd U de fer à pieds recourbés suspendu à quatre perches par des sangles. En contrebas, moulins encore entiers, lanternes et silhouettes de porteurs de sacs. Eau agitée mais pas de bateau détruit ni de lavoir ruiné visible : image d’arrivée avant la révélation des pertes. Colas porte encore sa veste bleu pétrole.
- **Alt de référence** : « Quatre silhouettes portent un étrier de fer sur des perches au-dessus de moulins éclairés dans la nuit. »

### `images/chapter-09.webp`

- **Chapitre** : 9 — Les mains disponibles.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Des habitants entourent Aubine près d’un tonneau portant un petit modèle d’appui en bois.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan moyen élargi à hauteur des gens dans la cour de la retenue au petit matin. Sur un tonneau, modèle mécanique muet : axe sur deux petites semelles au dos arrondi et une semelle fendue. Aubine montre le contact entre bois et axe. Autour, personnes de métiers avec pelles et perches, Mado avec une marmite en arrière-plan, Bertille et Orane de côté, Sabine et Colas près d’un établi. Colas porte les habits prêtés. Pas de geste magique ni d’anneau lumineux.
- **Alt de référence** : « Des habitants entourent Aubine près d’un tonneau portant un petit modèle d’appui en bois. »

### `images/chapter-10.webp`

- **Chapitre** : 10 — La part du vent.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Dans une chambre étroite sous la vanne, Aubine tient une lampe pendant que Sabine examine un appui.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Composition horizontale intérieure, vue oblique hors de la trajectoire de l’axe. Un fort étrier de fer porte l’axe de la vanne entre deux murs de pierre. Sabine mesure un logement, Colas tient un levier et Aubine éclaire avec une lampe à huile. Une petite pince maintient un dessin illisible sur une planche. Eau suintante, tons bleu sombre et ambre, gestes précis. Aucun sacrifice en cours, aucune couture offerte, aucun anneau brisé : début du chantier de ce chapitre.
- **Alt de référence** : « Dans une chambre étroite sous la vanne, Aubine tient une lampe pendant que Sabine examine un appui. »

### `images/chapter-11.webp`

- **Chapitre** : 11 — Ce que tient une épaule.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Six ouvriers attendent près des barres d’un treuil devant la vanne encore fermée.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan large depuis la cour de la retenue, treuil de bois et de fer au premier plan avec six ouvriers anonymes, Sabine leur fait signe d’attendre, Aubine porte une lampe basse et Colas est près des outils. La grande vanne est encore fermée, lac lumineux aperçu derrière les arches, air chargé d’humidité. Orane et Bertille sont au poste de signal au second plan. Aucun grenier détruit, aucune eau triomphante : ne pas anticiper l’issue du chapitre.
- **Alt de référence** : « Six ouvriers attendent près des barres d’un treuil devant la vanne encore fermée. »

### `images/chapter-12.webp`

- **Chapitre** : 12 — Le linge du lendemain.
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Du linge sèche sur les cordes d’un lavoir reconstruit, à côté d’une chambre dont le mur garde une marque d’eau.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Plan large horizontal d’un lavoir modeste neuf, plus court que ses anciennes fondations visibles. Aubine fixe un mouchoir sur une corde ; Mado se tient à la fenêtre au-dessus, cuillère à la main. Quelques enfants passent à distance, aucun danger. Marque d’eau sous la fenêtre, bois neuf blond, matin lumineux, draps avec du mou entre les pinces et vent doux. Aucune foule de célébration, aucune restauration fastueuse.
- **Alt de référence** : « Du linge sèche sur les cordes d’un lavoir reconstruit, à côté d’une chambre dont le mur garde une marque d’eau. »

## Images de notices

### `images/codex-aubine.webp`

- **Notice** : Aubine (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Aubine examine une toile tendue sur un petit cadre près d’une fenêtre.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation, horizontal, Aubine à sa table près d’une fenêtre de Rivebasse, examinant à contre-jour une toile sur un cadre de reprise. Aiguille et fil dans les mains, boîte de boutons et tablier rapiécé visibles. Matin calme ; scène d’avant le voyage, son métier est pleinement maîtrisé. Aucun anneau de magie.
- **Alt de référence** : « Aubine examine une toile tendue sur un petit cadre près d’une fenêtre. »

### `images/codex-mado.webp`

- **Notice** : Mado (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Mado replie une pâte à pain sur une table de bois dans une petite cuisine.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation, horizontal, Mado debout dans sa cuisine de Rivebasse, rabattant les côtés d’une pâte ovale. Panier de linge et cuillère en bois en arrière-plan, manches retroussées, lumière chaude du four latéral. Pas de pain tressé : elle plie, mains normales sans blessure.
- **Alt de référence** : « Mado replie une pâte à pain sur une table de bois dans une petite cuisine. »

### `images/codex-colas.webp`

- **Notice** : Colas (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Colas répare une planche sur le bord de sa barque amarrée à un quai.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation horizontal de Colas près de sa barque intacte à Rivebasse, veste bleu pétrole, un genou posé sur le bordage et un outil de bois en main. Fil de voile et copeaux visibles ; eau calme, fin de matinée. Plaque de nom retournée et illisible, aucune avarie grave, aucune allusion à sa perte future.
- **Alt de référence** : « Colas répare une planche sur le bord de sa barque amarrée à un quai. »

### `images/codex-bertille.webp`

- **Notice** : Bertille (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Bertille écrit sur une petite planche tenue contre son avant-bras, sa sacoche blanche à l’épaule.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation horizontal de Bertille sur une marche de pierre sèche à Rivebasse, écrivant avec une pointe sombre sur une feuille sans caractères lisibles posée sur son avant-bras. Capuche rabattue révélant les courtes boucles noires, sacoche blanche, regard attentif vers une personne hors champ. Pas de pince sur la sangle à ce stade, aucune surveillance cachée ni présence d’Orane.
- **Alt de référence** : « Bertille écrit sur une petite planche tenue contre son avant-bras, sa sacoche blanche à l’épaule. »

### `images/codex-orane.webp`

- **Notice** : Orane, prévôte (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Orane se tient devant une table chargée de cartes muettes, un bol placé entre deux rouleaux.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation horizontal d’Orane à la Maison des mesures, debout manches roulées, agrafe de cuivre et manteau gris, cartes sans noms ni chiffres, quelques cailloux blancs et un rouge comme poids. Bol de soupe dans un espace libre, lumière de fenêtre. Autorité attentive, aucun trône et aucune scène de condamnation.
- **Alt de référence** : « Orane se tient devant une table chargée de cartes muettes, un bol placé entre deux rouleaux. »

### `images/codex-sabine.webp`

- **Notice** : Sabine (personnage).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Sabine ajuste une porte de bois, des outils et de petites cales rangés à ses pieds.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Portrait en situation horizontal de Sabine devant une porte ordinaire de Rivebasse, testant son jeu avec une cale, ses deux crayons aux oreilles et ses poches lourdes de fragments. Pierre claire, lumière douce oblique. Aucun pont condamné, aucun anneau cassé comme symbole de faute : portrait contemporain de sa présentation.
- **Alt de référence** : « Sabine ajuste une porte de bois, des outils et de petites cales rangés à ses pieds. »

### `images/codex-vergers.webp`

- **Notice** : Les vergers suspendus (lieu).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Des filets recueillent les poires sous des arbres poussant sur d’étroites terrasses de pierre.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Vue large des vergers suspendus en journée, centrée sur leur fonctionnement : poiriers penchés, filets attachés à des perches, cueilleuse anonyme ramenant les fruits à l’aide d’une longue perche. Fleuve très en dessous, clair et calme. Ni veilleuses lumineuses ni personnages principaux : notice ouverte avant la scène nocturne.
- **Alt de référence** : « Des filets recueillent les poires sous des arbres poussant sur d’étroites terrasses de pierre. »

### `images/codex-forge.webp`

- **Notice** : La Forge des Échos (lieu).
- **Dimensions et poids** : 1600×900, ≤ 150 Ko.
- **Sujet** : Une forge abandonnée conserve son four froid, son établi et des outils protégés sous de la toile.
- **Prompt** : Gouache narrative lumineuse sur papier légèrement grainé, formes lisibles et coups de pinceau visibles, proportions humaines naturelles, détails choisis des matières ; aucun photoréalisme, aucune esthétique de jeu vidéo. Palette craie chaude, bleu d’eau, vert de poire, rouille et bois blond. Monde secondaire préindustriel de métiers, sans emprunt à une franchise. Lumière naturelle, aucune aura héroïque. Aucun texte, chiffre, logo, signature, filigrane ou pseudo-texte. Vue large intérieure de la Forge des Échos au soleil, sans personnage. Four éteint, rigole visible au seuil avec des herbes, établi, masses d’essai et outils protégés par des linges gras. Fleur dans le gobelet discrète sur l’établi. Le lieu est vide, sans fumée ; aucun trésor ni arme. La conservation des outils est le sujet.
- **Alt de référence** : « Une forge abandonnée conserve son four froid, son établi et des outils protégés sous de la toile. »

## Récapitulatif

**21 fichiers exactement** : 1 couverture + 12 chapitres + 8 notices (sur 24). Aucun fichier produit pendant la passe auteur.

| Fichier | Statut |
|---|---|
| `couvertures/la-part-du-vent.webp` | à produire |
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
| `images/codex-aubine.webp` | à produire |
| `images/codex-mado.webp` | à produire |
| `images/codex-colas.webp` | à produire |
| `images/codex-bertille.webp` | à produire |
| `images/codex-orane.webp` | à produire |
| `images/codex-sabine.webp` | à produire |
| `images/codex-vergers.webp` | à produire |
| `images/codex-forge.webp` | à produire |
