# Spécification — Ma Bibliothèque HTML

Version de la spécification : 1.0  
Statut : source normative du projet  
Langue de l’interface : français  
Cible d’hébergement : GitHub Pages

## 1. Objet du projet

« Ma Bibliothèque HTML » est un site statique public qui référence des livres interactifs autonomes au format HTML et permet de les ouvrir directement.

Le système doit respecter les invariants suivants :

1. Ajouter un livre consiste uniquement à déposer un fichier `*.html` directement dans `livres/` depuis l’interface web de GitHub, puis à valider le commit.
2. Aucun build local, terminal, gestionnaire de paquets ou outil de développement n’est requis pour l’usage courant.
3. Les fichiers déposés dans `livres/` sont servis sans transformation. Le site ne les encapsule pas dans une iframe et ne réécrit pas leur HTML.
4. Un fichier `catalog.json` est généré par GitHub Actions à chaque push sur la branche principale, puis inclus dans le site déployé.
5. Le catalogue accepte des documents HTML de structure libre, y compris un fichier vide, un HTML partiel, un HTML mal formé ou un document sans `<head>` ni `<title>`.
6. Une couverture est facultative. Si elle existe, elle porte exactement le même nom de base que le livre et se trouve dans `couvertures/`.
7. Si aucune couverture exploitable n’existe, l’interface génère une couverture de remplacement déterministe en CSS et SVG, sans fichier supplémentaire.
8. Le site d’index et chaque livre disposent d’une URL publique partageable.
9. Les URLs internes sont relatives afin de fonctionner aussi bien sur un site utilisateur GitHub Pages que sur un site de projet.
10. Aucun secret, jeton, identifiant privé ou donnée utilisateur n’est intégré au site publié.

Les termes **DOIT**, **NE DOIT PAS**, **DEVRAIT** et **PEUT** sont normatifs.

## 2. Choix d’architecture

### 2.1 Nature du site

Le site est réalisé en HTML, CSS et JavaScript natifs, sans framework et sans dépendance exécutée côté navigateur.

Le dépôt contient :

- les sources statiques du catalogue ;
- les livres HTML autonomes ;
- les couvertures optionnelles ;
- les scripts Python de génération et de validation ;
- le workflow GitHub Actions de construction et de déploiement ;
- la documentation du projet.

Python n’est utilisé que dans GitHub Actions. Les scripts DOIVENT utiliser uniquement la bibliothèque standard de Python 3.12 afin d’éviter un fichier de dépendances et les risques liés aux installations externes.

### 2.2 Mode de publication GitHub Pages

GitHub Pages DOIT être configuré avec la source **GitHub Actions**.

À chaque push sur la branche principale :

1. le dépôt est récupéré ;
2. les tests et validations sont exécutés ;
3. un répertoire temporaire `_site/` est construit ;
4. les livres et couvertures sont copiés sans modification dans `_site/` ;
5. `catalog.json` est généré dans `_site/` ;
6. l’artefact Pages est téléversé ;
7. l’artefact est déployé sur GitHub Pages.

`catalog.json` et `_site/` ne sont pas versionnés. Le catalogue publié est donc toujours produit à partir de l’état exact du commit déployé, sans commit automatique supplémentaire et sans risque de boucle de workflow.

### 2.3 Principe de confiance

Les livres sont des contenus publiés volontairement par le propriétaire du dépôt. Ils sont servis sur le même domaine que la bibliothèque et peuvent contenir leur propre JavaScript.

En conséquence :

- le site d’index NE DOIT stocker aucun secret ou donnée sensible ;
- le site d’index NE DOIT utiliser ni `localStorage` ni cookie applicatif ;
- les données du catalogue DOIVENT être injectées dans le DOM uniquement par des propriétés textuelles sûres telles que `textContent` ;
- les livres NE DOIVENT PAS être modifiés, nettoyés ou sandboxés par la bibliothèque ;
- l’auteur reste responsable des scripts et ressources externes éventuellement inclus dans ses livres.

## 3. Arborescence exacte du dépôt final

```text
/
├── .github/
│   └── workflows/
│       └── deploy-pages.yml
├── assets/
│   ├── css/
│   │   └── library.css
│   ├── icons/
│   │   └── favicon.svg
│   └── js/
│       └── library.js
├── couvertures/
│   ├── .gitkeep
│   └── livre-exemple.webp
├── guides/
│   ├── AJOUTER-UN-LIVRE.md
│   ├── AJOUTER-UNE-COUVERTURE.md
│   ├── DEPANNAGE.md
│   ├── METADONNEES.md
│   └── PUBLIER-ET-PARTAGER.md
├── livres/
│   ├── .gitkeep
│   └── livre-exemple.html
├── scripts/
│   ├── build_site.py
│   ├── generate_catalog.py
│   └── validate_project.py
├── tests/
│   └── test_generate_catalog.py
├── .gitignore
├── .nojekyll
├── 404.html
├── catalog.schema.json
├── CONVENTIONS.md
├── index.html
├── README.md
├── RECETTE.md
├── ROADMAP.md
└── SPEC.md
```

### 3.1 Artefact déployé

Le répertoire `_site/`, créé uniquement dans le workflow, contient exactement :

```text
_site/
├── assets/
│   ├── css/library.css
│   ├── icons/favicon.svg
│   └── js/library.js
├── couvertures/
│   └── [toutes les couvertures acceptées]
├── livres/
│   └── [tous les fichiers HTML valides par leur nom]
├── .nojekyll
├── 404.html
├── catalog.json
└── index.html
```

Les spécifications, guides, scripts, tests et fichiers de configuration ne sont pas copiés dans l’artefact public.

### 3.2 Rôle des fichiers principaux

| Fichier | Rôle |
|---|---|
| `index.html` | Coquille sémantique de la bibliothèque, états de chargement, zone de recherche, filtres, tri et grille. |
| `assets/css/library.css` | Mise en page, composants, responsive, accessibilité visuelle et couvertures de remplacement. |
| `assets/js/library.js` | Chargement du catalogue, rendu, recherche, filtres, tri, gestion des fallbacks et synchronisation des paramètres d’URL. |
| `404.html` | Page d’erreur statique avec lien relatif vers la racine de la bibliothèque. |
| `.nojekyll` | Désactive le traitement Jekyll et impose un service statique direct. |
| `scripts/generate_catalog.py` | Parcourt `livres/`, extrait les métadonnées et écrit le catalogue. |
| `scripts/validate_project.py` | Contrôle les noms, les fichiers, le schéma et la cohérence générale. |
| `scripts/build_site.py` | Construit `_site/` à partir d’une liste blanche et appelle génération puis validation. |
| `catalog.schema.json` | Schéma JSON normatif de `catalog.json`. |
| `.github/workflows/deploy-pages.yml` | Teste, construit et déploie GitHub Pages. |
| `tests/test_generate_catalog.py` | Tests unitaires de l’extraction, des fallbacks et de la résolution des couvertures. |

## 4. Fonctionnement de bout en bout

### 4.1 Ajout d’un livre

Parcours utilisateur nominal :

1. Ouvrir le dossier `livres/` dans l’interface GitHub.
2. Utiliser **Add file > Upload files**.
3. Déposer un seul fichier respectant la forme `<slug>.html`.
4. Valider le commit sur la branche principale.
5. Le workflow `deploy-pages.yml` démarre automatiquement.
6. Le générateur détecte le nouveau fichier, en extrait les métadonnées et ajoute une entrée au catalogue.
7. Le site est redéployé.
8. Le livre apparaît dans la bibliothèque et son lien ouvre directement `livres/<slug>.html`.

Aucun autre fichier n’est requis. L’absence de métadonnées ou de couverture ne bloque pas la publication.

### 4.2 Ajout ou remplacement d’une couverture

Une couverture PEUT être déposée dans `couvertures/` lors d’un commit distinct ou du même commit que le livre.

Exemple :

```text
livres/mon-livre.html
couvertures/mon-livre.webp
```

Au prochain déploiement, le catalogue associe automatiquement la couverture au livre. Aucun chemin d’image n’est écrit dans le HTML du livre ou dans un fichier de configuration.

### 4.3 Suppression ou renommage

- Supprimer `livres/<slug>.html` retire le livre du prochain catalogue.
- Renommer un livre est traité comme la suppression de l’ancien identifiant et l’ajout d’un nouveau. L’ancienne URL cesse de fonctionner.
- Une couverture orpheline est ignorée et produit un avertissement de validation, sans faire échouer le déploiement.
- Supprimer une couverture fait revenir automatiquement le livre à sa couverture de remplacement.

### 4.4 Construction du catalogue

Le générateur examine uniquement les enfants directs de `livres/` dont l’extension est exactement `.html` en minuscules.

Il NE parcourt PAS les sous-dossiers. Cette règle garantit une URL simple et évite les collisions de noms.

Pour chaque livre :

1. validation du nom de fichier ;
2. lecture binaire ;
3. décodage du texte ;
4. extraction tolérante des métadonnées ;
5. application des fallbacks ;
6. recherche d’une couverture correspondante ;
7. normalisation des valeurs ;
8. création d’une entrée de catalogue.

Les entrées sont triées de manière déterministe par titre normalisé, puis par identifiant.

### 4.5 Décodage des fichiers HTML

Le générateur applique cet ordre :

1. BOM UTF-8, si présent ;
2. encodage déclaré par `<meta charset="…">` ou par une balise `http-equiv="content-type"` trouvée dans les 16 premiers Kio ;
3. UTF-8 strict ;
4. Windows-1252 avec remplacement des séquences indécodables.

Un problème d’encodage ne doit pas empêcher l’ajout du livre au catalogue. Un avertissement est écrit dans les logs du workflow lorsque le fallback Windows-1252 ou le remplacement de caractères est utilisé.

### 4.6 Tolérance au HTML libre

L’extracteur utilise un parseur HTML tolérant de la bibliothèque standard. Il ne dépend pas d’un DOM valide.

Cas explicitement supportés :

- absence de `<!doctype html>` ;
- absence de `<html>`, `<head>` ou `<body>` ;
- balises non fermées ;
- ordre d’attributs arbitraire ;
- casse différente des noms de balises et d’attributs ;
- fichier vide ;
- plusieurs balises `<title>` ;
- plusieurs métadonnées du même nom ;
- JavaScript, CSS et données intégrés dans le document.

Le contenu du livre n’est jamais exécuté pendant la génération.

## 5. Format normatif de `catalog.json`

### 5.1 Encodage et sérialisation

Le fichier DOIT être :

- encodé en UTF-8 sans BOM ;
- un JSON valide ;
- indenté avec deux espaces ;
- sérialisé avec les caractères Unicode lisibles, sans conversion systématique en séquences `\uXXXX` ;
- terminé par un saut de ligne ;
- conforme à `catalog.schema.json`.

### 5.2 Objet racine

| Champ | Type | Obligatoire | Description |
|---|---:|---:|---|
| `schemaVersion` | entier | oui | Version du schéma. Valeur initiale : `1`. |
| `generatedAt` | chaîne | oui | Horodatage UTC RFC 3339, avec suffixe `Z`. |
| `bookCount` | entier | oui | Nombre exact d’éléments dans `books`. |
| `books` | tableau d’objets | oui | Livres publiés, triés par titre normalisé puis identifiant. |

Aucun champ racine supplémentaire n’est autorisé en version 1.

### 5.3 Objet livre

| Champ | Type | Obligatoire | Valeur et règle |
|---|---:|---:|---|
| `id` | chaîne | oui | Nom de base du fichier, sans `.html`. Correspond au slug. |
| `filename` | chaîne | oui | Nom du fichier avec extension, par exemple `mon-livre.html`. |
| `sourcePath` | chaîne | oui | Chemin source relatif, toujours `livres/<filename>`. |
| `href` | chaîne | oui | URL relative publique, identique à `sourcePath` en version 1. |
| `title` | chaîne non vide | oui | Titre final après application des priorités et fallbacks. |
| `author` | chaîne ou `null` | oui | Auteur issu de `book:author`, sinon `null`. |
| `description` | chaîne ou `null` | oui | Description issue de `book:description`, sinon `null`. |
| `tags` | tableau de chaînes | oui | Tags normalisés et dédupliqués ; tableau vide si absents. |
| `date` | chaîne ou `null` | oui | Date normalisée au format `YYYY`, `YYYY-MM` ou `YYYY-MM-DD`. |
| `datePrecision` | `"year"`, `"month"`, `"day"` ou `null` | oui | Précision correspondant à `date`, ou `null` si la date est absente ou invalide. |
| `cover` | objet ou `null` | oui | Couverture trouvée et validée, sinon `null`. |

Aucun champ livre supplémentaire n’est autorisé en version 1.

### 5.4 Objet couverture

| Champ | Type | Obligatoire | Valeur et règle |
|---|---:|---:|---|
| `filename` | chaîne | oui | Nom du fichier de couverture. |
| `sourcePath` | chaîne | oui | Chemin source relatif dans `couvertures/`. |
| `href` | chaîne | oui | URL relative publique de la couverture. |
| `format` | `"webp"`, `"png"` ou `"jpg"` | oui | Extension sélectionnée. |

### 5.5 Exemple complet

```json
{
  "schemaVersion": 1,
  "generatedAt": "2026-07-12T09:30:00Z",
  "bookCount": 2,
  "books": [
    {
      "id": "chroniques-du-seuil",
      "filename": "chroniques-du-seuil.html",
      "sourcePath": "livres/chroniques-du-seuil.html",
      "href": "livres/chroniques-du-seuil.html",
      "title": "Chroniques du Seuil",
      "author": "Ariane Valmont",
      "description": "Un récit interactif en douze chapitres.",
      "tags": [
        "fantasy",
        "interactif"
      ],
      "date": "2026-07-12",
      "datePrecision": "day",
      "cover": {
        "filename": "chroniques-du-seuil.webp",
        "sourcePath": "couvertures/chroniques-du-seuil.webp",
        "href": "couvertures/chroniques-du-seuil.webp",
        "format": "webp"
      }
    },
    {
      "id": "fragment-sans-titre",
      "filename": "fragment-sans-titre.html",
      "sourcePath": "livres/fragment-sans-titre.html",
      "href": "livres/fragment-sans-titre.html",
      "title": "Fragment sans titre",
      "author": null,
      "description": null,
      "tags": [],
      "date": null,
      "datePrecision": null,
      "cover": null
    }
  ]
}
```

## 6. Règles d’extraction et de normalisation

Les règles détaillées sont définies dans `CONVENTIONS.md`. Les points normatifs indispensables sont résumés ici.

### 6.1 Titre

Ordre de priorité :

1. première balise non vide `<meta name="book:title" content="…">` ;
2. première balise `<title>` dont le contenu textuel normalisé est non vide ;
3. nom de fichier humanisé.

Le titre final ne peut jamais être vide.

### 6.2 Auteur et description

- `author` provient exclusivement de `book:author` ;
- `description` provient exclusivement de `book:description` ;
- les métadonnées génériques telles que `author`, `description`, Open Graph ou Twitter Cards ne sont pas utilisées en version 1 ;
- une valeur absente ou vide donne `null`.

### 6.3 Tags

Toutes les balises `book:tags` non vides sont lues dans l’ordre du document. Leur contenu est séparé sur les virgules. Les tags sont nettoyés et dédupliqués sans tenir compte de la casse, tout en conservant la graphie de la première occurrence.

### 6.4 Date

`book:date` accepte uniquement :

- `YYYY` ;
- `YYYY-MM` ;
- `YYYY-MM-DD`.

La date doit être calendairement valide. Une date invalide est ignorée et produit un avertissement.

### 6.5 Nettoyage textuel

Pour chaque valeur textuelle :

1. décodage des entités HTML ;
2. normalisation Unicode NFC ;
3. remplacement de toute suite d’espaces, tabulations et sauts de ligne par un espace simple ;
4. suppression des espaces de début et de fin ;
5. suppression des caractères de contrôle, sauf tabulation et sauts de ligne avant l’étape 3.

Le site affiche ces valeurs par `textContent` et ne les interprète jamais comme du HTML.

## 7. Résolution des couvertures

### 7.1 Formats acceptés

Les seules extensions reconnues sont, en minuscules :

- `.webp` ;
- `.png` ;
- `.jpg`.

`.jpeg`, les extensions en majuscules, SVG, GIF, AVIF et tout autre format sont ignorés.

### 7.2 Correspondance

Pour un livre `livres/<id>.html`, le générateur cherche :

1. `couvertures/<id>.webp` ;
2. `couvertures/<id>.png` ;
3. `couvertures/<id>.jpg`.

Le premier fichier exploitable selon cet ordre est retenu. Si plusieurs fichiers existent, le premier est utilisé et le workflow émet un avertissement indiquant les fichiers ignorés.

### 7.3 Validation minimale du contenu

Le générateur vérifie que le fichier :

- n’est pas vide ;
- possède une signature binaire cohérente avec son extension : RIFF/WEBP, signature PNG ou marqueur JPEG.

Un fichier invalide est ignoré avec avertissement. Le livre reste publié avec une couverture de remplacement.

### 7.4 Couverture de remplacement déterministe

La couverture de remplacement est générée dans `library.js` et stylée dans `library.css`.

Algorithme version 1 :

1. construire la graine UTF-8 `id + "\n" + title` ;
2. calculer un hash FNV-1a 32 bits non signé ;
3. calculer `h1 = hash modulo 360` ;
4. calculer `h2 = (h1 + 40 + ((hash décalé de 8 bits) modulo 41)) modulo 360` ;
5. produire un fond `linear-gradient(145deg, hsl(h1 62% 42%), hsl(h2 58% 24%))` ;
6. superposer un motif SVG géométrique inline, fixe et semi-transparent ;
7. afficher le titre du livre au centre, avec au maximum quatre lignes visibles ;
8. afficher l’auteur sous le titre uniquement s’il est renseigné.

Le SVG est créé dans le DOM ou intégré comme URI de données. Il ne doit provoquer aucune requête réseau.

Le même `id` et le même titre produisent toujours la même couverture sur tous les navigateurs compatibles.

### 7.5 Erreur de chargement côté navigateur

Même lorsqu’une couverture est présente dans le catalogue, l’élément `<img>` doit gérer `error`. En cas de réponse 404, fichier corrompu ou décodage impossible, l’image est retirée et remplacée immédiatement par le placeholder déterministe.

## 8. Comportement fonctionnel du site bibliothèque

### 8.1 Initialisation

Au chargement de `index.html`, `library.js` :

1. affiche l’état « Chargement de la bibliothèque… » ;
2. effectue `fetch("catalog.json", { cache: "no-store" })` avec un chemin relatif ;
3. vérifie le code HTTP ;
4. vérifie sommairement `schemaVersion`, `bookCount` et `books` ;
5. rend les contrôles et les cartes ;
6. remplace l’état de chargement par le contenu ou un état d’erreur.

### 8.2 États obligatoires

Le site DOIT gérer :

- **chargement** : message visible et `aria-live="polite"` ;
- **catalogue vide** : « Aucun livre n’est encore publié. » ;
- **aucun résultat** : message distinct, avec bouton de réinitialisation des filtres ;
- **erreur réseau ou JSON invalide** : message expliquant que le catalogue est indisponible et proposant de recharger la page ;
- **JavaScript désactivé** : bloc `<noscript>` expliquant que l’index dynamique nécessite JavaScript, sans affecter les URLs directes des livres.

Une erreur de catalogue ne doit pas produire une page blanche.

### 8.3 Carte d’un livre

Chaque carte contient :

- la couverture réelle ou de remplacement au ratio 2:3 ;
- le titre ;
- l’auteur s’il existe ;
- la date s’il existe ;
- la description, limitée visuellement à quatre lignes ;
- les tags, limités visuellement aux six premiers avec indication du nombre restant ;
- un lien explicite « Lire ».

Le titre et la couverture font partie du même lien principal. Le lien pointe directement vers `book.href`. Aucun interstitiel, lecteur intermédiaire ou paramètre supplémentaire n’est ajouté.

### 8.4 Navigation vers un livre

Le lien s’ouvre dans l’onglet courant avec une ancre HTML normale :

```html
<a href="livres/mon-livre.html">Lire</a>
```

Le site NE DOIT PAS :

- charger le livre par `fetch` ;
- injecter son contenu dans la page ;
- l’ouvrir dans une iframe ;
- réécrire ses URLs ;
- lui imposer le CSS ou le JavaScript de la bibliothèque.

### 8.5 Recherche

La recherche porte sur :

- `title` ;
- `author` ;
- `description` ;
- `tags` ;
- `id`.

Elle est :

- insensible à la casse ;
- insensible aux accents par normalisation Unicode NFD puis suppression des marques diacritiques ;
- appliquée après un délai de 150 ms ;
- composée en logique ET entre les mots saisis : tous les termes doivent être présents dans l’ensemble textuel du livre.

### 8.6 Filtrage par tag

- La liste de tags est dérivée du catalogue.
- Les tags sont triés alphabétiquement avec `Intl.Collator("fr", { sensitivity: "base" })`.
- Un seul tag est sélectionnable à la fois en version 1.
- Le filtre de tag et la recherche textuelle se cumulent.

### 8.7 Tri

Trois tris sont proposés :

1. `title-asc` — titre A à Z, valeur par défaut ;
2. `date-desc` — date la plus récente d’abord, puis livres sans date, puis titre ;
3. `author-asc` — auteur A à Z, puis livres sans auteur, puis titre.

Le tri utilise `Intl.Collator("fr", { sensitivity: "base", numeric: true })`.

### 8.8 Paramètres d’URL de l’index

L’état de consultation PEUT être partagé grâce à ces paramètres :

- `q` : recherche ;
- `tag` : tag actif ;
- `sort` : valeur de tri.

Exemple :

```text
?q=fantasy&tag=interactif&sort=date-desc
```

Les paramètres inconnus ou invalides sont ignorés. Les mises à jour utilisent `history.replaceState` et ne rechargent pas la page.

### 8.9 Accessibilité

Le site DOIT respecter au minimum :

- structure sémantique `header`, `main`, `form`, `ul` ou grille de cartes, `footer` ;
- navigation complète au clavier ;
- focus visible ;
- libellés associés aux champs ;
- ordre de tabulation naturel ;
- contrastes compatibles WCAG AA ;
- texte alternatif `Couverture de « <titre> »` pour une image réelle ;
- placeholder décoratif masqué aux technologies d’assistance, le lien portant déjà le titre ;
- respect de `prefers-reduced-motion` ;
- tailles tactiles minimales de 44 × 44 px pour les commandes principales.

### 8.10 Responsive et compatibilité

Cibles : deux dernières versions stables de Chrome, Firefox, Safari et Edge, plus Safari iOS et Chrome Android récents.

La grille utilise :

```css
grid-template-columns: repeat(auto-fill, minmax(min(100%, 15rem), 1fr));
```

Le site doit rester utilisable à partir de 320 px de largeur. Aucun comportement essentiel ne dépend du survol.

## 9. URLs publiques

### 9.1 Site de projet

Pour un dépôt `bibliotheque` appartenant à `proprietaire` :

```text
https://proprietaire.github.io/bibliotheque/
https://proprietaire.github.io/bibliotheque/livres/mon-livre.html
```

### 9.2 Site utilisateur ou organisation

Pour un dépôt nommé `proprietaire.github.io` :

```text
https://proprietaire.github.io/
https://proprietaire.github.io/livres/mon-livre.html
```

Tous les liens et chargements internes utilisent des chemins relatifs sans slash initial. Aucun nom de propriétaire, dépôt ou domaine n’est codé en dur.

Un domaine personnalisé GitHub Pages reste compatible sans modification du code.

## 10. Matrice de fallback

| Situation | Comportement attendu |
|---|---|
| `book:title` présent et non vide | Utiliser cette valeur. |
| `book:title` absent ou vide, `<title>` présent | Utiliser le premier `<title>` non vide. |
| Aucun titre exploitable | Humaniser le slug du fichier. |
| Aucun auteur | `author: null`, ne pas afficher de ligne auteur. |
| Aucune description | `description: null`, ne pas afficher de bloc vide. |
| Aucun tag | `tags: []`, ne pas afficher de liste vide. |
| Date absente | `date: null`, `datePrecision: null`. |
| Date invalide | Même fallback que date absente, avec avertissement. |
| Couverture absente | Générer le placeholder déterministe. |
| Couverture présente mais invalide à la génération | Ignorer l’image, avertir, utiliser le placeholder. |
| Couverture cataloguée mais non chargeable dans le navigateur | Remplacer l’image par le placeholder via `error`. |
| HTML vide | Cataloguer avec le titre dérivé du nom de fichier. |
| HTML mal formé | Extraire au mieux ; les fallbacks garantissent une entrée. |
| Encodage inconnu | Décoder en Windows-1252 avec remplacement et avertissement. |
| `catalog.json` absent ou invalide | Afficher un état d’erreur explicite sur l’index. |
| JavaScript désactivé | Afficher le message `<noscript>` ; les URLs directes restent valides. |
| Aucune correspondance de recherche | Afficher « Aucun livre ne correspond à ces critères. ». |
| Catalogue vide | Afficher « Aucun livre n’est encore publié. ». |

## 11. Règles de validation et gestion des erreurs

### 11.1 Erreurs bloquantes

Le workflow échoue si :

- un fichier directement dans `livres/` se termine par `.html` mais ne respecte pas la convention de slug ;
- deux livres produisent le même identifiant après normalisation, notamment à cause d’une différence de casse ;
- le générateur ne peut pas lire un fichier ;
- le JSON produit ne respecte pas `catalog.schema.json` ;
- `bookCount` ne correspond pas à la longueur de `books` ;
- un chemin généré sort des répertoires autorisés ;
- un test unitaire échoue ;
- un fichier indispensable du site manque.

Un échec empêche le déploiement et conserve en ligne la dernière version valide.

### 11.2 Avertissements non bloquants

Le workflow continue avec avertissement si :

- une couverture est orpheline ;
- plusieurs couvertures correspondent au même livre ;
- une couverture a une signature invalide ;
- une date est invalide ;
- plusieurs métadonnées scalaires non vides sont présentes ;
- un fallback d’encodage est utilisé ;
- une valeur de métadonnée dépasse les limites de présentation recommandées ;
- un sous-dossier est présent dans `livres/` ou `couvertures/` et sera ignoré.

### 11.3 Annotations GitHub Actions

Les erreurs et avertissements DOIVENT utiliser le format d’annotation GitHub Actions lorsque le chemin et, si possible, la ligne sont connus :

```text
::warning file=livres/mon-livre.html,line=7::Date book:date invalide : 2026-14-40
```

## 12. Limites et recommandations de performance

- Le projet n’impose pas de limite de taille inférieure aux limites GitHub, car un livre autonome peut embarquer images, audio et données.
- Une taille inférieure à 25 Mio par livre est recommandée pour un chargement raisonnable sur mobile.
- Une couverture inférieure à 2 Mio est recommandée.
- Les images de couverture utilisent `loading="lazy"` et `decoding="async"`.
- Le catalogue ne contient jamais le contenu intégral du livre.
- Le rendu initial ne doit pas attendre le chargement des couvertures.
- Aucun appel réseau externe n’est requis par la bibliothèque elle-même.

## 13. Compatibilité avec les livres interactifs

Le système garantit uniquement :

- la conservation binaire du fichier HTML lors de la copie vers `_site/` ;
- une URL directe et stable tant que le nom de fichier ne change pas ;
- l’absence d’encapsulation et de réécriture.

Le système ne garantit pas le fonctionnement d’un livre qui :

- dépend de fichiers locaux non inclus dans son HTML ;
- utilise des chemins absolus propres à un autre domaine ;
- exige un serveur applicatif, une base de données ou des en-têtes HTTP personnalisés ;
- dépend d’une ressource externe devenue indisponible ;
- suppose une URL différente de son emplacement réel.

Les livres sont donc DEVRAIENT être réellement autonomes : CSS, JavaScript, images et données intégrés, ou ressources externes volontairement assumées par l’auteur.

## 14. Critères d’acceptation globaux

Le projet est considéré conforme lorsque les tests suivants réussissent :

1. un fichier `livres/test-sans-title.html` sans `<title>` apparaît avec le titre « Test sans title » ;
2. un fichier contenant `book:title` et `<title>` utilise `book:title` ;
3. un fichier HTML mal formé reste catalogué ;
4. un livre sans couverture affiche un placeholder stable après plusieurs rechargements ;
5. une couverture `webp`, `png` ou `jpg` correctement nommée est détectée ;
6. deux couvertures concurrentes suivent l’ordre `webp`, puis `png`, puis `jpg` ;
7. une image cataloguée mais cassée est remplacée côté navigateur ;
8. la recherche est insensible à la casse et aux accents ;
9. les filtres et tris produisent un résultat déterministe ;
10. le lien « Lire » ouvre directement le fichier HTML ;
11. le site fonctionne sous une URL de projet comportant un sous-chemin ;
12. un push ne contenant qu’un nouveau fichier HTML déclenche le déploiement complet ;
13. un build invalide ne remplace pas la dernière version publique valide ;
14. aucune opération locale n’est nécessaire pour l’ajout courant d’un livre.

## 15. Gouvernance du schéma

Toute modification incompatible du format de `catalog.json` exige :

1. l’incrément de `schemaVersion` ;
2. la mise à jour de `catalog.schema.json` ;
3. la mise à jour coordonnée de `generate_catalog.py`, `validate_project.py` et `library.js` ;
4. l’ajout ou la modification de tests ;
5. la mise à jour de `SPEC.md`, `CONVENTIONS.md` et des guides concernés.

Les champs existants ne doivent pas changer de sens sans incrément de version.
