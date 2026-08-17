# Atelier reportage — composer un reportage explorable

- **Version** : 3
- **Statut** : expérimental (en attente de son exécution pilote à froid —
  roadmap Conception, chantier 8)
- **Livrable** : un **reportage** — un livre-web HTML autonome **non romancé**
  qui fait découvrir un sujet réel demandé par le brief (un lieu, un
  personnage historique, un métier, un événement, un environnement),
  construit sur un **dossier documentaire sourcé**, restitué en lecture
  explorable (chapitres = étapes du parcours, notices de codex = matière
  documentaire à déverrouillage) et **illustré de documents récupérés sur le
  web** (photographies, cartes, graphes, gravures…), chacun crédité de sa
  source.
- **Moteur** : [`livres/_template/`](../../livres/_template/README.md)
  (`atelier-liseuse v2`) — le moteur se copie depuis le template, jamais
  depuis un livre publié.
- **Exemples publiés** : aucun encore.
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md) — le
  lire avant l'étape 1, il fait partie de la recette.
- **Brief** : gabarit d'entrée dans [`BRIEF.md`](BRIEF.md).

## Changelog

- **v3** (2026-08) — couverture strictement sans texte : titre, sous-titre,
  crédit, logo, signature, filigrane et pseudo-texte sont interdits dans le
  fichier image, puisque l'interface de la bibliothèque superpose déjà les
  métadonnées. Les crédits documentaires restent dans `recherche.md` et dans
  le livre. Motif : éviter les doublons et conflits de lisibilité observés sur
  des couvertures publiées.
- **v2** (2026-08) — l'atelier `mediation-culturelle` devient **`reportage`**
  (session Conception du 2026-08-17, sur demande de Pierre). Motifs : un nom
  qui dit mieux le format ; surtout, l'autorisation des **documents du web**
  dans le corps des chapitres et sur les notices du codex (moteur
  `atelier-liseuse v2`), collectés dès la recherche documentaire et insérés
  avec mention et lien de leur source — encadrée par une **règle de
  pertinence** qui interdit toute image décorative. Le premier tag imposé
  passe de `médiation culturelle` à `reportage`.
- **v1** (2026-08) — recette initiale, sous le nom `mediation-culturelle`
  (session Conception du 2026-08-13, chantier 8 de la
  [roadmap Conception](../../docs/conception/ROADMAP.md)). Motif : étendre la
  bibliothèque au-delà de la fiction en exploitant la capacité des agents à
  mener des recherches documentaires en amont de l'écriture. Jamais exécutée
  en production.

## Ce qui distingue ce format d'un roman

- **Rien n'est inventé** : ni personnage, ni intrigue, ni fait. Chaque
  affirmation du livre est traçable au dossier documentaire de l'étape 1 ; une
  hypothèse ou un débat d'historiens se présente comme tel, jamais comme un
  fait établi.
- **Le récit est un parcours** : les chapitres organisent la découverte du
  sujet (angles successifs, progression du général au particulier, fil
  chronologique ou thématique) — la qualité littéraire reste attendue (socle
  `PREFERENCES.md`), au service de la transmission.
- **Le codex est la salle des archives** : les notices portent les personnes,
  lieux, dates, concepts et vocabulaire du sujet, chacune avec ses sources.
- **Les images sont des documents** : une image n'entre dans le reportage que
  si elle **apporte une information que le texte seul ne porte pas** ; elle
  vient du monde réel (le web) et cite sa source. Voir « Les documents du
  web » plus bas.

## Avant de commencer

Prérequis de lecture : [`/AGENTS.md`](../../AGENTS.md) (règles d'or + protocole
de session), ce workflow,
[`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et
[`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md).
Rien d'autre n'est supposé connu.

1. **Recevoir le brief** : le message de lancement contient un
   [`BRIEF.md`](BRIEF.md) rempli. S'il manque, le demander. Le sujet (champ
   obligatoire) ne peut pas être délégué : pas de reportage sans sujet réel.
   En mode « recherche par l'agent » (le défaut), l'étape 1 exige un accès de
   recherche web : s'il manque, le signaler avant de commencer et convenir du
   mode délégué.
2. **Choisir le slug** : celui du brief, ou à défaut le proposer — kebab-case
   ASCII (`le-canal-du-midi`), définitif : URL, couverture et clé localStorage
   en dépendent.
3. **Copier le moteur** :
   ```bash
   mkdir -p livres/<slug>/images
   cp livres/_template/index.html livres/<slug>/index.html
   ```
   Ne copier ni `README.md` ni `DONNEES.md`. Le `<script>` du moteur ne se
   modifie pas (toute divergence est signalée dans la PR) ; la palette CSS
   (variables de `:root` et `[data-theme="dark"]`) peut être adaptée au sujet.
4. **Créer la branche** : `atelier/reportage-<slug>` (protocole de session).

## Étapes de fabrication

### Étape 1 — Recherche documentaire

La signature du format : elle s'exécute **toujours**, avant toute écriture.

- **Entrée** : le brief rempli (sujet, angle, axes de recherche, sources, mode
  de recherche).
- **Travail** : constituer le dossier documentaire du livre, selon le mode fixé
  par le brief :
  - **Recherche par l'agent** (défaut) : mener les recherches soi-même. Si
    l'agent d'exécution sait paralléliser des recherches (sub-agents),
    répartir par axe — lieux, personnes, événements, vocabulaire et jargon,
    contexte d'époque, état des connaissances et débats — sinon traiter les
    axes séquentiellement. Chaque fait notable est relié à sa source
    **datée** ; faits établis, débattus et incertains sont distingués.

    **Collecte des documents visuels** : au fil des recherches, repérer et
    télécharger les images qui documentent le sujet (photographies, cartes,
    plans, graphes de données, gravures, fac-similés…) dans
    `livres/<slug>/images/`, et tenir dans `recherche.md` une section
    **« Documents visuels »** — une entrée par document : fichier local, URL
    directe de l'image, page web qui l'héberge, auteur ou crédit si connu,
    date de consultation, et **l'information que le document apporte** (c'est
    la justification de pertinence exigée à l'insertion). Un document sans
    page source identifiable ne se collecte pas.
  - **Recherche déléguée** (sur demande du brief, pour économiser le quota de
    l'agent) : rédiger dans `livres/<slug>/recherche.md` une section
    « Requêtes en attente » — une requête de recherche **autoportante et
    copiable-collable** par axe, y compris pour les documents visuels
    (demander des URL d'images avec leur page source) —, committer, puis
    **suspendre la fabrication** en demandant à Pierre de soumettre ces
    requêtes à l'assistant externe de son choix (Perplexity, ChatGPT ou autre)
    et de coller les réponses en retour : c'est le tour d'échange
    supplémentaire prévu par la recette. À réception, consolider le dossier au
    même standard que ci-dessus, en marquant la provenance de chaque fait
    (« réponse d'assistant externe fournie le <AAAA-MM-JJ> »), et vérifier sa
    cohérence interne.
- **Sortie** : `livres/<slug>/recherche.md` — un fait notable par entrée, avec
  sa source datée ; les axes demandés par le brief tous couverts ; la section
  « Documents visuels » remplie (éventuellement vide si rien de pertinent) ;
  les fichiers collectés dans `livres/<slug>/images/` ; le brief recopié tel
  quel en `livres/<slug>/brief.md` (traçabilité de l'entrée).
- **Critère de fin** : chaque axe du brief a sa section dans le dossier ;
  chaque entrée porte une source datée ou la mention explicite de son
  incertitude ; chaque document visuel collecté a son entrée complète dans
  « Documents visuels » ; plus aucune section « Requêtes en attente ».
- **Commit** : « Dossier documentaire de <titre> : recherches sur <sujet> »
  (en mode délégué, un premier commit « Dossier documentaire de <titre> :
  requêtes en attente » précède la suspension).

### Étape 2 — Parcours et plan du reportage

- **Entrée** : le dossier documentaire committé, le socle `PREFERENCES.md`
  (§Fond).
- **Travail** : concevoir le parcours avant d'écrire — l'angle du reportage,
  la promesse de découverte, l'idée centrale, la question qui tient le lecteur
  (elles remplissent le bloc `world` de l'îlot JSON : ce que le lecteur aura
  compris et ressenti en refermant le livre), puis la liste des chapitres avec
  le rôle de chacun dans le parcours (chronologique, thématique, du général au
  particulier…).
- **Sortie** : `livres/<slug>/index.html` avec le `<head>` complet (§« Le
  `<head>` obligatoire ») et l'îlot JSON amorcé — blocs `meta`, `world` et
  `cover` remplis, chapitres en squelette (ids, numéros, titres).
- **Critère de fin** : `python scripts/build_catalog.py --output
  /tmp/catalog-verification.json` passe et le slug apparaît dans le JSON
  généré.
- **Commit** : « Parcours de <titre> : plan du reportage »

### Étape 3 — Chapitres et documents

- **Entrée** : le plan committé à l'étape 2, le dossier documentaire (section
  « Documents visuels » comprise).
- **Travail** : écrire les chapitres dans l'îlot JSON (blocs de texte), dans
  l'ordre du parcours. Un lot cohérent de chapitres par commit. Registre de
  reportage : adresse au lecteur possible, contextualisation, anecdotes
  sourcées — pas de personnages inventés ni de scènes imaginées ; quand le
  livre adopte la perspective d'un personnage historique, tout ce qu'il
  « voit » vient du dossier. **Chaque affirmation est traçable à une entrée de
  `recherche.md`.**

  **Insertion des documents** : au fil de l'écriture, poser les documents
  visuels retenus en figures de blocs (`blocks[].figure`, spécification :
  [`DONNEES.md`](../../livres/_template/DONNEES.md)) — le document s'affiche
  entre son paragraphe et le suivant. Renommer le fichier
  `images/figure-<id-bloc>.webp`, convertir en WebP et compresser (§« Les
  documents du web »), renseigner `alt`, `caption` (ce que le document
  apporte au propos), `source.label` + `source.url` (obligatoires) et les
  dimensions réelles. La **règle de pertinence** s'applique à chaque
  insertion ; l'entrée correspondante de « Documents visuels » est mise à
  jour avec le nom de fichier définitif.

  Longueurs : celles du brief, sinon les défauts de l'atelier (6 à 10
  chapitres, 1 000 à 2 000 mots chacun — plus courts que le roman : la
  densité documentaire fatigue plus vite que la fiction).
- **Sortie** : les `chapters[].blocks[]` de l'îlot remplis, figures posées
  (les champs `image` de bandeau de chapitre attendront l'étape 6, si le
  brief demande des illustrations générées).
- **Critère de fin** : le livre s'ouvre en `file://`, chaque chapitre écrit
  s'affiche avec ses documents (légende et crédit visibles), la navigation
  fonctionne, aucune erreur JavaScript dans la console du navigateur.
- **Commit(s)** : « Chapitres 1-3 de <titre> », « Chapitres 4-6 de <titre> »…

### Étape 4 — Codex documentaire

- **Entrée** : les chapitres écrits, le dossier documentaire.
- **Travail** : rédiger les notices du codex (personnes, lieux, dates,
  concepts, vocabulaire du sujet) dans la voix de `meta.codexVoice` — la voix
  qui guide le lecteur, définie au brief ou proposée par l'auteur —, avec
  **tous** les champs de la spécification
  ([`DONNEES.md`](../../livres/_template/DONNEES.md)), puis relier les notices
  aux blocs par les `mentions`. Compléter `entityAudit` pour toute entité
  nommée sans notice. Chaque notice qui énonce un fait cite sa source (dans le
  corps de la notice ou en fin de notice). Une notice peut être illustrée par
  un **document du web** : `image` (`images/codex-<id>.webp`) + `alt` +
  `source` (la règle de pertinence s'applique ; entrée à jour dans
  « Documents visuels »). Ajouter une notice **« Sources et méthode »**,
  déverrouillée dès le premier chapitre, qui liste les principales sources du
  dossier — documents visuels compris — et dit comment le livre a été
  documenté. Densité cible : celle du brief, sinon les défauts du socle (15 à
  30 notices, ≥ 40 % des blocs porteurs d'au moins une mention).
- **Sortie** : le `codex[]` de l'îlot rempli (notice « Sources et méthode »
  comprise), `mentions` posées, `entityAudit` complet.
- **Critère de fin** :
  `python ateliers/roman-atelier/outils/verifier.py livres/<slug> --sans-images`
  ne signale aucun défaut d'intégrité (0 notice orpheline, 0 lien mort,
  déverrouillages cohérents, crédits de source complets) — l'outil vit dans
  `roman-atelier` mais vérifie l'îlot du moteur commun, il s'applique tel
  quel.
- **Commit** : « Codex de <titre> : notices documentaires et sources »

### Étape 5 — Vérification factuelle et relecture

- **Entrée** : le livre complet (chapitres + documents + codex), le dossier
  documentaire.
- **Travail** : passe de **vérification factuelle** livre ↔ dossier — chaque
  affirmation du texte et du codex est traçable à une entrée sourcée de
  `recherche.md` ; toute affirmation introuvable est corrigée, sourcée a
  posteriori (et ajoutée au dossier), ou explicitement marquée comme
  hypothèse. **Vérification des documents** : chaque figure et image de
  notice a son entrée « Documents visuels » dans `recherche.md`, son crédit
  (`source.label` + `source.url`) exact, une légende juste, et passe la règle
  de pertinence — un document qui ne l'a jamais vraiment passée se retire.
  Puis relecture intégrale (clarté du parcours, orthographe, respect de
  `PREFERENCES.md` et du brief) et passage de la checklist « Vérifications
  avant PR ».
- **Sortie** : le livre corrigé.
- **Critère de fin** : toutes les cases de la checklist cochées.
- **Commit** : « Relecture de <titre> : vérification factuelle et corrections »

Puis : push et **pull request** (protocole de session — description structurée
Rôle : Production / reportage v3 ; si le brief demande des illustrations
générées, la mention explicite : « En attente de la passe illustrateur —
`livres/<slug>/illustrations.md` »).

### Étape 6 (optionnelle) — Illustrations générées

Seulement si le brief en demande. Reprendre le mécanisme éprouvé de
`roman-atelier` : renseigner les champs d'images de l'îlot (bandeaux de
chapitre, notices restantes, couverture) et écrire le manifeste autoportant
`livres/<slug>/illustrations.md` en copiant
[`../roman-atelier/GABARIT-ILLUSTRATIONS.md`](../roman-atelier/GABARIT-ILLUSTRATIONS.md),
puis relai vers un agent illustrateur — voir « Le relai illustrateur » du
[`WORKFLOW.md` de roman-atelier](../roman-atelier/WORKFLOW.md), qui s'applique
tel quel (mêmes formats, poids et interdits ; pour un sujet réel, privilégier
une direction artistique documentaire — gravures, planches, photographies
d'époque évoquées — plutôt qu'une esthétique de fiction). **Une image générée
ne porte jamais de champ `source`** : le crédit de source est réservé aux
documents du web ; c'est ce champ qui distingue les deux dans l'îlot et pour
le vérificateur. Les documents du web déjà posés (figures, notices) ne
figurent **pas** au manifeste : leur traçabilité vit dans `recherche.md`.

## Les documents du web

La spécificité du format : illustrer le réel par le réel.

- **Règle de pertinence (interdit d'atelier)** : un document n'entre dans le
  livre que s'il **apporte une information que le texte seul ne porte pas** —
  un document d'époque, une carte ou un plan, un graphe de données, la
  photographie du sujet réel, un fac-similé. Les images décoratives,
  d'ambiance ou génériques (photo d'illustration interchangeable, banque
  d'images) sont **interdites**. Pas de quota à remplir : dans le doute,
  pas d'image — un reportage sans aucun document est conforme si rien de
  pertinent n'a été trouvé.
- **Crédit obligatoire** : chaque document porte `source.label` (média,
  institution, auteur) et `source.url` (la page d'origine, en `http(s)://`) —
  le moteur les affiche sous la légende. Politique du dépôt : la mention et le
  lien de la source suffisent (pas de filtre de licence imposé) ; si une
  licence est connue, la noter dans le champ éditorial `origin` et dans
  `recherche.md`.
- **Le fichier est local** : le document est téléchargé dans
  `livres/<slug>/images/` (aucune ressource distante — l'autonomie du livre
  est une règle d'or) ; seule l'ancre `source.url` pointe vers l'extérieur.
- **Nommage** : `images/figure-<id-bloc>.webp` pour une figure de bloc,
  `images/codex-<id>.webp` pour une image de notice.
- **Format et poids** : conversion WebP (`cwebp -q 82` ; pour un graphe ou un
  document à texte fin, `cwebp -near_lossless 60` préserve la lisibilité),
  dimensions réelles conservées (pas de recadrage 1600×900 imposé — réduire
  seulement si > 1600 px de large), **≤ 150 Ko visé, 300 Ko maximum**
  (`verifier.py` bloque au-delà). PNG/JPEG tolérés en repli si la conversion
  dégrade un document (à signaler dans la PR).
- **Traçabilité** : chaque document a son entrée dans la section « Documents
  visuels » de `recherche.md` (fichier, URL directe, page hôte, crédit, date
  de consultation, information apportée) — c'est l'équivalent, pour les
  images, du « aucun fait sans source » du texte.

## Structure de fichiers

Un reportage est **toujours un dossier** :

```text
livres/<slug>/
  index.html          ← point d'entrée (obligatoirement index.html)
  brief.md            ← le brief d'entrée, recopié tel quel (étape 1)
  recherche.md        ← le dossier documentaire sourcé, avec sa section
                        « Documents visuels » (étape 1)
  images/             ← les documents du web (étapes 1 et 3) et, si l'étape 6
                        s'applique, les illustrations générées
  illustrations.md    ← le manifeste pour l'illustrateur (étape 6, si demandé)
```

- Profondeur maximale : **un seul niveau** de dossier sous `livres/`.
- Toutes les ressources du livre restent **dans son dossier** ; la couverture,
  elle, vit dans `couvertures/<slug>.webp` (ratio 2:3, < 300 Ko) et ne contient
  aucun texte, logo, signature, filigrane ou pseudo-texte. Si elle reprend un
  document du web, son crédit reste dans `recherche.md` et dans le livre, jamais
  incrusté dans l'image.

## Le `<head>` obligatoire

Le template en contient un gabarit prêt à remplacer. Pour référence :

```html
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- Métadonnées utilisées par Ma Bibliothèque -->
  <meta name="book:title" content="Titre complet du reportage">
  <meta name="book:author" content="Claude Fable">
  <meta
    name="book:description"
    content="Ce que le lecteur va découvrir, en une ou deux phrases (≤ 600 caractères)."
  >
  <meta name="book:tags" content="reportage, histoire, <lieu ou thème> (1 à 6 tags)">
  <meta name="book:date" content="2026-08-17">

  <!-- Traçabilité : recette et moteur (ignorées par le catalogue) -->
  <meta name="book:workflow" content="reportage v3">
  <meta name="reader-engine" content="atelier-liseuse v2">

  <title>Titre complet du reportage</title>
</head>
```

- **`book:tags` commence obligatoirement par `reportage`** : c'est le marqueur
  qui sépare ces lectures des fictions au catalogue, en attendant le champ
  `nature` du schéma v2 ([roadmap
  Bibliothèque](../../docs/bibliotheque/ROADMAP.md), chantier 5 ; règle de
  cohabitation de
  [`creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md) §6).
- **`book:author` = le nom du ou des modèles** (règle d'or d'`AGENTS.md`) ; si
  le reportage reçoit des illustrations générées, l'illustrateur ajoute
  « , <son modèle> (images) » pendant sa passe.

## Conventions spécifiques de l'atelier

- **Aucun fait sans source** : le dossier `recherche.md` est la source de
  vérité du livre ; les hypothèses et débats sont signalés comme tels dans le
  texte et les notices.
- **Aucune image sans information ni crédit** : règle de pertinence et section
  « Documents visuels » (§« Les documents du web »).
- **Notice « Sources et méthode » obligatoire**, déverrouillée dès le premier
  chapitre.
- **Défauts de longueur du format** : 6 à 10 chapitres de 1 000 à 2 000 mots
  (le brief peut surcharger) ; densité de notices : défauts du socle.
- **Persistance** : clé localStorage `<slug>-state-v1`, dérivée de `meta.slug`
  par le moteur — renseigner `meta.slug` correctement suffit.
- **Îlot JSON** : structure spécifiée par
  [`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md) ; le bloc
  `world` s'interprète au sens du reportage (promesse de découverte, idée
  centrale, question tenant lieu de fil rouge).

## Traçabilité

Le `<head>` du livrable produit contient la version de la recette utilisée :

```html
<meta name="book:workflow" content="reportage v3">
```

(meta ignorée par le générateur de catalogue — aucune incidence.) La PR de
production mentionne aussi cette version.

## Contraintes de plateforme

Ce livrable respecte les contraintes communes du
[`§1 de creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md)
(emplacement, slug, 5 meta `book:*`, couverture 2:3 sans texte, autonomie,
accessibilité).
Points où cet atelier est plus strict :

- premier tag imposé (`reportage`) ;
- dossier documentaire `recherche.md` committé, entrées sourcées et datées,
  section « Documents visuels » tenue ;
- aucune affirmation du livre sans trace dans le dossier ;
- aucune image sans apport d'information, sans crédit de source (documents du
  web) ni sans entrée de traçabilité.

## Vérifications avant PR

- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur et le reportage apparaît dans le JSON généré ;
- [ ] `python ateliers/roman-atelier/outils/verifier.py livres/<slug>`
      passe sans défaut (avec `--sans-images` tant que l'étape 6 est en
      attente d'illustrateur : les contrôles de champs des documents — alt,
      légende, crédit — s'exécutent quand même) ;
- [ ] le reportage s'ouvre et se lit en `file://` de bout en bout, documents
      affichés avec légende et crédit, sans erreur JavaScript en console ;
- [ ] les 5 meta `book:*` sont présentes et exactes, `book:tags` commence par
      `reportage` ;
- [ ] `<meta name="book:workflow" content="reportage v3">` et
      `<meta name="reader-engine" content="atelier-liseuse v2">` présentes ;
- [ ] `livres/<slug>/brief.md` et `livres/<slug>/recherche.md` committés
      (entrées sourcées et datées, section « Documents visuels » complète,
      plus de « Requêtes en attente ») ;
- [ ] chaque figure et image de notice issue du web : fichier local dans
      `images/`, `alt`, légende, `source.label` + `source.url` exacts, entrée
      « Documents visuels » à jour, règle de pertinence passée ;
- [ ] couverture inspectée visuellement : aucun texte, crédit, logo, signature,
      filigrane ni pseudo-texte incrusté ; son éventuelle source documentaire
      est créditée hors image ;
- [ ] vérification factuelle livre ↔ dossier passée (étape 5) ; notice
      « Sources et méthode » présente et déverrouillée dès le premier
      chapitre ;
- [ ] socle [`PREFERENCES.md`](../../docs/conception/PREFERENCES.md) et brief
      respectés (fond et forme — longueurs, densité de mentions) ;
- [ ] protocole de session d'`AGENTS.md` : commits d'étapes poussés, PR
      ouverte avec description structurée (Rôle : Production / reportage v3),
      divergences de moteur signalées, passe illustrateur annoncée si
      l'étape 6 s'applique.
