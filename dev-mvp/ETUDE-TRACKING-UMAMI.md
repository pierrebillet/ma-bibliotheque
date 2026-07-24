# Chantier d’exploration — Tracking avec Umami

Statut : document de cadrage exploratoire, non normatif  
Projet : Ma Bibliothèque HTML  
Périmètre : bibliothèque GitHub Pages, livres HTML autonomes, instance Umami self-hostée sur Cloudron

## 1. Intention

Étudier l’ajout d’une mesure d’usage utile, sobre et respectueuse de la vie privée, sans transformer prématurément la bibliothèque statique en application avec backend.

Le chantier doit répondre à deux questions distinctes :

1. quelles informations sont réellement utiles pour piloter la bibliothèque et améliorer l’expérience ;
2. quelle intégration technique permet de les collecter sans casser les invariants du projet.

Ce document ne présume pas du plan d’implémentation final. Il ouvre les axes à approfondir et demande de comparer plusieurs variantes avant décision.

## 2. Point de départ à préserver ou à réexaminer explicitement

La version actuelle repose sur les principes suivants :

- site public statique hébergé sur GitHub Pages ;
- catalogue généré automatiquement à partir de `livres/*.html` ;
- livres servis par URL directe, sans iframe ;
- HTML, CSS et JavaScript natifs ;
- chemins relatifs compatibles avec un sous-chemin GitHub Pages ;
- ajout courant d’un livre limité au dépôt d’un fichier HTML ;
- aucune clé privée ni donnée sensible dans le frontend ;
- chaque slug de fichier constitue l’identifiant stable du livre.

La spécification v1 demande également que les livres soient copiés sans modification et que le site d’index n’utilise pas de stockage applicatif. Une intégration automatique du tracking dans tous les livres pourrait donc nécessiter une évolution explicite de cette règle, ou une convention volontaire appliquée dans chaque livre.

Avant toute implémentation, réconcilier les documents et livrables existants : certaines versions décrivent un artefact `_site/` construit par GitHub Actions, d’autres un déploiement direct depuis `main` avec `catalog.json` versionné. Le choix retenu influence fortement la capacité à injecter automatiquement un script commun.

## 3. Questions produit à approfondir

Ne pas commencer par une liste exhaustive d’événements. Commencer par les décisions que les données devront éclairer.

Exemples :

- quels livres attirent réellement l’attention ;
- quels livres sont ouverts mais peu poursuivis ;
- quels chapitres concentrent les abandons ;
- quelles interactions internes sont utilisées ;
- quelles recherches ne retournent aucun résultat ;
- quels filtres facilitent la découverte ;
- quelle proportion des lecteurs revient ;
- quels parcours conduisent à une lecture terminée ;
- quels formats ou longueurs de livres fonctionnent le mieux ;
- quelles fonctionnalités ajoutées ont un usage suffisant pour être conservées.

Pour chaque question, préciser : décision associée, métrique nécessaire, granularité acceptable, risque de surcollecte et durée de conservation utile.

## 4. Périmètre d’événements à explorer

### Bibliothèque

- `library-view` : arrivée sur l’index.
- `search-use` : utilisation de la recherche, idéalement sans transmettre le texte libre brut.
- `search-no-result` : recherche ne produisant aucun résultat.
- `filter-change` : changement de tag, statut ou autre filtre.
- `sort-change` : changement du tri.
- `book-open` : clic depuis une carte vers un livre.
- `copy-link` : copie de l’URL d’un livre.
- `favorite-toggle` : ajout ou retrait local d’un favori, si cette fonction existe.
- `reading-list-view` : ouverture d’une vue personnelle locale.
- `progress-export` et `progress-import` : usage des fonctions de portabilité, sans envoyer le contenu du fichier.

### Livres

- `book-view` : chargement effectif du fichier HTML.
- `chapter-view` : chapitre ou section réellement affiché.
- `chapter-resume` : reprise depuis une progression sauvegardée.
- `progress-threshold` : franchissement de seuils sobres, par exemple 25, 50, 75 et 100 %.
- `book-complete` : lecture considérée comme terminée selon une règle explicite.
- `modal-open` : ouverture d’un codex, glossaire, aide ou autre panneau.
- `codex-entry-open` : consultation d’une entrée donnée.
- `map-location-open` : interaction avec un lieu sur une carte.
- `choice-made` : choix narratif ou interactif, uniquement si pertinent et non révélateur de données personnelles.
- `share-use` : utilisation d’une fonction de partage.
- `offline-save` : demande de disponibilité hors ligne, si une PWA est ajoutée.

### Principes de taxonomie

- préférer un petit nombre de noms génériques avec des propriétés structurées ;
- réutiliser le slug du livre comme `book_id` ;
- définir des identifiants stables pour chapitres, modales et entrées ;
- éviter de créer un événement distinct pour chaque titre ;
- versionner la convention d’événements ;
- documenter les événements supprimés ou renommés ;
- ne jamais envoyer de texte libre, email, nom, identifiant personnel ou contenu de note.

Exemple de propriétés conceptuelles :

```text
book_id
chapter_id
chapter_index
interaction_type
item_id
source
progress_threshold
catalog_version
event_schema_version
```

## 5. Scénarios techniques à comparer

### Scénario A — Intégration manuelle dans l’index et chaque livre

Chaque fichier charge le tracker Umami et déclenche ses événements.

Avantages :

- mise en œuvre immédiate ;
- aucune transformation au build ;
- chaque livre choisit ses événements spécifiques.

Limites :

- risque d’oubli ;
- duplication de code ;
- maintenance difficile sur une collection croissante ;
- instrumentation hétérogène.

### Scénario B — Script partagé référencé par convention

L’index et les livres chargent un fichier commun, par exemple `assets/js/analytics.js`.

Avantages :

- taxonomie et garde-fous centralisés ;
- désactivation globale possible ;
- maintenance plus simple ;
- adaptation future du fournisseur sans modifier toute la logique métier.

Limites :

- chaque livre doit encore inclure la référence ;
- le chemin relatif doit fonctionner depuis `livres/` ;
- les livres ne sont plus totalement autonomes hors du site, sauf fallback intégré.

### Scénario C — Injection automatique pendant le build GitHub Actions

Le dépôt conserve les fichiers sources, puis le build copie les livres dans `_site/` et ajoute le tracker à la version publiée.

Avantages :

- couverture exhaustive ;
- aucun oubli lors de l’ajout d’un livre ;
- conservation du geste utilisateur « déposer un seul HTML » ;
- possibilité d’injecter d’autres capacités communes plus tard.

Limites :

- contradiction avec la règle actuelle de copie octet pour octet ;
- complexité du parseur et des cas HTML mal formés ;
- risque de casser un livre atypique ;
- nécessité d’un mécanisme de contrôle, d’idempotence et de tests solides.

Étudier aussi une variante moins intrusive : injection uniquement dans les livres portant une métadonnée d’opt-in, ou ajout d’un petit bootstrap avant `</body>` avec fallback lorsque cette balise n’existe pas.

### Scénario D — Instrumentation limitée à l’index

Mesurer uniquement l’arrivée, la recherche, les filtres et le clic vers un livre.

Avantages : effort et risque très faibles.

Limites : aucune mesure de lecture réelle une fois le livre ouvert.

Cette variante peut constituer une première étape utile avant l’instrumentation des livres.

## 6. Umami et Cloudron : sujets à vérifier

L’étude détaillée devra confirmer sur la version réellement installée :

- méthode de déploiement Cloudron ;
- domaine dédié, certificat HTTPS et configuration DNS ;
- comportement du script sur un site GitHub Pages placé dans un sous-chemin ;
- prise en charge des événements personnalisés et de leurs propriétés ;
- définition de funnels, objectifs et segments ;
- API disponible pour exporter ou retraiter les données ;
- gestion des utilisateurs administrateurs ;
- stratégie de sauvegarde et restauration de la base ;
- mises à jour Cloudron et compatibilité des versions ;
- rétention configurable ;
- anonymisation ou traitement des adresses IP ;
- désactivation des paramètres d’URL ou des référents sensibles ;
- comportement avec bloqueurs de publicité et protections anti-tracking ;
- possibilité de renommer le fichier de collecte ou son endpoint ;
- disponibilité en cas d’indisponibilité temporaire de Cloudron ;
- impact de performance et stratégie de chargement non bloquante.

Ne pas supposer que toutes les fonctions de la documentation actuelle sont disponibles sur la version packagée par Cloudron : les vérifier dans l’instance cible.

## 7. Mesures et analyses potentielles

### Funnel minimal

```text
Visite de la bibliothèque
→ exposition ou clic sur une carte
→ ouverture effective du livre
→ premier chapitre vu
→ seuil de progression
→ fin du livre
```

### Analyses par livre

- taux d’ouverture depuis la carte ;
- progression médiane ;
- distribution des chapitres atteints ;
- taux de complétion ;
- délai entre première ouverture et fin ;
- reprise après interruption ;
- interactions utilisées ;
- source d’entrée directe ou bibliothèque.

### Analyses bibliothèque

- recherches fréquentes sans résultat, éventuellement transformées en catégories côté client plutôt qu’envoyées en clair ;
- tags et tris utilisés ;
- cartes visibles mais rarement ouvertes ;
- livres découverts par recherche, filtre, recommandation ou accès direct ;
- retour des visiteurs sur une période donnée, sans chercher à reconstruire une identité personnelle.

### Qualité des métriques

Pour chaque indicateur, documenter :

- définition exacte ;
- événement source ;
- déduplication ;
- cas offline ;
- rechargements et retours arrière ;
- bots et préchargements ;
- événements manquants causés par les bloqueurs ;
- précision acceptable.

## 8. Vie privée, conformité et sobriété

Le caractère self-hosted ou sans cookie ne suffit pas à conclure automatiquement à l’absence de consentement ou d’obligations.

Le chantier doit produire :

- une cartographie des données collectées ;
- une liste explicite des données interdites ;
- une analyse de la finalité et de la base juridique ;
- une durée de conservation ;
- une politique d’accès à l’instance ;
- un texte d’information utilisateur ;
- une option d’opposition si nécessaire ;
- une vérification du traitement des IP et user agents ;
- une vérification de l’absence de recoupement avec d’autres bases ;
- une procédure de purge ;
- une stratégie de journalisation technique distincte de l’analytics produit.

Principe par défaut : collecter moins, agréger davantage et refuser tout champ libre.

## 9. Plan d’expérimentation suggéré

### Phase 1 — Index uniquement

- intégrer Umami sur la page bibliothèque ;
- mesurer vues, clics livre, recherches sans résultat, filtres et tris ;
- vérifier la performance, la fiabilité et les impacts réglementaires ;
- stabiliser les conventions d’événements.

### Phase 2 — Livre pilote

- instrumenter uniquement le livre d’exemple ;
- mesurer chapitre, progression et interactions ;
- tester navigation mobile, rafraîchissement, accès direct et blocage réseau ;
- comparer les données avec des tests manuels connus.

### Phase 3 — Généralisation

- choisir entre convention manuelle, script partagé ou injection au build ;
- ajouter validations et tests ;
- documenter le protocole pour les futurs livres ;
- mettre à jour la recette de bout en bout.

## 10. Tests à prévoir

- sous-chemin GitHub Pages ;
- domaine personnalisé ;
- Chrome, Firefox, Safari, Edge, iOS et Android ;
- bloqueur de contenu ;
- mode privé ;
- accès direct à un chapitre par ancre ;
- navigation interne sans rechargement ;
- livre avec HTML incomplet ou mal formé ;
- perte de connexion à Umami ;
- instance Cloudron indisponible ;
- navigation hors ligne ;
- multiples onglets ;
- rechargements rapides ;
- absence totale du script analytics.

Le site et les livres doivent rester pleinement fonctionnels lorsque le tracker est bloqué ou indisponible.

## 11. Décisions ouvertes

- faut-il mesurer uniquement les usages globaux ou aussi des sessions anonymes ;
- faut-il instrumenter tous les livres ou uniquement ceux qui déclarent une compatibilité ;
- faut-il modifier la règle « livres copiés octet pour octet » ;
- faut-il conserver les paramètres d’URL ;
- faut-il suivre les textes de recherche, des catégories dérivées ou seulement le statut avec/sans résultat ;
- quelle définition fait foi pour « chapitre vu » et « livre terminé » ;
- quelle durée de conservation est réellement utile ;
- qui peut accéder aux données ;
- quelles métriques justifient durablement leur coût de maintenance.

## 12. Livrables attendus d’une étude approfondie

L’approfondissement libre devra idéalement produire :

1. une architecture cible comparant au moins trois scénarios ;
2. une taxonomie d’événements versionnée ;
3. un plan de mesure reliant questions, événements et décisions ;
4. un prototype sur l’index et un livre pilote ;
5. une analyse RGPD documentée ;
6. une matrice de compatibilité et de défaillance ;
7. un plan de déploiement progressif et de retour arrière ;
8. les modifications nécessaires dans `SPEC.md`, `CONVENTIONS.md`, les scripts, tests, guides et recette ;
9. une estimation de maintenance Cloudron ;
10. une recommandation argumentée, sans considérer Umami comme acquis si une solution plus simple suffit.

## 13. Critère de décision

Le tracking est pertinent s’il permet de répondre à quelques questions produit précises, reste non bloquant, n’introduit aucune donnée personnelle inutile et ne dégrade pas la promesse centrale : publier un livre autonome par simple dépôt d’un fichier HTML.
