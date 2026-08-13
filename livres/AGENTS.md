# AGENTS.md — livres/

Ce dossier contient les **livres publiés**. Pour en produire ou en modifier un :
lis [`/AGENTS.md`](../AGENTS.md) (règles d'or + protocole de session), puis le
workflow de ton atelier — ex. [`/ateliers/roman-atelier/WORKFLOW.md`](../ateliers/roman-atelier/WORKFLOW.md)
(registre : [`/ateliers/README.md`](../ateliers/README.md)).

Rappels vitaux :

- **Jamais éditer `catalog.json`** ni le bloc `#demo-catalog` d'`index.html` —
  régénérés par la CI, PR rejetée sinon.
- **Slug en kebab-case ASCII** (`mon-livre`), un seul niveau de dossier,
  `index.html` comme point d'entrée en forme dossier.
- **`book:author` = nom du modèle** qui écrit, pas de pseudonyme collectif.
