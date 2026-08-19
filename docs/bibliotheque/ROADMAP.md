# ROADMAP.md — chantiers de la Bibliothèque

Roadmap priorisée du rôle Bibliothèque, pilotée par la [`VISION.md`](VISION.md).
Chaque chantier porte son **niveau d'architecture** (①–⑤, voir VISION §Principes) et
sa **source** (audit [`../audits/2026-08-rapport-etonnement.md`](../audits/2026-08-rapport-etonnement.md)
§C.3.n / §D.4.n, ou études archivées).

> **Règle d'entretien** : la PR de chaque chantier terminé met à jour cette page
> (statut + date). Une roadmap qui ne bouge pas devient fausse — c'est exactement le
> destin de l'ancienne `ROADMAP.md`, aujourd'hui dans les archives.

## Déjà fait (socle, août 2026)

| Chantier | Source |
|---|---|
| Script de catalogue strict (slug invalide = exit 1, dossiers cachés et `_template` exclus) | audit §D.1 |
| Index tolérant (entrée invalide ignorée au lieu de rejeter tout le catalogue) | audit §D.1 |
| Validation en PR : génération à blanc + refus des éditions manuelles de `catalog.json` | audit §D.1 |
| Bloc `#demo-catalog` généré par la CI (plus de maintenance manuelle) | audit §D.4.2 — fait |
| Push du bot avec rebase + 3 tentatives, relance explicite du build Pages | audit §D.4.6 — fait |
| Documentation par rôles (`AGENTS.md`, `docs/`, `ateliers/`) | PR #5 |

## Vers la 1.0 « catalogue public soigné »

**1.0 atteinte le 2026-08-18** : les huit chantiers ci-dessous sont faits. La suite
relève du palier 2 de [`VISION.md`](VISION.md), résumé dans la section suivante.

Par ordre de priorité initial (VISION, palier 1).

| # | Chantier | Contenu | Niveau | Source | Statut |
|---|---|---|---|---|---|
| 1 | **Hygiène web** | Favicon, `404.html`, `.nojekyll`, Open Graph/Twitter Card sur l'index (partage social exploitable), `robots.txt` + sitemap (généré par la CI comme `catalog.json`) | ①/③ | §C.3.7, §D.4.5 | **fait (2026-08-15)** |
| 2 | **Purge CSS + ratio des cartes** | Supprimer les couches CSS mortes (~700 lignes, quatre refontes empilées) ; trancher cartes 4:5 vs couvertures 2:3 (aujourd'hui ~17 % de l'image rognée) et documenter le choix | ① | §C.3.2, §C.3.4 | **fait (2026-08-17)** — feuille consolidée en une couche (~600 lignes en moins), cartes alignées sur le 2:3 des couvertures ([`FRONTEND.md`](FRONTEND.md) §Feuille de style) |
| 3 | **Accessibilité et ergonomie de l'index** | Un seul lien par carte (au lieu de trois identiques), `aria-live` qui n'annonce que le résultat, select custom conforme (`aria-activedescendant`), lien statique de repli `<noscript>`, description visible sur mobile | ① | §C.3.6 | **fait (2026-08-15)** |
| 4 | **Couvertures optimisées et découplées** | Passage WebP (~1,5 Mo au lieu de 4,9), couverture embarquée `livres/<slug>/cover.*` (ou `images/cover.*`) acceptée en repli, formats `.jpeg`/`.avif` reconnus | ①/③ | §C.3.5, §D.4.4 | **fait (2026-08-16)** |
| 5 | **Schéma de catalogue v2** | `format` (texte/illustré), `nature` (fiction/reportage — sépare les romans des reportages à l'index ; prérequis de la séparation demandée par le chantier 8 de la [roadmap Conception](../conception/ROADMAP.md)), `variantOf` (groupement des éditions — condition de levée du moratoire), `wordCount`/`readingMinutes` (calculés par le script), `genre` (vocabulaire fermé, distinct des tags). `schemaVersion: 2` + validateur JS mis à jour de façon coordonnée ([`CATALOGUE.md`](CATALOGUE.md)). **Arbitrages tranchés** : `nature` dérivée de `book:workflow` via la table `ATELIER_NATURE` du script (défaut `fiction` si la meta est absente ou l'atelier inconnu — donc aucun rétrofit de `book:workflow` sur les livres publiés, leur nature tombe sur le défaut) ; vocabulaires fermés de `genre`, `format`, `tonalite`, `exigence` et `audience` fixés dans [`CATALOGUE.md`](CATALOGUE.md) et rétrofités dans le `<head>` des 13 livres publiés ; `wordCount`/`readingMinutes` calculés depuis l'îlot JSON des livres (200 mots/min), `null` pour les 3 livres anciens sans îlot (`archipel-intermittent`, `la-couronne-lente`, `letiage`) ; `variantOf` posé sur les 2 éditions dérivées (`la-doublure-v2`, `lequation-du-calme-illustree`) ; `schemaVersion: 2` et validateur JS bi-version (v1 + v2) pour absorber un catalogue servi depuis un cache | ③ | §D.4.1 ; Pierre, 2026-08-13 | **fait (2026-08-17)** |
| 6 | **Gouvernance des tags** | Vocabulaire contrôlé court (genre + format + 2-3 thèmes libres), documenté côté ateliers ; assainir les 30 tags actuels (12 orphelins) ; la distinction fiction/reportage ne passe pas par les tags mais par `nature` (chantier 5) : la règle « premier tag `reportage` » est **levée côté atelier depuis le chantier 5**, restent à assainir ici le tag `reportage` déjà présent dans le catalogue et les doublons tags/genre (`science-fiction`, `fantasy`…) que le vocabulaire fermé de `book:genre` rend redondants | ① | §D.4.7 | **fait (2026-08-18)** — règle « 2 à 4 thèmes libres, jamais un champ structuré » documentée dans [`CATALOGUE.md`](CATALOGUE.md) §Gouvernance des tags, double contrôle (générateur : tag écarté + avertissement ; vérificateur : défaut bloquant), 13 livres assainis — 39 tags distincts ramenés à 28, aucun tag inventé |
| 7 | **Catégories déclaratives affichées** | Badges durée de lecture, format et nature, plus le filtre d'index fiction/reportage : **livrés par le chantier 5**. Reste ici le seul volet non couvert, les **capacités interactives déclarées** (codex, carte, choix, audio…) — le sous-ensemble resserré de l'étude du champ des possibles §12 : les déclarer dans le `<head>` des livres, les extraire au catalogue, les afficher en badges | ①/③ | §D.4.1, étude MVP §12 | **fait (2026-08-18)** — meta `book:capacites` (vocabulaire fermé `codex`, `carte`, `relations`, `choix`, `audio`), champ `capabilities` du **schéma v3**, badges en trait pointillé à l'index (« ce que le livre fait ») et capacités indexées par la recherche ; 13 livres déclarés d'après ce qu'ils offrent réellement (`codex` partout, `carte` + `relations` sur les deux livres-routes) |
| 8 | **Page « à propos »** | Raconter le projet : quel modèle a écrit quoi, comment les livres sont fabriqués, comment contribuer | ① | §D.4.8 | **fait (2026-08-17)** — `a-propos.html`, lien au pied de l'index, ajout au sitemap généré |

## En 1.x « exploration et bibliothèque du lecteur »

Détail dans [`VISION.md`](VISION.md) palier 2. Prérequis communs : 1.0 atteinte,
**moteur de liseuse unifié** (palier 0, chantier Conception/Production) et
`variantOf` en place.

| Chantier | Contenu | Niveau |
|---|---|---|
| Exploration éditoriale (direction B) | Collections, parcours de lecture, mises en avant calculées depuis le schéma v2 | ①/③ |
| Couche d'état locale (direction A) | Lots 1→4 de l'[étude fonctionnalités locales](../archives/dev-mvp/ETUDE-FONCTIONNALITES-LOCALES.md) : fondation (progression, favoris), **portabilité (export/import) avant visibilité (page « Ma liste »)**, robustesse. Couche d'accès unique, vocabulaire « sur cet appareil » | ② |
| Cadre de mesure sobre (direction E) | Questions produit d'abord, taxonomie versionnée, « l'usage oui, le contenu non », non bloquant ; choix d'outil non présupposé | ④ |

## Post-1.x

Paliers 3 (PWA installable, cache sélectif par livre, kill-switch du service worker
obligatoire) et 4 (comptes utilisateur, backend sur frontend statique d'abord) —
critères d'entrée et cahiers des charges dans [`VISION.md`](VISION.md). Pas de
détail ici tant que les critères d'entrée ne sont pas en vue.
