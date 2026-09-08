# Brief — Les Mots donnés

Brief reçu tel quel (message de lancement de la session Production, 2026-09-08 —
concours heroic fantasy jeunes adultes, septembre 2026) :

> # Brief — Concours heroic fantasy jeunes adultes
>
> ## Identité (obligatoire)
> - **Pitch** : un roman d'heroic fantasy pour jeunes adultes, en français, dans
>   un monde secondaire entièrement inventé. L'histoire est la tienne ; elle
>   contient nécessairement :
>   - un monde qui tient debout — institutions, métiers, géographie, nourriture,
>     droit, croyances — et dont la magie (ou le savoir qui en tient lieu) obéit
>     à des règles et a un prix ;
>   - une héroïne ou un héros de seize à vingt ans qui part d'une position de
>     faiblesse ou de marge et grandit par ses choix, pas par ce qu'on lui a
>     prédit ;
>   - un voyage ou une quête concrète, avec des compagnons dont chacun a sa
>     propre raison d'être là et sa propre trajectoire ;
>   - un antagoniste qui a raison de son point de vue ;
>   - de l'aventure véritable : des dangers, des décisions irréversibles, des
>     pertes, des victoires payées.
>   L'idée centrale, la question thématique et la promesse émotionnelle sont à
>   toi ; elles figurent dans le bloc `world` et le livre les tient.
> - **Slug proposé** : au choix de l'auteur.
>
> ## Cadrage éditorial (optionnel)
> - **Genre** : heroic fantasy — `book:genre` = `fantasy`.
> - **Ton** : élan et lumière. Tension retenue plutôt que spectaculaire ; le
>   souffle épique se gagne par la précision des gestes et des lieux, pas par
>   les adjectifs. L'humour fin est bienvenu s'il sert la voix. `book:tonalite`
>   au choix, sauf `sombre`.
> - **Longueur** : libre — l'auteur dimensionne chapitres et notices à la
>   pertinence, sans jamais écrire pour remplir (socle §« Quantités »).
> - **Public** : jeunes adultes — `book:audience` = `ados et adultes` ;
>   `book:exigence` = `accessible` ou `intermédiaire`. Violence possible mais
>   jamais graphique ; romance possible mais pudique.
> - **Codex** : 20 à 35 notices, dans une voix incarnée — un document du monde
>   (chronique, bestiaire, carnet de route, registre d'une guilde, manuel d'un
>   métier…), pas une encyclopédie neutre. Exploration dense (repère ≥ 40 % des
>   blocs porteurs d'une mention, sans sur-lier).
>
> ## Ancrage réel (optionnel)
> - Aucun : monde secondaire, pas d'étape 0. En revanche l'onomastique et la
>   toponymie doivent **sonner en français** — pas de noms anglo-saxons ni de
>   suffixes génériques de fantasy — et la texture du réel vient des métiers,
>   des objets, des gestes et de la cuisine du monde inventé.
>
> ## Illustrations (optionnel)
> - **Volume** : défaut de la recette — 1 image par chapitre + couverture +
>   environ un tiers des notices (personnages, lieux, créatures ; pas les
>   concepts abstraits).
> - **Direction artistique** : proposée par l'auteur dans la bible visuelle du
>   manifeste. Le manifeste est autoportant (l'illustrateur n'aura pas lu le
>   livre) ; les prompts d'images peuvent être rédigés en anglais si tu juges
>   que cela sert les générateurs, tout le reste du manifeste en français ;
>   couverture strictement sans texte.
>
> ## Modules de lecture (optionnel)
> - **Carte des lieux** : oui — le territoire du voyage, 6 à 12 lieux, fond
>   schématique dessiné dans l'îlot.
> - **Graphe de relations** : oui — personnages et factions ; au moins un lien
>   dont l'existence est elle-même une révélation (`unlockBlock`).
>
> ## Divers (optionnel)
> - **Effet recherché sur le lecteur** : qu'il veuille lire le chapitre suivant
>   à chaque fin de chapitre ; qu'il admire le protagoniste pour ce qu'il a
>   choisi, pas pour ce qu'il a reçu ; qu'il referme le livre avec l'envie de
>   repartir dans ce monde — et que la fin ne soit pas une défaite.
> - **Fonctionnalités hors socle** : aucune.
> - **Contraintes et envies** :
>   - **Interdits** : l'élu et la prophétie ; le seigneur des ténèbres sans
>     mobile ; l'école de magie ; l'exposition du monde en premier chapitre ;
>     la fin ouverte qui promet une suite — l'histoire tient en un tome.
>   - **Envies** : une magie (ou un savoir) qui coûte à qui s'en sert ; des
>     adultes ni absents ni idiots ; au moins un moment de pur émerveillement
>     par tiers de livre ; un objet du quotidien du monde qui devient central
>     au récit ; des titres de chapitres qui évoquent sans divulgâcher.

## Lecture du brief par l’auteur

- **Auteur** : Claude Fable 5.1 — `book:author` = « Claude Fable 5.1 (texte) »
  (le modèle et sa version, comme l’exige le concours ; l’illustrateur ajoutera
  sa part).
- **Titre et slug** : *Les Mots donnés* → `les-mots-donnes` (vérifié absent de
  `livres/`).
- **Branche** : la session a été configurée par l’orchestrateur sur
  `claude/roman-heroic-fantasy-ya-3fl1d0`, qui remplace la convention
  `atelier/roman-<slug>` (même situation que le pilote v3
  `la-clause-du-meilleur-ennemi`) ; le manifeste d’illustrations le précise à
  l’illustrateur.
- **Cadrage retenu** : `fantasy` / `illustré` / `lumineuse` / `intermédiaire` /
  `ados et adultes` ; capacités `codex, carte, relations`. Tags : corde,
  montagne, parole, guilde.
- **Longueur** : 12 chapitres de 2 300 à 2 800 mots (trois tiers de quatre
  chapitres : la ville, la route, les Hauts et le retour) ; codex d’environ
  32 notices ; un tiers illustré.
- **Voix du codex** : le *Carnet de colportage de la Tende*, tenu par Garance
  Malaurie, colporteuse et compagne de route de l’héroïne — un carnet de
  métier (prix, lieux, gens, recettes, on-dit), repris au propre après les
  événements ; jamais neutre, souvent drôle, tendre quand elle ne s’en rend
  pas compte.
- **Point de vue et temps** : troisième personne, focalisation interne sur
  Aube de bout en bout ; passé simple et imparfait. Dialogues au tiret
  cadratin, guillemets à chevrons pour les citations, apostrophe
  typographique.
- **Onomastique** : prénoms et toponymes à consonance française ancienne
  (Aube, Hersende, Aymon, Séverin, Garance, Bastien, Ysabeau, Aurèle,
  Ancelle ; Tressaille, la Tende, la Retenue, la Levée, Pont-Sauvage,
  Sombreval, Malebosse, le col de la Déliée, Haut-Charme). Aucun ancrage
  réel : étape 0 non déclenchée.
- **Objet du quotidien central** : la **cordelette** — la corde de vie que
  chaque habitant file à sept ans et noue tout au long de son existence
  (naissances, dettes, récoltes), déliée à sa mort par les siens.
- **Magie et prix** : le *nœud qui tient*. Un nœud noué sur une corde dont on
  a filé l’âme, serré sur un mot qu’on a vécu, fixe ce qu’il tient (un pont,
  une plaie, une digue). Le mot est perdu à jamais pour la bouche qui l’a
  donné ; un mot qu’on n’a pas vécu ne tient rien ; un mot arraché non plus.
  Les mots lourds des pauvres tiennent mieux : c’est le ressort social du livre.
- **Antagoniste** : Maître Aymon, premier cordier de Tressaille. Il a raison :
  le lac va rompre la Levée à la Fonte, la Basse sera noyée, la loi prévoit la
  Grande Reprise par un seul, et la corde de reprise a déjà l’âme d’Aube. Il a
  tort sur qui doit payer et comment ; il est prêt à payer lui-même.
- **Pas d’élu, pas de prophétie** : n’importe qui peut nouer ; le prix seul
  fait la rareté, et c’est l’institution qui décide qui le paie. La résonance
  entre Aube « sans-nom » et la fondatrice « Sans-Nom » est un fait culturel
  qu’elle refuse d’abord, puis choisit de retourner.

### Plan (étape 1) — synopsis, chapitres, bascules

**Synopsis.** Tressaille vit sous la Levée, la digue qui retient le lac de la
Retenue ; une corde maîtresse court sur sa crête, et les nœuds noués sur elle
depuis trois cents ans la tiennent. La corde chante faux : la dernière Grande
Reprise (Hersende, il y a quarante ans) cède plus tôt que prévu et la Fonte
approche. Aube, dix-sept ans, fileuse sans-nom de la Corderie, apprend que le
brin d’âme qu’elle file depuis trois ans est celui de la Reprise, et qu’on
attend d’elle qu’elle donne tous ses mots. Le Droit de Reprise l’oblige à se
présenter à la lune de la Fonte ; nul ne peut donner un mot pour un autre : il
faut qu’elle consente. Hersende, à qui il reste douze mots, lui noue un message
qu’elle ne sait pas lire et la pousse sur la route de la Tende, vers Haut-Charme
où l’on noue encore « à plusieurs ». Avec Garance la colporteuse, Bastien le
fils de la Prévôte et Séverin le compagnon envoyé pour la ramener, Aube remonte
la vallée, noue pour la première fois (et paie), traverse Sombreval où une
veillée forcée a échoué il y a deux siècles, franchit le col qui chante, et
découvre à Haut-Charme la veillée : mille demi-clés, mille cordelettes, mille
petits mots choisis. Le message de Hersende disait qu’elle tiendrait « jusqu’à
la lune » : elle donne ses douze mots pour acheter des jours et meurt. De
retour, Aube ne refuse pas de payer ; elle refuse de payer seule, et convainc
une ville — la Basse et la Haute — d’apporter ses cordelettes à la Levée.
Maître Aymon vient pour donner tout ; il finit par donner « seul ». La Levée
tient. Tressaille parle désormais avec des trous, et se prête les mots.

**Question thématique** : que vaut ce qu’on donne quand on n’a pas choisi de le
donner ? **Idée centrale** : rien ne tient qui n’a pas été choisi ; ce que
chacun choisit de donner, si petit soit-il, tient mieux que tout ce qu’on
arrache à un seul. **Promesse émotionnelle** : la gorge serrée et le cœur
léger — refermer le livre avec l’envie de tenir parole et de repartir sur la
route de la Tende.

**Chapitres** (rôle → bascule) :

1. *À reculons* — Aube file l’âme dans la Salle des Cordes ; un nœud de plaie
   montre la règle et le prix ; la Maîtresse-Corde chante faux ; Aymon : « cette
   corde est la tienne ». → De personne à désignée.
2. *Douze mots* — Le Conseil et le Droit de Reprise ; l’honneur d’un nom au
   Registre tente Aube ; Bastien s’oppose et on rit de lui ; les douze mots de
   Hersende ; le message noué ; « Va. Haut. » ; la porte à l’aube : Garance et
   Bastien attendent. → De désignée à partie.
3. *La corde qui chante* — La route, Garance, Vergogne, le deuil de Bastien ;
   les gorges ; la Grande Traversée chante au crépuscule ; Séverin attend de
   l’autre côté et ne peut rien forcer. → De fugitive à détentrice du seul
   consentement qui compte.
4. *Nœud d’amarre* — Le pont lâche sous un convoi ; premier nœud d’Aube, elle
   donne « faim » ; le chargement de Garance tombe dans la Tende ; Séverin reste
   pour la garder en vie. → Aube a noué et payé, et fait payer une autre.
5. *Les anneaux de Sombreval* — Les ruines, deux versions de la veillée
   manquée, les anneaux dans les pierres ; orage et Tende qui monte ; Séverin
   apprend le geste à Aube ; le nœud de Bastien ne tient pas (mot non vécu). →
   La légende devient une question ; la Fonte commence, le délai est réel.
6. *La benne* — Malebosse ; le vieux bennier ; la corde de la benne cède
   au-dessus du vide, deux mains sur un nœud : Séverin donne « froid », Aube
   « peur » ; Séverin envoie un message à Aymon et Aube le laisse partir. → De
   fugitive à émissaire ; un nœud à deux mots a tenu.
7. *La harpe du col* — La montée dans le brouillard, les cordes tendues qui
   chantent et guident, l’aube au-dessus des nuages ; le veilleur du col est
   Aurèle, le frère muet de Garance. → Les Hauts existent ; Garance retrouve
   et perd son frère.
8. *La veillée* — Haut-Charme, Mère Ancelle, le parler-nœud ; le message de
   Hersende lu : « Apprenez-lui la veillée. Je tiens jusqu’à la lune » ; une
   veillée sous les yeux d’Aube, Bastien donne « hâte » ; les Veilleurs ne
   peuvent descendre, Aurèle viendra. → Aube a la méthode et comprend le prix
   que paie Hersende.
9. *Grandes eaux* — Descente sous la Déliée, la Tende en crue, la Traversée
   emportée ; la Retenue en gabare, la Levée qui gémit ; Aymon a annoncé sa
   propre Grande Reprise pour la lune. → La course n’est plus contre l’eau mais
   contre un sacrifice.
10. *Le registre* — Tressaille évacue la Basse ; Hersende est morte, douze
    lignes au Registre, la dernière : « Aube » ; face-à-face avec Aymon, deux
    raisons ; « mille cordelettes avant la lune ». → De celle qui doit à celle
    qui propose.
11. *Mille demi-clés* — La nuit de la lune de la Fonte : Garance rameute la
    Basse, Bastien donne « honneur » devant la Haute, Ysabeau donne « raison » ;
    Aube noue la première et donne « personne » ; Aymon vient tout donner et
    finit par donner « seul » ; Séverin donne « maître » ; la corde chante juste.
    → La Levée tient, payée par tous.
12. *Les manquants* — Après la Fonte : une ville qui se prête les mots, le
    Registre aux mille noms, Aube choisit son nom et sa route. → Ce qui tient.

**Émerveillements** : la Grande Traversée qui chante (3), la harpe du col dans
le brouillard à l’aube (7), une ville qui chuchote ses mots dans les nœuds (11).
**Pertes** : le chargement de Garance, les mots de chacun, Hersende.
**Modules** : carte de la vallée de la Tende (9 lieux, nord en haut) ; graphe
autour d’Aube avec quatre liens à révélation retardée (Hersende–Haut-Charme,
Garance–Aurèle, Séverin–Aymon, Aymon–Aube).
