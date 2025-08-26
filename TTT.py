
import copy
import random

class ttt:
    def __init__(self):
        self.board = [' '] * 9
        self.player = 'X'

    def get_valid_moves(self):
        valid = []
        for i in range(9):
            if self.board[i] == ' ':
                valid.append(i)

        return valid

    
    def make_move(self, move):
        # Make move on board
        self.board[move] = self.player 
        # Switch player after move 
        self.player = 'O' if self.player == 'X' else 'X'


    def get_winner(self):
        wins = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,7)]
        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return self.board[a]
            if ' ' not in self.board:
                return 'Draw'
            return None
    
    def is_terminal(self):
        return self.get_winner() is not None
    
    # TODO: make readable
    def print_board(self):
        for i in range(9):
            tile_char = self.board[i]
            if (i == 2 or i == 5 or i == 8) and i != 0:
                print(f" {tile_char} ")
                if i != 8:
                    print("-----------")
            else:
                print(f" {tile_char} |", end="")
        print('\n', end='')

    
