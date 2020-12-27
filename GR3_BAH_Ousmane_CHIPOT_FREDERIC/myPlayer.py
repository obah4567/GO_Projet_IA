# -*- coding: utf-8 -*-
''' This is the file you have to modify for the tournament. Your default AI player must be called by this module, in the
myPlayer class.

Right now, this class contains the copy of the randomPlayer. But you have to change this!
'''

import numpy as np
import time
import Goban 
from random import choice
from playerInterface import *

class myPlayer(PlayerInterface):
    ''' Example of a random player for the go. The only tricky part is to be able to handle
    the internal representation of moves given by legal_moves() and used by push() and 
    to translate them to the GO-move strings "A1", ..., "J8", "PASS". Easy!

    '''

    def __init__(self):
        self._board = Goban.Board()
        self._mycolor = None

    def getPlayerName(self):
        return "Random Player"

    def getPlayerMove(self):
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
        print("Opponent played ", move) # New here
        # the board needs an internal represetation to push the move.  Not a string
        self._board.push(Goban.Board.name_to_flat(move)) 

    def newGame(self, color):
        self._mycolor = color
        self._opponent = Goban.Board.flip(color)

    def endGame(self, winner):
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
                if y > 0 and y < 8:
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
                if y > 0 and y < 8:
                    degre+=1
                    if (board[Board.flatten((x-1,y))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y - 1))] != 0):
                        degre += 1
                    if (board[Board.flatten((x,y + 1))] != 0):
                        degre += 1
            if x > 0 and x < 8:
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
        
        return 4 - degre

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
        
        for x in range (0, _BOARDSIZE, 1):
            for y in range (0, _BOARDSIZE, 1):

                if board[Board.flatten((x,y))] == _BLACK :
                    degre = calculDegreLiberte(board, x, y)
                    if degre==0 or degree==4:
                            scoreBlack += 1
                            break
                    if degre==3:
                        if nbAmis(board, x, y) == 0:
                            scoreBlack+=3
                        else:
                            scoreBlack+=2
                        break
                    if degre==2:
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
                    if degre==1:
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
                if  board[Board.flatten((x,y))] == _WHITE:
                    degre = calculDegreLiberte(board, x, y)
                    if degre==0 or degre==4:
                        scoreWhite += 1
                        break
                    if degre==3:
                        if nbAmis(board, x, y) == 0:
                            scoreWhite+=3
                        else:
                            scoreWhite+=2
                        break
                    if degre==2:
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
                    if degre==1:
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
        return scoreBlack - scoreWhite


    ##########################
    ### --- MinValue   --- ###
    ##########################

    def min_value( board, horizon, alpha=-np.inf, beta=np.inf):
        if board.is_game_over() or horizon<=0:
            return heuristique(board)

        for move in board.generate_legal_moves():
            board.push(move)
            beta = min( beta, max_value(board, alpha, beta, horizon-1))
            board.pop()
            if beta <= alpha :
                return alpha
        return beta

    ##########################
    ### --- MaxValue   --- ###
    ##########################

    def max_value( board, horizon, alpha=-np.inf, beta=np.inf):
        if board.is_game_over() or horizon<=0:
            return heuristique(b)

        for move in b.generate_legal_moves():
            board.push(move)
            alpha = max( alpha, min_value( board, alpha, beta, horizon-1))
            board.pop()
            if alpha >= beta:
                return beta
        return alpha

    def meilleur_coups_AlphaBeta( board, horizon):
        best_move = None
        max_score = -np.inf
        for move in board.generate_legal_moves():
            board.push(move)
            score = min_value( board, horizon-1)
            if max_score < score:
                max_score = score
                best_move = move
            board.pop()
        return best_move
'''
# ---------------------------------------- TESTS --------------------------------------# 
    board = Goban.Board()

    start_game = time.time()
    print(board)
    while not board.is_game_over():
        print("Ici")
        start = time.time()

        board.push(meilleur_coups_AlphaBeta(board, 3))
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
 '''
