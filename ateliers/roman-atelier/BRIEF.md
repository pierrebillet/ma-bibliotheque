# BRIEF.md — gabarit du brief de lancement (roman-atelier v6)

C'est le **seul document d'entrée** d'une fabrication : Pierre le remplit et le
colle dans le message de lancement de la session Production. Tout champ optionnel
absent prend la valeur par défaut indiquée (celles du socle
[`docs/conception/PREFERENCES.md`](../../docs/conception/PREFERENCES.md)).
L'agent auteur recopie le brief reçu tel quel dans `livres/<slug>/brief.md` à
l'étape 1 (traçabilité).

Copier le bloc ci-dessous et remplacer les valeurs :

```markdown
# Brief — <titre de travail>

## Identité (obligatoire)
- **Pitch** : <le sujet du livre en 1 à 5 phrases — thème, situation, enjeu.
  C'est le seul champ vraiment obligatoire : tout le reste peut être délégué.>
- **Slug proposé** : <kebab-case ASCII, ex. `les-brumes-du-port` — ou
  « au choix de l'auteur »>

## Cadrage éditorial (optionnel)
- **Genre** : <ex. espionnage, SF sociale, mystère… — défaut : au choix de
  l'auteur, dans le terrain du socle>
- **Ton** : <ex. contemplatif, haletant, ironique… — défaut : registre
  littéraire soigné, tension retenue>
- **Longueur** : <nombre de chapitres et de mots — défaut : 8 à 12 chapitres,
  2 000 à 3 000 mots par chapitre>
- **Public** : <défaut : tout public, pas de contenus sensibles>
- **Codex** : <nombre de notices, voix souhaitée pour le codex — défaut :
  15 à 30 notices, voix au choix de l'auteur, ≥ 40 % des blocs avec mention>

## Ancrage réel (optionnel — déclenche l'étape 0 de recherche documentaire)
- **Éléments réels à ancrer** : <personnage historique, lieux réels, métier et
  son jargon, événements, époque — ce que le récit doit rendre juste>
- **Degré d'ancrage** : <tout le récit, ou seulement certains éléments —
  préciser ce qui reste inventé>
- **Axes prioritaires** : <les recherches à mener en premier — défaut : tous
  les éléments listés ci-dessus>
- **Sources** : <à privilégier ou à exclure — défaut : au choix de l'auteur,
  sources datées exigées>
- **Mode de recherche** : <par l'agent (défaut) ou déléguée : l'agent prépare
  des requêtes à copier-coller dans un assistant externe (Perplexity, ChatGPT
  ou autre) pour économiser son quota — prévoir un tour d'échange en plus>

## Illustrations (optionnel)
- **Volume** : <défaut : 1 image par chapitre + couverture + environ un tiers
  des notices>
- **Direction artistique** : <technique, palette, époque, références… —
  défaut : proposée par l'auteur dans la bible visuelle du manifeste>

## Modules de lecture (optionnel — déclenche l'étape 3 bis)
- **Carte des lieux** : <oui / non (défaut : non) ; si oui, préciser le
  territoire à représenter et les lieux qui comptent — le fond est schématique,
  dessiné dans le livre, jamais une image>
- **Graphe de relations** : <oui / non (défaut : non) ; si oui, préciser les
  entités à faire figurer (personnages, mais aussi lieux ou institutions) et
  les liens dont l'existence est elle-même une révélation>

## Divers (optionnel)
- **Fonctionnalités hors socle** : <ce que le moteur ne sait pas encore faire
  (choix et branches, lecture audio, gestes tactiles…) — défaut : aucune ;
  une telle demande est une divergence de moteur, signalée dans la PR. La
  carte, le graphe de relations et l'impression, eux, sont dans le moteur :
  les demander ci-dessus>
- **Contraintes et envies** : <tout le reste : personnages imposés, clins
  d'œil, interdits…>
```

## Exemple rempli

```markdown
# Brief — La gardienne de Kervel

## Identité (obligatoire)
- **Pitch** : Une gardienne entretient depuis douze ans un phare
  officiellement éteint. Son registre consigne, nuit de tempête après nuit de
  tempête, une lumière au large qu'aucune carte n'explique. Un inspecteur de
  l'administration des feux débarque pour fermer le site.
- **Slug proposé** : la-gardienne-de-kervel

## Cadrage éditorial (optionnel)
- **Ton** : contemplatif, tension sourde ; le fantastique reste à hauteur de
  doute.
- **Codex** : voix du registre de la gardienne — sec, daté, administratif qui
  se fissure.

## Ancrage réel (optionnel)
- **Éléments réels à ancrer** : le métier de gardien de phare (jargon,
  routines d'entretien, hiérarchie de l'administration des Phares et Balises)
  et les côtes du Finistère.
- **Degré d'ancrage** : le cadre et le métier seulement — le phare de Kervel,
  ses personnages et la lumière au large restent inventés.
- **Mode de recherche** : par l'agent.

## Illustrations (optionnel)
- **Direction artistique** : gouache sombre, lumières rares et chaudes, mer
  d'hiver bretonne.

## Modules de lecture (optionnel)
- **Carte des lieux** : oui — la côte, le village de Kervel, le phare sur son
  îlot, la digue submersible.
- **Graphe de relations** : non.
```

Tout ce que ce gabarit ne demande pas (structure des données, conventions de
fichiers, checklists) est fixé par [`WORKFLOW.md`](WORKFLOW.md) : le brief dit
**quoi**, la recette dit **comment**.
