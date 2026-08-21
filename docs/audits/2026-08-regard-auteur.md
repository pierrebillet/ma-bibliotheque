# Regard d'auteur — les workflows d'écriture de Ma Bibliothèque (août 2026)

> Note : document d'audit non normatif, dans l'esprit du
> [rapport d'étonnement](2026-08-rapport-etonnement.md). Les règles qui en
> découlent vivent dans les documents normatifs qu'il cite (socle et recettes) ;
> ce fichier garde la trace du **pourquoi**.

Audit réalisé le 21 août 2026, à la demande de Pierre : *qu'est-ce qu'un auteur
expérimenté dirait des workflows et des préférences de rédaction du dépôt ?*
Méthode : lecture du socle (`docs/conception/PREFERENCES.md`), des deux recettes
(`ateliers/roman-atelier/WORKFLOW.md` v7, `ateliers/reportage/WORKFLOW.md` v5),
de leurs briefs et gabarits, et des livres publiés qui les appliquent
(`la-clause-du-meilleur-ennemi`, `loi-malraux`, `la-foret-de-troncais`,
`lequation-du-calme`).

---

## Ce qu'un auteur salue

Le dépôt fait déjà, et impose par recette, des choses que beaucoup d'auteurs
mettent des années à s'imposer :

- **L'univers est pensé avant d'être écrit.** Promesse émotionnelle, idée
  centrale, question thématique posées à l'étape de plan et embarquées dans le
  livre lui-même (bloc `world`) : c'est une discipline d'écrivain
  professionnel, rendue vérifiable.
- **La méthode anti-divulgâchage du codex** (`spoilerRisk`, `delayReason`,
  `earliestSafeBlock`…) traite le déverrouillage comme un problème de
  dramaturgie, pas de mécanique — rare et juste.
- **La traçabilité brief → livre → recette** : le brief recopié tel quel, un
  commit par étape de fabrication, la version de recette dans le `<head>`.
  L'historique git est un carnet de brouillons conservés.
- **La meilleure consigne éditoriale du dépôt** est dans le brief de
  `la-clause-du-meilleur-ennemi` : *« il faut que le lecteur rit/sourit autant
  que possible […] sans porter atteinte au point 1 [l'admiration des deux
  protagonistes] »*. Formuler l'**effet recherché sur le lecteur** est
  exactement ce qu'un éditeur demande à un auteur — mais elle était enterrée
  dans un champ « Divers ».

## Ce qu'un auteur corrigerait

### 1. « La relecture » n'est pas une révision

L'étape 5 des deux recettes était une passe unique « cohérence + orthographe ».
Aucun auteur ne travaille ainsi : on révise d'abord la **structure** (chaque
chapitre fait-il basculer quelque chose ? la fin paie-t-elle la promesse ? le
rythme alterne-t-il scènes et respirations ?), puis — et seulement ensuite — la
**phrase** (répétitions, tics, dialogues, typographie). Polir une phrase d'un
chapitre qu'on va couper est du travail perdu ; corriger l'orthographe en même
temps que la structure, c'est ne bien faire ni l'un ni l'autre.

→ Étape 5 scindée en **5a (révision structurelle)** et **5b (passe ligne à
ligne)**, chacune avec son commit — `roman-atelier` v8, `reportage` v6.

### 2. Aucune préférence de style au niveau de la phrase

Le socle disait la langue, le registre, les longueurs — rien sur le point de
vue, le temps du récit, les dialogues, les titres de chapitres, l'incipit, la
chute, ni la typographie française. Conséquence mesurable : le corpus publié
mélange l'apostrophe droite `'` et l'apostrophe typographique `’`, parfois dans
le même livre. Une maison d'édition a une feuille de style ; « registre
littéraire soigné » n'en est pas une.

→ Nouvelle entrée **« Style et voix »** dans les défauts proposés du socle
(`PREFERENCES.md` §Fond) : point de vue et temps choisis au plan et tenus,
montrer plutôt qu'expliquer, incipit qui promet, chute qui paie, titres qui
évoquent sans divulgâcher, typographie française uniforme.

### 3. Les métriques risquent de devenir l'objectif

« Au moins 40 % des blocs porteurs d'une mention » a produit un livre à
**98 %** de blocs liés (`la-clause-du-meilleur-ennemi`, 183/186). C'est la loi
de Goodhart appliquée au codex : quand l'indicateur devient la cible, il cesse
de mesurer la qualité. Une mention se justifie parce qu'elle récompense la
curiosité — un récit sur-lié sollicite le lecteur à chaque paragraphe comme un
récit sous-lié l'abandonne.

→ Le socle dit désormais explicitement que ses chiffres sont des **repères
planchers, pas des cibles à maximiser**.

### 4. Le plan n'était jamais éprouvé avant l'écriture

Le critère de fin de l'étape 1 était purement technique (`build_catalog.py`
passe) : on pouvait dérouler 25 000 mots sur un synopsis que personne n'avait
relu en éditeur sceptique. Et rien n'autorisait explicitement l'écart au plan
en cours d'écriture — or la fiction se découvre en s'écrivant ; interdire
l'écart produit des livres qui obéissent à leur plan plutôt qu'à leur récit.

→ Étape 1 : **épreuve du plan** (une bascule par chapitre, promesse tenable,
question thématique qui a une réponse) ; étape 2 : **écart au plan autorisé**
s'il est resynchronisé (plan + bloc `world`) dans le même commit —
`roman-atelier` v8.

### 5. L'effet recherché sur le lecteur mérite son champ de brief

Voir « Ce qu'un auteur salue » : la consigne d'effet émotionnel du brief de
`la-clause-du-meilleur-ennemi` est le meilleur outil de direction éditoriale
observé dans le corpus, et le gabarit de brief ne l'invitait nulle part.

→ Champ **« Effet recherché sur le lecteur »** ajouté au gabarit
`ateliers/roman-atelier/BRIEF.md` (section Divers, défaut : délégué à
l'auteur).

## Incohérences documentaires corrigées au passage

- Le socle disait « 1 à 6 tags » quand la gouvernance
  (`docs/bibliotheque/CATALOGUE.md`), les deux recettes et `verifier.py`
  imposent **2 à 4** — le socle, censé être décliné, était contredit par ses
  déclinaisons. Aligné sur 2 à 4.
- **Deux pilotes existaient sans être enregistrés** :
  `la-clause-du-meilleur-ennemi` (`roman-atelier v3`, illustré en deux passes)
  et `loi-malraux` (`reportage v5`) — alors que recette et registre disaient
  « aucun livre v3 encore » et « aucun [reportage] encore ». Exactement le
  « résultat non formalisé = résultat perdu » contre lequel
  `docs/conception/VISION.md` met en garde. Exemples publiés et statuts mis à
  jour dans les recettes et `ateliers/README.md`.
- `roman-atelier/WORKFLOW.md` (v7) parlait encore de « livre v6 » (2
  occurrences) ; les en-têtes des `BRIEF.md` retardaient d'une ou deux versions
  sur leur recette ; `GABARIT-ILLUSTRATIONS.md` codait en dur
  « roman-atelier v3 » dans chaque manifeste généré. Corrigés.

## Chantiers candidats signalés (hors périmètre de cette session)

- **Dédoublonner les deux recettes** : ~85 % de `roman-atelier/WORKFLOW.md` et
  `reportage/WORKFLOW.md` sont identiques (moteur, `<head>`, vocabulaires,
  images, structure de fichiers). Chaque nouvel atelier recopiera ~250 lignes
  de tronc commun ; un document partagé référencé (comme le socle l'est déjà)
  réduirait le coût d'un nouveau format à sa seule spécificité.
- **`verifier.py` vit dans `roman-atelier/` mais vérifie le moteur commun** :
  `reportage` en dépend avec une note d'excuse. Sa place naturelle serait près
  du moteur (`livres/_template/`).
- **La validation du socle par Pierre** (chantier 3 de la roadmap Conception,
  ouvert depuis le 2026-08-13) reste à acter — les « défauts proposés »,
  désormais enrichis, gouvernent tous les livres produits en attendant.
