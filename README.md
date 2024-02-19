# JeuLogique

1 - Les règles du jeu
Entre 2 et 8 joueurs s’affrontent sur un plateau rectangulaire initialement vide comportant par défaut 8 lignes et 5 colonnes. Chaque joueur possède des pions d’une certaine couleur.

Alternativement, chacun des joueurs va poser l’un de ses pions soit sur une case vide, soit sur une case contenant déjà un ou plusieurs de ses pions.

Les cases situées dans les coins du plateau ont une capacité maximale de 2 pions, celles situées sur les bords mais pas dans les coins ont une capacité maximale de 3 pions, et enfin celles situées à l’intérieur du plateau ont une capacité maximale de 4 pions.

Quand le nombre de pions sur une case est égal à la capacité maximale que celle-ci peut contenir, ces pions sont envoyés vers les cases adjacentes et la case se libère. Si sur l’une des cases adjacentes se trouvaient des pions du joueur le nouveau pion se rajoute à ceux-ci. Si sur l’une des cases adjacentes se trouvaient des pions adverses, ceux-ci sont capturés, ils changent de couleur et le nouveau pion se rajoute ensuite.

Après un tel déplacement de pions, les cases adjacentes contiennent donc plus de pions qu’elles n’en avaient auparavant et peuvent donc à leur tour atteindre leur capacité maximale. Si c’est le cas, le phénomène se reproduit et ainsi de suite. On peut donc assister à une réaction en chaîne.


2 - Implémentation de ce jeu en Python

   - Une classe "case" avec pour attributs un entier indiquant le nombre de pions sur cette case et un autre entier représentant le joueur auquel ces (éventuels) pions appartiennent.
   - Une classe “jeu“ avec plusieurs attributs à déterminer dont l'un d'eux sera une liste à deux dimensions d'objets de la classe “case“ modélisant le plateau de jeu.
Le design de l'application est libre, mais votre programme devra au moins comporter les fonctionnalités suivantes :

   - Choix d'un nombre de joueurs entre 2 et 8, chacun d'eux aura une couleur d'attribuée.
   - Choix d'un nombre de lignes entre 3 et 10 et choix d'un nombre de colonnes entre 3 et 12. Il faudra nécessairement que le nombre de cases du plateau soit supérieur ou égal au nombre de joueurs afin que chaque joueur puisse au moins jouer une fois.
   - Affichage de la grille en utilisant la couleur du joueur dont c'est le tour.
   - Sélection à la souris d'une case conformément aux règles par le joueur dont c'est le tour.
   - Déplacement des pions vers les cases adjacentes si la capacité maximale d'une case est atteinte. Captures éventuelles des pions adverses lors de ce déplacement.
   - Si après un déplacement une ou plusieurs autres cases atteignent leur capacité maximale, de nouveaux déplacements sont réalisés. Et ainsi de suite.
   - Gestion des tours de jeu et de l'alternance des joueurs en éliminant au fur et à mesure les joueurs n'ayant plus de pions.
   - Gestion de la fin de partie (affichage du résultat, proposition d'une nouvelle partie, etc.).
   - On prendra soin de découpler au maximum les méthodes algorithmiques, i.e. celles qui interagissent avec la structure de données modélisant le plateau, des méthodes graphiques qui elles s'occupent de l'affichage et de la gestion des événements.

## Important 

Le jeu se lance en éxecutant Lancement jeu.py.

## Attention :
 Programme réalisé sous python3 et plus precisemment, veillez à utiliser la version 3.10.11 de python.
Le module 'Playsound' version 1.2.2 est requis pour le bon fonctionnement du programme.