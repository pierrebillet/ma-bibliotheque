# GABARIT — BRIEF.md d'un atelier

> Copier ce fichier vers `ateliers/<nom-atelier>/BRIEF.md` et l'adapter au
> format. **Tout atelier fournit son gabarit de brief** : c'est un critère
> d'acceptation de [`creer-un-atelier.md`](creer-un-atelier.md) §4 — sans
> brief, pas de lancement de production reproductible. Exemples aboutis :
> [`../../ateliers/roman-atelier/BRIEF.md`](../../ateliers/roman-atelier/BRIEF.md)
> et [`../../ateliers/reportage/BRIEF.md`](../../ateliers/reportage/BRIEF.md).

## Ce qu'est un brief

Le `BRIEF.md` d'un atelier est le **seul document d'entrée** d'une
fabrication : Pierre le remplit et le colle dans le message de lancement de la
session Production. Il dit **quoi** produire ; la recette (`WORKFLOW.md`) dit
**comment**. Principes invariants, quel que soit le format :

- **Un seul champ vraiment obligatoire** : l'identité du livrable (pitch,
  sujet…) — tout le reste peut être délégué à l'auteur.
- **Chaque champ optionnel énonce son défaut** : un brief minimal doit
  suffire ; les défauts viennent du `WORKFLOW.md` et du socle
  [`PREFERENCES.md`](PREFERENCES.md), le brief ne fait que les surcharger.
- **Traçabilité** : l'agent auteur recopie le brief reçu tel quel dans
  `livres/<slug>/brief.md` à la première étape de la recette.
- **Un exemple rempli** conclut le gabarit : c'est lui qui montre le niveau de
  détail attendu.

## Squelette à adapter

Structure attendue du `BRIEF.md` d'un atelier (les commentaires `<!-- … -->`
expliquent ce qui est attendu ; les supprimer une fois la section rédigée) :

````markdown
# BRIEF.md — gabarit du brief de lancement (<nom-atelier> v<N>)

C'est le **seul document d'entrée** d'une fabrication : Pierre le remplit et le
colle dans le message de lancement de la session Production. Tout champ
optionnel absent prend la valeur par défaut indiquée (celles du
[`WORKFLOW.md`](WORKFLOW.md) et du socle
[`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md)).
L'agent auteur recopie le brief reçu tel quel dans `livres/<slug>/brief.md` à
l'étape 1 (traçabilité).

Copier le bloc ci-dessous et remplacer les valeurs :

```markdown
# Brief — <titre de travail>

## Identité (obligatoire)
- **<Pitch ou Sujet>** : <l'objet du livrable — le seul champ vraiment
  obligatoire : tout le reste peut être délégué.>
- **Slug proposé** : <kebab-case ASCII — ou « au choix de l'auteur »>

## <Sections optionnelles propres au format>
<!-- Cadrage éditorial (public, longueur, ton, codex…), recherche,
     illustrations, documents du web… : chaque champ avec son défaut
     explicite, hérité du WORKFLOW.md ou du socle. -->

## Divers (optionnel)
- **Contraintes et envies** : <périmètre à exclure, thèmes sensibles,
  clins d'œil…>
```

## Exemple rempli

<!-- Un brief complet et réaliste du format, prêt à copier. -->

Tout ce que ce gabarit ne demande pas (structure des données, conventions de
fichiers, checklists) est fixé par [`WORKFLOW.md`](WORKFLOW.md) : le brief dit
**quoi**, la recette dit **comment**.
````
