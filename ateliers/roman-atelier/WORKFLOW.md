# Atelier roman-atelier — écrire un roman-web illustré avec la liseuse « Atelier »

- **Version** : 5
- **Statut** : stable (l'étape illustrations et le relai illustrateur, nouveaux
  en v3, et l'étape de recherche documentaire, nouvelle en v4, attendent leur
  exécution pilote à froid — roadmap Conception, session S2)
- **Livrable** : un roman-web HTML autonome **illustré nativement** (récit +
  liseuse intégrée : sommaire, barre de progression, codex à déverrouillage,
  illustrations de chapitres et de notices, thème sombre, réglage de taille de
  police), visible au catalogue après merge sans aucune intervention manuelle.
  Si le brief le demande, le récit est **ancré dans le monde réel** (personnage
  historique, lieux réels, jargon d'un métier), sur la base d'un dossier
  documentaire sourcé constitué avant l'écriture (étape 0).
- **Moteur** : [`livres/_template/`](../../livres/_template/README.md)
  (`atelier-liseuse v1`) — le moteur se copie depuis le template, plus jamais
  depuis le dernier livre publié.
- **Exemples publiés** : [`livres/lequation-du-calme/`](../../livres/lequation-du-calme)
  et [`livres/la-doublure.html`](../../livres/la-doublure.html) (v2, non
  illustrés) ; aucun livre v3 encore.
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md) — le lire
  avant l'étape 1, il fait partie de la recette.

## Changelog

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
  ([`outils/verifier.py`](outils/verifier.py)) ; images en WebP. Motif : les
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

Un livre v5 se fabrique en **deux passes, sur la même branche** :

1. **L'auteur** (étapes 0 à 5 ; l'étape 0 seulement si le brief demande
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
session), ce workflow, [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et
[`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md).
Rien d'autre n'est supposé connu.

1. **Recevoir le brief** : le message de lancement contient un
   [`BRIEF.md`](BRIEF.md) rempli. S'il manque, le demander ; s'il est
   incomplet, les défauts de `PREFERENCES.md` s'appliquent aux champs absents.
   Si le brief contient la section « Ancrage réel », l'étape 0 s'applique — en
   mode « recherche par l'agent » (le défaut), elle exige un accès de recherche
   web : s'il manque, le signaler avant de commencer et convenir du mode
   délégué.
2. **Choisir le slug** : celui du brief, ou à défaut le proposer — kebab-case
   ASCII (`les-brumes-du-port`), définitif : URL, couverture et clé
   localStorage en dépendent.
3. **Copier le moteur** :
   ```bash
   mkdir -p livres/<slug>/images
   cp livres/_template/index.html livres/<slug>/index.html
   ```
   Ne copier ni `README.md` ni `DONNEES.md`. Le `<script>` du moteur ne se
   modifie pas (toute divergence est signalée dans la PR) ; la palette CSS
   (variables de `:root` et `[data-theme="dark"]`) peut être adaptée à
   l'univers du livre.
4. **Créer la branche** : `atelier/roman-<slug>` (protocole de session).

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
  idée centrale, question thématique, liste des chapitres avec leur rôle narratif,
  personnages et lieux principaux. Pour un livre ancré dans le réel, l'univers
  s'appuie sur le dossier documentaire (perspective du personnage historique,
  lieux réels, époque) ; ce que le récit invente par-dessus est un choix
  d'auteur, pas une erreur — mais il ne contredit pas un fait établi du dossier.
- **Sortie** : `livres/<slug>/index.html` avec le `<head>` complet (§« Le
  `<head>` obligatoire ») et l'îlot JSON amorcé — blocs `meta`, `world` et
  `cover` remplis, chapitres en squelette (ids, numéros, titres) ; le brief
  recopié tel quel en `livres/<slug>/brief.md` (traçabilité de l'entrée).
- **Critère de fin** : `python scripts/build_catalog.py --output
  /tmp/catalog-verification.json` passe et le slug apparaît dans le JSON généré.
- **Commit** : « Plan de <titre> : synopsis et structure »

### Étape 2 — Chapitres

- **Entrée** : le plan committé à l'étape 1.
- **Travail** : écrire les chapitres dans l'îlot JSON (blocs de texte), dans l'ordre
  du plan. Un lot cohérent de chapitres par commit. Longueurs : celles du brief,
  sinon les défauts du socle (8 à 12 chapitres, 2 000 à 3 000 mots chacun).
  Pour un livre ancré dans le réel : jargon du métier, lieux, dates et gestes
  techniques viennent du dossier documentaire — toute affirmation ancrée doit
  y être traçable.
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
  Densité cible : celle du brief, sinon les défauts du socle (15 à 30 notices,
  ≥ 40 % des blocs porteurs d'au moins une mention). Pour un livre ancré dans
  le réel, les notices qui décrivent des personnes, lieux ou faits réels
  s'appuient sur le dossier documentaire.
- **Sortie** : le `codex[]` de l'îlot rempli, `mentions` posées, `entityAudit`
  complet.
- **Critère de fin** :
  `python ateliers/roman-atelier/outils/verifier.py livres/<slug>` ne signale
  aucun défaut d'intégrité (0 notice orpheline, 0 lien mort, déverrouillages
  cohérents) — les manques d'images sont encore tolérés à ce stade (`--sans-images`).
- **Commit** : « Codex de <titre> : personnages, lieux, concepts »

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
- **Critère de fin** : `python ateliers/roman-atelier/outils/verifier.py
  livres/<slug> --sans-images` passe (il vérifie notamment que chaque image de
  l'îlot a son entrée au manifeste et réciproquement) ; le livre reste
  entièrement lisible en `file://` alors qu'aucun fichier d'image n'existe
  encore (les emplacements se masquent, aucune image cassée à l'écran).
- **Commit** : « Illustrations de <titre> : champs d'images et manifeste »

### Étape 5 — Relecture et finitions

- **Entrée** : le livre complet (texte + champs d'images + manifeste).
- **Travail** : relecture intégrale (cohérence narrative, orthographe, respect de
  `PREFERENCES.md` et du brief), corrections ; si l'étape 0 a eu lieu, passe de
  **vérification factuelle** livre ↔ dossier (chaque référence au réel du texte
  et du codex est traçable à une entrée sourcée de `recherche.md`) ; passage de
  la checklist « Vérifications avant PR (auteur) ».
- **Sortie** : le livre corrigé.
- **Critère de fin** : toutes les cases de la checklist auteur cochées.
- **Commit** : « Relecture de <titre> : corrections »

Puis : push et **pull request** (protocole de session — description structurée
Rôle : Production / roman-atelier v5, divergences de moteur signalées, et la
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

## Structure de fichiers

Un livre v5 est **toujours un dossier** (il porte des images) :

```text
livres/<slug>/
  index.html          ← point d'entrée (obligatoirement index.html)
  brief.md            ← le brief d'entrée, recopié tel quel (étape 1)
  recherche.md        ← le dossier documentaire sourcé (étape 0 —
                        seulement si le brief demande l'ancrage réel)
  illustrations.md    ← le manifeste pour l'illustrateur (étape 4)
  images/
    chapter-01.webp   ← une par chapitre, numérotation sur 2 chiffres
    codex-<id>.webp   ← notices illustrées (id = id de la notice)
```

- Profondeur maximale : **un seul niveau** de dossier sous `livres/`.
- Toutes les ressources du livre restent **dans son dossier** ; la couverture,
  elle, vit dans `couvertures/<slug>.webp`.

## Le `<head>` obligatoire

Le template en contient un gabarit prêt à remplacer. Pour référence (les 5 meta
`book:*` alimentent le catalogue ; `book:workflow` et `reader-engine` tracent la
recette et le moteur) :

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Métadonnées utilisées par Ma Bibliothèque -->
  <meta name="book:title" content="Titre complet du livre">
  <meta name="book:author" content="Claude Fable (texte), GPT 5.5 (images)">
  <meta
    name="book:description"
    content="Résumé en une ou deux phrases (≤ 600 caractères), destiné à la carte du catalogue."
  >
  <meta name="book:tags" content="genre, thème, lieu (1 à 6 tags, séparés par des virgules)">
  <meta name="book:date" content="2026-08-13">

  <!-- Traçabilité : recette et moteur (ignorées par le catalogue) -->
  <meta name="book:workflow" content="roman-atelier v5">
  <meta name="reader-engine" content="atelier-liseuse v1">

  <!-- Utilisé par l'onglet du navigateur et comme fallback de titre -->
  <title>Titre complet du livre</title>
</head>
```

- **`book:author` = le nom du ou des modèles** (`Claude Fable`, `GPT 5.5`,
  `Gemini 3.1 pro`…). **Pas de pseudonyme collectif** type « Atelier des récits
  explorables » — cette dérive a effacé la provenance de la moitié du catalogue
  (audit §B.6). Depuis la v3 le champ liste les deux rôles : l'auteur l'écrit à l'étape
  1 sous la forme « <son modèle> (texte) » ; l'illustrateur y ajoute
  « , <son modèle> (images) » pendant sa passe.
- `book:date` : `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ`.

## Le moteur de liseuse

- **Source unique** : [`livres/_template/index.html`](../../livres/_template/index.html)
  (`atelier-liseuse v1`), copié tel quel. Les trois défauts historiques du
  moteur (audit §B.4 : `close()` écrasé, `entry()` sans garde, recherche du
  codex) y sont corrigés — ne pas les réintroduire en copiant un ancien livre.
- **Données** : le récit vit dans l'îlot
  `<script type="application/json" id="book-data">`, dont la structure est
  spécifiée champ par champ dans
  [`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md).
- **Persistance** : la clé localStorage `<slug>-state-v1` est dérivée de
  `meta.slug` par le moteur — renseigner `meta.slug` correctement suffit.
- **Fonctionnalités à ne pas régresser** : sommaire, `role="progressbar"` mis à
  jour, codex à déverrouillage robuste au rechargement, thème sombre, taille de
  police, piège de focus dans les dialogues, région `aria-live` pour les
  déblocages, `prefers-reduced-motion`, échappement HTML systématique des
  données de l'îlot, visionneuse d'images, dégradation propre des images
  manquantes.

## Images et couverture

- **Format** : **WebP** pour tout (chapitres, notices, couverture). JPEG toléré
  en repli si la chaîne de l'illustrateur ne produit pas de WebP — le signaler
  dans la PR.
- **Couverture obligatoire** : `couvertures/<slug>.webp`, ratio **2:3**
  (cible : 800×1200), poids **< 300 Ko**. Le nom doit être **exactement** le
  slug, sinon elle est ignorée en silence et un placeholder est généré. Son
  image ne contient **aucun texte**, sans exception : ni titre, sous-titre,
  nom, crédit, logo, signature, filigrane ou pseudo-texte. Le titre et les
  métadonnées sont ajoutés par-dessus en HTML dans la bibliothèque.
- **Images de chapitre** : `livres/<slug>/images/chapter-NN.webp` (NN = numéro
  du chapitre sur 2 chiffres), **1600×900**, poids **≤ 150 Ko** ; une par
  chapitre.
- **Images de notice** : `livres/<slug>/images/codex-<id>.webp` (id = id exact
  de la notice), **1600×900**, poids **≤ 150 Ko** ; notices majeures seulement
  (défaut : environ un tiers du codex).
- Le moteur pose `width`/`height` (1600×900 par défaut) et `loading="lazy"`
  hors première image ; si une image déroge aux dimensions, renseigner
  `imageWidth`/`imageHeight` dans l'îlot.
- Les `alt` sont écrits par l'**auteur** (étape 4) et vivent dans l'îlot — pas
  par l'illustrateur.
- Conversion/compression (commandes de référence, reprises dans le manifeste) :
  ```bash
  cwebp -q 82 -resize 1600 900 source.png -o images/chapter-01.webp
  # ou, si seul ImageMagick est disponible :
  magick source.png -resize 1600x900^ -gravity center -extent 1600x900 -quality 82 images/chapter-01.webp
  ```

## Interdits spécifiques

- **Moratoire sur les éditions dérivées en doublon** (`-v2`, `-illustree`) : ne pas
  créer une entrée de catalogue séparée pour une variante d'un livre existant.
  Un livre v3 naît illustré ; on n'illustre pas rétroactivement un livre publié
  par une nouvelle entrée — audit
  [`docs/audits/2026-08-rapport-etonnement.md`](../../docs/audits/2026-08-rapport-etonnement.md) §D.
- Jamais toucher `catalog.json` ni le bloc `#demo-catalog` (règles d'or).
- Aucune ressource distante (CDN, fonts, images externes).
- L'illustrateur ne modifie que les fichiers d'images et la meta `book:author`.

## Vérifications avant PR (auteur, fin d'étape 5)

- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur et le livre apparaît dans le JSON généré ;
- [ ] `python ateliers/roman-atelier/outils/verifier.py livres/<slug> --sans-images`
      passe sans défaut ;
- [ ] le livre s'ouvre et se lit en `file://` de bout en bout, sans erreur
      JavaScript en console et **sans image cassée à l'écran** (les emplacements
      d'images se masquent) ;
- [ ] les 5 meta `book:*` sont présentes et exactes (`book:author` =
      « <modèle> (texte) » à ce stade) ;
- [ ] `<meta name="book:workflow" content="roman-atelier v5">` et
      `<meta name="reader-engine" content="atelier-liseuse v1">` présentes ;
- [ ] `livres/<slug>/brief.md` et `livres/<slug>/illustrations.md` committés ;
- [ ] si le brief demande l'ancrage réel : `livres/<slug>/recherche.md`
      committé (entrées sourcées et datées, plus de « Requêtes en attente »)
      et vérification factuelle livre ↔ dossier passée (étape 5) ;
- [ ] socle [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et brief
      respectés (fond et forme — longueurs, densité de mentions) ;
- [ ] protocole de session d'`AGENTS.md` : commits d'étapes poussés, PR ouverte
      avec description structurée (Rôle : Production / roman-atelier v5),
      divergences de moteur signalées, passe illustrateur annoncée.

## Vérifications avant merge (après la passe illustrateur)

- [ ] `python ateliers/roman-atelier/outils/verifier.py livres/<slug>`
      passe sans défaut **sans** `--sans-images` (toutes les images du manifeste
      existent, formats, dimensions et poids conformes) ;
- [ ] couverture en place (`couvertures/<slug>.webp`, ratio 2:3, nom = slug
      exact, < 300 Ko) et inspectée visuellement : aucun texte, logo,
      signature, filigrane ni pseudo-texte incrusté ;
- [ ] `book:author` liste les deux rôles : « <modèle> (texte), <modèle> (images) » ;
- [ ] le livre se lit en `file://` avec toutes ses illustrations affichées ;
- [ ] la PR détaille les rôles (auteur / illustrateur) et l'outil ayant produit
      les images.
