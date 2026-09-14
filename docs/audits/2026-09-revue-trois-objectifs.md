# Revue des trois objectifs — Ma Bibliothèque (septembre 2026)

> Note : document d'audit non normatif, dans l'esprit du
> [rapport d'étonnement](2026-08-rapport-etonnement.md) et du
> [regard d'auteur](2026-08-regard-auteur.md). Les décisions qui en découlent vivent
> dans les documents normatifs (roadmaps, recettes) ; ce fichier garde la trace du
> **pourquoi** et de la direction proposée.

Revue réalisée le 4 septembre 2026, à la demande de Pierre : *où en sommes-nous, quelles
erreurs avons-nous faites, quelle est la bonne direction ?* — selon les trois objectifs du
projet : (1) explorer les interactions possibles d'un livre HTML, (2) concevoir une
machine qui produit ces récits, (3) offrir une bibliothèque pour les lire.

> Méthode : lecture des documents de
> pilotage, du moteur et de la recette canonique, trois inventaires parallèles (livres,
> machine, bibliothèque), historique git, corps des 30 PR, puis vérification de
> faisabilité des corrections proposées dans le code. Limites : le site public n'a pas pu
> être ouvert depuis cet environnement (réseau sortant bloqué) ; le clone est superficiel,
> donc un `catalog.json` régénéré ici ne se compare pas à celui de la CI.

## Contexte

Six semaines d'existence (premier commit le 24 juillet 2026), mais l'essentiel s'est fait
en douze jours, du 12 au 24 août : 157 des 165 commits et les 30 PR, toutes mergées.
Rien depuis le 24 août. Aucune PR ouverte, aucune issue.

Répartition des 30 PR : 13 Conception (docs, recettes, moteur), 9 Bibliothèque
(plateforme), 8 Production (livres). Documentation active : ~34 000 mots pour ~5 400
lignes de code. La recette roman en est à sa version 9 ; trois romans ont été produits
avec elle.

---

## 1. Où en sommes-nous ?

**En une phrase : la bibliothèque est finie, la machine tourne, l'exploration n'a pas
commencé — alors que les deux documents de vision la désignent comme « l'objectif
majeur d'innovation ».**

### Objectif 3 — la bibliothèque : atteint (1.0 le 18 août)

- `index.html` autonome (zéro dépendance), accessibilité sérieuse (skip-link, listbox
  ARIA conforme, `aria-live` ciblé), recherche insensible aux accents, onglets
  fiction/reportage, filtres genre et tag, tris, badges, URL partageable.
- `scripts/build_catalog.py` (stdlib, 23 tests verts), CI complète : vérification en PR,
  garde contre l'édition manuelle des trois artefacts générés, régénération après merge.
- Catalogue schéma v3, 15 livres, tous les champs remplis. Doc technique presque sans
  dérive.
- **Ce qui manque** : aucune fonction transverse de lecture (zéro `localStorage` dans
  l'index : pas de « reprendre ma lecture », pas de progression, pas de favoris) ;
  15 cartes pour 13 œuvres (deux paires d'éditions dérivées) ; badge « capacités » sans
  pouvoir discriminant (13 livres sur 15 = `codex` seul) ; `exigence` et `audience`
  saisis 15/15 mais ni filtrables, ni cherchables, ni affichés ; le tri par défaut
  re-trie côté client sur `book:date` (précision jour, 5 ex æquo — `index.html`
  l. 2182-2187) et abandonne l'ordre par date git que la CI paie en `fetch-depth: 0`.

### Objectif 2 — la machine : fonctionne, mais lourde et dépendante de Pierre

- Deux ateliers (`roman-atelier` v9, `reportage` v7), un tronc commun, un socle
  éditorial, un moteur versionné (`atelier-liseuse v3`), un vérificateur (687 lignes).
- **Preuve que ça marche** : 4 livres produits par la recette, 0 défaut au vérificateur,
  par deux modèles différents (Claude Fable, GPT 5.6) exécutant la recette à froid.
  Passe auteur des *Moules de la colère* : 17 000 mots, 31 notices, dossier
  documentaire, en **59 minutes** d'agent et 11 commits d'étapes.
- **Ce qui coince** :
  - ~12 600 mots de lecture obligatoire avant d'écrire un mot (AGENTS + WORKFLOW +
    TRONC-COMMUN + PREFERENCES + DONNEES + BRIEF + GABARIT-ILLUSTRATIONS).
  - Publication en **2,5 jours** pour 1 h de travail d'agent : quatre points de contact
    humains (rédiger le brief, lancer l'agent, relayer à l'illustrateur, merger). Le relai
    illustrateur a attendu 26 h, puis Pierre a généré lui-même les 23 images avec Codex.
  - Le vérificateur, présenté comme le contrôle bloquant amont, **n'est pas exécuté en
    CI** et n'a aucun test. La règle « le `<script>` du moteur ne se modifie pas » n'est
    contrôlée par rien : le parc compte 14 blobs JS distincts.
  - Le brief est en pratique de la prose libre ; l'agent a dû écrire une « lecture du
    brief » de 20 lignes (`livres/les-moules-de-la-colere/brief.md`). Selon
    `creer-un-atelier.md` §3 c'est par définition un défaut de recette — jamais réinjecté.
  - Registre et gabarit en dérive : le template déclare encore `roman-atelier v7`
    (recette v9) ; le seul livre v9 n'est pas dans les « exemples publiés » ; deux livres
    cités comme « v2 » ne portent aucune meta `book:workflow`.

### Objectif 1 — l'exploration : pas commencée

- **Interactions nettes nouvelles depuis juillet : zéro.** Les livres GPT de juillet
  (`le-livre-des-routes`, `les-longues-routes`) avaient déjà carte SVG, graphe de
  relations et impression. La standardisation d'août les a perdus ; le moteur v3
  (19 août) les a réintroduits comme modules… **utilisés par aucun livre produit par la
  recette**.
- `choix` (branches) et `audio` figurent dans le vocabulaire des capacités et ne sont
  implémentés nulle part. Pas d'annotations, de frise, de bascule de point de vue, de
  synthèse vocale. Le « récit explorable » reste le codex à déverrouillage de juillet.
- **Aucun lieu pour une expérience jetable** : tout artefact doit être un livre
  catalogable avec 11 metas, brief, vérificateur et révision en deux passes.
- **Aucun retour de lecture** : les deux audits parlent de process et de code, jamais de
  « était-ce bon à lire ? le déverrouillage apporte-t-il quelque chose ? ». Sans capteur,
  la boucle « produire → observer → formaliser » de la VISION tourne à vide sur le fond.

### Le parc de livres

- 15 livres, **14 moteurs JS distincts** : 5 moteurs uniques de juillet (dont 3 sans
  îlot JSON — texte en littéraux JS, invisibles au comptage de mots) et une lignée
  « Atelier » pré-v1 → v1 → v2 → v3. Seuls 3 fichiers partagent un moteur
  byte-identique (`_template`, `les-moules-de-la-colere`, `loi-malraux`).
- 51 Mo, dont **~40 Mo de JPEG** (400–740 Ko l'image) dans 4 livres, pour une règle
  « WebP ≤ 150 Ko ». Les deux éditions illustrées sont byte-identiques à leur texte
  d'origine : 23 Mo pour republier 43 000 mots déjà présents.
- Clés `localStorage` : 7 canoniques (`<slug>-state-v1`), 3 hors convention, 5 livres
  sans aucune persistance. Le champ `chapter` est pourtant déjà stocké par 10 livres :
  la donnée d'un « reprendre ma lecture » existe, personne ne la lit.

---

## 2. Quelles erreurs avons-nous faites ? Comment les corriger ?

| # | Erreur | Preuve | Correction |
|---|---|---|---|
| E1 | **La gouvernance a mangé l'exploration.** 22 PR de plateforme et de recettes pour 8 de production ; 9 versions de recette pour 3 romans ; deux visions, deux roadmaps, un registre, un vivier, des changelogs — et zéro forme de lecture nouvelle | répartition des PR ; `docs/conception/IDEES.md` (table « écartées » vide) | Geler les documents de pilotage (mise à jour d'une ligne de statut, pas plus). Pas de version de recette sans verdict d'une expérience ou interprétation remontée par un pilote. L'innovation retourne dans des prototypes, pas dans des documents |
| E2 | **L'exploration est soumise aux règles de la production.** Impossible d'essayer une idée sans en faire un livre complet | `docs/conception/README.md` (« un format sans atelier n'est pas terminé »), `creer-un-atelier.md` §1 | Ouvrir `labo/` à la racine (hors `livres/`, donc hors catalogue et hors CI — vérifié) : un fichier HTML par idée, une page de notes, un verdict. Aucune autre règle |
| E3 | **Le « palier 0 » est posé comme condition et rendu impossible par une autre règle.** Toute fonction transverse attend le moteur unifié, mais « les livres publiés ne sont pas régénérés » : le parc ne s'unifiera jamais | `docs/bibliotheque/VISION.md` palier 0 ; `ateliers/README.md` l. 18-19 | Séparer **l'œuvre (l'îlot JSON) de la liseuse (la coquille)**. Un script de ré-encapsulage réinjecte la coquille du template autour de l'îlot. Faisable mécaniquement sur 7 livres (îlots déjà conformes ou à 1-2 champs près) ; `la-part-des-pluies` (schéma antérieur : `reveal`/`unlock`) et les 5 livres de juillet sont marqués `hérité`. L'œuvre est intouchée, la coquille est du logiciel |
| E4 | **Les doublons ont été conservés** alors que `variantOf`, condition annoncée de levée du moratoire, est livré depuis le 17 août | `AGENTS.md` l. 82-85 ; `catalog.json` (2 `variantOf`) | Fusionner chaque paire en un livre illustré sous le slug d'origine ; supprimer `-v2` et `-illustree` ; images en WebP ; anciennes URL redirigées par `404.html` (servi à toute profondeur par Pages), sans stub dans `livres/` — un stub y serait catalogué |
| E5 | **Contrôle qualité déclaratif.** Vérificateur hors CI et sans test ; « aucun texte sur la couverture » énoncé 5 fois, vérifié par personne ; « moteur non modifié » sans contrôle | `.github/workflows/catalog.yml` (aucune mention de `verifier.py`) ; `tests/` (un seul fichier) | La CI exécute le vérificateur pour tout livre portant `book:workflow` (les 4 livres de recette passent déjà ; les anciens en sont exempts) ; 4 tests du vérificateur |
| E6 | **Chaque règle vit en 4 à 6 endroits.** Densité 40 % (6 endroits), contraintes d'images (5), « supprimer map/relations » (5), vocabulaires fermés (3 copies synchronisées à la main). La dérive s'est produite deux fois de la même façon | `verifier.py` l. 82-84 et `build_catalog.py` l. 60-63 (« tenir synchrone ») | Une règle = un endroit, les autres renvoient. À faire dans le prochain bump de recette motivé par une forme promue — pas avant (un bump sans motif contredirait E1) |
| E7 | **On saisit ce qui se dérive, on ignore ce qu'on calcule.** 10 champs anti-divulgâchage par notice jamais lus par le moteur (310 champs pour *Moules*) ; `unlockChapter`/`unlockPosition` recalculés par le vérificateur ; `illustrations.md` (21 Ko) recopie l'îlot ; `exigence`/`audience` remplis 15/15 et inexploités ; dates git calculées et ignorées par l'index | `DONNEES.md` l. 224-225 et 256-261 ; `index.html` l. 2182-2187 | Rendre optionnel ce qui se dérive (même bump que E6). Afficher `exigence`/`audience` plutôt que les retirer (retrait = schéma v4, cinq fichiers). Tri par défaut = ordre du catalogue |
| E8 | **Boucle d'amélioration sans capteur.** Aucune lecture évaluée ; densité de mentions à 98–100 % sur deux livres (Goodhart) ; merge en 7 minutes médianes, sans relecture | PR #17, #25, #29 : création → merge en 1 à 3 min | Une fiche de lecture par livre lu, 5 questions fixes, 10 minutes de Pierre. Assumer que la PR est de la traçabilité, pas une revue |
| E9 | **La machine dépend de Pierre à 4 points**, le relai illustrateur en tête (26 h, puis fait à la main) | PR #29/#30 ; commit `c57f9c0` (Pierre, 01:41) | L'agent auteur enchaîne la passe illustration s'il génère des images ; sinon il prépare le message de relai. Cible : 2 points de contact (brief → merge) |
| E10 | **Petites dérives** : template `roman-atelier v7` ; README racine « 5 metas » (13 réelles), CATALOGUE « 12 » vs AUTOMATISATION « treize » ; bloc de 22 lignes d'instructions du gabarit livré en production dans 2 livres ; `lequation-du-calme/lequation-du-calme.html` viole la règle `index.html` ; test d'or contradictoire corrigé après coup (commit `2c35946`) | rapports livres et bibliothèque | Corriger au fil des sessions ci-dessous, sans PR dédiée. **Ne pas renommer** les `<slug>.html` en `index.html` : le calcul de date d'ajout (`--diff-filter=A --no-renames`) ferait sauter le livre en tête du catalogue |

Les erreurs ne sont pas des fautes de qualité : le code et la doc sont bons. Ce sont des
erreurs **d'allocation** (l'effort est allé au cadre, pas au cœur) et **de conception**
(des règles qui se neutralisent : palier 0 vs non-régénération ; standard de recette vs
brief libre ; contrôle bloquant vs CI qui ne l'appelle pas).

---

## 3. Quelle est la bonne direction ?

**Principe : recentrer sur l'objectif 1.** Les objectifs 2 et 3 sont « assez bons » ;
on n'y touche que pour servir le 1 — débloquer les fonctions transverses (E3, E4) et
réduire la friction (E5, E9). Tout le reste est gelé : pas de nouveau document de
pilotage, pas de bump de recette sans verdict, pas de filtre par capacité tant que
13 livres sur 15 n'en ont qu'une, pas de PWA, de comptes ni de « 2.0 » tant qu'un second
utilisateur réel n'existe pas.

### Prochaine session (≤ 2 h d'agent)

Deux sessions disjointes en fichiers, donc deux PR parallélisables. **A d'abord** (elle
sert l'objectif 1) ; B si une seconde session est disponible.

**Session A — Conception : ouvrir le labo, première expérience « embranchements »**
(branche `conception/labo-embranchements`)

1. `labo/README.md` (~20 lignes) : un fichier HTML par expérience, une idée ; pas de
   metas, brief ni vérificateur ; zéro dépendance externe et `<meta name="robots"
   content="noindex">` ; `NOTES.md` ≤ 10 lignes terminé par un verdict — *garder* →
   module du moteur + option de recette, *jeter* → ligne dans `IDEES.md` « écartées » ;
   hors catalogue et hors CI ; pas de seconde expérience avant le verdict de la première.
2. `labo/embranchements/index.html` : **copie du gabarit v3** (pour que la promotion soit
   un diff du moteur, pas une réécriture). Îlot : `blocks[].choices:[{label,target}]`,
   `chapters[].ending:true`. Moteur : boutons de choix sous le bloc, `state.path` et
   `state.endings` persistés, sommaire limité aux chapitres visités, « Fins découvertes :
   x/y » en accueil. 6-8 chapitres courts, 2-3 fins — l'objet est l'interaction, pas le
   texte.
3. `labo/embranchements/NOTES.md` : idée, essais, questions ouvertes, verdict « en attente
   de la fiche de lecture ».
4. `docs/lectures/GABARIT.md` : les 5 questions (fini ? où arrêté ? codex ouvert — le
   déverrouillage a-t-il apporté quelque chose ? une chose à garder ; une à jeter). Une
   ligne dans `docs/README.md`.
5. Une ligne dans la table des rôles d'`AGENTS.md` ; `livres/_template/index.html` l. 40 :
   `v7` → `v9`.

Vérifier : `python -m http.server` puis jouer les deux fins, recharger → parcours
persistant ; `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
→ toujours 15 livres ; `python -m unittest discover -s tests` vert ; `git diff --stat` :
rien sous `livres/` hors la ligne du gabarit.

**Session B — Bibliothèque : tri de l'index, vérificateur en CI, repli de date**
(branche `bibliotheque/tri-catalogue-verificateur-ci`)

1. `index.html` `sortBooks` (l. 2180-2198) : si `state.sort === DEFAULT_SORT`, rendre
   l'ordre du catalogue tel quel ; supprimer la branche `date-desc` et `dateKey`.
2. `.github/workflows/catalog.yml`, job `verification` : étape bash (~10 lignes) qui
   lance `livres/_template/outils/verifier.py` sur chaque livre dont le point d'entrée
   contient `name="book:workflow"`, statut cumulé.
3. `tests/test_verifier.py` : 4 tests par `subprocess` sur une copie du gabarit
   (`--sans-images`) : conforme → 0 ; `unlockBlock` cassé → 1 ; clé `KEY` modifiée → 1 ;
   `book:genre` retirée → 1.
4. `scripts/build_catalog.py` `addition_date` (l. 869-880) : repli sur la plus ancienne
   date connue des chemins historiques du slug (`livres/<slug>.html`,
   `livres/<slug>/<slug>.html`, `livres/<slug>/index.html`) + 1 test — prérequis de la
   fusion de `la-doublure` (fichier plat → dossier).
5. Une ligne dans `docs/bibliotheque/AUTOMATISATION.md` et `FRONTEND.md`.

Vérifier : `python -m unittest discover -s tests -v` ; la boucle en local → 4 × « Aucun
défaut — livre conforme » ; `python -m http.server` → ordre des cartes = ordre de
`catalog.json` (témoin : le trio du 11 août, aujourd'hui inversé) ; `?sort=title-asc`
fonctionne ; `git diff --quiet -- catalog.json sitemap.xml`.

### Dans une semaine (3 à 5 sessions d'agent, 30 minutes de Pierre)

| Ordre | Rôle | Session | Prérequis |
|---|---|---|---|
| S1 | Conception | Labo + embranchements (session A) | — |
| S1′ | Bibliothèque | Tri, vérificateur CI, repli de date (session B), en parallèle | — |
| S2 | **Pierre** (30 min, pas une session agent) | Deux fiches `docs/lectures/` : `labo/embranchements` et un livre récent jamais lu (`loi-malraux` ou `les-moules-de-la-colere`) → verdict de l'expérience 1 | S1 |
| S3 | Conception | `livres/_template/outils/reencapsuler.py` (stdlib ; dry-run par défaut ; idempotent sur `loi-malraux`, refuse `la-part-des-pluies`) + tests. **Si S2 dit « garder »** : moteur v4 = module `choix` (spec `DONNEES.md`, contrôle vérificateur) et bump `roman-atelier` v10 — le seul bump autorisé, motivé par un verdict ; y regrouper E6 et E7 | S2 |
| S4 | Production | Flotte : script appliqué en place aux 7 livres Atelier (sans renommage) ; fusion des deux paires (`lequation-du-calme/`, `la-doublure/` en dossier) ; conversion WebP de `les-ombres-de-midi`, `la-part-des-pluies` et des images fusionnées (cwebp ou Pillow dans l'environnement de l'agent, rien en CI) ; redirections dans `404.html` ; `hérité` pour les 5 livres de juillet et `la-part-des-pluies` | S3, S1′, choix de couvertures par Pierre |
| S5 | Production | Pilote à froid `roman-atelier` avec un brief exigeant **carte + relations** : les modules v3 n'ont aucun livre depuis le 19 août ; premier livre à trois capacités ; fiche de lecture ensuite | S4 pour profiter de la CI |
| S6 (si temps) | Bibliothèque | « Reprendre ma lecture » sur les cartes (lecture de `<slug>-state-v1`, ~25 lignes, schéma intact) ; afficher `exigence`/`audience` | S4 |

### À la fin

Le projet est « fini » quand ces quatre états sont vérifiables, pas quand une version est
atteinte :

1. **Un catalogue de formes lues** : au moins **trois formes** de lecture (codex à
   déverrouillage ; carte et relations ; une forme issue du labo), chacune avec module du
   moteur + option de recette + au moins un livre + **une fiche de lecture positive**.
   La table « écartées » d'`IDEES.md` n'est plus vide. (L'ambition « 5 à 8 formes » est
   pour plus tard ; sans fiche de lecture, « bonne forme » n'est pas mesurable.)
2. **Deux points de contact par livre** : Pierre écrit le brief et clique merge ; 1 PR par
   livre, 0 relai humain — donc relai illustrateur automatisé (travail objectif 2, après
   la semaine).
3. **Le test du fork** (objectif 2, secondaire) : clone frais, un agent qui n'est pas celui
   de Pierre lit `AGENTS.md`, exécute un atelier depuis un brief, vérificateur et
   catalogue verts, livre lisible en `python -m http.server`, Pierre n'ayant écrit que le
   brief. C'est la « seconde vocation » du README, jamais testée.
4. **Une flotte unifiée** : tous les livres Atelier sur la même version du moteur (hérités
   à part), 13 œuvres et 0 doublon, moins de 15 Mo d'images, ordre de l'index = ordre du
   catalogue, vérificateur en CI, « reprendre ma lecture » sur l'accueil.

### Décisions qui reviennent à Pierre (aucune ne bloque la prochaine session)

- Couvertures des deux livres fusionnés : garder celle de l'édition texte ou celle de
  l'édition illustrée (choix esthétique).
- Accepter la perte de progression des lecteurs des deux éditions illustrées (clés
  orphelines) et le 404 comme mécanisme de redirection.
- Le verdict de l'expérience « embranchements » passe par sa fiche de lecture — pas par
  l'agent qui l'a écrite.
