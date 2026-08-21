# Atelier roman-atelier — écrire un roman-web illustré avec la liseuse « Atelier »

- **Version** : 8
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
- **Exemples publiés** : [`livres/lequation-du-calme/`](../../livres/lequation-du-calme)
  et [`livres/la-doublure.html`](../../livres/la-doublure.html) (v2, non
  illustrés) ;
  [`livres/la-clause-du-meilleur-ennemi/`](../../livres/la-clause-du-meilleur-ennemi)
  (v3, illustré en deux passes).
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md) — le lire
  avant l'étape 1, il fait partie de la recette.

## Changelog

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
  Densité cible : celle du brief, sinon les défauts du socle (15 à 30 notices,
  ≥ 40 % des blocs porteurs d'au moins une mention). Pour un livre ancré dans
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
Rôle : Production / roman-atelier v8, divergences de moteur signalées, et la
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

Un livre de cet atelier est **toujours un dossier** (il porte des images) :

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

Le template en contient un gabarit prêt à remplacer. Pour référence (les 11 meta
`book:*` alimentent le catalogue ; `reader-engine` trace le moteur) :

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
  <meta name="book:tags" content="thème, lieu, motif (2 à 4 tags, séparés par des virgules)">
  <meta name="book:date" content="2026-08-13">

  <!-- Metas qualitatives (vocabulaires fermés, voir ci-dessous) -->
  <meta name="book:genre" content="anticipation">
  <meta name="book:format" content="illustré">
  <meta name="book:tonalite" content="douce-amère">
  <meta name="book:exigence" content="intermédiaire">
  <meta name="book:audience" content="ados et adultes">

  <!-- Capacités interactives réellement offertes (vocabulaire fermé, liste) -->
  <!-- « codex » toujours ; « carte » et « relations » si l'étape 3 bis a eu lieu -->
  <meta name="book:capacites" content="codex">

  <!-- Recette (lue par le générateur : elle en dérive la nature) et moteur -->
  <meta name="book:workflow" content="roman-atelier v8">
  <meta name="reader-engine" content="atelier-liseuse v3">

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

### Les cinq metas qualitatives (vocabulaires fermés)

Elles sont **obligatoires** et n'acceptent que les valeurs ci-dessous, à la
graphie exacte (accents compris). Source de vérité :
[`docs/bibliotheque/CATALOGUE.md`](../../docs/bibliotheque/CATALOGUE.md) — s'y
reporter en cas de doute, et n'inventer aucune valeur : une valeur hors
vocabulaire est un défaut bloquant du vérificateur. Un seul terme par meta, celui
qui décrit le mieux le livre dans son ensemble.

| Meta | Valeurs admises |
|---|---|
| `book:genre` | `science-fiction`, `fantasy`, `fantastique`, `anticipation`, `espionnage`, `policier`, `aventure`, `comédie dramatique`, `drame`, `histoire`, `société`, `sciences`, `portrait` |
| `book:format` | `texte`, `illustré` |
| `book:tonalite` | `lumineuse`, `douce-amère`, `contemplative`, `ironique`, `tendue`, `sombre` |
| `book:exigence` | `accessible`, `intermédiaire`, `exigeante` |
| `book:audience` | `tout public`, `ados et adultes`, `adultes` |
| `book:capacites` | `codex`, `carte`, `relations`, `choix`, `audio` — **liste** séparée par des virgules |

- Un livre de cet atelier naît illustré : `book:format` vaut normalement
  `illustré` (`texte` seulement si le brief renonce explicitement aux images).
- `book:capacites` déclare **ce que le livre fait** en plus de dérouler son texte.
  Un livre de cet atelier a toujours un codex : `codex` au minimum, et le
  vérificateur en fait un défaut bloquant si l'îlot porte un codex non déclaré.
  Ajouter `carte`, `relations`, `choix` ou `audio` **seulement si le livre les
  offre réellement** — une capacité annoncée et absente est pire qu'un badge
  manquant. Les illustrations ne sont pas une capacité : `book:format` le dit
  déjà.
- Les `book:tags` restent **libres et complémentaires** (thème, lieu, motif) mais
  gouvernés depuis le chantier 6 : **2 à 4 tags**, jamais une valeur de vocabulaire
  fermé (`genre`, `format`, `tonalite`, `exigence`, `audience`) ni une nature
  (`fiction`, `reportage`), jamais une étiquette de manière (`récit littéraire`,
  `exploration documentaire`) ou d'édition (`édition illustrée`). Le vérificateur en
  fait un défaut bloquant et le générateur écarte le tag fautif. Règle complète :
  [`docs/bibliotheque/CATALOGUE.md`](../../docs/bibliotheque/CATALOGUE.md)
  §Gouvernance des tags.
- Rien à renseigner pour la longueur : `wordCount` et le temps de lecture sont
  **calculés** par `scripts/build_catalog.py` à partir de l'îlot JSON.

### La nature du livre : dérivée, jamais déclarée

Le catalogue range les livres par `nature` (`fiction` ou `reportage`), mais
**aucune meta ne la porte** : `scripts/build_catalog.py` la déduit du nom
d'atelier lu dans `book:workflow` (le contenu sans son suffixe ` vN`) via sa
table `ATELIER_NATURE`. Cet atelier y est enregistré comme producteur de
**fictions** : renseigner `<meta name="book:workflow" content="roman-atelier v8">`
suffit, et c'est aussi ce qui trace la version de recette utilisée. Une meta
absente ou un atelier inconnu de la table retombent sur `fiction`.

### `book:variant-of` (optionnelle, cas rare)

Réservée aux **éditions dérivées** : un livre qui est une autre édition d'un
livre déjà publié déclare le slug de ce livre source
(`<meta name="book:variant-of" content="lequation-du-calme">`), ce qui permet au
catalogue de les regrouper au lieu de les afficher en doublon. Le slug doit
exister sous `livres/` (`<slug>.html` ou dossier `<slug>/`) et ne peut pas être
celui du livre lui-même. **Ne pas l'utiliser pour créer un doublon** : le
moratoire sur les éditions dérivées (§« Interdits spécifiques ») reste en
vigueur. Un livre ordinaire n'a pas cette meta.

## Le moteur de liseuse

- **Source unique** : [`livres/_template/index.html`](../../livres/_template/index.html)
  (`atelier-liseuse v3`), copié tel quel. Les trois défauts historiques du
  moteur (audit §B.4 : `close()` écrasé, `entry()` sans garde, recherche du
  codex) y sont corrigés — ne pas les réintroduire en copiant un ancien livre.
- **Données** : le récit vit dans l'îlot
  `<script type="application/json" id="book-data">`, dont la structure est
  spécifiée champ par champ dans
  [`livres/_template/DONNEES.md`](../../livres/_template/DONNEES.md).
- **Persistance** : la clé localStorage `<slug>-state-v1` est dérivée de
  `meta.slug` par le moteur — renseigner `meta.slug` correctement suffit.
- **Modules optionnels** (v3) : les blocs `map` et `relations` de l'îlot
  ajoutent une carte des lieux et un graphe de relations, avec leur bouton de
  barre, leur entrée de sommaire et leur équivalent textuel (étape 3 bis).
  Absents de l'îlot, ils n'existent pas pour le lecteur : c'est le défaut.
- **Impression** (v3) : la vue affichée s'imprime sans le mobilier de la liseuse
  — rien à faire, mais ne pas casser la feuille `@media print` en adaptant la
  palette.
- **Fonctionnalités à ne pas régresser** : sommaire, `role="progressbar"` mis à
  jour, codex à déverrouillage robuste au rechargement, thème sombre, taille de
  police, piège de focus dans les dialogues, région `aria-live` pour les
  déblocages, `prefers-reduced-motion`, échappement HTML systématique des
  données de l'îlot, visionneuse d'images, dégradation propre des images
  manquantes, impression propre, et — si le brief les demande — carte et graphe
  de relations à révélation progressive.

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
- [ ] `<meta name="book:workflow" content="roman-atelier v8">` et
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
      avec description structurée (Rôle : Production / roman-atelier v8),
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
