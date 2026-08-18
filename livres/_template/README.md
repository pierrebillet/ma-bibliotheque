# livres/_template/ — moteur de liseuse de référence « Atelier »

- **Version du moteur** : `atelier-liseuse v2` (déclarée par
  `<meta name="reader-engine">` dans chaque livre qui l'embarque).
- **Rôle** : c'est la brique commune annoncée par
  [`docs/conception/creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md)
  §6 (chantier n° 2 de la roadmap Conception). Les livres de l'atelier
  [`roman-atelier`](../../ateliers/roman-atelier/WORKFLOW.md) (v3+) se créent en
  **copiant ce dossier**, plus jamais en recopiant le dernier livre publié.
- Ce dossier est **exclu du catalogue** par `scripts/build_catalog.py` (préfixe
  `_`) : il peut embarquer des placeholders sans risque.

## Contenu

| Fichier | Rôle |
|---|---|
| [`index.html`](index.html) | Le moteur complet, avec un `<head>` gabarit (11 meta `book:*` et leurs vocabulaires fermés en commentaire) et un îlot JSON d'exemple minimal (2 chapitres, 3 notices) qui illustre chaque champ. |
| [`DONNEES.md`](DONNEES.md) | Spécification normative de l'îlot `#book-data` : champs, types, obligatoire/optionnel, champs lus par le moteur vs champs éditoriaux, règles de cohérence. |

## Créer un livre à partir du template

Procédure détaillée dans
[`ateliers/roman-atelier/WORKFLOW.md`](../../ateliers/roman-atelier/WORKFLOW.md).
En bref :

1. `cp livres/_template/index.html livres/<slug>/index.html` (jamais de copie du
   `README.md` ni de `DONNEES.md` dans le dossier du livre) ;
2. remplacer tout le `<head>` gabarit (11 meta `book:*` — dont les cinq metas
   qualitatives à vocabulaire fermé listées en commentaire et `book:capacites` —,
   `book:workflow`,
   titre) ; `book:variant-of` reste commentée sauf édition dérivée ; conserver
   `<meta name="reader-engine" content="atelier-liseuse v2">` telle quelle ;
3. remplacer intégralement l'îlot JSON d'exemple (spec : `DONNEES.md`) ;
4. ne pas modifier le `<script>` du moteur. Toute divergence doit être signalée
   dans la PR (règle de `roman-atelier`) ; une amélioration durable se fait ici,
   dans le template, avec incrément de la version `atelier-liseuse`.

La feuille de style est un point de personnalisation **autorisé** : les
variables de `:root` et `[data-theme="dark"]` (palette) peuvent être adaptées à
l'univers du livre ; le reste du CSS se conserve tel quel.

## Origine et changelog du moteur

- **atelier-liseuse v2** (2026-08) — figures documentaires, pour le format
  reportage (session Conception du 2026-08-17) :
  - champ optionnel `figure` sur les blocs de chapitre : image affichée **entre
    deux paragraphes** avec légende visible et, pour un document récupéré sur le
    web, crédit « Source : … » lié à la page d'origine (spécification :
    [`DONNEES.md`](DONNEES.md) §`chapters[].blocks[].figure`) ;
  - champ optionnel `source` sur les notices du codex : même crédit sous
    l'image de la fiche quand elle est un document du web ; **la présence de
    `source` distingue le document récupéré de l'illustration générée** (qui,
    elle, ne cite pas de source) ;
  - garde-fous : fichier image local uniquement (URL absolue refusée), lien de
    source limité à `http(s)://`, échappement des attributs (`escA`), figure
    incomplète ignorée, figure entière masquée si le fichier manque (même
    dégradation propre qu'en v1) ; dimensions intrinsèques libres (pas de
    1600×900 imposé aux documents), `loading="lazy"`, zoom par la visionneuse
    existante ;
  - rétrocompatible : sans `figure` ni `source`, rendu identique à v1 ; les
    livres publiés (copies embarquées du moteur) ne sont pas régénérés.
- **atelier-liseuse v1** (2026-08) — moteur extrait de
  `livres/lequation-du-calme-illustree/` (le plus abouti du catalogue), avec les
  corrections et durcissements suivants :
  - les trois défauts connus du moteur (audit
    [`docs/audits/2026-08-rapport-etonnement.md`](../../docs/audits/2026-08-rapport-etonnement.md)
    §B.4) sont corrigés : `function close()` renommée `closeDialog()` (n'écrase
    plus `window.close`) ; tous les appels à `entry(id)` sont gardés (un id de
    codex inexistant n'interrompt plus le rendu : la référence est retirée) ; la
    recherche du codex n'escamote plus les fiches verrouillées pendant la frappe
    (correction de précédence `||`/`&&`) ;
  - **dégradation propre quand une image manque** : bandeau de chapitre, image
    de notice et couverture se masquent au lieu d'afficher une image cassée —
    c'est ce qui permet la fabrication en deux temps (texte d'abord, images de
    l'illustrateur ensuite) du workflow v3 ;
  - `width`/`height` sur les images injectées (défaut 1600×900, surchargeables
    par `imageWidth`/`imageHeight`) et `loading="lazy"` hors première image
    (exigence de `PREFERENCES.md` §Forme, jusqu'ici non tenue) ;
  - la clé localStorage est dérivée de `meta.slug` (`<slug>-state-v1`) au lieu
    d'être recopiée à la main — la convention ne peut plus être violée ;
  - l'accueil et l'en-tête du codex se remplissent depuis `meta`/`cover` (titre,
    description, couverture, voix du codex) au lieu d'être dupliqués en dur dans
    le HTML — une seule source de vérité, l'îlot.

Fonctionnalités garanties (à ne jamais régresser, cf. `WORKFLOW.md` §« Le moteur
de liseuse ») : sommaire, `role="progressbar"`, codex à déverrouillage robuste
au rechargement, thème sombre, taille de police, piège de focus dans les
dialogues, `aria-live`, `prefers-reduced-motion`, échappement HTML systématique,
visionneuse d'images, reprise de lecture.
