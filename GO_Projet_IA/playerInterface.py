class PlayerInterface():
    ''' Abstract class that must be implemented by you AI. Typically, a file "myPlayer.py" will implement it for your
    AI to enter the tournament.
    
    You may want to check to player implementations of this interface:
    - the random player
    - the gnugo player
    '''

    board = Goban.Board()

    #https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
    #https://adrien.poupa.fr/tpe/algorithme-minmax
    #https://www.youtube.com/watch?v=l-hh51ncgDI

    #Pour reviser 
    #https://www.labri.fr/perso/vlepetit/teaching/d4.pdf


    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        ''' Must return the name of your AI player.'''
        #return "Not Defined"
        return "Ousmane&Fred"

    def getPlayerMove(self): 
        ''' This is where you will put your AI. This function must return the move as a standard
        move in GO, ie, "A1", "A2", ..., "D5", ..., "J8", "J9" or "PASS"

        WARNING: In the Board class, legal_moves() and weak_legal_moves() are giving internal
        coordinates only (to speed up the push/pop methods and the game tree traversal). However,
        to communicate with this interface, you can't use these moves anymore here.

        You have to use the helper function flat_to_name to translate the internal representation of moves
        in the Goban.py file into a named move.

        The result of this function must be one element of [Board.flat_to_name(m) for m in b.legal_moves()]
        (it has to be legal, so at the end, weak_legal_moves() may not be sufficient here.)
        '''
        #return "PASS" 
        if self._board.is_game_over():
            print("Referee told me to play but the game is over!")
            return "PASS" 
        moves = self._board.legal_moves() # Dont use weak_legal_moves() here!
        move = choice(moves) 
        self._board.push(move)

        # New here: allows to consider internal representations of moves
        print("I am playing ", self._board.move_to_str(move))
        print("My current board :")
        self._board.prettyPrint()
        # move is an internal representation. To communicate with the interface I need to change if to a string
        return Goban.Board.flat_to_name(move) 

    def playOpponentMove(self, move): 
        '''Inform you that the oponent has played this move. You must play it with no 
        search (just update your local variables to take it into account)

        The move is given as a GO move string, like "A1", ... "J9", "PASS"
         
        WARNING: because the method Goban.push(m) needs a move represented as a flat move (integers),
        you can not directly call this method with the given move here. You will typically call
        b.push(Board.name_to_flat(move)) to translate the move into its flat (internal) representation. 
         '''
        #pass
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color): 
        '''Starts a new game, and give you your color.  As defined in Goban.py : color=1
        for BLACK, and color=2 for WHITE'''
        #pass
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, color):
        '''You can get a feedback on the winner
        This function gives you the color of the winner'''
        #pass
        if self._mycolor == winner:
            print("I won!!!")
        else:
            print("I lost :(!!")

### --- Calcul Degre de Liberte d'une piéce --- ###

    def calculDegreLiberte(board, x, y):
        degre = 0
        if x==0 or y==0 or x==8 or y==8:
            if x==0:
                if y==0:
                    degre+=2
                    if (board[Board.flatten((x + 1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y + 1))] != 0):
                        degre += 1
                if y==8:
                    degre+=2
                    if (board[Board.flatten((x + 1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y - 1))] != 0):
                        degre += 1
                else:
                    degre+=1
                    if (board[Board.flatten((x + 1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y - 1))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y + 1))] != 0):
                        degre += 1
            if x==8:
                if y==0:
                    degre+=2
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y + 1))] != 0):
                        degre += 1
                if y==8:
                    degre+=2
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y - 1))] != 0):
                        degre += 1
                else:
                    degre+=1
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y - 1))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y + 1))] != 0):
                        degre += 1
            else:
                if y==0:
                    degre+=1
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x + 1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y+1))] != 0):
                        degre+=1
                if y==8:
                    degre+=1
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x + 1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y-1))] != 0):
                        degre+=1
        else:
            if (board[Board.flatten((x - 1,y))] != 0):
                degre += 1
            if (board[Board.flatten((x + 1,y))] != 0):
                degre += 1
            if (board[Board.flatten((x,y + 1))] != 0):
                degre += 1
            if (board[Board.flatten((x,y - 1))] != 0):
                degre += 1
            return degre

### --- Calcul Le Nombre d'amis d'une piéce --- ###

    def nbAmis(board, x, y):
        nbAmis = 0
        id = board[Board.flatten((x,y))]
        if x==0 or x==8 or y==0 or y==8:
            if x==0:
                if y==0:
                    if (board[Board.flatten((x+1,y))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x,y+1))] == id):
                        nbAmis += 1
                if y==8:
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x+1,y))] == id):
                        nbAmis += 1
                else:
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x+1,y))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
            if x==8:
                if y==0:
                    if (board[Board.flatten((x,y+1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x-1,y))] == id):
                        nbAmis += 1
                if y==8:
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x-1,y))] == id):
                        nbAmis += 1
                else:
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x-1,y))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x,y+1))] == id):
                        nbAmis += 1
            else:
                if y==0:
                    if (board[Board.flatten((x,y+1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x-1,y))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x+1,y))] == id):
                        nbAmis += 1
                if y==8:
                    if (board[Board.flatten((x,y-1))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x-1,y))] == id):
                        nbAmis += 1
                    if (board[Board.flatten((x+1,y))] == id):
                        nbAmis += 1
                    
        else:
            if (board[Board.flatten((x-1,y))] == id):   
                nbAmis += 1
            if (board[Board.flatten((x+1,y))] == id):
                nbAmis += 1
            if (board[Board.flatten((x,y-1))] == id):
                nbAmis += 1
            if (board[Board.flatten((x,y+1))] == id):
                nbAmis += 1
        return nbAmis

##########################
### --- Heuristic --- ###
##########################

    def heuristique(board):
        scoreWhite = 0
        degre = 0
        scoreBlack = 0
        # for (x = 0; x < _BOARDSIZE; x = x+1)
        #     for (y = 0; y < _BOARDSIZE; y = y+1)
        for x in range (0, _BOARDSIZE, 1):
            for y in range (0, _BOARDSIZE, 1):

                if board[Board.flatten((x,y))] == _BLACK :
                    degre = calculDegreLiberte(board, x, y)
                    switch degre:
                        case 0:
                            scoreBlack += 1
                            break
                        case 1:
                            if nbAmis(board, x, y) == 0:
                                scoreBlack+=3
                            else:
                                scoreBlack+=2
                            break
                        case 2:
                            nbAmis = nbAmis(board, x, y)
                            if nbAmis == 0:
                                scoreBlack-=2
                                break
                            if nbAmis == 2:
                                scoreBlack+=2
                                break
                            if nbAmis == 1:
                                scoreBlack+=3
                                break
                        case 3:
                            nbAmis = nbAmis(board, x, y)
                            if nbAmis == 0:
                                scoreBlack-=5
                            if nbAmis == 3:
                                scoreBlack+=3 
                            if nbAmis == 1:
                                scoreBlack-=2
                            if nbAmis ==2:
                                scoreBlack+=4
                            break
                        case 4:
                            scoreBlack+=1
                            break
                if board[Board.flatten((x,y)) == _WHITE:
                    degre = calculDegreLiberte(board, x, y)
                    switch degre:
                        case 4:
                            scoreWhite += 1
                            break
                        case 3:
                            if nbAmis(board, x, y) == 0:
                                scoreWhite+=3
                            else:
                                scoreWhite+=2
                            break
                        case 2:
                            nbAmis = nbAmis(board, x, y)
                            if nbAmis == 2:
                                scoreWhite-=2
                                break
                            if nbAmis == 0:
                                scoreWhite+=2
                                break
                            if nbAmis == 1:
                                scoreWhite+=3
                                break
                        case 1:
                            nbAmis = nbAmis(board, x, y)
                            if nbAmis == 0:
                                scoreWhite-=5
                                break
                            if nbAmis == 3:
                                scoreWhite+=3 
                                break
                            if nbAmis == 1:
                                scoreWhite-=2
                                break
                            if nbAmis == 2:
                                scoreWhite+=4
                                break
                        case 0:
                            scoreWhite+=1
                            break
        return scoreWhite - scoreWhite


##########################
### --- MinMAX --- ###
##########################

#détermine le meilleur coup pour l'IA

    # def minmax( board, horizon):
    #     if b.is_game_over() or horizon<=0:
    #         return heuristique(b)

    #     min_score = np.inf
    #     for move in b.generate_legal_moves():
    #         b.push(move)
    #         min_score = min( min_score, maxmin( b, horizon-1))
    #         b.pop()
    #     return min_score

##########################
### --- MaxMIN --- ###
##########################

#étermine le meilleur coup pour le joueur

    #def maxmin( b, horizon=4):
    # def maxmin( board, horizon):
    #     if b.is_game_over() or horizon<=0:
    #         return heuristique(b)

    #     max_score = -np.inf
    #     for move in b.generate_legal_moves():
    #         b.push(move)
    #         max_score = max( max_score, minmax( b, horizon-1))
    #         b.pop()
    #     return max_score

    ########################

    def min_value( board, alpha=-np.inf, beta=np.inf, horizon):
        if board.is_game_over() or horizon<=0:
            return heuristique(b)

        for move in b.generate_legal_moves():
            board.push(move)
            beta = min( beta, max_value(board, alpha, beta, horizon-1))
            board.pop()
            if beta <= alpha :
                return alpha
        return beta

    def max_value( board, alpha=-np.inf, beta=np.inf, horizon):
        if board.is_game_over() or horizon<=0:
            return heuristique(b)

        for move in b.generate_legal_moves():
            board.push(move)
            alpha = max( alpha, min_value( board, alpha, beta, horizon-1))
            board.pop()
            if alpha >= beta:
                return beta
        return alpha

    def meilleur_coups_alphabeta( board, horizon):
        best_move = None
        max_score = -np.inf
        for move in b.generate_legal_moves():
            board.push(move)
            score = min_value( board, horizon = horizon-1)
            if max_score < score:
                max_score = score
                best_move = move
            board.pop()
        return best_move

# ---------------------------------------- TESTS --------------------------------------# 


start_game = time.time()
print(board)
while not board.is_game_over():
    print("Ici")
    start = time.time()

    board.push(meilleur_coups_alphabeta(board, horizon = 3))
    elapsed_time = time.time() - start
    print(board)
    print("Move played in ", elapsed_time)
    print("-------------------------------")
    if board.is_game_over():
        break
    print("Black to move:")
    start = time.time()
    #black_move = minimaxAB(board, 3, False)
    black_move = randomMove(board)
    board.push(black_move)
    elapsed_time = time.time() - start
    print(board)
    #print(black_move.uci(), " played in ", elapsed_time)
    print("-------------------------------")
print("Result: ", board.result())
print("Game duration: ", time.time() - start_game)


# -----------------------------------------------TESTS-------------------------------#
 