# GABARIT — WORKFLOW.md d'un atelier

> Copier ce fichier vers `ateliers/<nom-atelier>/WORKFLOW.md` et remplacer chaque
> section. Les commentaires `<!-- … -->` expliquent ce qui est attendu ; les
> supprimer une fois la section rédigée. Le standard de recette (exécutable à
> froid, étapes-contrats, agent-agnostique, versionné) est défini dans
> [`creer-un-atelier.md`](creer-un-atelier.md) §3. Exemple abouti :
> [`../../ateliers/roman-atelier/WORKFLOW.md`](../../ateliers/roman-atelier/WORKFLOW.md).

# Atelier <nom> — <livrable produit en une phrase>

<!-- En-tête factuel : -->
- **Version** : 1 <!-- s'incrémente à chaque évolution de la recette -->
- **Statut** : expérimental | stable
- **Livrable** : <ce que produit l'atelier, ex. « roman-web avec liseuse intégrée »>
- **Exemples publiés** : <chemins dans livres/, ou « aucun encore »>
- **Préférences** : ce workflow décline le socle éditorial
  [`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md).

## Changelog

<!-- Une ligne par version : ce qui a changé et POURQUOI (quel défaut de recette,
     quelle observation d'exécution). Exemple :
- **v1** (AAAA-MM) — recette initiale.
-->

## Avant de commencer

<!-- Prérequis de lecture (toujours AGENTS.md + ce workflow, rien d'autre), livre
     ou livrable de référence à ouvrir, matériel à réunir (brief, thème,
     contraintes de longueur…). La recette doit être exécutable à froid : ne rien
     supposer connu qui ne soit pas lié ici. -->

## Étapes de fabrication

<!-- Le cœur de la recette. Chaque étape est un contrat :
     entrée → travail → sortie → critère de fin → commit attendu.
     Commandes exactes copiables-collables ; chemins complets depuis la racine ;
     AUCUNE référence à un outil propre à un agent donné. Exemple de forme :

### Étape 1 — <nom>
- **Entrée** : <ce dont l'étape a besoin>
- **Travail** : <quoi faire, précisément>
- **Sortie** : <fichiers produits/modifiés, chemins exacts>
- **Critère de fin** : <commande ou observation objective>
- **Commit** : « <message type en français> »
-->

## Conventions spécifiques de l'atelier

<!-- Nommage des fichiers internes, structure des données embarquées (îlot JSON…),
     images (dossier, numérotation, format, poids), clé localStorage
     (<slug>-state-v1), tout ce qui doit être identique d'un livrable à l'autre.
     Ne pas recopier le socle PREFERENCES.md : seulement ce qui est propre au
     format. -->

## Traçabilité

Le `<head>` du livrable produit contient la version de la recette utilisée :

```html
<meta name="book:workflow" content="<nom-atelier> v<N>">
```

(meta ignorée par le générateur de catalogue — aucune incidence.) La PR de
production mentionne aussi cette version.

## Contraintes de plateforme

Ce livrable respecte les contraintes communes du
[`§1 de creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md)
(emplacement, slug, 5 meta `book:*`, couverture 2:3, autonomie, accessibilité).
<!-- Ne PAS recopier la liste ici ; ajouter seulement les points où cet atelier est
     plus strict que la plateforme. -->

## Vérifications avant PR

<!-- Checklist propre au format (rendu, navigation, données), qui se termine
     toujours par :
- [ ] `<meta name="book:workflow">` présente avec la bonne version ;
- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur ;
- [ ] protocole de session d'AGENTS.md respecté (branche, commits d'étapes, PR
      structurée mentionnant la version de recette).
-->
