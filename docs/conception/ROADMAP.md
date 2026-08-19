# ROADMAP.md — chantiers Conception & Production

Roadmap priorisée du couple Conception/Production, pilotée par la
[`VISION.md`](VISION.md). Sources : audit
[`../audits/2026-08-rapport-etonnement.md`](../audits/2026-08-rapport-etonnement.md)
§B.4, §D.3.

> **Règle d'entretien** : la PR de chaque chantier terminé met à jour cette page
> (statut + date), comme pour la roadmap Bibliothèque.

| # | Chantier | Contenu | Statut |
|---|---|---|---|
| 1 | **Standard de recette + roman-atelier v2** | Définir le standard « recette hyper claire, agent-agnostique, versionnée » et refondre `ateliers/roman-atelier/WORKFLOW.md` en exemple canonique | fait (cette PR) |
| 2 | **Palier 0 : template de moteur versionné** | `livres/_template/` (déjà exclu du catalogue par le script) : le moteur « Atelier » corrigé de ses bugs connus (audit §B.4 : `function close()`, `entry(id)` sans garde, précédence de la recherche codex), marqué `<meta name="reader-engine" content="atelier-liseuse v1">`, avec spécification de l'îlot de données (`livres/_template/DONNEES.md`). Chaque livre reste autonome (copie), mais on sait quel livre embarque quelle version du moteur. **Le chantier le plus structurant du projet** : conditionne les fonctionnalités transverses de la Bibliothèque (progression, offline, comptes — voir [`../bibliotheque/VISION.md`](../bibliotheque/VISION.md) palier 0) | fait (2026-08-13) |
| 3 | **Validation du socle éditorial** | Relecture/correction par Pierre de [`PREFERENCES.md`](PREFERENCES.md) — les emplacements ouverts (thèmes, tons, longueurs, public, fonctionnalités) sont désormais comblés par des **défauts proposés** extraits des meilleurs livres ; reste leur validation ou correction par Pierre | défauts proposés (2026-08-13) — validation Pierre |
| 4 | **Ateliers candidats** (audit §D.3) | Édition illustrée par bascule d'affichage dans le livre existant (lève le moratoire, prérequis : `variantOf` du schéma v2) ; fiction interactive à branches (« récit explorable » au sens plein) ; ~~fabrication multi-agents tracée (rôles auteur / illustrateur)~~ → formalisée dans `roman-atelier` v3 (brief + manifeste d'illustrations + relai illustrateur), reste son pilote à froid ; ~~réintroduction de la carte et du graphe de relations comme modules optionnels du moteur~~ → **fait (2026-08-19)** : moteur `atelier-liseuse v3` (îlots `map` et `relations`, révélation calquée sur les déverrouillages du codex, équivalents textuels accessibles), recettes `roman-atelier` v7 (étape 3 bis) et `reportage` v5 (étape 4 bis), contrôles du vérificateur v4 — reste leur pilote à froid | en cours (un atelier = une session Conception) |
| 5 | **Spécification « Ma Bibliothèque 2.0 »** | Paramétrage explicite des recettes (quels champs de formulaire), architecture de l'exécution pour compte d'utilisateur, sécurité des clés API — à ouvrir quand les critères d'entrée du palier P2 approchent | plus tard |
| 6 | **Conformité des métadonnées des livres publiés** | 5 livres portaient encore `book:author = "Atelier des récits explorables"` (violation de la règle d'or n° 4, audit §B.6). Arbitrage de Pierre (2026-08-17) : **rétrofit du seul `book:author`** (meta + îlot JSON), reconstitué depuis l'historique git — pas de rétrofit de `book:workflow` ni `reader-engine` sur les anciens livres (métadonnées qui auraient été inventées : ni atelier ni moteur versionnés à l'époque) ; les livres produits depuis le template les portent nativement | fait (2026-08-17) |
| 7 | **`roman-atelier` v4 : ancrage dans le réel** | Option de brief « Ancrage réel » ([`BRIEF.md`](../../ateliers/roman-atelier/BRIEF.md)) + étape de recherche documentaire **préalable à l'écriture** : l'agent auteur constitue un dossier documentaire committé `livres/<slug>/recherche.md` — lieux, époque, jargon d'un métier, personnage historique, chaque fait relié à sa source datée — en parallélisant par sub-agents de recherche s'il en est capable, ou en **mode délégué** (requêtes copiables-collables soumises par Pierre à un assistant externe, un tour d'échange en plus). Évolution de recette : version +1 + changelog ([`creer-un-atelier.md`](creer-un-atelier.md) §5) | fait (cette PR) — reste son pilote à froid (S2 pilote la v4) |
| 8 | **Atelier reportage** (ex-médiation culturelle) | Nouveau format **non romancé** ([`ateliers/reportage/`](../../ateliers/reportage/WORKFLOW.md)) : documenter un sujet réel demandé par le brief — lieu, personnage historique, métier, événement — par recherche documentaire sourcée, restitué en lecture explorable (parcours, notices de codex) et illustré de **documents du web** crédités (moteur `atelier-liseuse v2`, règle de pertinence). Absorbe l'« essai de vulgarisation explorable » d'[`IDEES.md`](IDEES.md). En attendant le champ `nature` du schéma v2 ([roadmap Bibliothèque](../bibliotheque/ROADMAP.md), chantier 5), ses livrables se signalent par le tag `reportage` (règle de cohabitation, [`creer-un-atelier.md`](creer-un-atelier.md) §6) | fait — v1 (2026-08-13, sous le nom `mediation-culturelle`) puis v2 (2026-08-17 : renommage + documents du web) ; pilote Production à programmer ; séparation à l'index quand `nature` existera |
| 9 | **Mode impression du moteur** | Troisième fonctionnalité régressée par la standardisation (audit §B.3 et §D.3.7, promue depuis [`IDEES.md`](IDEES.md)) : feuille `@media print` du moteur de référence, pour que la vue affichée s'imprime sans le mobilier de la liseuse (barre, sommaire, navigation, dialogues), en noir sur blanc, figures et cartes non coupées, URL des sources imprimée. Acquis par tous les ateliers sans rien demander aux recettes | fait (2026-08-19, moteur `atelier-liseuse v3`) |

## Séquencement des premières sessions

Ordre de travail arbitré avec Pierre (session Conception du 2026-08-13). Chaque
ligne renvoie à un chantier ci-dessus ou à la
[roadmap Bibliothèque](../bibliotheque/ROADMAP.md) — rien n'est re-décrit ici.

| Ordre | Rôle | Session | Prérequis |
|---|---|---|---|
| S1 | Conception | ~~Template de moteur versionné (chantier 2)~~ **fait** (session du 2026-08-13, avec `roman-atelier` v3 : brief, illustrations, relai) | — |
| S1′ (parallèle) | Bibliothèque | Schéma de catalogue v2 — `format`, `variantOf`, `nature` (roadmap Bibliothèque, chantier 5) | indépendant ; **prérequis dur de S3** (`variantOf`) et de la séparation fiction/reportage à l'index (chantier 8, `nature`) |
| S1″ (parallèle) | Pierre | Validation des défauts proposés de [`PREFERENCES.md`](PREFERENCES.md) (chantier 3) | aucun |
| S2 | Production | **Pilote à froid de `roman-atelier`** (version courante : v7) : un brief rempli ([`BRIEF.md`](../../ateliers/roman-atelier/BRIEF.md)) → livre écrit par l'auteur → relai du manifeste `illustrations.md` à un agent illustrateur (audit §D.3.5). L'étape de recherche documentaire (chantier 7) ne s'active que si le brief demande l'ancrage réel | aucun prérequis technique |
| S2′ | Conception | Corrections de la recette d'après les interprétations remontées par le pilote S2 (boucle de [`VISION.md`](VISION.md)) | S2 |
| S2″ | Production | **Pilote à froid de `reportage`** (version courante : v5) : un brief rempli ([`BRIEF.md`](../../ateliers/reportage/BRIEF.md)) → recherche documentaire sourcée (documents visuels compris) → reportage publié (chantier 8) | aucun prérequis technique |
| S3 | Conception | Atelier édition illustrée par bascule d'affichage (chantier 4) | S1 + S1′ (`variantOf` lève le moratoire) |
| Ensuite | Conception | Fiction interactive à branches (chantier 4) | S1 ; les candidats suivants se piochent dans [`IDEES.md`](IDEES.md) |

> **Session Conception du 2026-08-19** — hors nouvel atelier (l'alternance est
> donc respectée) : les modules carte et relations du chantier 4 et le mode
> impression du chantier 9 sont livrés dans le **moteur** commun
> (`atelier-liseuse v3`) et branchés aux deux recettes existantes par une étape
> conditionnelle. Les pilotes S2 et S2″ en héritent : un brief qui demande une
> carte ou un graphe éprouvera aussi ces modules, sans session supplémentaire.

Deux principes de cadence accompagnent ce séquencement :

- **Alternance Conception/Production** : tout nouvel atelier est suivi d'au moins
  une exécution Production à froid avant d'ouvrir l'atelier suivant — c'est le test
  d'acceptation de [`creer-un-atelier.md`](creer-un-atelier.md) §4, et ce qui évite
  d'accumuler des recettes jamais validées.
- **Un atelier = une session Conception** (rappel du chantier 4).

> **Dérogation tracée (2026-08-13)** : sur arbitrage de Pierre, la session
> Conception du 2026-08-13 a livré deux recettes (`roman-atelier` v4 et
> `mediation-culturelle` v1 — l'atelier devenu `reportage` —, chantiers 7 et 8) avant le pilote S2 — dérogation
> ponctuelle à l'alternance. Elle reprend ensuite : les pilotes S2 et S2″
> précèdent tout nouvel atelier.
