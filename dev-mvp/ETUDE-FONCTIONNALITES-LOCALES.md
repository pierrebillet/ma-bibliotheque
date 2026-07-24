# Chantier d’exploration — Fonctionnalités utilisateur locales

Statut : document de cadrage exploratoire, non normatif  
Projet : Ma Bibliothèque HTML  
Technologies envisagées : `localStorage`, APIs navigateur, export/import de fichiers

## 1. Intention

Créer un « espace lecteur » utile sans compte, sans backend et sans synchronisation automatique, en assumant clairement que les données appartiennent au navigateur et à l’appareil courant.

Le but n’est pas de simuler une authentification. Il s’agit de donner une continuité locale à l’usage : reprendre une lecture, organiser sa bibliothèque, noter les livres et transporter manuellement ses données entre appareils.

## 2. Écart avec la version normative actuelle

La spécification v1 interdit explicitement l’usage de `localStorage` par l’index et demande que le livre d’exemple ne conserve rien entre les sessions. Ajouter ces fonctions constitue donc une évolution de produit et de schéma, pas une simple correction invisible.

Avant implémentation, prévoir une version suivante des documents normatifs et mettre à jour au minimum :

- `SPEC.md` ;
- `CONVENTIONS.md` ;
- le frontend ;
- le livre d’exemple ;
- les tests ;
- les guides ;
- la recette ;
- éventuellement le schéma du catalogue si de nouvelles métadonnées publiques sont nécessaires.

La règle d’ajout « déposer un seul livre HTML » doit rester un invariant central. Toute capacité commune doit donc être disponible sans demander une manipulation technique supplémentaire à chaque publication ordinaire, ou être clairement déclarée comme optionnelle.

## 3. Fonctionnalités de base à étudier

### Continuité de lecture

- mémoriser le dernier chapitre ou la dernière section consultée ;
- mémoriser le chapitre le plus avancé atteint ;
- enregistrer un pourcentage ou un seuil de progression ;
- proposer « reprendre » depuis l’index ;
- distinguer « jamais commencé », « en cours », « terminé » et éventuellement « abandonné » ;
- enregistrer la date de dernière ouverture ;
- conserver le dernier emplacement visible pour les livres à défilement continu.

### Organisation personnelle

- favoris ;
- liste « à lire » ;
- étagères locales : en cours, terminé, abandonné ;
- listes personnalisées ;
- archivage ou masquage local ;
- historique des livres ouverts ;
- tri par dernière consultation ou progression.

### Évaluation et préférences

- note personnelle sur 5 ;
- appréciation rapide ;
- préférences d’affichage : thème, taille, largeur de colonne, interlignage ;
- filtres et tri persistants ;
- mode faible distraction ;
- paramètres d’accessibilité mémorisés.

### Portabilité

- export de toutes les données locales dans un fichier ;
- import sur un autre navigateur ou appareil ;
- choix entre remplacement et fusion ;
- aperçu du contenu avant validation ;
- export sélectif : progression, favoris, notes, filtres ou tout ;
- sauvegardes datées ;
- restauration d’une sauvegarde antérieure.

## 4. Architecture à approfondir

### Couche de stockage centralisée

Éviter tout accès direct dispersé à `localStorage`. Créer une couche unique, par exemple :

```text
assets/js/library-state.js
```

Cette couche devrait être responsable de :

- lecture et écriture ;
- valeurs par défaut ;
- validation ;
- migrations de version ;
- gestion des erreurs ;
- import et export ;
- fusion ;
- synchronisation entre onglets ;
- abstraction future vers IndexedDB ou Supabase.

Les composants d’interface ne devraient manipuler que des fonctions métier telles que :

```text
getBookState
updateBookProgress
setBookRating
toggleFavorite
saveLibraryFilters
exportState
importState
```

### Modèle de données conceptuel

```json
{
  "schemaVersion": 1,
  "exportedAt": "2026-07-24T10:00:00Z",
  "library": {
    "filters": {},
    "preferences": {}
  },
  "books": {
    "le-jardin-des-possibles": {
      "status": "reading",
      "currentChapter": "le-sentier",
      "furthestChapter": "le-sentier",
      "progress": 75,
      "rating": 4,
      "favorite": true,
      "lastOpenedAt": "2026-07-24T09:55:00Z",
      "updatedAt": "2026-07-24T09:55:00Z"
    }
  }
}
```

Ce modèle est illustratif. L’étude devra comparer une structure unique, plusieurs clés spécialisées et éventuellement IndexedDB.

### Identifiants

Le slug est aujourd’hui l’identifiant stable d’un livre. Conséquence : renommer le fichier crée techniquement un nouveau livre et laisse une ancienne progression orpheline.

Approfondir :

- politique de non-renommage ;
- table d’alias au build ;
- métadonnée d’identifiant durable distincte du slug ;
- migration manuelle des données ;
- détection des entrées locales sans livre correspondant.

## 5. Intégration aux livres autonomes

Le stockage est partagé uniquement entre pages de même origine. La bibliothèque et les livres doivent donc être servis sous le même domaine et protocole.

Comparer plusieurs modalités :

### Convention dans chaque livre

Chaque livre inclut une petite API commune ou son propre code de progression.

- simple à tester ;
- compatible avec les livres vraiment autonomes ;
- risque d’hétérogénéité.

### Script partagé

Les livres appellent un fichier commun situé dans les assets de la bibliothèque.

- logique centralisée ;
- maintenance facilitée ;
- dépendance au contexte de publication ;
- autonomie hors ligne ou hors domaine à traiter.

### Injection au build

Le pipeline ajoute un bootstrap commun lors de la publication.

- aucun oubli ;
- préserve l’expérience d’ajout d’un fichier ;
- remet en cause la copie binaire actuelle ;
- nécessite une stratégie robuste pour les HTML atypiques.

### Contrat minimal par métadonnées

Un livre déclare des informations comme son identifiant de chapitre courant ou ses capacités, puis la couche commune s’adapte.

- extensible ;
- nécessite de définir une convention supplémentaire ;
- doit rester facultatif pour les livres simples.

## 6. Export et import

### Export

Le fichier devrait être :

- lisible et portable ;
- versionné ;
- daté ;
- limité aux données personnelles locales de lecture ;
- indépendant des détails internes du navigateur ;
- exempt de secrets ;
- validable avant import.

Explorer les formats :

- JSON comme format canonique ;
- CSV pour certains tableaux ;
- HTML autonome pour un bilan lisible ;
- archive ZIP uniquement si plusieurs fichiers deviennent nécessaires.

### Import avec remplacement

Comportement : effacer l’état local actuel et le remplacer par celui du fichier.

Prévoir :

- avertissement clair ;
- aperçu du nombre de livres et données concernées ;
- sauvegarde automatique préalable ;
- confirmation finale ;
- restauration en cas d’échec partiel.

### Import avec fusion

Définir explicitement les conflits :

- progression : valeur la plus avancée ou donnée la plus récente ;
- chapitre courant : donnée la plus récente ;
- statut terminé : conserver sauf choix explicite contraire ;
- note : valeur la plus récente ;
- favori : stratégie booléenne à définir ;
- filtres : conserver local, importé ou demander ;
- listes personnalisées : union, remplacement ou fusion par identifiant.

Aucune règle de fusion n’est universellement correcte. L’étude doit proposer plusieurs politiques et des exemples de conflits concrets.

### Robustesse de l’import

- taille maximale raisonnable ;
- type de fichier ;
- JSON invalide ;
- version future inconnue ;
- champs supplémentaires ;
- livres absents du catalogue actuel ;
- doublons ;
- dates invalides ;
- progression hors bornes ;
- import interrompu ;
- fichier créé par une ancienne version.

Ne jamais exécuter de contenu importé ni l’injecter comme HTML.

## 7. Limites à communiquer clairement

- aucune synchronisation automatique entre appareils ;
- aucune récupération si le navigateur est réinitialisé sans export ;
- données perdues en navigation privée ;
- stockage distinct par domaine et protocole ;
- migration non automatique lors d’un changement de domaine ;
- données modifiables par l’utilisateur dans les outils développeur ;
- absence de garantie forte de conservation ;
- capacités variables selon navigateur et politiques de stockage ;
- pas de contrôle d’accès réel ;
- pas de contenu payant ou privé fondé sur cet état.

Le vocabulaire d’interface devrait parler de « données enregistrées sur cet appareil » et non de « compte ».

## 8. `localStorage` ou IndexedDB

### `localStorage`

Adapté à :

- états légers ;
- favoris ;
- notes ;
- progression ;
- filtres ;
- préférences ;
- listes simples.

Contraintes : synchrone, capacité limitée, sérialisation JSON, absence de transactions complexes.

### IndexedDB

À étudier lorsque le produit ajoute :

- annotations nombreuses ;
- contenu hors ligne ;
- fichiers ou couvertures stockés localement ;
- historique détaillé ;
- index de recherche volumineux ;
- objets complexes ou migrations importantes.

Le chantier peut prévoir une interface de stockage indépendante pour éviter une réécriture future.

## 9. Expérience utilisateur à approfondir

- indicateur discret « enregistré sur cet appareil » ;
- bouton reprendre sur les cartes ;
- progression visible sans surcharger la grille ;
- vue « Ma liste » ;
- contrôle accessible de note et favori ;
- gestion des données dans un panneau unique ;
- export/import compréhensible pour un utilisateur non technique ;
- retour après fusion précisant ce qui a changé ;
- fonction « effacer mes données locales » ;
- réinitialisation par livre ;
- option pour ne pas mémoriser l’historique ;
- comportement lisible lorsque le stockage est indisponible.

Ne pas imposer une interface de compte ou un avatar qui suggérerait une persistance serveur inexistante.

## 10. Synchronisation locale et cohérence

Approfondir l’usage de :

- l’événement `storage` pour refléter les changements entre onglets ;
- `BroadcastChannel` pour des messages plus explicites ;
- horodatages `updatedAt` ;
- verrouillage léger lors d’un import ;
- écritures atomiques par remplacement complet ;
- sauvegarde précédente avant migration ;
- journal minimal de migrations, sans historique illimité.

Tester le cas où un livre et l’index sont ouverts simultanément.

## 11. Vie privée et sécurité

Même locales, les données peuvent révéler des habitudes de lecture. Prévoir :

- absence de données sensibles par défaut ;
- pas de note textuelle libre dans le premier MVP ;
- export déclenché explicitement ;
- aucune transmission automatique ;
- avertissement avant import ;
- validation stricte des fichiers ;
- affichage uniquement avec `textContent` ;
- possibilité de supprimer l’ensemble des données ;
- documentation de ce qui reste local et de ce qui pourrait être envoyé à l’analytics.

Si Umami est ajouté, décider quels événements locaux peuvent être mesurés sans envoyer leur contenu. Par exemple, suivre `favorite-toggle` est possible, mais pas le nom d’une liste personnalisée.

## 12. Migration future vers Supabase

Préparer sans implémenter prématurément :

- modèle local proche du futur modèle distant ;
- identifiants stables ;
- couche d’accès abstraite ;
- champ `updatedAt` ;
- mécanisme de fusion déjà défini ;
- import initial de l’état local lors de la création d’un compte ;
- mode offline-first éventuel ;
- séparation entre préférences locales et données synchronisées.

Le passage à Supabase devient pertinent lorsque sont nécessaires :

- synchronisation automatique multi-appareils ;
- récupération de compte ;
- partage de listes ;
- données privées hébergées ;
- recommandations serveur ;
- interactions sociales ;
- notifications ;
- droits d’accès.

Une migration vers Supabase n’oblige pas automatiquement à quitter GitHub Pages. Le passage à une web app Vercel doit être justifié par des besoins supplémentaires, pas par l’authentification seule.

## 13. Plan de mise en œuvre progressif à étudier

### Lot 1 — Fondation

- couche de stockage versionnée ;
- progression par livre ;
- favoris ;
- note sur 5 ;
- filtres persistants ;
- panneau d’effacement des données.

### Lot 2 — Portabilité

- export JSON ;
- import avec remplacement ;
- import avec fusion ;
- validation et aperçu ;
- sauvegarde automatique avant import.

### Lot 3 — Expérience personnelle

- page « Ma liste » ;
- reprendre la lecture ;
- historique ;
- statuts ;
- tris personnels.

### Lot 4 — Robustesse

- migrations de schéma ;
- compatibilité entre onglets ;
- gestion des livres renommés ou supprimés ;
- IndexedDB si nécessaire ;
- tests étendus.

## 14. Matrice de tests

- première visite sans données ;
- stockage désactivé ou quota atteint ;
- navigation privée ;
- rechargement ;
- fermeture et réouverture ;
- livre ouvert directement ;
- index et livre dans deux onglets ;
- changement de chapitre rapide ;
- note et favori ;
- export vide ;
- export volumineux ;
- import valide ;
- import invalide ;
- remplacement ;
- fusion sans conflit ;
- fusion avec conflits ;
- ancienne version du schéma ;
- livre absent du catalogue ;
- renommage de slug ;
- mobile Safari et Chrome Android ;
- domaine GitHub Pages puis domaine personnalisé.

## 15. Décisions ouvertes

- progression par chapitre, pourcentage, position de scroll ou combinaison ;
- définition de « terminé » ;
- favoris et liste à lire comme notions séparées ou non ;
- statut manuel ou automatique ;
- portée des notes ;
- prise en charge de listes personnalisées dès le MVP ;
- stratégie de conflit à l’import ;
- conservation des données orphelines ;
- identifiant durable indépendant du slug ;
- besoin d’IndexedDB ;
- niveau de transparence dans l’interface ;
- frontière exacte entre état du livre et état de la bibliothèque.

## 16. Livrables attendus d’une étude approfondie

1. modèle de données versionné ;
2. contrat de l’API de stockage ;
3. règles d’import, remplacement et fusion illustrées ;
4. maquettes des principaux états ;
5. prototype sur l’index et le livre d’exemple ;
6. plan de migration depuis la v1 sans stockage ;
7. matrice de compatibilité navigateur ;
8. tests automatisés et manuels ;
9. modifications documentaires nécessaires ;
10. stratégie de migration future vers un backend, sans l’implémenter tant qu’elle n’est pas justifiée.

## 17. Critère de décision

Ces fonctionnalités sont adaptées au MVP si elles restent compréhensibles, locales, exportables, non critiques et compatibles avec l’ajout d’un livre en un seul fichier. Elles ne doivent jamais être présentées comme un compte sécurisé ou une sauvegarde garantie.
