# DONNEES.md — spécification de l'îlot `#book-data` (atelier-liseuse v1)

Spécification **normative** des données embarquées dans un livre de la famille
« Atelier » : le bloc `<script type="application/json" id="book-data">` du point
d'entrée HTML. Le moteur de [`index.html`](index.html) lit exactement ce qui est
décrit ici ; l'exemple minimal embarqué dans le template illustre chaque champ.

Deux natures de champs :

- **[moteur]** : lu par le JavaScript de la liseuse — une erreur casse le rendu.
- **[éditorial]** : jamais lu par le moteur ; documente la méthode (anti-
  divulgâchage, audit d'entités, briefs d'illustration). Ces champs sont
  **obligatoires quand même** là où indiqué : ils sont le contrat de qualité que
  `ateliers/roman-atelier/outils/verifier.py` contrôle, et la matière première du
  manifeste d'illustrations.

Tout le contenu est en français. Le JSON doit être valide (vérification :
`python -c "import json,re,sys;h=open(sys.argv[1],encoding='utf-8').read();json.loads(re.search(r'<script type=\"application/json\" id=\"book-data\">(.*?)</script>',h,re.S).group(1))" livres/<slug>/index.html`).

## Racine

| Champ | Type | Statut | Nature |
|---|---|---|---|
| `meta` | objet | obligatoire | mixte |
| `world` | objet | obligatoire | éditorial |
| `entityAudit` | objet | obligatoire | éditorial |
| `cover` | objet | obligatoire | moteur |
| `chapters` | tableau | obligatoire | moteur |
| `codex` | tableau | obligatoire | moteur |

## `meta`

| Champ | Type | Statut | Nature | Contenu |
|---|---|---|---|---|
| `slug` | chaîne | obligatoire | [moteur] | Identique au dossier `livres/<slug>/`. Sert de racine à la clé localStorage `<slug>-state-v1`. |
| `title` | chaîne | obligatoire | [moteur] | Identique à `book:title` du `<head>`. Affiché en accueil et en marque de barre. |
| `author` | chaîne | obligatoire | [éditorial] | Identique à `book:author` du `<head>` (nom du ou des modèles). |
| `description` | chaîne | obligatoire | [moteur] | Identique à `book:description`. Affichée en accueil. |
| `tags` | tableau de chaînes | obligatoire | [éditorial] | Identiques à `book:tags`. |
| `date` | chaîne | obligatoire | [éditorial] | Identique à `book:date` (`AAAA-MM-JJ`). |
| `language` | chaîne | obligatoire | [éditorial] | `"fr"`. |
| `edition` | chaîne | optionnel | [moteur] | Sur-titre d'accueil (ex. `"Roman explorable"`). Défaut : rien, seul « N chapitres » s'affiche. |
| `codexLabel` | chaîne | recommandé | [moteur] | Nom court du codex, affiché en tête de la vue codex et de chaque notice (ex. `"Dossier ALCYONE/LISERON"`). Défaut : `"Codex"`. |
| `codexVoice` | chaîne | obligatoire | [moteur] | La voix située du codex : qui le tient, sur quel ton, à partir de quelles sources. Affichée en introduction de la vue codex ; toutes les notices s'écrivent dans cette voix. |

## `world` — l'univers pensé avant d'être écrit

Exigé par `docs/conception/PREFERENCES.md` §Fond. Tout est [éditorial].

| Champ | Type | Statut | Contenu |
|---|---|---|---|
| `emotionalPromise` | chaîne | obligatoire | Ce que le lecteur doit éprouver (une phrase). |
| `centralIdea` | chaîne | obligatoire | L'idée centrale, une phrase affirmative. |
| `satellites` | tableau de chaînes | recommandé | 2 à 5 idées secondaires qui orbitent autour de l'idée centrale. |
| `thematicQuestion` | chaîne | obligatoire | La question que le récit pose sans y répondre à la place du lecteur. |

## `entityAudit` — l'audit des entités sans notice

[éditorial]. Preuve que le périmètre du codex est un choix et non un oubli :
toute entité nommée dans le récit qui n'a **pas** de notice y est listée avec sa
raison.

| Champ | Type | Statut | Contenu |
|---|---|---|---|
| `excluded` | tableau d'objets `{label, reason}` | obligatoire (peut être vide) | `label` : le nom tel qu'il apparaît dans le texte ; `reason` : pourquoi pas de notice (couverte par une autre, purement fonctionnelle…). |

## `cover`

| Champ | Type | Statut | Nature | Contenu |
|---|---|---|---|---|
| `image` | chaîne | obligatoire | [moteur] | Chemin **relatif au livre** vers la couverture : `../../couvertures/<slug>.webp`. Affichée en accueil ; masquée proprement si le fichier manque encore. |
| `catalogImage` | chaîne | obligatoire | [éditorial] | Le même fichier vu depuis la racine du dépôt : `couvertures/<slug>.webp`. |
| `alt` | chaîne | obligatoire | [moteur] | Description de la couverture pour les lecteurs d'écran. |

## `chapters[]`

| Champ | Type | Statut | Nature | Contenu |
|---|---|---|---|---|
| `id` | chaîne | obligatoire | [moteur] | `chapitre-<n>` (ex. `chapitre-1`). Unique. Sert d'ancre d'URL `#chapter/<id>`. |
| `number` | entier | obligatoire | [moteur] | Numéro affiché, 1..N, dans l'ordre du tableau. Sert de clé de progression. |
| `title` | chaîne | obligatoire | [moteur] | Titre du chapitre. |
| `blocks` | tableau | obligatoire | [moteur] | Voir ci-dessous. |
| `image` | chaîne | obligatoire (livre illustré) | [moteur] | `images/chapter-NN.webp`, NN = `number` sur 2 chiffres. Bandeau d'ouverture du chapitre, zoomable. Masqué proprement tant que le fichier n'existe pas (phase d'attente de l'illustrateur). |
| `alt` | chaîne | obligatoire si `image` | [moteur] | Texte alternatif : ce que l'image **montre**, une phrase concrète (personnes, lieu, action, lumière) — pas une légende d'ambiance. Sert aussi de légende affichée. |
| `visualDescription` | chaîne | obligatoire si `image` | [éditorial] | Brief de l'illustration : cadrage, sujet, heure/lumière, ambiance. C'est la source du prompt dans `illustrations.md`. |
| `imageWidth`, `imageHeight` | entiers | optionnels | [moteur] | Dimensions intrinsèques de l'image. Défaut : 1600×900 (la convention de l'atelier). Ne les renseigner que si l'image déroge. |

### `chapters[].blocks[]`

Un bloc = un paragraphe du récit.

| Champ | Type | Statut | Nature | Contenu |
|---|---|---|---|---|
| `id` | chaîne | obligatoire | [moteur] | `c<chapitre>-b<NN>` (ex. `c1-b01`, NN sur 2 chiffres). Unique dans tout le livre. Cible des déverrouillages et des liens profonds `#chapter/<id-chapitre>/<id-bloc>`. |
| `text` | chaîne | obligatoire | [moteur] | Le paragraphe, texte brut (échappé par le moteur — jamais de HTML). |
| `mentions` | tableau de chaînes | obligatoire (peut être vide) | [moteur] | Ids de notices du codex évoquées par ce paragraphe. Affichées en références contextuelles sous le bloc (« Notice à venir » tant que verrouillées). Chaque id doit exister dans `codex[]`. |

## `codex[]` — les notices

Champs lus par le moteur :

| Champ | Type | Statut | Contenu |
|---|---|---|---|
| `id` | chaîne | obligatoire | kebab-case ASCII (ex. `phare-de-kervel`). Unique. Référencé par `mentions`, `links` et l'URL `#codex/<id>`. |
| `title` | chaîne | obligatoire | Titre de la notice. |
| `category` | chaîne | obligatoire | Catégorie affichée (ex. `personnage`, `lieu`, `objet`, `concept`, `institution`, `événement` — libre, mais cohérente dans le livre). |
| `hook` | chaîne | obligatoire | Accroche d'une phrase, sans divulgâcher (c'est elle qu'on voit sur la carte). |
| `text` | chaîne | obligatoire | Corps de la notice, dans la voix de `meta.codexVoice`. Paragraphes séparés par une ligne vide (`\n\n`). |
| `links` | tableau de chaînes | obligatoire (peut être vide) | Ids de notices liées (navigation entre fiches). Chaque id doit exister. |
| `unlockBlock` | chaîne | obligatoire | Id du bloc dont la lecture déverrouille la notice. Doit exister dans un chapitre. |
| `image` | chaîne | optionnel | `images/codex-<id>.webp`. Colonne illustrée de la fiche. |
| `alt` | chaîne | obligatoire si `image` | Comme pour les chapitres. |
| `visualDescription` | chaîne | obligatoire si `image` | Comme pour les chapitres. |
| `imageWidth`, `imageHeight` | entiers | optionnels | Comme pour les chapitres. |

Champs de méthode anti-divulgâchage — tous [éditorial], **obligatoires** (c'est
la marque de qualité des livres récents ; `verifier.py` contrôle leur présence
et leur cohérence) :

| Champ | Type | Contenu |
|---|---|---|
| `firstMentionChapter` | entier | Numéro du chapitre de la première mention de l'entité dans le texte. |
| `firstMentionBlock` | chaîne | Id du bloc de cette première mention. |
| `earliestSafeChapter` | entier | Premier chapitre où lire la notice ne divulgâche rien. |
| `earliestSafeBlock` | chaîne | Id du premier bloc « sûr ». |
| `unlockChapter` | entier | Numéro du chapitre de `unlockBlock` (redondance de contrôle). |
| `unlockPosition` | entier | Position (1-indexée) de `unlockBlock` dans son chapitre (redondance de contrôle). |
| `spoilerRisk` | chaîne | `aucun`, `modéré` ou `fort` : risque si la notice était lue dès la première mention. |
| `delayReason` | chaîne | Pourquoi le déverrouillage est retardé au-delà de la première mention (vide si `unlockBlock` = `firstMentionBlock`). |
| `editorialFunction` | chaîne | Ce que la notice apporte au lecteur, en une phrase (son rôle dans l'économie du récit). |

Règles de cohérence (vérifiées par
`python ateliers/roman-atelier/outils/verifier.py livres/<slug>`) :

- `unlockBlock` ≥ `earliestSafeBlock` ≥ `firstMentionBlock` dans l'ordre de
  lecture ;
- chaque notice est atteignable : son `id` apparaît dans les `mentions` d'au
  moins un bloc (aucune fiche orpheline) ;
- aucune `mention` ni aucun `link` ne pointe vers un id inexistant (aucun lien
  mort) ;
- `unlockChapter`/`unlockPosition` correspondent bien à la position réelle de
  `unlockBlock`.

## Ce que le moteur ignore

`world`, `entityAudit`, `meta.author/tags/date/language`, `cover.catalogImage`
et tous les champs anti-divulgâchage voyagent dans le fichier sans être lus par
le JavaScript : ils font partie du livrable (traçabilité de la méthode) et sont
exploités par la relecture, le manifeste d'illustrations et `verifier.py`.
