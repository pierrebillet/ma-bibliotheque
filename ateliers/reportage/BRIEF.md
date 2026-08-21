# BRIEF.md — gabarit du brief de lancement (reportage v7)

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
- **Sujet** : <le sujet réel à faire découvrir — un lieu, un personnage
  historique, un métier, un événement, un environnement. C'est le seul champ
  vraiment obligatoire : tout le reste peut être délégué.>
- **Angle** : <ce qui rend la découverte désirable — la question, le paradoxe,
  la perspective (ex. « par les yeux de… ») — défaut : proposé par l'auteur
  après la recherche>
- **Slug proposé** : <kebab-case ASCII, ex. `le-canal-du-midi` — ou « au choix
  de l'auteur »>

## Recherche (optionnel)
- **Axes prioritaires** : <les recherches à mener en premier — défaut : lieux,
  personnes, événements, vocabulaire et jargon, contexte d'époque, débats et
  état des connaissances>
- **Sources** : <à privilégier ou à exclure — défaut : au choix de l'auteur,
  sources datées exigées>
- **Mode de recherche** : <par l'agent (défaut) ou déléguée : l'agent prépare
  des requêtes à copier-coller dans un assistant externe (Perplexity, ChatGPT
  ou autre) pour économiser son quota — prévoir un tour d'échange en plus>

## Documents du web (optionnel)
- **Volume** : <attente sur la densité de documents (photos, cartes, graphes,
  gravures… insérés dans le corps et sur les notices, avec crédit de source) —
  défaut : au jugement de l'auteur, règle de pertinence de l'atelier : un
  document n'entre que s'il apporte une information que le texte ne porte
  pas, jamais de décoratif ; zéro document est conforme>
- **Types attendus** : <ex. cartes d'époque, graphes de données, portraits,
  fac-similés — défaut : ce que la recherche fait émerger>
- **Sources d'images** : <à privilégier ou à exclure (institutions, archives,
  presse…) — défaut : au choix de l'auteur, page source identifiable exigée>

## Cadrage éditorial (optionnel)
- **Public** : <défaut : tout public curieux, aucun prérequis sur le sujet>
- **Longueur** : <nombre de chapitres et de mots — défaut : libre, l'auteur
  dimensionne à la pertinence, sans remplissage (socle §« Quantités » ;
  repère de l'atelier : des chapitres plus courts qu'un roman, la densité
  documentaire fatigue plus vite)>
- **Parcours** : <chronologique, thématique, du général au particulier… —
  défaut : au choix de l'auteur, au service du sujet>
- **Codex** : <nombre de notices, voix qui guide le lecteur — défaut : nombre
  libre (chaque notice mérite sa place), exploration dense (repère : ≥ 40 %
  des blocs avec mention), voix proposée par l'auteur>

## Illustrations générées (optionnel)
- **Volume** : <défaut : aucune illustration générée — l'étape 6 ne s'applique
  que si ce bloc est rempli ; les documents du web, eux, relèvent du bloc
  « Documents du web »>
- **Direction artistique** : <défaut : documentaire — gravures, planches,
  photographies d'époque évoquées>

## Modules de lecture (optionnel — déclenche l'étape 4 bis)
- **Carte des lieux** : <oui / non (défaut : non) ; si oui, préciser le
  territoire à situer — le fond est un schéma dessiné dans le livre, sourcé
  comme le reste ; une carte trouvée sur le web relève du bloc « Documents du
  web »>
- **Graphe de relations** : <oui / non (défaut : non) ; si oui, préciser les
  entités à faire figurer (personnes, institutions, lieux) — chaque lien
  affiché doit être attesté par le dossier>

## Divers (optionnel)
- **Contraintes et envies** : <périmètre à exclure, thèmes sensibles à
  traiter avec précaution, clins d'œil…>
```

## Exemple rempli

```markdown
# Brief — Le canal du Midi

## Identité (obligatoire)
- **Sujet** : le canal du Midi — sa construction au XVIIe siècle, Pierre-Paul
  Riquet, le chantier (ingénierie, financement, main-d'œuvre), et ce que le
  canal est devenu.
- **Angle** : comment un percepteur des gabelles obstiné a réalisé le rêve
  romain de relier l'Atlantique à la Méditerranée — et ce que le chantier doit
  aux femmes et aux ouvriers qu'on a longtemps oubliés.
- **Slug proposé** : le-canal-du-midi

## Recherche (optionnel)
- **Axes prioritaires** : la vie de Riquet ; l'ingénierie du canal (alimentation
  en eau, écluses, vocabulaire des ouvrages) ; le chantier et sa main-d'œuvre ;
  le canal aujourd'hui (patrimoine mondial, menaces sur les platanes).
- **Mode de recherche** : par l'agent.

## Documents du web (optionnel)
- **Types attendus** : une carte du tracé, le portrait de Riquet, un plan ou
  une gravure d'époque des ouvrages (écluses, seuil de Naurouze) ; un graphe
  du trafic si les données existent.

## Cadrage éditorial (optionnel)
- **Codex** : voix d'un éclusier qui fait visiter — précise, chaleureuse,
  fière du vocabulaire du métier.

## Modules de lecture (optionnel)
- **Carte des lieux** : oui — schéma de situation du tracé Toulouse → étang de
  Thau, avec le seuil de Naurouze, l'alimentation depuis la Montagne Noire et
  trois ou quatre ouvrages remarquables.
- **Graphe de relations** : oui — Riquet, Colbert, Louis XIV, l'abbé Mourgues,
  les entrepreneurs du chantier ; chaque lien daté et sourcé.
```

Tout ce que ce gabarit ne demande pas (structure des données, conventions de
fichiers, checklists) est fixé par [`WORKFLOW.md`](WORKFLOW.md) : le brief dit
**quoi**, la recette dit **comment**.
