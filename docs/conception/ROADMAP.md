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
| 4 | **Ateliers candidats** (audit §D.3) | Édition illustrée par bascule d'affichage dans le livre existant (lève le moratoire, prérequis : `variantOf` du schéma v2) ; fiction interactive à branches (« récit explorable » au sens plein) ; ~~fabrication multi-agents tracée (rôles auteur / illustrateur)~~ → formalisée dans `roman-atelier` v3 (brief + manifeste d'illustrations + relai illustrateur), reste son pilote à froid ; réintroduction de la carte et du graphe de relations comme modules optionnels du moteur | en cours (un atelier = une session Conception) |
| 5 | **Spécification « Ma Bibliothèque 2.0 »** | Paramétrage explicite des recettes (quels champs de formulaire), architecture de l'exécution pour compte d'utilisateur, sécurité des clés API — à ouvrir quand les critères d'entrée du palier P2 approchent | plus tard |
| 6 | **Conformité des métadonnées des livres publiés** | 5 livres portent encore `book:author = "Atelier des récits explorables"` (violation de la règle d'or n° 4, audit §B.6) et aucun livre ne porte `book:workflow` ni `reader-engine`. À arbitrer : rétrofit des 11 livres publiés, ou application aux seuls prochains livres | à arbitrer — Pierre |

## Séquencement des premières sessions

Ordre de travail arbitré avec Pierre (session Conception du 2026-08-13). Chaque
ligne renvoie à un chantier ci-dessus ou à la
[roadmap Bibliothèque](../bibliotheque/ROADMAP.md) — rien n'est re-décrit ici.

| Ordre | Rôle | Session | Prérequis |
|---|---|---|---|
| S1 | Conception | ~~Template de moteur versionné (chantier 2)~~ **fait** (session du 2026-08-13, avec `roman-atelier` v3 : brief, illustrations, relai) | — |
| S1′ (parallèle) | Bibliothèque | Schéma de catalogue v2 — `format`, `variantOf` (roadmap Bibliothèque, chantier 5) | indépendant ; **prérequis dur de S3** |
| S1″ (parallèle) | Pierre | Validation des défauts proposés de [`PREFERENCES.md`](PREFERENCES.md) (chantier 3) | aucun |
| S2 | Production | **Pilote à froid de `roman-atelier` v3** : un brief rempli ([`BRIEF.md`](../../ateliers/roman-atelier/BRIEF.md)) → livre écrit par l'auteur → relai du manifeste `illustrations.md` à un agent illustrateur (audit §D.3.5) | aucun prérequis technique |
| S2′ | Conception | Corrections de la recette v3 d'après les interprétations remontées par le pilote S2 (boucle de [`VISION.md`](VISION.md)) | S2 |
| S3 | Conception | Atelier édition illustrée par bascule d'affichage (chantier 4) | S1 + S1′ (`variantOf` lève le moratoire) |
| Ensuite | Conception | Fiction interactive à branches, modules carte/graphe (chantier 4) | S1 ; les candidats suivants se piochent dans [`IDEES.md`](IDEES.md) |

Deux principes de cadence accompagnent ce séquencement :

- **Alternance Conception/Production** : tout nouvel atelier est suivi d'au moins
  une exécution Production à froid avant d'ouvrir l'atelier suivant — c'est le test
  d'acceptation de [`creer-un-atelier.md`](creer-un-atelier.md) §4, et ce qui évite
  d'accumuler des recettes jamais validées.
- **Un atelier = une session Conception** (rappel du chantier 4).
