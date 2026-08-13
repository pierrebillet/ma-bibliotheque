# CATALOGUE.md — le schéma de `catalog.json`

`catalog.json` est le contrat d'interface entre le générateur
(`scripts/build_catalog.py`), la page d'accueil (`index.html`) et les livres. Ce
document fait foi pour le schéma version 1.

## Cycle de vie

- **Généré, jamais édité à la main.** Après chaque merge sur `main`, le job
  `catalogue` de la CI exécute `build_catalog.py --sync-demo-catalog`, commite
  `catalog.json` et le bloc `#demo-catalog` d'`index.html` en tant que
  `github-actions[bot]` (message `[skip ci]`), puis relance le build GitHub Pages.
- La CI **rejette** toute pull request qui modifie `catalog.json` ou le bloc
  `#demo-catalog`.
- `generatedAt` est conservé tel quel si la liste des livres n'a pas changé, pour
  éviter les commits de bruit.

## Schéma version 1

```json
{
  "schemaVersion": 1,
  "generatedAt": "2026-08-12T20:48:12Z",
  "bookCount": 11,
  "books": [
    {
      "id": "mon-livre",
      "filename": "index.html",
      "sourcePath": "livres/mon-livre/index.html",
      "href": "livres/mon-livre/index.html",
      "title": "Mon livre",
      "author": "Claude Fable",
      "description": "Résumé en une ou deux phrases.",
      "tags": ["fiction", "aventure"],
      "date": "2026-08-11",
      "datePrecision": "day",
      "cover": {
        "filename": "mon-livre.jpg",
        "sourcePath": "couvertures/mon-livre.jpg",
        "href": "couvertures/mon-livre.jpg",
        "format": "jpg"
      }
    }
  ]
}
```

### Champs racine

| Champ | Type | Contenu |
|---|---|---|
| `schemaVersion` | entier | `1`. Toute rupture de compatibilité exige de l'incrémenter et de mettre à jour le validateur JS d'`index.html`. |
| `generatedAt` | chaîne | Horodatage UTC ISO 8601 de la génération. |
| `bookCount` | entier | Nombre d'entrées de `books` (vérifié par l'index). |
| `books` | tableau | Une entrée par livre, triée par date d'ajout Git décroissante, puis titre, puis id (clés insensibles aux accents). |

### Champs d'un livre

| Champ | Type | Contenu |
|---|---|---|
| `id` | chaîne | Le slug (`[a-z0-9]+(-[a-z0-9]+)*`), identifiant public et stable. Slug invalide = génération en erreur (exit 1). |
| `filename` | chaîne | Nom du fichier d'entrée (`mon-livre.html` ou `index.html`). |
| `sourcePath` / `href` | chaîne | Chemin relatif du point d'entrée depuis la racine du site, sans slash initial. |
| `title` | chaîne | Jamais vide (voir fallbacks ci-dessous). |
| `author` | chaîne ou `null` | Le **modèle** qui a écrit le livre (règle d'or d'`AGENTS.md`). |
| `description` | chaîne ou `null` | Texte brut, ≤ 600 caractères recommandés. |
| `tags` | tableau de chaînes | Dédupliqués (insensible casse/accents), graphie de la première occurrence conservée. |
| `date` | chaîne ou `null` | `AAAA`, `AAAA-MM` ou `AAAA-MM-JJ` ; valeur invalide ignorée avec avertissement. |
| `datePrecision` | chaîne ou `null` | `year`, `month` ou `day` selon la forme de `date`. |
| `cover` | objet ou `null` | `filename`, `sourcePath`, `href`, `format` (`webp`/`png`/`jpg`). `null` si aucune couverture valide — l'index génère alors un placeholder déterministe (FNV-1a sur `id + "\n" + title`). |

## Règles d'extraction (résumé du comportement réel du script)

- **Découverte** : `livres/*.html` de premier niveau + sous-dossiers de premier
  niveau (point d'entrée : `index.html`, sinon `<slug>.html`, sinon l'unique fichier
  HTML — sinon livre ignoré avec avertissement). Les noms commençant par `.` et le
  dossier `_template` sont exclus.
- **Métadonnées** : les 5 meta `book:*` du `<head>`, lues par un vrai parseur HTML
  (lecture bornée à `</head>` ou 4 Mio). Fallbacks du titre : `book:title` →
  `<title>` → nom de fichier humanisé (tirets → espaces, première lettre en
  majuscule). Auteur, description, date : première balise non vide, sinon `null`.
  Les balises génériques (`og:*`, `twitter:*`, JSON-LD…) sont volontairement
  ignorées.
- **Normalisation** : décodage des entités, suppression des caractères de contrôle,
  Unicode NFC, blancs réduits à un espace, trim. Tags découpés sur la virgule
  uniquement.
- **Couverture** : `couvertures/<slug>.webp`, puis `.png`, puis `.jpg` — le premier
  fichier dont la **signature binaire** correspond au format. Nom ≠ slug exact ⇒
  couverture ignorée en silence.
- **Date d'ajout** (clé de tri) : `git log --diff-filter=A` sur le point d'entrée,
  sans `--follow` (pour que les éditions dérivées n'héritent pas de la date de leur
  livre source), repli sur la date de modification du fichier.

Le détail exhaustif (avertissements, cas limites) est lisible dans
`scripts/build_catalog.py`, abondamment commenté en français.

## Le bloc `#demo-catalog`

Copie de secours du catalogue inlinée dans `index.html`, utilisée uniquement quand
`fetch()` échoue en `file://`. Régénérée par `--sync-demo-catalog` : JSON identique à
`catalog.json` **à un détail près** — les séquences `</` sont échappées en `<\/` pour
rester valides dans une balise `<script>` (strictement équivalent après
`JSON.parse`). Le script exige exactement une occurrence du bloc, sinon
`DemoBlockError`.

## Évolutions envisagées (schéma v2)

Non implémentées, voir l'audit
[`../audits/2026-08-rapport-etonnement.md`](../audits/2026-08-rapport-etonnement.md) §D.4.1 :
`format` (`texte`/`illustré`), `variantOf` (groupement des éditions dérivées —
condition de levée du moratoire), `wordCount`/`readingMinutes`, `genre` (vocabulaire
fermé, distinct des tags). Toute implémentation passe par `schemaVersion: 2` et une
mise à jour coordonnée du validateur d'`index.html`.
