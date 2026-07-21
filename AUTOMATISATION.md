# Automatisation du catalogue

## Fichiers concernés

```text
scripts/build_catalog.py
.github/workflows/catalog.yml
catalog.json
```

Le site GitHub Pages doit être configuré dans **Settings > Pages > Build and deployment** avec :

- **Source** : `Deploy from a branch` ;
- **Branch** : `main` ;
- **Folder** : `/(root)`.

Aucun lancement local n’est nécessaire pour l’ajout courant d’un livre.

## Déclencheurs

Le workflow **Mettre à jour le catalogue** démarre :

1. à chaque push sur `main` modifiant `livres/**` ;
2. à chaque push sur `main` modifiant `couvertures/**` ;
3. à chaque push sur `main` modifiant `scripts/**` ;
4. manuellement depuis **Actions > Mettre à jour le catalogue > Run workflow**.

Un commit qui ne touche que `catalog.json` ne relance pas ce workflow. Le commit automatique contient également `[skip ci]`.

## Déroulé d’un run

1. `actions/checkout` récupère `main` avec tout l’historique Git (`fetch-depth: 0`).
2. Python 3.12 exécute `scripts/build_catalog.py`, sans installation de paquet.
3. Le script parcourt uniquement les fichiers `livres/*.html` du premier niveau.
4. Pour chaque livre, il extrait les métadonnées `book:*`, puis applique les fallbacks prévus pour le titre.
5. La lecture s’arrête à la fermeture de `<head>` lorsqu’elle existe ; sans `<head>` exploitable, elle est plafonnée à 4 Mio pour rester sûre avec les fichiers très volumineux.
6. Les couvertures sont recherchées dans l’ordre `.webp`, `.png`, `.jpg` et leur signature binaire minimale est contrôlée.
7. La date du premier commit Git du livre est récupérée. Si l’historique est indisponible, la date de modification du fichier est utilisée. Cette date sert uniquement à classer les entrées du catalogue du plus récent au plus ancien ; le champ JSON `date` reste réservé à `book:date`.
8. `catalog.json` est écrit en UTF-8, JSON indenté, avec un saut de ligne final.
9. Si le fichier n’a pas changé, le workflow s’arrête sans commit.
10. S’il a changé, le bot GitHub committe et pousse `catalog.json` sur `main`.
11. Le workflow demande explicitement un nouveau build GitHub Pages. Cette étape est nécessaire parce qu’un commit poussé avec `GITHUB_TOKEN` ne déclenche pas seul un build Pages en mode branche.

## Vérifier qu’un run a réussi

1. Ouvrir l’onglet **Actions** du dépôt.
2. Sélectionner **Mettre à jour le catalogue**.
3. Vérifier que le dernier run affiche une coche verte.
4. Si le catalogue a changé, vérifier la présence d’un commit nommé :

   ```text
   chore: met à jour catalog.json [skip ci]
   ```

5. Dans **Actions**, vérifier ensuite que le workflow système GitHub Pages (`pages-build-deployment`) est vert.
6. Ouvrir `catalog.json` sur la branche `main` et contrôler `bookCount`, l’entrée du nouveau livre et son éventuelle couverture.
7. Ouvrir le site public et effectuer un rechargement forcé si le navigateur conserve une ancienne réponse.

## Trois pannes probables

### 1. Le workflow ne peut pas pousser `catalog.json`

**Symptômes**

- étape `Committer catalog.json` rouge ;
- message `Permission denied`, `403` ou `refusing to allow a GitHub App to create or update workflow` ;
- aucun commit du bot.

**Cause probable**

Les Actions du dépôt sont limitées en lecture, ou une règle de protection de `main` interdit les commits du bot.

**Résolution**

- ouvrir **Settings > Actions > General > Workflow permissions** ;
- autoriser les permissions d’écriture pour `GITHUB_TOKEN` si la politique du dépôt l’exige ;
- dans les règles de protection de `main`, autoriser GitHub Actions à pousser ce commit technique, ou retirer l’exigence incompatible pour `catalog.json` ;
- relancer le workflow avec **Run workflow**.

### 2. La reconstruction GitHub Pages renvoie 403 ou 404

**Symptômes**

- le commit du catalogue existe ;
- l’étape `Demander la reconstruction GitHub Pages` échoue ;
- le site public conserve l’ancien catalogue.

**Cause probable**

GitHub Pages n’est pas encore activé en mode branche, la source n’est pas `main / (root)`, ou la permission `pages: write` a été retirée du workflow.

**Résolution**

- ouvrir **Settings > Pages** ;
- sélectionner `Deploy from a branch`, puis `main` et `/(root)` ;
- vérifier que `.github/workflows/catalog.yml` contient `pages: write` ;
- relancer manuellement le workflow.

### 3. Un livre ou une couverture n’apparaît pas comme prévu

**Symptômes**

- le run est vert, mais le titre est dérivé du nom de fichier ;
- une couverture est remplacée par le placeholder ;
- le livre est absent après filtrage ou semble mal classé.

**Cause probable**

- métadonnée vide ou mal nommée ;
- HTML ou encodage atypique au-delà de la zone lue ;
- couverture avec un nom, une extension ou une signature incorrecte ;
- fichier placé dans un sous-dossier au lieu de `livres/`.

**Résolution**

- placer le livre directement sous `livres/` avec l’extension `.html` en minuscules ;
- utiliser exactement `book:title`, `book:author`, `book:description`, `book:tags` et `book:date` dans `<head>` ;
- enregistrer les nouveaux livres en UTF-8 avec `<meta charset="utf-8">` ;
- nommer la couverture avec le même nom de base et une extension `.webp`, `.png` ou `.jpg` en minuscules ;
- consulter les annotations jaunes du run, corriger le fichier, puis committer à nouveau.
