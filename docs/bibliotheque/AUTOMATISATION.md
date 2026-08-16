# Automatisation du catalogue

## Fichiers concernés

```text
scripts/build_catalog.py
.github/workflows/catalog.yml
catalog.json
sitemap.xml
index.html          (bloc #demo-catalog uniquement)
```

Le site GitHub Pages doit être configuré dans **Settings > Pages > Build and deployment** avec :

- **Source** : `Deploy from a branch` ;
- **Branch** : `main` ;
- **Folder** : `/(root)`.

Aucun lancement local n’est nécessaire pour l’ajout courant d’un livre. Un contributeur (humain ou agent) peut toutefois vérifier son travail avant d’ouvrir une pull request avec :

```bash
python scripts/build_catalog.py --output /tmp/catalog-verification.json
```

Le script sort en erreur (code 1) si un identifiant de livre est hors convention kebab-case ASCII. Les pull requests exécutent automatiquement cette même vérification (job `verification` du workflow).

## Déclencheurs

Le workflow **Mettre à jour le catalogue** démarre :

1. à chaque push sur `main` modifiant `livres/**` ;
2. à chaque push sur `main` modifiant `couvertures/**` ;
3. à chaque push sur `main` modifiant `scripts/**` ;
4. à chaque push sur `main` modifiant `index.html` (resynchronisation du bloc `#demo-catalog`, sans effet si le bloc est déjà à jour) ;
5. manuellement depuis **Actions > Mettre à jour le catalogue > Run workflow**.

Un commit qui ne touche que `catalog.json` ne relance pas ce workflow, et le commit automatique du bot (qui peut contenir `catalog.json` et `index.html`) porte `[skip ci]` : aucune boucle possible.

## Déroulé d’un run

1. `actions/checkout` récupère `main` avec tout l’historique Git (`fetch-depth: 0`).
2. Python 3.12 exécute `scripts/build_catalog.py`, sans installation de paquet.
3. Le script parcourt les fichiers `livres/*.html` du premier niveau **et** les sous-dossiers `livres/<slug>/` (point d’entrée : `index.html`, sinon `<slug>.html`, sinon l’unique fichier HTML du dossier). Les fichiers et dossiers cachés (préfixe `.`) et le dossier `_template` sont ignorés. La profondeur est limitée à un niveau : `livres/serie/tome-1/` n’est pas découvert.
4. Pour chaque livre, il extrait les métadonnées `book:*`, puis applique les fallbacks prévus pour le titre.
5. La lecture s’arrête à la fermeture de `<head>` lorsqu’elle existe ; sans `<head>` exploitable, elle est plafonnée à 4 Mio pour rester sûre avec les fichiers très volumineux.
6. Les couvertures sont recherchées dans `couvertures/<slug>.*` dans l’ordre `.webp`, `.avif`, `.png`, `.jpg`, `.jpeg` et leur signature binaire minimale est contrôlée. En l’absence de couverture valide dans `couvertures/`, un livre-dossier peut embarquer la sienne : `livres/<slug>/cover.*`, puis `livres/<slug>/images/cover.*` (mêmes extensions, même contrôle). `couvertures/` garde toujours la priorité.
7. La date d’ajout Git du fichier (`git log --diff-filter=A`, sans `--follow` pour qu’une édition dérivée n’hérite pas de la date de son livre source) est récupérée. Si l’historique est indisponible, la date de modification du fichier est utilisée. Cette date sert uniquement à classer les entrées du catalogue du plus récent au plus ancien ; le champ JSON `date` reste réservé à `book:date`.
8. `catalog.json` est écrit en UTF-8, JSON indenté, avec un saut de ligne final.
9. Le bloc `#demo-catalog` de `index.html` est réécrit avec le même JSON (option `--sync-demo-catalog` du script ; les `</` y sont échappés en `<\/` pour rester valides en HTML). Si le bloc est introuvable ou présent plusieurs fois, le script sort en erreur.
10. `sitemap.xml` est régénéré (options `--sitemap` et `--base-url` du script) : la page d’accueil puis chaque livre du catalogue, en URL absolues. L’URL de base est dérivée de `GITHUB_REPOSITORY` (`https://<owner>.github.io/<repo>/`) — aucun domaine codé en dur dans le workflow. La sortie est déterministe (pas d’horodatage) : le fichier ne change que si la liste des livres change.
11. Si ni `catalog.json`, ni `index.html`, ni `sitemap.xml` n’ont changé, le workflow s’arrête sans commit.
12. Sinon, le bot GitHub committe les fichiers modifiés (`chore: met à jour le catalogue (catalog.json, bloc demo, sitemap) [skip ci]`) et pousse sur `main`, avec rebase et jusqu’à trois tentatives en cas de push concurrent.
13. Le workflow demande explicitement un nouveau build GitHub Pages. Cette étape est nécessaire parce qu’un commit poussé avec `GITHUB_TOKEN` ne déclenche pas seul un build Pages en mode branche.

## Vérifier qu’un run a réussi

1. Ouvrir l’onglet **Actions** du dépôt.
2. Sélectionner **Mettre à jour le catalogue**.
3. Vérifier que le dernier run affiche une coche verte.
4. Si le catalogue a changé, vérifier la présence d’un commit nommé :

   ```text
   chore: met à jour le catalogue (catalog.json, bloc demo, sitemap) [skip ci]
   ```

5. Dans **Actions**, vérifier ensuite que le workflow système GitHub Pages (`pages-build-deployment`) est vert.
6. Ouvrir `catalog.json` sur la branche `main` et contrôler `bookCount`, l’entrée du nouveau livre et son éventuelle couverture.
7. Au besoin, vérifier que le bloc `#demo-catalog` de `index.html` sur `main` contient le même catalogue que `catalog.json` (à l’échappement `<\/` et au saut de ligne final près : comparer les JSON parsés, pas les octets).
8. Ouvrir le site public et effectuer un rechargement forcé si le navigateur conserve une ancienne réponse.

## Quatre pannes probables

### 1. Le workflow ne peut pas pousser le commit du catalogue

**Symptômes**

- étape `Committer le catalogue` rouge ;
- message `Permission denied`, `403` ou `refusing to allow a GitHub App to create or update workflow` ;
- aucun commit du bot.

**Cause probable**

Les Actions du dépôt sont limitées en lecture, ou une règle de protection de `main` interdit les commits du bot. Les simples courses de push (un humain pousse au même moment) sont absorbées par le rebase et les trois tentatives : un échec persistant signale un vrai problème de droits.

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
- sous-dossier sans point d’entrée identifiable (plusieurs fichiers HTML et aucun `index.html`), ou imbriqué à plus d’un niveau sous `livres/`.

**Résolution**

- placer le livre directement sous `livres/` avec l’extension `.html` en minuscules ;
- utiliser exactement `book:title`, `book:author`, `book:description`, `book:tags` et `book:date` dans `<head>` ;
- enregistrer les nouveaux livres en UTF-8 avec `<meta charset="utf-8">` ;
- nommer la couverture avec le même nom de base et une extension `.webp`, `.avif`, `.png`, `.jpg` ou `.jpeg` en minuscules (ou, pour un livre-dossier, embarquer `cover.*` à la racine du dossier ou dans `images/`) ;
- consulter les annotations jaunes du run, corriger le fichier, puis committer à nouveau.

### 4. Le bloc `#demo-catalog` est introuvable

**Symptômes**

- run rouge avec `DemoBlockError` (« Bloc #demo-catalog attendu exactement une fois… ») ;
- le job `verification` échoue sur une pull request qui remanie `index.html`.

**Cause probable**

La balise `<script id="demo-catalog" type="application/json">` a été renommée, supprimée ou dupliquée dans `index.html`.

**Résolution**

- restaurer une unique balise `<script id="demo-catalog" type="application/json">…</script>` dans `index.html` (son contenu importe peu, le bot le réécrit) ;
- le job `verification` détecte ce cas dès la pull request, avant tout merge.
