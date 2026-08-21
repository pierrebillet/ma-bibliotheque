# PREFERENCES.md — socle éditorial commun

> **Statut : socle validé par Pierre le 2026-08-21** (chantier 3 de la
> [roadmap Conception](ROADMAP.md)), avec un assouplissement : les **quantités**
> (nombre et taille des chapitres et des notices) sont libres par défaut —
> voir « Quantités ». Ce document évolue par pull request, et chaque brief
> peut le surcharger ponctuellement.

Ce socle rassemble les préférences transverses à **toutes** les lectures de la
bibliothèque : le **fond** (contenu) et la **forme** (fonctionnalités). Autorité :
chaque atelier **décline et précise** ce socle dans son `WORKFLOW.md` — il le
référence au lieu de le recopier, et ne le contredit jamais. Une évolution du socle
s'applique à tous les ateliers.

## Fond — le contenu des lectures

Tenu pour acquis :

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
  sans divulgâcher, 2 à 4 tags pertinents (gouvernance des tags :
  [`docs/bibliotheque/CATALOGUE.md`](../bibliotheque/CATALOGUE.md)).
- **Provenance assumée** : `book:author` = le nom du modèle qui écrit ; pour un
  livre multi-agents, les rôles sont détaillés dans la PR.

**Défauts du socle** *(validés par Pierre le 2026-08-21 ; ils évoluent par PR
et chaque brief peut les surcharger au cas par cas)* :

- **Genres** : ceux du catalogue actuel comme terrain naturel — récit
  d'atmosphère littéraire, espionnage, science-fiction sociale, mystère — sans
  s'y enfermer : le brief fixe le genre. Pas de genre exclu a priori.
- **Tons** : registre littéraire soigné, tension retenue plutôt que
  spectaculaire ; l'humour est bienvenu s'il sert la voix du livre.
- **Style et voix** : le point de vue et le temps du récit se choisissent à
  l'étape de plan et se tiennent sur tout le livre. Montrer plutôt
  qu'expliquer — l'émotion naît des gestes, des lieux et des silences, pas de
  leur commentaire. L'incipit fait une promesse dès la première page ; la
  chute paie la promesse émotionnelle et répond, même obliquement, à la
  question thématique. Les titres de chapitres évoquent sans divulgâcher.
  Typographie française soignée et **uniforme** : apostrophe typographique
  (« ’ », jamais « ' »), guillemets à chevrons « … » avec espaces insécables,
  dialogues au tiret cadratin (—) ou entre guillemets — une seule convention
  par livre, tenue de bout en bout.
- **Quantités : libres, la pertinence décide.** Le nombre et la taille des
  chapitres, le nombre et la taille des notices sont fixés par le brief quand
  il le demande ; à défaut, **l'auteur en décide librement** — le seul critère
  est la pertinence : tout ce qui sert le livre y entre, et **rien ne s'écrit
  pour remplir**. Un chapitre ou une notice qui n'apporte rien se fusionne ou
  se retire. À titre de repère, la référence de qualité `lequation-du-calme`
  fait 10 chapitres d'environ 2 500 mots et une trentaine de notices.
- **Exploration dense** : c'est ce qui distingue les meilleurs livres du
  catalogue — une bonne part des blocs de texte porte une mention vers la
  matière annexe (repère : **au moins 40 %**, le vérificateur avertit en
  dessous). Ce repère est un **plancher indicatif, pas une cible à
  maximiser** : une mention se pose parce qu'elle récompense la curiosité du
  lecteur, jamais pour cocher un quota — un récit sur-lié sollicite le lecteur
  à chaque paragraphe comme un récit sous-lié l'abandonne.
- **Public** : tout public. Pas de contenus sensibles (violence graphique,
  sexualité explicite) sauf demande explicite du brief.

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
- **Couverture sans texte** : aucun titre, sous-titre, nom, crédit, logo,
  signature, filigrane ni pseudo-texte n'est incrusté dans l'image ; l'interface
  HTML de la bibliothèque porte déjà le titre et les métadonnées.

**Défauts du socle** *(même statut que ci-dessus)* :

- **À généraliser** — le socle du moteur de référence
  [`livres/_template/`](../../livres/_template/README.md) : dialogues natifs
  avec piège de focus, visionneuse d'illustrations, annonces `aria-live` des
  déblocages, dégradation propre des images manquantes, et **impression propre
  de la vue affichée** (acquise depuis `atelier-liseuse v3`).
- **Optionnelles sur demande du brief** — **carte des lieux** et **graphe de
  relations** : depuis `atelier-liseuse v3` ce sont des modules du moteur, plus
  des inventions à refaire livre par livre. Ne pas les imposer, ne pas les
  interdire ; le brief les demande, l'atelier les remplit depuis le codex, et le
  livre les déclare dans `book:capacites`. Rien à signaler dans la PR : ce n'est
  plus une divergence de moteur.
- **Encore hors moteur** — les fonctionnalités qu'aucune version du template ne
  sait faire (choix et branches, lecture audio, gestes tactiles) : une demande
  de brief reste alors une divergence de moteur, signalée dans la PR.
- **À abandonner** — aucune fonctionnalité identifiée à ce jour.

## Ce que ce socle n'est pas

- Ce n'est **pas** le contrat de plateforme (slug, meta `book:*`, couverture 2:3,
  1 niveau de dossier…) — celui-ci est dans
  [`creer-un-atelier.md`](creer-un-atelier.md) §1 et vérifié par la CI.
- Ce n'est **pas** la recette d'un format : les choix propres à un type de livrable
  (structure de l'îlot JSON, nombre d'images, style de codex) vivent dans le
  `WORKFLOW.md` de l'atelier concerné.
