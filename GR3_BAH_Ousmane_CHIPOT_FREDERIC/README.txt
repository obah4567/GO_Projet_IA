#Projet IA Ousmane Bah - Frédéric Chipot
============================================================================================================================================================

#Lignes de commandes : 


------------------------------

#Techniques :
Une fonction calcule la liste des coups possibles. A l'aide de cette liste de coups possibles on va dérouler 
un arbre de jeu qui aura une profondeur d'horizon. Nous utiliserons une heuristique qui attribuera des scores
à chaque coup et utiliserons l'algorithme alphabeta pour choisir le meilleur coup à jouer. 

#L'heuristique : 
Différence des scores des degrés de libertés entre les pierres AMIS contre les pierres ENNEMIS.
Nous attribuons des scores selon leurs degrés de liberté et l'identité des pierres voisines.

Une pierre entouré par 3 pierres ennemis aura un score très mauvais vu qu'elle sera facilement prise. 
Une pierre situé proche d'une pierre ennemie dans une situation "non désavantageuse" aura un meilleur
score qu'une pierre qu'entourée par des alliées. 

C'est une heuristique extrêmement basique qui essaie de pousser au jeu audacieux sans pour autant être téméraire.

L'heuristique utilisent deux autres fonctions calculDegreLiberte(board, x, y) et nbAmis(board, x, y).
Ces fonctions font exactement ce que leur nom indique : elles calculent le degré de liberté de la pierre de 
coordonnée x,y et le nombres de pierre voisine de la pierre x,y de même identité (si je suis le joueur Black,
alors mes pierres seront Black).

Les très nombreux if présents dans ces fonctions sont là afin de différencier les cas où on est au bord, 
sur les coins ou "à l'intérieur" du Goban. 

#AlphaBeta :
Algorithme vu en cours qui nous permet de sélectionner le coup le plus susceptible de nous amener à la victoire 
parmi les coups possibles. 

AlphaBeta utilisent les fonctions également vu en cours min_value et max_value qui calculent à tours de rôles 
le coup le plus susceptible de gagner pour ami et le coup le moins susceptible de gagner pour ennemi. 

-------------------------------