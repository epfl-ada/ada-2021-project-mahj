# Plan rendu

* Dire sur le site un truc du genre: "Pour plus d'infos aller voir le notebook"
* Pour le README: Faire un plan du notebook.
* Mais est-ce que les "topics" qu'on identifie ce ne sont pas les journaux
eux-mêmes justement? -> normalement pas exactement, though proche:
un journal devrait être lié à *quelques* topics.

### Décrire les données au viewer
* Montrer quelques samples au lecteur pour qu'il comprenne à quoi ressemble
  la data.
* Montrer quelques stats

### Parler de ce qu'on a réussi à faire:
  * Notre clustering marche sur des éléments sous-jacents, qui permettent parfois de
    séparer les journaux notamment:
    * géographique (pays, et même états des USA)
    * sujet traité (musique, sport, politique ...)

### Ainsi que de comment:
  * Traitement de la donnée de base:
    * Comment on a traité des fichiers aussi gros?
      * bla
  * Augmentation de la donnée:
    * Identifier les journaux (obtention du QID wikidata)
    * Scrapping wikidata pour obtenir les group owners.
    * Lier les journaux aux endroits
  * Traitement de ce qu'on obtient après:
    * TF IDF
      * À quoi on l'applique
      * Pk on fait ça
      * Vitef comment ça marche
    * SVD
      * pk on fait ça
      * Vitef comment ça marche
      * Retirer certaines data pcque grosse variance selon eux
      (e.g. ne garder que  les journaux des USA)
      * Analyse des significations des axes **vérifier interprétation!!!**

### Dire quelles étaient les limitations
  * On a tout fait à partir de citations (mais on peut aussi même ça pour illustrer
  la "puissance" de notre clustering)
  * La manière dont sont récupérés les citations/speakers
    * Comment quotebank choisit les journaux
      * certains sont bcp moins sampled -> pk?
    * Comment quotebank choisit les articles/speakers dans les journaux

## Mais quelle est donc la conclusion?
#### Répéter ce qu'on a réussi à faire
  On a réussi à trouver certains groupes (avec les citations ET avec les speakers)
  (répéter?).   
  On a réussi à identifier les axes?
  -> On identifie des groupes qui parlent tjrs de la même chose  
  -> VS des qui parlent de plein de trucs différents

#### Idée: parler de la concentration des articles:
Exemple de *Newsquest (UK)*:
  * certains journaux dans un groupe disent à peu près tjrs la même chose
  * ou ptetre même cetains groupes en copient d'autres?

Ouvrir rapidement vers une suite

#### un 6 svp **(⊙_⊙;)**
































a
