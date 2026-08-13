# PREFERENCES.md — socle éditorial commun

> **Statut : premier jet, extrait des livres existants du catalogue — à valider et
> corriger par Pierre.** Les points marqués *(à compléter par Pierre)* sont des
> emplacements volontairement laissés ouverts. Ce document évolue par pull request.

Ce socle rassemble les préférences transverses à **toutes** les lectures de la
bibliothèque : le **fond** (contenu) et la **forme** (fonctionnalités). Autorité :
chaque atelier **décline et précise** ce socle dans son `WORKFLOW.md` — il le
référence au lieu de le recopier, et ne le contredit jamais. Une évolution du socle
s'applique à tous les ateliers.

## Fond — le contenu des lectures

Observé dans les livres publiés, tenu pour acquis sauf correction :

- **Langue française**, registre littéraire soigné (`lang="fr"`).
- **Un univers pensé avant d'être écrit** : promesse émotionnelle, idée centrale et
  question thématique posées dès l'étape de plan (elles figurent dans les données
  du livre, bloc `world` de l'îlot JSON pour la famille « Atelier »).
- **Une dimension explorable** : le récit s'accompagne d'une matière encyclopédique
  (codex de personnages, lieux, concepts — ou l'équivalent du format) qui
  récompense la curiosité sans être nécessaire à la compréhension.
- **Intégrité référentielle parfaite** : aucune fiche orpheline, aucun lien mort,
  aucune incohérence entre le récit et sa matière annexe.
- **Métadonnées de catalogue soignées** : description en 1-2 phrases donnant envie
  sans divulgâcher, 1 à 6 tags pertinents.
- **Provenance assumée** : `book:author` = le nom du modèle qui écrit ; pour un
  livre multi-agents, les rôles sont détaillés dans la PR.

*(à compléter par Pierre)* :

- Thèmes et genres favoris ; thèmes à éviter ou exclus.
- Tons privilégiés (contemplatif, haletant, humoristique…).
- Longueurs cibles (nombre de chapitres, mots par chapitre).
- Public visé (tout public ? contenus sensibles ?).

## Forme — les fonctionnalités des lectures

Attendu de toute lecture publiée, quel que soit son format :

- **Autonomie totale** : un fichier/dossier téléchargé se lit hors ligne, sans CDN
  ni ressource distante.
- **Accessibilité** : navigation clavier complète, `alt` sur toutes les images,
  `prefers-color-scheme` (thème sombre) et `prefers-reduced-motion` respectés.
- **Orientation du lecteur** : un sommaire, une indication de progression.
- **Exploration non linéaire** : l'accès à la matière annexe (codex ou équivalent)
  depuis le fil du récit, avec déverrouillage progressif si le format s'y prête.
- **Reprise de lecture** : persistance de la position en localStorage, clé
  **exactement** `<slug>-state-v1`, dans le livre uniquement (jamais côté index).
- **Confort** : réglage de taille de texte ; pas de décalage de mise en page
  (images dimensionnées, chargement paresseux hors première image).
- **Sobriété des ressources** : images compressées (WebP ≤ 150 Ko visé par image de
  chapitre, couverture < 300 Ko), pas de JavaScript superflu.

*(à compléter par Pierre)* :

- Fonctionnalités de liseuse à généraliser ou au contraire à abandonner (ex. carte,
  graphe de relations, mode impression, lecture audio).

## Ce que ce socle n'est pas

- Ce n'est **pas** le contrat de plateforme (slug, meta `book:*`, couverture 2:3,
  1 niveau de dossier…) — celui-ci est dans
  [`creer-un-atelier.md`](creer-un-atelier.md) §1 et vérifié par la CI.
- Ce n'est **pas** la recette d'un format : les choix propres à un type de livrable
  (structure de l'îlot JSON, nombre d'images, style de codex) vivent dans le
  `WORKFLOW.md` de l'atelier concerné.
