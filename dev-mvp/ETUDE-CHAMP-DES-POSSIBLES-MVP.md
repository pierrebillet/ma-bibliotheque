# Chantier d’exploration — Champ des possibles fonctionnels du MVP

Statut : document d’opportunités, non normatif  
Projet : Ma Bibliothèque HTML  
Périmètre : GitHub Pages, JavaScript navigateur, GitHub Actions, fichiers statiques, Cloudron/n8n en extension facultative

## 1. Intention

Explorer largement ce que la stack actuelle permet avant de conclure qu’une migration vers une web app complète est nécessaire.

La stack n’est pas limitée à une grille de liens. Elle peut combiner :

- calcul et état dans le navigateur ;
- stockage local ;
- APIs natives du navigateur ;
- génération de fichiers ;
- prétraitements au build par GitHub Actions ;
- publication statique rapide ;
- services facultatifs comme Umami ou n8n ;
- progressive web app et cache hors ligne.

Le but est d’identifier des directions produit fortes, pas d’empiler toutes les fonctions possibles.

## 2. Invariants à protéger

- ajouter un livre reste aussi simple que déposer un HTML dans `livres/` ;
- les livres restent accessibles par URL directe ;
- aucune opération locale ou ligne de commande n’est imposée à l’utilisateur du dépôt ;
- aucune clé privée n’est publiée ;
- les chemins restent relatifs ;
- les fonctions avancées échouent sans empêcher la lecture ;
- le site reste utilisable sur mobile et au clavier ;
- les fonctionnalités locales sont présentées comme locales ;
- toute dépendance réseau est optionnelle et non bloquante ;
- les automatisations restent testables et maintenables.

Tout concept qui détruit ces invariants doit prouver une valeur produit nettement supérieure.

## 3. Cadre d’évaluation

Pour chaque idée, évaluer :

1. valeur lecteur ;
2. valeur éditoriale ;
3. différenciation ;
4. fréquence d’usage ;
5. effort initial ;
6. coût de maintenance ;
7. dépendances ;
8. compatibilité mobile ;
9. accessibilité ;
10. vie privée ;
11. impact sur l’ajout d’un livre ;
12. réversibilité.

Classer ensuite les idées selon quatre niveaux :

- navigateur statique uniquement ;
- navigateur + stockage local ;
- génération au build GitHub Actions ;
- service externe léger facultatif ;
- backend/authentification réellement requis.

## 4. Accueil personnalisé et continuité

- bloc « Reprendre ma lecture » calculé depuis l’état local ;
- derniers livres ouverts ;
- favoris et liste à lire ;
- progression visible sur les cartes ;
- statuts jamais commencé, en cours, terminé, abandonné ;
- étagères personnelles ;
- filtres et tri persistants ;
- vue dédiée aux livres non commencés ;
- masquage local de certains titres ;
- accueil différent selon l’historique de lecture ;
- raccourci vers la dernière interaction dans un livre ;
- plusieurs profils locaux sur un appareil partagé, sans prétendre à une sécurité réelle.

## 5. Découverte et curation

- bouton « Surprends-moi » ;
- roulette de sélection ;
- livre du jour déterministe ;
- recommandations basées sur tags, notes et historique local ;
- « Parce que vous avez aimé… » ;
- sélection selon le temps disponible ;
- filtre par humeur ou intensité ;
- parcours de lecture ordonnés ;
- collections éditoriales saisonnières ;
- « Commencer ici » pour les nouveaux visiteurs ;
- suggestions parmi les livres jamais ouverts ;
- découverte par proximité de tags ;
- mélange contrôlé entre nouveautés et fonds de catalogue ;
- règles de recommandation transparentes et calculées localement.

## 6. Recherche et navigation avancées

- recherche plein texte dans les livres ;
- index de recherche généré au build ;
- recherche tolérante aux fautes ;
- recherche par chapitre ou section ;
- recherche dans le codex de plusieurs livres ;
- suggestions automatiques ;
- filtres multiples ;
- filtres enregistrés ;
- recherches favorites ;
- palette de commandes au clavier ;
- navigation par auteur, série, univers ou collection ;
- frise chronologique des publications ;
- liens profonds vers un chapitre ;
- URL partageable représentant une recherche ou une collection ;
- graphe de proximité entre livres ;
- navigation « précédent/suivant » selon le tri actif ;
- détection des recherches sans résultat pour enrichir les métadonnées.

L’étude devra comparer la taille de l’index, son temps de génération, sa mise en cache et le respect des livres qui ne souhaitent pas être indexés intégralement.

## 7. PWA et usage hors ligne

- installation sur l’écran d’accueil ;
- icône et écran de lancement ;
- mode standalone ;
- catalogue disponible hors ligne ;
- mise en cache des livres choisis ;
- bouton « disponible hors ligne » ;
- gestion du stockage local utilisé ;
- suppression des téléchargements ;
- bannière de nouvelle version ;
- conservation de la dernière version valide ;
- raccourcis vers reprendre, favoris et recherche ;
- page hors ligne explicite ;
- préchargement des couvertures ou du prochain chapitre ;
- stratégie différente pour les livres très volumineux.

Approfondir les limites iOS, les mises à jour de service worker, les quotas et le risque de servir une version obsolète.

## 8. Portabilité, partage et objets générés

- export/import de progression ;
- export d’une liste de lecture ;
- fichier HTML autonome présentant sa bibliothèque personnelle ;
- CSV des notes et statuts ;
- QR code vers un livre ;
- QR code vers un chapitre ;
- partage natif mobile ;
- lien partageable d’une sélection publique ;
- carte visuelle d’une recommandation ;
- poster de bibliothèque personnelle ;
- bilan annuel exporté en image ou HTML ;
- « passeport de lecteur » ;
- sauvegardes datées ;
- fusion de plusieurs exports ;
- import de listes reçues d’autres lecteurs ;
- mode impression propre ;
- génération d’une fiche bibliographique.

Distinguer les contenus partageables sans donnée sensible des états privés destinés uniquement à la sauvegarde.

## 9. Statistiques personnelles locales

- temps de lecture estimé ;
- sessions de lecture ;
- livres commencés et terminés ;
- progression globale ;
- répartition par tags ;
- auteurs les plus lus ;
- jours de lecture ;
- séries de jours consécutifs ;
- carte thermique annuelle ;
- objectifs mensuels ou annuels ;
- bilan de fin d’année ;
- rythme moyen d’avancement ;
- livres souvent repris mais jamais terminés ;
- comparaison entre intention « à lire » et lecture réelle ;
- tableau de bord entièrement local.

Éviter une gamification qui détourne de la lecture ou laisse croire à une précision excessive du temps mesuré.

## 10. Expériences visuelles

- vue étagère ;
- mur de couvertures ;
- galerie minimaliste ;
- constellation reliant les livres proches ;
- carte des univers ;
- frise chronologique ;
- rayonnages personnels ;
- couleur d’interface dérivée de la couverture ;
- animations de classement ;
- visualisation des zones explorées de la bibliothèque ;
- carte de relations entre auteurs, thèmes et œuvres ;
- mode plein écran de découverte ;
- navigation spatiale sur grand écran ;
- visualisation des parcours de lecture ;
- poster généré depuis les favoris.

Chaque visualisation doit avoir une alternative simple et accessible ; aucune ne doit remplacer la navigation standard.

## 11. Confort, accessibilité et contrôle du lecteur

- profils typographiques persistants ;
- taille, interlignage et largeur réglables ;
- mode sombre manuel ou automatique ;
- contraste élevé ;
- réduction des animations ;
- mode focus ;
- minuteur de lecture ;
- maintien de l’écran allumé ;
- raccourcis clavier ;
- navigation gestuelle optionnelle ;
- reprise exacte au dernier emplacement ;
- lecture vocale via capacités du navigateur, avec limites documentées ;
- table des matières générée lorsqu’elle peut l’être ;
- estimation du temps restant ;
- indicateur de progression non intrusif ;
- synchronisation entre onglets ;
- contrôle global des données locales.

## 12. Fonctions éditoriales sur le catalogue

- badges nouveau, court, long, interactif, terminé ou mis à jour ;
- sélections éditoriales ;
- ordre de mise en avant configurable ;
- collections cachées accessibles par lien ;
- parcours thématiques ;
- calendrier de publication ;
- page nouveautés ;
- journal des changements ;
- mise en avant automatique des livres récemment modifiés ;
- recommandations croisées déclarées dans les métadonnées ;
- séries et ordre de lecture ;
- niveaux de difficulté ;
- temps de lecture estimé ;
- compatibilité hors ligne déclarée ;
- capacités interactives déclarées : carte, audio, codex, choix, etc.

Ces extensions pourraient nécessiter une nouvelle version du schéma `catalog.json`. Toute évolution doit rester compatible avec les livres sans métadonnées.

## 13. Automatisation par GitHub Actions

- génération du catalogue ;
- validation des métadonnées ;
- détection des slugs invalides ;
- index plein texte ;
- calcul du temps de lecture ;
- extraction de la table des matières ;
- création de miniatures ;
- optimisation des couvertures ;
- génération d’images sociales ;
- génération d’un flux RSS ou Atom ;
- sitemap ;
- manifeste PWA ;
- contrôle des liens ;
- audit d’accessibilité automatisé ;
- détection de ressources externes ;
- rapport de poids des livres ;
- inventaire des capacités interactives ;
- contrôle des identifiants de chapitres ;
- détection de doublons ;
- création d’un journal des nouveautés ;
- création d’un bundle de sauvegarde ;
- pré-calcul de recommandations ;
- validation de compatibilité offline.

Approfondir la durée de build, la simplicité des logs, les erreurs bloquantes et la conservation de la dernière version valide.

## 14. n8n et services légers facultatifs

Sans transformer le site en application serveur, n8n peut servir de périphérie :

- formulaire de retour ;
- signalement d’un problème ;
- inscription aux nouveautés ;
- email de publication ;
- création automatique d’une issue GitHub ;
- notification en cas de build invalide ;
- rapport périodique Umami ;
- sauvegarde externe ;
- enrichissement de métadonnées ;
- génération assistée de tags ;
- publication sur un canal social ;
- vote anonyme sur des évolutions ;
- réception de suggestions de lecture ;
- collecte volontaire de témoignages.

Chaque appel réseau doit avoir une finalité claire, une gestion d’erreur et une politique de données. Les secrets restent uniquement côté n8n.

## 15. Fonctions intelligentes compatibles avec une stack statique

- recommandations locales par règles ;
- recherche sémantique avec embeddings précalculés ;
- regroupement de livres par proximité ;
- classification automatique au build ;
- génération de résumés de catalogue ;
- détection des thèmes dominants ;
- parcours personnalisés depuis les favoris ;
- suggestions selon la durée disponible ;
- détection locale des livres probablement abandonnés ;
- auto-complétion à partir de l’index ;
- questions-réponses sur les métadonnées du catalogue ;
- aide à la découverte sans envoyer l’historique personnel à un serveur.

Toute fonction IA doit être évaluée selon son poids, sa transparence, sa reproductibilité et ses coûts. Le build peut pré-calculer des données, mais ne doit pas exposer de clé privée.

## 16. Qualité, gouvernance et maintenance

- page de diagnostic public ;
- rapport de compatibilité par livre ;
- version du schéma affichée ;
- détection des livres cassés ;
- badges de validation ;
- historique des déploiements ;
- mode aperçu avant publication ;
- environnement de test Pages distinct ;
- journal des migrations ;
- sauvegarde des fichiers de configuration ;
- tests de non-régression visuelle ;
- contrôle automatique des performances ;
- budgets de poids ;
- documentation générée ;
- inventaire des fonctionnalités activées ;
- recette enrichie après chaque nouveau lot.

## 17. Directions produit possibles

### Direction A — Bibliothèque personnelle augmentée

Priorité à la reprise, aux favoris, listes, notes, statistiques locales, export/import et confort de lecture.

### Direction B — Catalogue éditorial exploratoire

Priorité à la découverte, aux collections, graphes, parcours, recommandations, recherche avancée et visualisations.

### Direction C — Plateforme d’expériences HTML

Priorité à la détection des capacités interactives, aux démonstrations, au partage, aux badges techniques et aux parcours entre œuvres.

### Direction D — Liseuse installable et hors ligne

Priorité à la PWA, aux téléchargements, à la continuité, aux paramètres de lecture et à la résilience réseau.

### Direction E — Laboratoire éditorial mesurable

Priorité à Umami, aux funnels, aux tests de formats, aux recommandations pilotées par l’usage et aux rapports automatisés.

Ces directions peuvent se combiner, mais le chantier doit identifier une proposition principale afin d’éviter un produit incohérent.

## 18. Frontière où un backend devient réellement nécessaire

Un backend ou Supabase devient justifié pour :

- comptes et récupération d’identité ;
- synchronisation automatique multi-appareils ;
- listes partagées modifiables ;
- commentaires publics ;
- collaboration ;
- contenu privé ou payant ;
- recommandations calculées sur des données serveur ;
- notifications individualisées ;
- droits et rôles ;
- historique fiable et restauration distante ;
- données devant être protégées contre la modification locale.

Même dans ces cas, le frontend peut rester statique dans un premier temps. Vercel ou une web app Next.js ne doit être choisi que si le rendu serveur, les routes applicatives, les fonctions backend, l’auth intégrée ou la complexité du frontend le justifient.

## 19. Séquence d’exploration proposée

### Horizon 1 — Valeur immédiate

- accueil reprendre/favoris ;
- progression locale ;
- export/import ;
- filtres persistants ;
- quelques événements Umami ;
- recherche enrichie du catalogue.

### Horizon 2 — Différenciation

- PWA ;
- hors ligne sélectif ;
- listes et statistiques locales ;
- recommandations ;
- partage visuel ;
- index plein texte.

### Horizon 3 — Expériences avancées

- graphes ;
- recherche sémantique ;
- collections éditoriales avancées ;
- automatisations n8n ;
- rapports analytics ;
- génération d’objets partageables.

### Horizon 4 — Réévaluation d’architecture

Mesurer les limites observées avant de décider d’une auth Supabase ou d’une web app : volume de données, besoin de synchronisation, complexité de maintenance, performance, demandes réelles des utilisateurs.

## 20. Questions de fond à approfondir librement

- la bibliothèque sert-elle d’abord à lire, découvrir, collectionner ou démontrer ;
- l’utilisateur principal est-il le propriétaire, un petit cercle ou un public large ;
- faut-il privilégier la sobriété ou une expérience spectaculaire ;
- quels comportements méritent d’être persistés ;
- quels éléments doivent rester privés ;
- quelle part d’automatisation est acceptable ;
- quels livres doivent fonctionner totalement hors du contexte de la bibliothèque ;
- quelles métadonnées supplémentaires sont réellement durables ;
- comment éviter que la couche commune limite la liberté des livres ;
- comment tester les livres très atypiques ;
- quelles fonctions ont une valeur récurrente plutôt qu’un effet de démonstration ;
- quels besoins observés justifieraient un backend.

## 21. Livrables attendus d’un approfondissement

1. carte d’opportunités complète ;
2. regroupement en quelques propositions produit cohérentes ;
3. scoring valeur, effort, risque et dépendances ;
4. architecture par fonctionnalité ;
5. identification des évolutions de schéma ;
6. prototypes des concepts les plus différenciants ;
7. tests utilisateurs ou scénarios d’usage ;
8. feuille de route en lots réversibles ;
9. critères explicites de passage à Supabase ou Vercel ;
10. analyse des impacts sur le geste central d’ajout d’un livre ;
11. mise à jour coordonnée des spécifications et de la recette ;
12. recommandations libres, y compris l’abandon d’idées séduisantes mais coûteuses ou peu utiles.

## 22. Critère directeur

La bonne évolution n’est pas celle qui exploite toutes les possibilités techniques. C’est celle qui augmente nettement la valeur de la bibliothèque tout en conservant sa simplicité éditoriale, sa robustesse statique et la liberté des livres autonomes.
