from math import sqrt

class ttt:
    def __init__(self, board_size = 3):
        # Assign board size and raise error if not perfect square
        self.board_size = board_size
        self.num_squares = board_size * board_size 
        self.board = [' '] * self.num_squares
        assert sqrt(self.num_squares) == self.board_size

        # Player turn tracker
        self.player = 'X'

    def get_valid_moves(self):
        valid = []
        for i in range(self.num_squares):
            if self.board[i] == ' ':
                valid.append(i)

        return valid

    
    def make_move(self, move):
        # Make move on board
        self.board[move] = self.player 
        # Switch player after move 
        self.player = 'O' if self.player == 'X' else 'X'


    def get_winner(self):
        # Get wins 
        wins = self.calculate_possible_wins()

        # Check win lines for winner
        for win in wins:
            last_seen = None
            for pos in win:
                if self.board[pos] == ' ':
                    last_seen = None
                    break
                if last_seen == None: 
                    last_seen = self.board[pos]
                    continue
                elif last_seen != self.board[pos]:
                    last_seen = None 
                    break
            if last_seen != None:
                return last_seen
        
        # If no empty spaces then game is draw
        if ' ' not in self.board:
            return 'Draw'

        return None

    def calculate_possible_wins(self):
        wins = []
        squares_per_row = self.board_size

        # Horizontal wins 
        for i in range(0, self.num_squares, squares_per_row):
            win = []
            for j in range(squares_per_row):
                win.append(i+j)
            wins.append(tuple(win))
        
        # Vertical wins 
        for i in range(squares_per_row):
            win = []
            for j in range(0, self.num_squares, squares_per_row):
                win.append(i+j)
            wins.append(tuple(win))

        # Diagonal wins
        top_left_diag_win = []
        for i in range(squares_per_row):
            top_left_diag_win.append(i + (i*squares_per_row))
        wins.append(tuple(top_left_diag_win))

        top_right_diag_win = []
        for i in range(squares_per_row):
            top_right_diag_win.append((squares_per_row-1)*(i+1))
        wins.append(tuple(top_right_diag_win))
        
        # Trust me bro.
        return wins
    
    def is_terminal(self):
        return self.get_winner() is not None
    
    def print_board(self):
        # Dynamically check how many squares are in each row 
        squares_per_row = self.board_size
        
        # Print entire board
        for i in range(self.num_squares):
            square_char = self.board[i]
            # It just works.
            if i % squares_per_row == squares_per_row - 1:
                print(f" {square_char} ")
                if i != self.num_squares - 1:
                    print("----" * squares_per_row)
            else:
                print(f" {square_char} |", end="")
        print('\n', end='')

    
