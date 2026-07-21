# Frontend — Ma Bibliothèque HTML

## Fichiers

- `index.html` : page complète, autonome, sans framework ni dépendance externe. Le HTML, le CSS et le JavaScript sont réunis dans ce fichier.
- `catalog.json` : catalogue de démonstration conforme au schéma version 1, avec trois livres fictifs.
- `couvertures/` et `livres/` : ressources facultatives incluses dans le paquet de prévisualisation pour que les images et les liens de démonstration fonctionnent localement.

## Fonctionnement de `index.html`

Au chargement, la page appelle :

```js
fetch("catalog.json", { cache: "no-store" })
```

Le chemin est relatif : le site fonctionne à la racine d’un domaine, dans un sous-répertoire GitHub Pages ou derrière un domaine personnalisé.

Le catalogue est validé légèrement avant affichage : version du schéma, tableau `books`, cohérence de `bookCount`, identifiants, titres et chemins relatifs sûrs. Les contenus sont injectés dans le DOM avec `textContent`, jamais comme HTML.

La page fournit :

- recherche insensible à la casse et aux accents, avec logique ET entre les termes ;
- recherche dans le titre, l’auteur, la description, les tags et l’identifiant ;
- filtre par tag ;
- tris par date, titre ou auteur ;
- paramètres partageables `q`, `tag` et `sort` ;
- couvertures réelles avec remplacement automatique en cas d’erreur ;
- placeholder stable calculé par FNV-1a à partir de `id + "\n" + title` ;
- ouverture des livres dans un nouvel onglet ;
- copie de l’URL absolue de chaque livre ;
- états de chargement, catalogue vide, aucun résultat et erreur ;
- mode sombre automatique, navigation clavier et réduction des animations.

## Prévisualisation locale

Les navigateurs bloquent généralement `fetch()` entre fichiers ouverts avec le protocole `file://`. Pour permettre l’ouverture directe de `index.html`, le fichier contient une copie intégrée du catalogue de démonstration, utilisée uniquement lorsque le chargement échoue sous `file://`.

Sur GitHub Pages ou tout serveur HTTP, `catalog.json` reste la source effective. La copie intégrée est ignorée dès que le `fetch()` réussit.

## Format attendu de `catalog.json`

Le fichier suit le schéma version 1 de `SPEC.md` :

```json
{
  "schemaVersion": 1,
  "generatedAt": "2026-07-12T09:30:00Z",
  "bookCount": 1,
  "books": [
    {
      "id": "mon-livre",
      "filename": "mon-livre.html",
      "sourcePath": "livres/mon-livre.html",
      "href": "livres/mon-livre.html",
      "title": "Mon livre",
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

Les couvertures utilisent un objet `cover` dont le champ `href` pointe vers `couvertures/<slug>.webp`, `.png` ou `.jpg`. En l’absence de couverture, la valeur doit être `null`.

## Évolution

- Ne pas coder de nouvelles cartes directement dans le HTML : faire évoluer le générateur de `catalog.json`.
- Conserver les chemins relatifs, sans slash initial ni domaine codé en dur.
- Conserver l’injection par API DOM sûres et `textContent`.
- Toute modification incompatible du catalogue exige une nouvelle `schemaVersion` et une mise à jour coordonnée du validateur JavaScript.
- Le catalogue de démonstration intégré peut être régénéré depuis `catalog.json` pour maintenir la prévisualisation locale ; il n’intervient pas dans le fonctionnement publié.
