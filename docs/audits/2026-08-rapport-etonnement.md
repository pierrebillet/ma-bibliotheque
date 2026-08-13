# Rapport d'étonnement — Ma Bibliothèque (août 2026)

> Note (13 août 2026) : document daté, conservé tel quel. Les chemins cités sont ceux
> d'août 2026, avant la restructuration par rôles (`SPEC.md` et consorts sont depuis
> dans `docs/archives/`, l'écriture d'un livre dans `ateliers/roman-atelier/`).

Audit réalisé le 12 août 2026, à la demande de Pierre, pour reprendre les fondamentaux
du projet avant son ouverture à des agents de code arbitraires. Trois volets :

- **A.** Le workflow de production des deux derniers livres, reconstitué depuis git
- **B.** Le format et les fonctionnalités des livres
- **C.** La Bibliothèque elle-même (index, catalogue, CI)
- **D.** Propositions : changements immédiats, expérimentations, évolutions

Méthode : trois audits parallèles (documentation, historique git + fichiers livres,
chaîne index/catalogue), menés en lecture seule sur le commit `cf50430`.

---

## Étonnement n° 0 — le méta-constat

**Le projet est gouverné par des documents qui décrivent un autre projet.** `SPEC.md`
(« source normative ») spécifie un artefact `_site/`, un `catalog.json` non versionné,
des tests CI, des dossiers `assets/`, `guides/`, `tests/` : rien de tout cela n'existe.
`CONVENTIONS.md` interdit les sous-dossiers dans `livres/` alors que 5 livres sur 11
en utilisent. La `ROADMAP.md` n'a jamais été réactualisée : les étapes 4 (guides) et
5 (livre d'exemple + recette) sont à 0 %, et les étapes 2-3 ont été réalisées
*autrement* que décrit. Le plus frappant : cette dérive était **déjà diagnostiquée**
dans `dev-mvp/ETUDE-TRACKING-UMAMI.md` (l. 33, commit `af06b4f` du 24 juillet) et n'a
jamais été traitée.

Conséquence directe pour l'objectif d'ouverture : un agent qui lit la doc normative
et un agent qui imite le dépôt produisent **deux conventions incompatibles**. C'est
le premier verrou à faire sauter — d'où le socle posé avec cet audit (README,
AGENTS.md, encarts d'obsolescence, garde-fous CI).

---

## A. Workflow des deux derniers livres

### A.1 Reconstitution

| Commit | Date | Auteur réel | Contenu | Voie |
|---|---|---|---|---|
| `48de0eb` | 24/07 | Pierre (`Assisted-by: OpenAI Codex`) | *Les Ombres de midi* + 21 images + catalog.json + index.html | branche `claude/interactive-political-espionage-book-d4fo7c` |
| `23cd099` | 07/08 | Claude | *L'Équation du calme* + couverture + index.html | même branche |
| `d30759a` | 08/08 | Pierre | merge **PR #1** | main |
| `e0ef6f2` | 11/08 | Pierre | *L'Équation du calme — illustrée* (18 images) + catalog.json + index.html + 4 `.DS_Store` | **direct sur main, hors PR** |
| `fc02f31` | 11/08 | Claude | *La Doublure* (2 fichiers) | branche `claude/fashion-espionage-novel-gzt1qt` |
| `3459ee7` | 11/08 | Pierre | merge **PR #2** | main |
| `710e4fc` | 11/08 | Pierre | *La Doublure — v2 illustrée* (19 images) + catalog.json + index.html | **direct sur main, hors PR** |
| `cf50430` | 11/08 | bot | `catalog.json` réécrit — annule l'édition manuelle précédente | main |

### A.2 Les étonnements

1. **Deux régimes de production coexistent sans être documentés.** Les livres texte
   arrivent par PR, avec des commits atomiques signés et tracés (trailer
   `Claude-Session:`). Les éditions illustrées arrivent **directement sur main**,
   sans PR ni revue, avec des messages laconiques en anglais dans un dépôt
   entièrement francophone, et sans traçabilité de l'outil ayant produit les images.
2. **PR #1 contient en réalité deux livres de deux origines différentes** (un livre
   Codex committé par Pierre + un livre Claude), sous un nom de branche qui n'en
   annonce qu'un. Le `--stat` du merge masque 25 fichiers du premier commit.
3. **Le travail manuel sur `catalog.json` a été écrasé par le bot.** `710e4fc` édite
   le catalogue à la main (en devinant un ordre de tri), puis `cf50430` le réécrit
   intégralement — 17 insertions/17 suppressions qui ne font qu'inverser deux
   entrées. Travail gaspillé + bruit d'historique : la démonstration parfaite que
   la règle « ne pas toucher au catalogue » (CONVENTIONS §11-12) est la bonne, mais
   qu'elle n'était ni connue ni outillée au moment des faits.
4. **Chaque ajout de livre a dû éditer `index.html`** pour maintenir la copie de
   secours `#demo-catalog` (≈ 280 lignes dupliquées de `catalog.json`) — copie
   aujourd'hui **désynchronisée** (ordre et horodatage divergents). Une double
   source de vérité manuelle est le principal générateur de dérive du dépôt.
5. **Aucun historique de fabrication.** Chaque livre apparaît en un seul commit
   « fini » : pas de plan, pas d'étapes, pas de relecture visible. Pour un projet
   dont l'objet est précisément le processus d'écriture par agents, c'est une perte
   sèche d'information (impossible d'auditer une révision, de comparer des
   approches, de rejouer une étape).
6. **Hygiène** : aucun `.gitignore`, quatre `.DS_Store` versionnés (introduits par
   `e0ef6f2`).

### A.3 Verdict

Le workflow PR fonctionne bien quand il est suivi (PR #2 est propre). Ce qui manque
n'est pas la discipline mais **l'outillage** : rien ne vérifiait une contribution
avant merge, rien ne disait à un contributeur ce qu'il avait le droit de toucher, et
la maintenance manuelle du catalogue était structurellement obligatoire. Les
garde-fous posés avec cet audit (validation en PR, refus des éditions de
`catalog.json`, AGENTS.md) rendent le « bon chemin » automatique.

---

## B. Les livres : formats et fonctionnalités

### B.1 Trois structures de fichiers pour onze livres

| Forme | Livres |
|---|---|
| Fichier plat `livres/<slug>.html` | 6 livres, dont *La Doublure* (récent) |
| Dossier + `<slug>.html` (+ `images/`) | 4 livres, dont un dossier **sans** images qui ne se justifie pas (`lequation-du-calme/`) |
| Dossier + `index.html` + `images/` | 1 livre (`la-doublure-v2/`) |

Les deux derniers livres ont tranché **différemment à trois heures d'intervalle**
(fichier plat pour *La Doublure*, dossier + `index.html` pour sa version illustrée).
Même la numérotation des images diverge (`chapter-1.jpg` vs `chapter-01.jpg`). Le
script de catalogue accepte tout, ce qui masque le désordre au lieu de le contraindre.
→ Tranché dans `AGENTS.md` : dossier + `index.html` + `images/chapter-NN.jpg` dès
qu'il y a des images.

### B.2 Deux familles de moteurs de liseuse — et pas de moteur du tout

**Famille historique** (5 livres, juillet) : un moteur *ad hoc* par livre, sans
parenté de code. De 12 Ko à 240 Ko de JS, texte tantôt dans des littéraux JS, tantôt
dans un îlot JSON à clés françaises.

**Famille « Atelier des récits explorables »** (5 livres récents) : îlot JSON à clés
anglaises + moteur commun. Mais « commun » signifie **copié-collé à 99,7 %**
(similarité mesurée entre *L'Équation du calme* et *La Doublure* : JS 0.997,
CSS 0.967). Preuves de copie non relue :

- la couleur du lien d'évitement de *La Doublure* est restée celle de *L'Équation du
  calme* (`background:var(--yellow);color:#14181a` — l'encre d'un autre livre) ;
- `<figure id="chapter-art">` sans `hidden` dans *Les Ombres de midi* seul (flash de
  mise en page) ;
- *La Part des pluies* (l'ancêtre) est resté sur un ancien schéma de données
  (`unlockBlock: null` × 6) : le moteur a changé de contrat sans migration.

### B.3 La standardisation a fait régresser les fonctionnalités

| | Anciens (le-livre-des-routes) | Récents (famille Atelier) |
|---|---|---|
| Sommaire, progression, codex à déverrouillage | ✅ | ✅ |
| Thème sombre, persistance localStorage | ✅ | ✅ |
| Taille de police réglable | ❌ | ✅ |
| `<dialog>` natif + piège de focus | partiel | ✅ |
| Images de chapitre/codex | ❌ | ✅ |
| **Carte du monde (SVG + coordonnées)** | ✅ | **❌ abandonné** |
| **Graphe de relations entre personnages** | ✅ | **❌ abandonné** |
| **Mode impression (`@media print`)** | ✅ | **❌ abandonné** |
| Choix interactifs / branches narratives | ❌ | ❌ |
| Audio / synthèse vocale | ❌ | ❌ |

Autres constats : *La Couronne lente* (le CSS le plus soigné du dépôt) **ne persiste
rien** — le lecteur perd sa position à chaque rechargement. Aucun livre n'a de choix
interactifs : « récit explorable » désigne uniquement le codex à déverrouillage.

### B.4 Qualités réelles du moteur récent

À souligner, car c'est une bonne base : échappement HTML systématique (pas
d'injection depuis l'îlot JSON), piège de focus complet dans les dialogues,
`role="progressbar"` mis à jour, région `aria-live` annonçant les déblocages,
`prefers-reduced-motion`, déverrouillage du codex robuste au rechargement, et
**intégrité référentielle parfaite** sur les 4 livres récents (0 mention orpheline,
0 lien cassé, 0 image sans `alt`).

Défauts JS relevés : `function close()` écrase `window.close` ; `entry(id)` sans
garde (un id de codex manquant bloquerait tout le rendu) ; précédence `||`/`&&` dans
la recherche du codex qui masque les fiches verrouillées dès qu'on tape ; codex de
*La Doublure* quasi inaccessible depuis le texte (15 blocs porteurs de mentions sur
106, contre 105/195 pour *L'Équation du calme*).

### B.5 Le poids : 40 Mo dont ~95 % d'images sous-compressées

- 23 Mo pour les deux éditions illustrées, qui republient 43 000 mots déjà présents
  dans le dépôt. JPEG de chapitre : 390-740 Ko pour 1672×941 px — un WebP équivalent
  ferait 60-120 Ko. Aucun WebP dans le dépôt alors que la doc le privilégie.
- Images de chapitre injectées **sans `loading="lazy"`, sans `width`/`height`, sans
  `srcset`** → décalage de mise en page garanti à chaque ouverture de chapitre.
- *L'Équation du calme* : 248 Ko de JSON parsés au chargement pour lire le chapitre 1.

### B.6 La provenance des modèles a été effacée

Les anciens livres créditent le modèle (`GPT 5.5`, `GPT 5.6 Sol`, `Gemini 3.1 pro`,
`Claude Fable`) ; les 5 récents disent tous `book:author = "Atelier des récits
explorables"`. Le tri par auteur de l'index agglomère la moitié du catalogue sous une
étiquette unique, et « quel modèle a écrit quoi » — l'objet même du projet — ne
survit que dans les trailers de commit. → Tranché dans `AGENTS.md` : `book:author`
crédite le modèle.

### B.7 Les éditions illustrées : deux techniques, zéro convention

- `lequation-du-calme-illustree` : images injectées dans l'îlot JSON (propre).
- `la-doublure-v2` : îlot JSON laissé byte-identique à l'original + 4 Ko de JS qui
  greffent les images à l'exécution, avec du code mort (`book.cover`, `meta.slug`
  réassignés mais jamais lus).
- Slugs incohérents (`-v2` vs `-illustree`), aucun champ de liaison au catalogue,
  descriptions et dates identiques → **deux paires de doublons indiscernables** dans
  la grille. Le tag `édition illustrée` n'est posé que sur une édition sur deux.
- Progression de lecture non transférée (clés localStorage disjointes) : le lecteur
  qui passe à l'illustrée recommence à zéro.
- Bonus vicieux : `git log --follow` reliait `la-doublure-v2/index.html` à
  `la-doublure.html` par similarité de contenu → l'édition illustrée **héritait de
  la date d'ajout de l'édition texte** dans le tri du catalogue (corrigé avec cet
  audit : `--diff-filter=A`).

---

## C. La Bibliothèque

### C.1 Ce qui est solide

`scripts/build_catalog.py` est de bonne facture : vrai parseur HTML (pas de regex),
lecture bornée à `</head>` et 4 Mio, cascade d'encodage BOM → déclaré → UTF-8 →
cp1252, tolérance par livre, écriture atomique, `generatedAt` stable (pas de commit
inutile), validation de signature binaire des couvertures. Côté `index.html` :
recherche insensible aux accents avec debounce, URL partageable (`?q=&tag=&sort=`),
placeholder de couverture déterministe (FNV-1a), `prefers-reduced-motion`,
`forced-colors`, aucun `innerHTML` sur données externes. Les couvertures sont
nommées à 100 % conformément aux slugs.

### C.2 Le défaut critique (corrigé avec cet audit)

**Asymétrie fatale entre générateur et consommateur.** Le script acceptait n'importe
quel nom de fichier (simple `::warning`, CI verte) ; l'index rejetait **tout le
catalogue** à la première entrée invalide. Enchaînement : un agent dépose
`livres/Mon Livre.html` → CI verte → catalogue publié avec `id: "Mon Livre"` → la
page d'accueil affiche « Catalogue indisponible », **zéro livre**, y compris les 11
valides. Même effet via `bookCount` désynchronisé (édition manuelle) ou un dossier
caché (`livres/.obsidian/`).

Corrections appliquées : script strict (slug invalide → `::error` + exit 1, dossiers
cachés exclus), index tolérant (entrée invalide ignorée + console.warn, seule
l'invalidité totale rejette), validation en PR (génération à blanc + refus des
modifications de `catalog.json`).

### C.3 Les autres défauts constatés

1. **Duplication du catalogue** : le bloc `#demo-catalog` inliné (≈ 280 lignes,
   13 % du fichier) est maintenu à la main et déjà désynchronisé. À générer
   automatiquement ou à supprimer.
2. **Dette CSS : quatre refontes empilées.** Quatre blocs `:root` successifs se
   surchargent (accent brun → bordeaux → bleu), `.site-header` défini 4 fois,
   `.book-card` 3 fois, media queries en triple exemplaire. ~700 lignes mortes mais
   téléchargées et évaluées ; toute modification exige de savoir quelle couche gagne.
3. **Bug `[hidden]`** : `.library-grid` déclare `display:grid` en dur, ce qui
   neutralise l'attribut `hidden` posé par le JS (corrigé avec cet audit).
4. **Couvertures recadrées** : cartes en ratio 4:5 alors que les couvertures sont en
   2:3 (promis par la doc) → ~17 % de l'image perdue. À trancher : soit assumer le
   4:5 (documenter le cadrage), soit revenir au 2:3.
5. **Couplage couverture/slug rigide** : seul `couvertures/<slug>.{webp,png,jpg}`
   est cherché. Un livre-dossier ne peut pas embarquer sa couverture
   (`la-part-des-pluies/images/cover.jpg` existe et est ignoré) ; `.jpeg`/`.avif`
   ignorés en silence.
6. **Ergonomie/accessibilité** : trois liens identiques par carte (verbeux au
   lecteur d'écran, tout en `target="_blank"`), `aria-live` qui réannonce aussi le
   bouton « Réinitialiser », select custom sans `aria-activedescendant`, page
   inutilisable sans JavaScript (aucun lien statique de repli), description masquée
   sur mobile.
7. **Absents** : favicon, `404.html`, `.nojekyll`, Open Graph/Twitter Card (aucun
   partage social exploitable), `robots.txt`/`sitemap.xml`.
8. **CI** : le push du bot est sans rebase ni retry (échoue si un humain pousse au
   même moment) ; l'appel de rebuild Pages peut mettre le job au rouge après un
   commit déjà poussé (échec trompeur).
9. **Tags non gouvernés** : 30 tags pour 11 livres dont 12 orphelins, mélangeant
   genre, format, lieu et thème dans une liste à plat.

---

## D. Propositions

### D.1 Fait avec cet audit (socle)

| Changement | Fichiers |
|---|---|
| Point d'entrée + hiérarchie de vérité des docs | `README.md` (nouveau) |
| Contrat de contribution pour agents | `AGENTS.md`, `CLAUDE.md` (nouveaux) |
| Hygiène | `.gitignore`, suppression des `.DS_Store` versionnés |
| Script strict : slug invalide → exit 1 ; dossiers cachés et `_template` exclus ; `--diff-filter=A` (dates d'ajout non contaminées) | `scripts/build_catalog.py` |
| Index tolérant : entrée invalide ignorée au lieu de tout rejeter ; fix `.library-grid[hidden]` | `index.html` |
| Validation en PR : génération à blanc + refus des éditions manuelles de `catalog.json` | `.github/workflows/catalog.yml` |
| Encarts d'obsolescence + corrections factuelles | `SPEC.md`, `CONVENTIONS.md`, `ROADMAP.md`, `AUTOMATISATION.md`, `FRONTEND.md` |

Effet de bord assumé : au premier run du bot après merge, l'ordre du catalogue
changera (les dates d'ajout ne sont plus contaminées par `--follow` ; les anciens
livres renommés datent désormais de leur renommage).

### D.2 Façons de fonctionner (à adopter dès le prochain livre)

1. **Tout par PR, éditions illustrées comprises.** La CI le vérifie désormais.
2. **Commits d'étapes** pour les livres : plan/synopsis, chapitres, codex, relecture.
   L'historique de fabrication est une richesse du projet, pas un déchet.
3. **`book:author` = le modèle.** Pour un livre multi-agents, tous les modèles, et
   les rôles détaillés dans la PR.
4. **Une seule structure** : dossier + `index.html` + `images/chapter-NN.jpg` dès
   qu'il y a des images (voir `AGENTS.md`).
5. **Moratoire sur les éditions dérivées en doublon** jusqu'au schéma v2.

### D.3 À tester sur les prochains livres (expérimentations)

Classées par ratio intérêt/effort décroissant :

1. **Template de livre versionné** (`livres/_template/`, hors catalogue — déjà exclu
   par le script) : le moteur « Atelier » actuel, corrigé de ses bugs connus (§B.4),
   avec un marqueur `<meta name="reader-engine" content="atelier-v3">`. Chaque livre
   reste autonome (copie), mais on sait quel livre embarque quelle version du moteur,
   et on peut mesurer la dérive. C'est la brique qui rend le repo appropriable.
2. **Édition illustrée = même livre, bascule d'affichage.** Les images rejoignent le
   livre existant (îlot JSON + `images/`), un réglage « avec/sans illustrations »
   dans la barre d'outils de la liseuse. Supprime les doublons de catalogue, la
   double clé localStorage et 50 % du poids dupliqué.
3. **Réintroduire la carte et le graphe de relations** comme modules optionnels du
   moteur (les anciens livres prouvent que ça marche ; c'est une régression, pas une
   impossibilité).
4. **Vraie fiction interactive** : un livre à choix/branches (le nom « récit
   explorable » le promet déjà). Le moteur a déjà l'infrastructure de déverrouillage,
   les branches en sont une extension naturelle.
5. **Fabrication multi-agents tracée** : un livre écrit par 2-3 modèles aux rôles
   explicites (auteur / illustrateur / éditeur-relecteur), chacun committant sous son
   nom sur la même branche. C'est le pilote du mode « livres illustrés par ChatGPT »
   généralisé.
6. **Discipline images** : WebP ≤ 150 Ko par image de chapitre, `loading="lazy"`,
   `width`/`height` déclarés. Mesurable immédiatement sur le poids du dépôt.
7. **Mode impression** (`@media print`) et, plus exploratoire, **lecture audio**
   (Web Speech API, hors ligne, zéro dépendance).

### D.4 Évolutions de la Bibliothèque (brique par brique)

1. **Schéma catalogue v2** : `format` (`texte`/`illustré`), `variantOf` (groupement
   des éditions), `wordCount`/`readingMinutes` (calculables par le script), `genre`
   (vocabulaire fermé, distinct des tags). Résout d'un coup les doublons de grille,
   l'absence de filtre durée et l'étiquetage incohérent.
2. **Générer le bloc `#demo-catalog`** depuis `catalog.json` dans le workflow (ou le
   supprimer au profit d'une consigne « servir en HTTP local »). Ferme la dernière
   source de dérive manuelle.
3. **Purge CSS** : ne garder que les couches 3-4 (~700 lignes de moins), puis
   trancher le ratio des cartes (4:5 assumé ou retour au 2:3).
4. **Couvertures WebP** (~1,2 Mo au lieu de 4,9) + accepter la couverture embarquée
   `livres/<slug>/cover.*` en repli.
5. **Petits manquants** : favicon, `404.html`, `.nojekyll`, Open Graph sur l'index,
   un lien statique de secours en `<noscript>`.
6. **Robustesse CI** : `git pull --rebase` + retry avant le push du bot ; séparer le
   rebuild Pages dans une étape non bloquante.
7. **Gouvernance des tags** : vocabulaire contrôlé court (genre + format + 2-3 thèmes
   libres), documenté dans `AGENTS.md`.
8. **Plus tard** : page « à propos » racontant le projet (quel modèle a écrit quoi,
   comment contribuer), skills/guides embarqués (`.claude/skills/ecrire-un-livre`),
   et reprise des briefs `dev-mvp/` (tracking Umami, fonctionnalités locales) sur la
   base assainie.

---

## Conclusion

Le projet a produit en trois semaines une bibliothèque réelle de 11 livres avec une
chaîne de publication automatisée qui fonctionne — c'est beaucoup. Mais il a grandi
plus vite que ses règles : la doc décrit un projet imaginaire, le « moteur » est un
copier-coller, les éditions illustrées ont contourné le seul processus sain (la PR),
et un simple nom de fichier pouvait éteindre toute la bibliothèque. Le socle posé
avec cet audit (vérité documentaire minimale, garde-fous CI, contrat agents) rend le
bon chemin automatique ; les propositions §D.3-D.4 sont les briques suivantes, à
ajouter une par une, chacune testable sur un livre ou une PR.
