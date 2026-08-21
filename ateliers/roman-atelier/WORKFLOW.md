# Atelier roman-atelier — écrire un roman-web illustré avec la liseuse « Atelier »

- **Version** : 9
- **Statut** : stable (l'étape illustrations et le relai illustrateur ont eu
  leur pilote — `livres/la-clause-du-meilleur-ennemi/`, v3, deux passes
  tracées ; l'étape de recherche documentaire, nouvelle en v4, et les modules
  de lecture, nouveaux en v7, attendent encore le leur — roadmap Conception)
- **Livrable** : un roman-web HTML autonome **illustré nativement** (récit +
  liseuse intégrée : sommaire, barre de progression, codex à déverrouillage,
  illustrations de chapitres et de notices, thème sombre, réglage de taille de
  police, impression propre), visible au catalogue après merge sans aucune
  intervention manuelle. Sur demande du brief, le livre peut porter une
  **carte des lieux** et un **graphe de relations** à révélation progressive
  (étape 3 bis) — deux modules du moteur, sans divergence à justifier.
  Si le brief le demande, le récit est **ancré dans le monde réel** (personnage
  historique, lieux réels, jargon d'un métier), sur la base d'un dossier
  documentaire sourcé constitué avant l'écriture (étape 0).
- **Moteur** : [`livres/_template/`](../../livres/_template/README.md)
  (`atelier-liseuse v3`) — le moteur se copie depuis le template, plus jamais
  depuis le dernier livre publié.
- **Tronc commun** : [`ateliers/TRONC-COMMUN.md`](../TRONC-COMMUN.md) — les
  conventions communes des ateliers du moteur « Atelier » ; il fait partie de
  la recette.
- **Exemples publiés** : [`livres/lequation-du-calme/`](../../livres/lequation-du-calme)
  et [`livres/la-doublure.html`](../../livres/la-doublure.html) (v2, non
  illustrés) ;
  [`livres/la-clause-du-meilleur-ennemi/`](../../livres/la-clause-du-meilleur-ennemi)
  (v3, illustré en deux passes).
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md) — le lire
  avant l'étape 1, il fait partie de la recette.

## Changelog

- **v9** (2026-08) — **dédoublonnage et quantités libres** : les conventions
  communes aux ateliers du moteur « Atelier » (mise en place, structure de
  fichiers, `<head>`, vocabulaires fermés, moteur, images générées,
  vérification, interdits) sont extraites vers
  [`TRONC-COMMUN.md`](../TRONC-COMMUN.md), que cette recette référence au lieu
  de les recopier ; le vérificateur déménage en
  [`livres/_template/outils/`](../../livres/_template/outils/verifier.py), à
  côté du moteur qu'il contrôle. Application du socle validé (chantier 3) :
  les **quantités sont libres** par défaut — chapitres et notices se
  dimensionnent à la pertinence, le brief peut les fixer. Motif : chantiers
  actés par Pierre (session Conception du 2026-08-21), audit
  [`2026-08-regard-auteur.md`](../../docs/audits/2026-08-regard-auteur.md).
- **v8** (2026-08) — **regard d'auteur** sur la recette (audit
  [`docs/audits/2026-08-regard-auteur.md`](../../docs/audits/2026-08-regard-auteur.md)) :
  l'étape 1 gagne l'**épreuve du plan** (une bascule par chapitre, synopsis
  relu en éditeur sceptique, point de vue et temps du récit fixés) ; l'étape 2
  autorise l'**écart au plan** à condition de le resynchroniser dans le même
  commit ; l'étape 5 se scinde en **5a — révision structurelle** puis **5b —
  passe ligne à ligne**, chacune avec son commit. La recette applique la
  nouvelle entrée « Style et voix » du socle. Mises à jour de cohérence :
  exemples publiés (le pilote v3 `la-clause-du-meilleur-ennemi` existait sans
  être enregistré), mentions « v6 » résiduelles, version du gabarit de
  manifeste. Motif : demande de Pierre (session Conception du 2026-08-21) —
  critique des workflows d'écriture dans l'esprit d'un auteur expérimenté.
- **v7** (2026-08) — **modules de lecture optionnels** : le moteur
  (`atelier-liseuse v3`) sait afficher une carte des lieux et un graphe de
  relations à révélation progressive, ainsi qu'imprimer proprement la vue
  affichée. Nouvelle section « Modules de lecture » du [`BRIEF.md`](BRIEF.md) et
  nouvelle **étape 3 bis**, conditionnelle, qui remplit les îlots `map` et
  `relations` depuis le codex déjà écrit. Ces trois fonctionnalités ne sont plus
  des « divergences de moteur » à justifier dans la PR : elles font partie de la
  recette. Motif : chantier 4 de la [roadmap
  Conception](../../docs/conception/ROADMAP.md) — réintroduire les
  fonctionnalités régressées par la standardisation (audit §B.3) sans revenir
  aux moteurs faits main.
- **v6** (2026-08) — schéma de catalogue v2 : le `<head>` porte cinq
  **metas qualitatives à vocabulaire fermé** (`book:genre`, `book:format`,
  `book:tonalite`, `book:exigence`, `book:audience`), plus `book:variant-of`
  pour les seules éditions dérivées ; `book:workflow`, jusqu'ici purement
  documentaire, est désormais **lue par le générateur** qui en dérive la
  `nature` du livre (l'atelier n'a donc rien à déclarer de plus pour être rangé
  du côté des fictions). Le vérificateur exige les onze metas et contrôle les
  vocabulaires. Motif : chantier 5 de la [roadmap
  Bibliothèque](../../docs/bibliotheque/ROADMAP.md) — donner à l'index de quoi
  trier et filtrer sans faire porter cette charge aux tags libres.
- **v5** (2026-08) — couverture strictement sans texte : le titre et les
  métadonnées sont déjà superposés en HTML dans la bibliothèque. Le manifeste,
  les contraintes d'images et la vérification finale interdisent désormais
  aussi logos, signatures, filigranes et pseudo-texte, sans exception pour la
  couverture. Motif : éviter les doublons et conflits de lisibilité observés
  sur plusieurs couvertures publiées.
- **v4** (2026-08) — ancrage dans le réel sur option du brief : nouvelle
  section « Ancrage réel » du [`BRIEF.md`](BRIEF.md) et nouvelle **étape 0 —
  Recherche documentaire**, conditionnelle, qui constitue un dossier sourcé
  (`livres/<slug>/recherche.md`) avant toute écriture — recherche menée par
  l'agent lui-même (parallélisée par sub-agents s'il en est capable) ou, sur
  demande du brief, déléguée par copier-coller à un assistant externe via
  Pierre. La relecture (étape 5) gagne une passe de vérification factuelle
  livre ↔ dossier. Motif : demande de Pierre (session Conception du
  2026-08-13, chantier 7 de la roadmap Conception) — vraisemblance des récits
  qui empruntent au monde réel (perspective d'un personnage historique, jargon
  d'un métier, lieux réels).
- **v3** (2026-08) — le livre naît illustré, en deux passes tracées : entrée
  formalisée par un brief ([`BRIEF.md`](BRIEF.md)) ; moteur copié depuis
  `livres/_template/` (chantier n° 2 de la roadmap Conception — les trois
  défauts connus du moteur y sont corrigés) ; structure de l'îlot JSON
  spécifiée ([`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md))
  au lieu d'être « observable dans les livres de référence » ; nouvelle étape 4
  « Illustrations » avec manifeste committé (`livres/<slug>/illustrations.md`)
  et relai vers un agent illustrateur ; vérifications outillées
  ([`verifier.py`](../../livres/_template/outils/verifier.py), alors dans
  `roman-atelier/outils/`) ; images en WebP. Motif : les
  éditions illustrées d'août ont été produites hors processus et sans
  traçabilité (audit §B.7) ; la v3 fait de l'illustration une étape de la
  recette au lieu d'une dérive.
- **v2** (2026-08) — mise au standard de recette
  ([`creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md) §3) : étapes
  au format entrée/travail/sortie/critère de fin/commit, traçabilité
  `book:workflow`, exigences transverses déplacées vers `PREFERENCES.md`.
- **v1** (2026-08) — première formalisation de la pratique observée sur les livres
  d'août (PR #5).

## Les deux rôles de la fabrication

Un livre de cet atelier se fabrique en **deux passes, sur la même branche** :

1. **L'auteur** (étapes 0 à 5b ; l'étape 0 seulement si le brief demande
   l'ancrage réel) écrit le livre complet — texte, codex, champs
   d'images déjà renseignés dans l'îlot JSON — et committe le **manifeste
   d'illustrations** `livres/<slug>/illustrations.md`. À la fin de sa session,
   le livre est publiable : il se lit intégralement, les emplacements d'images
   se masquent proprement tant que les fichiers n'existent pas.
2. **L'illustrateur** (un autre agent, une autre session — voir §« Le relai
   illustrateur ») exécute le manifeste : il produit les fichiers d'images aux
   noms exacts, et rien d'autre. Aucune édition de l'îlot JSON n'est nécessaire
   ni autorisée de sa part.

Chaque rôle committe sous son nom ; `book:author` liste les deux modèles.

## Avant de commencer

Prérequis de lecture : [`/AGENTS.md`](../../AGENTS.md) (règles d'or + protocole de
session), ce workflow, le tronc commun des ateliers
([`TRONC-COMMUN.md`](../TRONC-COMMUN.md)),
[`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et
[`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md).
Rien d'autre n'est supposé connu.

1. **Recevoir le brief** : le message de lancement contient un
   [`BRIEF.md`](BRIEF.md) rempli. S'il manque, le demander ; s'il est
   incomplet, les défauts de `PREFERENCES.md` s'appliquent aux champs absents.
   Si le brief contient la section « Ancrage réel », l'étape 0 s'applique — en
   mode « recherche par l'agent » (le défaut), elle exige un accès de recherche
   web : s'il manque, le signaler avant de commencer et convenir du mode
   délégué.
2. **Mise en place** : suivre le §« Mise en place » du
   [tronc commun](../TRONC-COMMUN.md) — slug, copie du moteur depuis
   `livres/_template/`, branche `atelier/roman-<slug>`.

## Étapes de fabrication

### Étape 0 — Recherche documentaire (seulement si le brief demande l'ancrage réel)

Sans section « Ancrage réel » au brief, passer directement à l'étape 1.

- **Entrée** : la section « Ancrage réel » du brief (éléments réels à ancrer,
  degré d'ancrage, axes prioritaires, sources, mode de recherche).
- **Travail** : constituer le dossier documentaire du livre **avant toute
  écriture**, selon le mode fixé par le brief :
  - **Recherche par l'agent** (défaut) : mener les recherches soi-même. Si
    l'agent d'exécution sait paralléliser des recherches (sub-agents), répartir
    par axe — lieux, personnes et personnage historique, événements,
    vocabulaire et jargon du métier, contexte d'époque — sinon traiter les axes
    séquentiellement. Chaque fait notable est relié à sa source **datée** ;
    faits établis, débattus et incertains sont distingués.
  - **Recherche déléguée** (sur demande du brief, pour économiser le quota de
    l'agent) : rédiger dans `livres/<slug>/recherche.md` une section
    « Requêtes en attente » — une requête de recherche **autoportante et
    copiable-collable** par axe —, committer, puis **suspendre la fabrication**
    en demandant à Pierre de soumettre ces requêtes à l'assistant externe de
    son choix (Perplexity, ChatGPT ou autre) et de coller les réponses en
    retour : c'est le tour d'échange supplémentaire prévu par la recette. À
    réception, consolider le dossier au même standard que ci-dessus, en
    marquant la provenance de chaque fait (« réponse d'assistant externe
    fournie le <AAAA-MM-JJ> »), et vérifier sa cohérence interne.
- **Sortie** : `livres/<slug>/recherche.md` — un fait notable par entrée, avec
  sa source datée ; les axes demandés par le brief tous couverts.
- **Critère de fin** : chaque axe du brief a sa section dans le dossier ;
  chaque entrée porte une source datée ou la mention explicite de son
  incertitude ; plus aucune section « Requêtes en attente ».
- **Commit** : « Dossier documentaire de <titre> : recherches d'ancrage réel »
  (en mode délégué, un premier commit « Dossier documentaire de <titre> :
  requêtes en attente » précède la suspension).

### Étape 1 — Plan et synopsis

- **Entrée** : le brief rempli, le socle `PREFERENCES.md` (§Fond) ; si l'étape
  0 a eu lieu, le dossier `livres/<slug>/recherche.md`.
- **Travail** : poser l'univers avant d'écrire — synopsis, promesse émotionnelle,
  idée centrale, question thématique, liste des chapitres avec leur rôle
  narratif **et leur bascule** (ce qui a changé entre le début et la fin du
  chapitre), personnages et lieux principaux. Fixer le **point de vue** et le
  **temps du récit** (socle §« Style et voix ») — ils se tiennent ensuite sur
  tout le livre. Pour un livre ancré dans le réel, l'univers
  s'appuie sur le dossier documentaire (perspective du personnage historique,
  lieux réels, époque) ; ce que le récit invente par-dessus est un choix
  d'auteur, pas une erreur — mais il ne contredit pas un fait établi du dossier.
  Puis **éprouver le plan** avant d'écrire, en éditeur sceptique : un chapitre
  sans bascule se fusionne ou se supprime ; la promesse émotionnelle doit être
  tenable dans la longueur prévue ; la question thématique doit avoir une vraie
  réponse — même oblique — en fin de parcours. Corriger le plan maintenant
  coûte dix lignes ; le corriger à l'étape 5a coûte des chapitres.
- **Sortie** : `livres/<slug>/index.html` avec le `<head>` complet (tronc
  commun §« Le `<head>` obligatoire ») et l'îlot JSON amorcé — blocs `meta`, `world` et
  `cover` remplis, chapitres en squelette (ids, numéros, titres) ; le brief
  recopié tel quel en `livres/<slug>/brief.md` (traçabilité de l'entrée).
- **Critère de fin** : `python scripts/build_catalog.py --output
  /tmp/catalog-verification.json` passe et le slug apparaît dans le JSON généré.
- **Commit** : « Plan de <titre> : synopsis et structure »

### Étape 2 — Chapitres

- **Entrée** : le plan committé à l'étape 1.
- **Travail** : écrire les chapitres dans l'îlot JSON (blocs de texte), dans l'ordre
  du plan. Un lot cohérent de chapitres par commit. Longueurs : celles du
  brief s'il en fixe ; sinon **libres** — dimensionner à la pertinence (socle
  §« Quantités »), sans jamais écrire pour remplir.
  Pour un livre ancré dans le réel : jargon du métier, lieux, dates et gestes
  techniques viennent du dossier documentaire — toute affirmation ancrée doit
  y être traçable.
  Si le récit exige de **s'écarter du plan** (un personnage prend de la place,
  une bascule se déplace), l'écart est un choix d'auteur, pas une faute — à une
  condition : resynchroniser le plan (rôles et bascules des chapitres) et le
  bloc `world` **dans le même commit** que les chapitres concernés. Un écart
  non tracé est un défaut.
- **Sortie** : les `chapters[].blocks[]` de l'îlot remplis (les champs `image`
  attendront l'étape 4).
- **Critère de fin** : le livre s'ouvre en `file://`, chaque chapitre écrit
  s'affiche et la navigation fonctionne, aucune erreur JavaScript dans la
  console du navigateur.
- **Commit(s)** : « Chapitres 1-3 de <titre> », « Chapitres 4-6 de <titre> »…

### Étape 3 — Codex et annexes

- **Entrée** : les chapitres écrits.
- **Travail** : rédiger les notices du codex (personnages, lieux, concepts…)
  dans la voix de `meta.codexVoice`, avec **tous** les champs de la spécification
  ([`DONNEES.md`](../../livres/_template/DONNEES.md)) — y compris les champs de
  méthode anti-divulgâchage — puis relier les notices aux blocs par les
  `mentions`. Compléter `entityAudit` pour toute entité nommée sans notice.
  Nombre de notices : celui du brief s'il en fixe ; sinon **libre** — chaque
  notice mérite sa place (socle §« Quantités »). Viser l'exploration dense du
  socle (repère : ≥ 40 % des blocs porteurs d'au moins une mention — un
  plancher indicatif, pas un quota). Pour un livre ancré dans
  le réel, les notices qui décrivent des personnes, lieux ou faits réels
  s'appuient sur le dossier documentaire.
- **Sortie** : le `codex[]` de l'îlot rempli, `mentions` posées, `entityAudit`
  complet.
- **Critère de fin** :
  `python livres/_template/outils/verifier.py livres/<slug>` ne signale
  aucun défaut d'intégrité (0 notice orpheline, 0 lien mort, déverrouillages
  cohérents) — les manques d'images sont encore tolérés à ce stade (`--sans-images`).
- **Commit** : « Codex de <titre> : personnages, lieux, concepts »

### Étape 3 bis (optionnelle) — Modules de lecture : carte et graphe de relations

Seulement si le brief demande une carte, un graphe de relations, ou les deux
(section « Modules de lecture » du [`BRIEF.md`](BRIEF.md)). Sans demande : ne
rien faire, et **supprimer les blocs `map` et `relations`** hérités de l'îlot
d'exemple du template.

- **Entrée** : le codex écrit (étape 3) — les modules ne montrent que des
  entités qui ont déjà leur notice.
- **Travail** :
  1. **carte** (`map`) : dessiner un fond schématique en chemins SVG
     (`shapes[]`, quatre natures : `eau`, `terre`, `route`, `limite`) dans le
     repère `"0 0 100 72"`, puis placer les lieux (`places[]`) en reliant
     chacun à sa notice par `codexId`. Une carte sobre et juste vaut mieux
     qu'une carte détaillée : 4 à 12 lieux, un fond qui tient en quelques
     chemins. Aucune image de fond (le fond vit dans l'îlot, pas dans
     `images/`) ;
  2. **graphe de relations** (`relations`) : déclarer les entités (`nodes[]`,
     `codexId` d'une notice) et les liens (`links[]`) avec, pour chacun, une
     `nature` écrite dans la voix du codex (« Sœur cadette, tenue à distance »).
     Laisser les coordonnées vides suffit (disposition en cercle) ; les
     renseigner permet de composer une disposition parlante. Un lien qui est
     lui-même une révélation porte son `unlockBlock` ;
  3. déclarer les capacités : ajouter `carte` et/ou `relations` à
     `<meta name="book:capacites">` — le vérificateur en fait un défaut bloquant
     si le module est là sans sa capacité.
  Spécification champ par champ :
  [`DONNEES.md`](../../livres/_template/DONNEES.md) §`map` et §`relations`.
- **Sortie** : les blocs `map` et/ou `relations` de l'îlot, `book:capacites` à
  jour.
- **Critère de fin** :
  `python livres/_template/outils/verifier.py livres/<slug> --sans-images`
  ne signale aucun défaut ; à l'ouverture en `file://`, les boutons « Carte » et
  « Relations » apparaissent, un lecteur qui n'a rien lu ne voit **aucun nom de
  lieu ni d'entité**, et les éléments se révèlent bien au fil de la lecture.
- **Commit** : « Modules de lecture de <titre> : carte et relations »

### Étape 4 — Illustrations : champs d'images et manifeste

- **Entrée** : le livre écrit (chapitres + codex), la direction artistique du
  brief s'il y en a une.
- **Travail** :
  1. renseigner dans l'îlot les champs d'images (spec `DONNEES.md`) : pour
     **chaque chapitre**, `image` (`images/chapter-NN.webp`, NN = numéro sur
     2 chiffres), `alt` et `visualDescription` ; pour les **notices majeures**
     (par défaut : les mieux reliées, environ un tiers du codex — le brief peut
     fixer autre chose), `image` (`images/codex-<id>.webp`), `alt` et
     `visualDescription` ; et le bloc `cover` (couverture
     `../../couvertures/<slug>.webp`) ;
  2. écrire le manifeste `livres/<slug>/illustrations.md` en copiant le gabarit
     [`GABARIT-ILLUSTRATIONS.md`](GABARIT-ILLUSTRATIONS.md) : bible visuelle
     commune, une entrée par image (nom de fichier exact, dimensions, prompt,
     alt), contraintes techniques et consignes de session pour l'illustrateur.
- **Sortie** : l'îlot avec tous les champs d'images remplis +
  `livres/<slug>/illustrations.md`.
- **Critère de fin** : `python livres/_template/outils/verifier.py
  livres/<slug> --sans-images` passe (il vérifie notamment que chaque image de
  l'îlot a son entrée au manifeste et réciproquement) ; le livre reste
  entièrement lisible en `file://` alors qu'aucun fichier d'image n'existe
  encore (les emplacements se masquent, aucune image cassée à l'écran).
- **Commit** : « Illustrations de <titre> : champs d'images et manifeste »

### Étape 5a — Révision structurelle

La révision se fait en deux passes séparées : d'abord la structure (ici), puis
la phrase (étape 5b). Polir une phrase d'un passage qu'on va couper est du
travail perdu.

- **Entrée** : le livre complet (texte + champs d'images + manifeste).
- **Travail** : relecture intégrale **en éditeur**, au niveau du récit — pas
  encore de polissage de phrases : chaque chapitre a bien sa bascule (ce qui a
  changé entre son début et sa fin) ; le rythme alterne scènes et
  respirations ; l'incipit fait sa promesse dès la première page ; la chute
  paie la promesse émotionnelle et répond, même obliquement, à la question
  thématique du bloc `world`. Corriger par coupes, déplacements et réécritures
  de passages. Si l'étape 0 a eu lieu, passe de **vérification factuelle**
  livre ↔ dossier (chaque référence au réel du texte et du codex est traçable
  à une entrée sourcée de `recherche.md`).
- **Sortie** : le récit révisé (structure, rythme, fins de chapitres) ; le
  bloc `world` et le codex resynchronisés si la révision a déplacé des
  éléments.
- **Critère de fin** : plus aucune correction structurelle en attente ; si
  l'étape 0 a eu lieu, aucune affirmation ancrée introuvable au dossier ;
  `python livres/_template/outils/verifier.py livres/<slug>
  --sans-images` passe toujours sans défaut.
- **Commit** : « Révision de <titre> : structure et rythme »

### Étape 5b — Passe ligne à ligne et finitions

- **Entrée** : le récit révisé (étape 5a).
- **Travail** : passe ligne à ligne — prose (répétitions, tics de langage,
  adverbes superflus), dialogues, orthographe ; typographie française
  **uniforme** (apostrophe « ’ », guillemets à chevrons, tirets de dialogue —
  la convention choisie à l'étape 1, tenue partout) ; cohérence du point de
  vue et du temps du récit ; respect de `PREFERENCES.md` (dont §« Style et
  voix ») et du brief ; passage de la checklist « Vérifications avant PR
  (auteur) ».
- **Sortie** : le livre corrigé.
- **Critère de fin** : toutes les cases de la checklist auteur cochées.
- **Commit** : « Relecture de <titre> : corrections »

Puis : push et **pull request** (protocole de session — description structurée
Rôle : Production / roman-atelier v9, divergences de moteur signalées, et la
mention explicite : « En attente de la passe illustrateur —
`livres/<slug>/illustrations.md` »).

## Le relai illustrateur

C'est le seul point de passage entre les deux rôles, et il tient en un message.

- **Qui** : Pierre (ou l'orchestrateur de la session) lance un agent
  illustrateur — Codex, Claude Code ou autre agent capable de générer des
  images — après la PR de l'auteur.
- **Le message de relai**, en une phrase :
  > Sur la branche `atelier/roman-<slug>` du dépôt, exécute le manifeste
  > `livres/<slug>/illustrations.md`.
- **Ce que fait l'illustrateur** (tout est écrit dans le manifeste, qui est
  autoportant) : produire chaque fichier d'image listé, au nom exact, au format
  et au poids prescrits ; ajouter son modèle à `book:author` (seule édition de
  HTML autorisée, voir le manifeste) ; committer en français et pousser sur la
  même branche. **Rien d'autre** : pas d'édition de l'îlot JSON, pas de retouche
  du texte, pas de nouveau fichier hors de `livres/<slug>/images/` et
  `couvertures/<slug>.webp`.
- **Après sa passe** : la checklist « Vérifications avant merge » (ci-dessous)
  se passe sur la branche — par l'illustrateur s'il le peut, sinon par l'auteur
  ou un relecteur. La PR ne se merge qu'une fois cette checklist verte.
- **Traçabilité** : `book:author` = « <modèle auteur> (texte), <modèle
  illustrateur> (images) » ; les rôles sont détaillés dans la PR.

## Tronc commun et spécificités de l'atelier

Les conventions communes à tous les ateliers du moteur « Atelier » —
mise en place, structure de fichiers, `<head>` obligatoire, metas qualitatives
et capacités (vocabulaires fermés), gouvernance des tags, nature dérivée de
`book:workflow`, `book:variant-of`, moteur de liseuse, images générées et
couverture, vérification outillée, interdits communs — sont dans
[`TRONC-COMMUN.md`](../TRONC-COMMUN.md). **Ne pas les recopier ici : s'y
reporter.** Cet atelier précise seulement :

- **Recette et nature** :
  `<meta name="book:workflow" content="roman-atelier v9">` — l'atelier est
  enregistré dans la table `ATELIER_NATURE` comme producteur de **fictions**.
- **Format** : un livre de cet atelier naît illustré — `book:format` vaut
  normalement `illustré` (`texte` seulement si le brief renonce explicitement
  aux images).
- **Auteur en deux passes** : `book:author` liste les deux rôles — l'auteur
  l'écrit à l'étape 1 sous la forme « <son modèle> (texte) » ; l'illustrateur
  y ajoute « , <son modèle> (images) » pendant sa passe.
- **Structure de fichiers** : celle du tronc commun, avec `recherche.md`
  seulement si le brief demande l'ancrage réel (étape 0) et
  `illustrations.md` toujours (étape 4).
- **Interdit propre à l'atelier** : l'illustrateur ne modifie que les
  fichiers d'images et la meta `book:author` (voir le manifeste) ; on
  n'illustre pas rétroactivement un livre publié par une nouvelle entrée de
  catalogue (moratoire du tronc commun).

## Vérifications avant PR (auteur, fin d'étape 5b)

- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur et le livre apparaît dans le JSON généré ;
- [ ] `python livres/_template/outils/verifier.py livres/<slug> --sans-images`
      passe sans défaut ;
- [ ] le livre s'ouvre et se lit en `file://` de bout en bout, sans erreur
      JavaScript en console et **sans image cassée à l'écran** (les emplacements
      d'images se masquent) ;
- [ ] les 11 meta `book:*` sont présentes et exactes (`book:author` =
      « <modèle> (texte) » à ce stade ; les cinq metas qualitatives prennent
      une valeur du vocabulaire fermé ; `book:capacites` liste les capacités
      réellement offertes, `codex` compris) ;
- [ ] `book:variant-of` **absente**, sauf édition dérivée assumée (slug d'un
      livre existant) ;
- [ ] `<meta name="book:workflow" content="roman-atelier v9">` et
      `<meta name="reader-engine" content="atelier-liseuse v3">` présentes ;
- [ ] si le brief demande des modules de lecture (étape 3 bis) : blocs `map`
      et/ou `relations` remplis, capacités correspondantes déclarées, et rien
      ne se révèle avant sa lecture ; sinon, blocs `map` et `relations` du
      gabarit **supprimés** de l'îlot ;
- [ ] `livres/<slug>/brief.md` et `livres/<slug>/illustrations.md` committés ;
- [ ] si le brief demande l'ancrage réel : `livres/<slug>/recherche.md`
      committé (entrées sourcées et datées, plus de « Requêtes en attente »)
      et vérification factuelle livre ↔ dossier passée (étape 5a) ;
- [ ] révision en deux passes faite et committée séparément (étape 5a
      structure et rythme, étape 5b ligne à ligne) : une bascule par chapitre,
      chute qui paie la promesse émotionnelle et répond à la question
      thématique, point de vue et temps du récit tenus, typographie française
      uniforme ;
- [ ] socle [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et brief
      respectés (fond et forme — longueurs et densité de mentions lues comme
      des repères planchers, pas des cibles à maximiser) ;
- [ ] protocole de session d'`AGENTS.md` : commits d'étapes poussés, PR ouverte
      avec description structurée (Rôle : Production / roman-atelier v9),
      divergences de moteur signalées, passe illustrateur annoncée.

## Vérifications avant merge (après la passe illustrateur)

- [ ] `python livres/_template/outils/verifier.py livres/<slug>`
      passe sans défaut **sans** `--sans-images` (toutes les images du manifeste
      existent, formats, dimensions et poids conformes) ;
- [ ] couverture en place (`couvertures/<slug>.webp`, ratio 2:3, nom = slug
      exact, < 300 Ko) et inspectée visuellement : aucun texte, logo,
      signature, filigrane ni pseudo-texte incrusté ;
- [ ] `book:author` liste les deux rôles : « <modèle> (texte), <modèle> (images) » ;
- [ ] le livre se lit en `file://` avec toutes ses illustrations affichées ;
- [ ] la PR détaille les rôles (auteur / illustrateur) et l'outil ayant produit
      les images.
