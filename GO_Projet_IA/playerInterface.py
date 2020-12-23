class PlayerInterface():
    ''' Abstract class that must be implemented by you AI. Typically, a file "myPlayer.py" will implement it for your
    AI to enter the tournament.
    
    You may want to check to player implementations of this interface:
    - the random player
    - the gnugo player
    '''

    ##b = Goban.Board()

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
        return "Ousmane"

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

##########################
### --- Heuristic --- ###
##########################

    def heuristic (b):
        poids = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'J':8}
        score = 0
        for x in b.piece_map().values():
            x = x.symbol()
            sign = 1 if x.isupper() else -1
            x = x.lower()
            score += sign * poids[x]
        return score


##########################
### --- MinMAX --- ###
##########################

#détermine le meilleur coup pour l'IA

    def minmax( b, horizon):
        if b.is_game_over() or horizon<=0:
            return heuristique(b)

        min_score = np.inf
        for move in b.generate_legal_moves():
            b.push(move)
            min_score = min( min_score, maxmin( b, horizon-1))
            b.pop()
        return min_score

##########################
### --- MaxMIN --- ###
##########################

#étermine le meilleur coup pour le joueur

    #def maxmin( b, horizon=4):
    def maxmin( b, horizon):
        if b.is_game_over() or horizon<=0:
            return heuristique(b)

        max_score = -np.inf
        for move in b.generate_legal_moves():
            b.push(move)
            max_score = max( max_score, minmax( b, horizon-1))
            b.pop()
        return max_score