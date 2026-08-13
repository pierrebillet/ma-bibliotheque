# BRIEF.md — gabarit du brief de lancement (roman-atelier v3)

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

## Illustrations (optionnel)
- **Volume** : <défaut : 1 image par chapitre + couverture + environ un tiers
  des notices>
- **Direction artistique** : <technique, palette, époque, références… —
  défaut : proposée par l'auteur dans la bible visuelle du manifeste>

## Divers (optionnel)
- **Fonctionnalités hors socle** : <ex. carte, graphe de relations, mode
  impression — défaut : aucune ; toute divergence de moteur sera signalée
  dans la PR>
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

## Illustrations (optionnel)
- **Direction artistique** : gouache sombre, lumières rares et chaudes, mer
  d'hiver bretonne.
```

Tout ce que ce gabarit ne demande pas (structure des données, conventions de
fichiers, checklists) est fixé par [`WORKFLOW.md`](WORKFLOW.md) : le brief dit
**quoi**, la recette dit **comment**.
