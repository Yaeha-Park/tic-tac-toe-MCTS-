
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
        new = copy.deepcopy(self)
        new.board[move] = self.player
        new.player = 'O' if self.player == 'X' else 'X'

    def winner(self):
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
    
    def print_board(self):
        for i in range(3):
            print(self.board[i*3:(i+1)*3])
        print()

    
