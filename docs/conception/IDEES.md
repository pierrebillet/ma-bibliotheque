# IDEES.md — vivier d'idées de Conception

Réserve d'idées pour les prochains ateliers et évolutions de formats : fonctionnalités
de lecture d'un côté, variété de contenus de l'autre. Complète la
[`ROADMAP.md`](ROADMAP.md) (les engagements) sans s'y substituer.

> **Règle d'entretien** : ce vivier n'est pas un engagement. Une idée n'en sort que
> **promue** (elle devient une ligne de [`ROADMAP.md`](ROADMAP.md), avec renvoi) ou
> **écartée** (déplacée en fin de fichier, avec le pourquoi — la mémoire des
> non-choix a autant de valeur que celle des choix). Toute session Conception qui
> pioche ou ajoute une idée met ce fichier à jour dans sa PR.

Statuts possibles : `vivier` · `promue → ROADMAP #n` · `écartée`.

## Formes et fonctionnalités de lecture

| Idée | Intérêt | Effort / prérequis | Source | Statut |
|---|---|---|---|---|
| Branches à fins multiples, avec suivi des fins découvertes (localStorage du livre) | Le « récit explorable » au sens plein ; rejouabilité | Élevé — extension du moteur ; après le template versionné (ROADMAP #2) | audit §D.3.4 | promue → ROADMAP #4 (fiction interactive) |
| Carte SVG du monde et graphe de relations entre personnages, en modules optionnels du moteur | Réintroduit des fonctionnalités régressées appréciées | Moyen — modules du template (ROADMAP #2) | audit §B.3, §D.3.3 | promue → ROADMAP #4 |
| Mode impression (CSS `@media print` soigné) | Lecture papier ; fonctionnalité régressée des moteurs de juillet | Faible — CSS seul, généralisable via le template | audit §D.3.7 | vivier |
| Lecture audio via Web Speech API (TTS du navigateur, hors ligne) | Accessibilité ; « livre audio » sans fichier audio ni dépendance externe | Moyen — qualité de voix variable selon navigateur | audit §D.3.7 | vivier |
| Annotations et surlignage du lecteur, persistés en localStorage | Appropriation du texte ; reste dans le contrat « tout local » | Moyen — UI de sélection + stockage par chapitre | session 2026-08 | vivier |
| Frise chronologique de l'univers, alimentée par l'îlot JSON | Prolonge le codex ; aide aux récits non linéaires | Moyen — module optionnel du moteur | session 2026-08 | vivier |
| Récapitulatif « ce qu'il faut retenir » déverrouillé en fin de chapitre | Renforce la boucle codex/curiosité ; aide à la reprise de lecture | Faible — convention d'écriture + petit ajout moteur | session 2026-08 | vivier |
| Suivi des fins et des embranchements visités (arbre de parcours affichable) | Compagnon naturel des branches ; rend l'exploration visible | Moyen — dépend de la fiction interactive | session 2026-08 | vivier |

## Variété de contenus

Aujourd'hui au catalogue : 11 romans, 3 familles de genres (espionnage,
SF/anticipation sociale, fantasy). Tout le reste est à explorer.

| Idée | Intérêt | Effort / prérequis | Source | Statut |
|---|---|---|---|---|
| Recueil de nouvelles (3-6 textes courts liés par un thème) | Format court, production rapide, diversité par session | Faible — moteur actuel suffit (sommaire par nouvelle) | docs/conception/README.md | vivier |
| Polar / whodunit dont les indices vivent dans le codex | Le déverrouillage devient mécanique d'enquête, pas seulement bonus | Moyen — écriture exigeante (intégrité des indices) | session 2026-08 | vivier |
| Docu-fiction historique (récit + codex documentaire daté) | Étend la bibliothèque au-delà de la fiction pure | Moyen — exigence de rigueur factuelle | session 2026-08 | vivier |
| Essai de vulgarisation explorable (concepts en codex, parcours de lecture multiples) | Nouveau public ; le non-linéaire sert la pédagogie | Moyen | session 2026-08 | vivier |
| Roman épistolaire (lettres, journaux, documents) | La forme fragmentaire épouse naturellement l'îlot JSON | Faible | session 2026-08 | vivier |
| Formes brèves : poésie, micro-fictions | Sessions de production très courtes ; variété de tons | Faible | session 2026-08 | vivier |
| Livre jeunesse illustré (texte court, images porteuses) | Nouveau public ; met à l'épreuve la discipline images | Moyen — dépend du poids des images (PREFERENCES) | session 2026-08 | vivier |
| Genres absents du catalogue : comédie, historique, horreur psychologique | Diversité éditoriale à moteur constant | Faible — choix éditorial, à cadrer par PREFERENCES.md | session 2026-08 | vivier |

## Idées écartées

| Idée | Pourquoi |
|---|---|
| *(aucune pour l'instant)* | |
