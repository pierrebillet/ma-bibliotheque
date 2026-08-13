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
| 2 | **Palier 0 : template de moteur versionné** | `livres/_template/` (déjà exclu du catalogue par le script) : le moteur « Atelier » corrigé de ses bugs connus (audit §B.4 : `function close()`, `entry(id)` sans garde, précédence de la recherche codex), marqué `<meta name="reader-engine" content="atelier-v3">`. Chaque livre reste autonome (copie), mais on sait quel livre embarque quelle version du moteur. **Le chantier le plus structurant du projet** : conditionne les fonctionnalités transverses de la Bibliothèque (progression, offline, comptes — voir [`../bibliotheque/VISION.md`](../bibliotheque/VISION.md) palier 0) | à faire |
| 3 | **Validation du socle éditorial** | Relecture/correction par Pierre du premier jet de [`PREFERENCES.md`](PREFERENCES.md) (thèmes, tons, longueurs cibles à compléter) | à faire — Pierre |
| 4 | **Ateliers candidats** (audit §D.3) | Édition illustrée par bascule d'affichage dans le livre existant (lève le moratoire, prérequis : `variantOf` du schéma v2) ; fiction interactive à branches (« récit explorable » au sens plein) ; fabrication multi-agents tracée (rôles auteur / illustrateur / relecteur, chacun committant sous son nom) ; réintroduction de la carte et du graphe de relations comme modules optionnels du moteur | à faire (un atelier = une session Conception) |
| 5 | **Spécification « Ma Bibliothèque 2.0 »** | Paramétrage explicite des recettes (quels champs de formulaire), architecture de l'exécution pour compte d'utilisateur, sécurité des clés API — à ouvrir quand les critères d'entrée du palier P2 approchent | plus tard |
