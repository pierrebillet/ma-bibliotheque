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

Par ordre de priorité. La 1.0 est atteinte quand tout est fait (VISION, palier 1).

| # | Chantier | Contenu | Niveau | Source | Statut |
|---|---|---|---|---|---|
| 1 | **Hygiène web** | Favicon, `404.html`, `.nojekyll`, Open Graph/Twitter Card sur l'index (partage social exploitable), `robots.txt` + sitemap | ①/③ | §C.3.7, §D.4.5 | à faire |
| 2 | **Purge CSS + ratio des cartes** | Supprimer les couches CSS mortes (~700 lignes, quatre refontes empilées) ; trancher cartes 4:5 vs couvertures 2:3 (aujourd'hui ~17 % de l'image rognée) et documenter le choix | ① | §C.3.2, §C.3.4 | à faire |
| 3 | **Accessibilité et ergonomie de l'index** | Un seul lien par carte (au lieu de trois identiques), `aria-live` qui n'annonce que le résultat, select custom conforme (`aria-activedescendant`), lien statique de repli `<noscript>`, description visible sur mobile | ① | §C.3.6 | à faire |
| 4 | **Couvertures optimisées et découplées** | Passage WebP (~1,2 Mo au lieu de 4,9), couverture embarquée `livres/<slug>/cover.*` acceptée en repli, formats `.jpeg`/`.avif` reconnus | ①/③ | §C.3.5, §D.4.4 | à faire |
| 5 | **Schéma de catalogue v2** | `format` (texte/illustré), `variantOf` (groupement des éditions — condition de levée du moratoire), `wordCount`/`readingMinutes` (calculés par le script), `genre` (vocabulaire fermé, distinct des tags). `schemaVersion: 2` + validateur JS mis à jour de façon coordonnée ([`CATALOGUE.md`](CATALOGUE.md)) | ③ | §D.4.1 | à faire |
| 6 | **Gouvernance des tags** | Vocabulaire contrôlé court (genre + format + 2-3 thèmes libres), documenté côté ateliers ; assainir les 30 tags actuels (12 orphelins) | ① | §D.4.7 | à faire |
| 7 | **Catégories déclaratives affichées** | Badges calculés depuis le schéma v2 : durée de lecture, format, capacités interactives déclarées (codex, carte, choix, audio) — le sous-ensemble resserré de l'étude du champ des possibles §12 | ①/③ | §D.4.1, étude MVP §12 | dépend de 5 |
| 8 | **Page « à propos »** | Raconter le projet : quel modèle a écrit quoi, comment les livres sont fabriqués, comment contribuer | ① | §D.4.8 | à faire |

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
