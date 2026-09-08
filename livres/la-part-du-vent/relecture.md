# Relecture de La Part du vent

## Étape 5a — structure et rythme

Relecture du récit complet et de ses vingt-quatre feuillets. Aucun chapitre sans bascule ; les douze bascules et la chronologie figurent dans `world.chapterPlan` et `world.chronology` de [l’îlot du livre](index.html). Point de vue : Aubine, première personne au présent. Les souvenirs sont identifiés comme tels. Pas de scène hors de sa perception.

Corrections intégrées :

- Attache de sécurité du sauvetage rendue explicite ; références déplacées hors de l’incipit vers la première apparition de l’objet et du prénom.
- Amarrage de la barque aux moulins et retour de la forge par la crête clarifiés ; différence de charge sur le vieux pont explicitée. Le parcours de quatre jours est resynchronisé dans le plan.
- Transfert de charge de la tenue temporaire vers les appuis décrit avant le don final. Ni restitution du geste, ni levée magique de la vanne.
- Coutume du repas aux morts introduite par un geste quotidien, sans certitude surnaturelle ajoutée.
- Émerveillements répartis dans les trois tiers : vergers lumineux (3), cristaux du chenal (6), arcs d’embruns (11). La découverte du lac (7) et la nuit partagée avec Mado (12) les prolongent.
- Aucun nom de lieu n’apparaît dans l’introduction de la carte avant lecture. Le feuillet d’Orane attend sa rencontre ; le lien secret de Bertille attend son aveu.

La résolution répond à la question du partage des coûts : don individuel choisi avec une réelle possibilité de refus, travail collectif rémunéré, destruction assumée d’équipements urbains, conséquences encore visibles six semaines plus tard. La maison ne revient pas intacte, le bateau ne revient pas, le geste ne revient pas. La ville et le quartier sont sauvés ; aucune menace non résolue n’annonce un tome suivant. Le dernier échange sonore avec Mado paie la perte du sifflement et revient au linge de la première page.

Chaque ancrage de notice et de relation a été recalculé dans le même commit que les ajouts. Le manifeste reste cohérent : les bandeaux précèdent leurs chapitres et ne montrent pas les pertes, l’aveu ni le don avant leur lecture.

## Étape 5b — ligne à ligne et finitions

Passe complète sur les douze chapitres et les vingt-quatre notices : apostrophes courbes, ponctuation double précédée d’une espace insécable, dialogues au tiret cadratin, absence de marqueurs de travail. Les formulations qui attribuaient une pensée certaine à un autre personnage ont été ramenées à des observations d’Aubine. Le chapitre 8 devient « Les lumières sur la rive » pour ne pas annoncer la perte. La description de catalogue et les phrases de géographie précisent ce qui est effectivement connu. Les renvois redondants du dénouement et de la coda ont été retirés : 41 % des blocs gardent au moins une référence.

Le titre du chapitre a été reporté dans le plan et le manifeste ; les règles, les ancrages et la chronologie demeurent synchronisés. Aucune correction éditoriale en attente.

## Vérifications exécutées

- `python3 livres/_template/outils/verifier.py livres/la-part-du-vent --sans-images` : **Aucun défaut — livre conforme.** Douze chapitres, 349 blocs, 11 832 mots de récit, 24 notices, densité de mentions 41 %. Les 20 images intérieures déclarées s’ajoutent à la couverture, soit 21 images.
- `python3 scripts/build_catalog.py --output /private/tmp/catalog-verification-vent.json` : sortie 0, livre présent, auteur `gpt-6-astra (texte)`, durée calculée 59 minutes. Trois avertissements de comptage concernent des livres préexistants, aucun ne concerne ce roman. Le catalogue suivi n’a pas été modifié.
- `git diff --check` : sortie 0.
- Moteur JavaScript identique octet pour octet au [template](../_template/index.html), SHA-256 `9ba6609bf99ff47b2582ed2444b153debc7df1ec59bb1592bd2d777ea03d17a0`. Une substitution trop large du titre HTML avait aussi touché une balise SVG dans le script : le contrôle d’identité l’a détectée et la version exacte du template a été rétablie avant publication.
- Manifeste : ensemble exact des 21 chemins ; chaque alt et chaque `visualDescription` de l’îlot se retrouve dans son entrée. Aucun fichier image produit, aucun chemin externe, aucune entrée dérivée.
- Chrome isolé, Playwright, `file://` : parcours des 349 paragraphes avec comparaison du texte rendu à l’îlot ; navigation des douze chapitres, progression à 100 %, 24 notices ouvertes puis refermées au clavier, recherche du codex, thème, taille et persistance au rechargement. Zéro erreur JavaScript, zéro requête réseau distante. Les erreurs attendues de chargement des images absentes masquent bien tous leurs emplacements, couverture incluse.
- Carte et graphe : zéro nom de lieu ou d’entité visible avant lecture ; huit lieux, sept nœuds et huit liens en fin de parcours. Le mandat secret reste absent avant `c5-b10` et apparaît après ce bloc. Les infobulles portent les natures de relation exactes.
- Inspection visuelle sur bureau (1280×900) et mobile (390×844), thème sombre compris : prose, carte et graphe lisibles. Contrôle ciblé final du nouveau titre du chapitre 8 après correction.

**Limite du template constatée et reproduite** : à 390 px, la barre supérieure mesure 448 px avec les deux modules activés ; ses derniers boutons débordent vers la droite. Le même comportement existe dans le template source. La prose, la carte et le graphe restent contenus dans l’écran ; la navigation clavier fonctionne. Aucune modification du moteur ou de son CSS n’a été introduite pour ce livre. Ce point relève d’une correction commune de la liseuse.

## Checklist auteur — roman-atelier v9

- [x] Générateur de catalogue passé ; livre présent dans la sortie temporaire.
- [x] Vérificateur `--sans-images` passé sans défaut.
- [x] Lecture en `file://` de bout en bout ; zéro erreur JavaScript et aucune image cassée visible.
- [x] Métadonnées obligatoires exactes ; auteur confirmé par l’identifiant de modèle de la session ; genre, public, exigence, tonalité et capacités conformes.
- [x] Aucune meta `book:variant-of`.
- [x] `roman-atelier v9` et `atelier-liseuse v3` déclarés.
- [x] Carte et relations présentes, capacités déclarées, déverrouillages testés.
- [x] [Brief](brief.md) conservé textuellement, suivi de la lecture de l’auteur ; [manifeste](illustrations.md) complet.
- [x] Ancrage réel sans objet : monde entièrement inventé, aucune étape 0 nécessaire.
- [x] Révision structurelle et passe ligne à ligne distinctes ; bascules, chute, point de vue et temps contrôlés.
- [x] Socle éditorial et brief respectés, quantités justifiées par le récit, exploration sans renvois redondants dans la coda.
- [ ] Commits d’étapes poussés et PR ouverte avec le protocole Production, concours et relai illustrateur annoncés.
