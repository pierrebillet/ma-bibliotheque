# GABARIT — WORKFLOW.md d'un atelier

> Copier ce fichier vers `ateliers/<nom-atelier>/WORKFLOW.md` et remplacer chaque
> section. Les commentaires `<!-- … -->` expliquent ce qui est attendu ; les
> supprimer une fois la section rédigée. Référence complète :
> [`creer-un-atelier.md`](creer-un-atelier.md). Exemple abouti :
> [`../../ateliers/roman-atelier/WORKFLOW.md`](../../ateliers/roman-atelier/WORKFLOW.md).

# Atelier <nom> — <livrable produit en une phrase>

<!-- En-tête factuel : -->
- **Statut** : expérimental | stable
- **Livrable** : <ce que produit l'atelier, ex. « roman-web avec liseuse intégrée »>
- **Exemples publiés** : <chemins dans livres/, ou « aucun encore »>

## Avant de commencer

<!-- Prérequis de lecture (toujours AGENTS.md), livre/livrable de référence à
     ouvrir, matériel à réunir (brief, thème, contraintes de longueur…). -->

## Étapes de fabrication

<!-- Le cœur du workflow. Étapes numérotées ; chaque étape se termine par un COMMIT
     dont le message type est donné. Exemple de forme :

### Étape 1 — <nom> (commit : « <message type> »)
<contenu de l'étape, critères de fin>
-->

## Conventions spécifiques de l'atelier

<!-- Nommage des fichiers internes, structure des données embarquées (îlot JSON…),
     images (dossier, numérotation, format, poids), clé localStorage
     (<slug>-state-v1), tout ce qui doit être identique d'un livrable à l'autre. -->

## Contraintes de plateforme

Ce livrable respecte les contraintes communes du
[`§1 de creer-un-atelier.md`](../../docs/conception/creer-un-atelier.md)
(emplacement, slug, 5 meta `book:*`, couverture 2:3, autonomie, accessibilité).
<!-- Ne PAS recopier la liste ici ; ajouter seulement les points où cet atelier est
     plus strict que la plateforme. -->

## Vérifications avant PR

<!-- Checklist propre au format (rendu, navigation, données), qui se termine
     toujours par :
- [ ] `python scripts/build_catalog.py --output /tmp/catalog-verification.json`
      passe sans erreur ;
- [ ] protocole de session d'AGENTS.md respecté (branche, commits d'étapes, PR
      structurée).
-->
