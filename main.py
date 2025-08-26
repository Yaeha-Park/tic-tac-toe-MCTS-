#!/usr/bin/python3 
import sys
from TTT import ttt

def main():
    run_cli_human_game()

def run_cli_human_game():
    # Game loop
    BOARD_SIZE = 9
    game = ttt(BOARD_SIZE)
    while (game.get_winner() == None):
        game.print_board()
        inp = get_user_input(game.get_valid_moves(), game.player)
        game.make_move(inp)
    
    # Print result and winner
    game.print_board()
    result = game.get_winner()
    if result == "Draw":
        print(result)
    else:
        print(f"{game.get_winner()} is the winner!")

def get_user_input(valid_moves, turn):
    print(f"{turn}'s move. Select a valid move: {valid_moves} or (q to quit)")
    
    # Get input that matches one of the valid moves (or q)
    while (True):
        try: 
            inp = input("> ")
            if inp.lower() == 'q':
                break
            elif int(inp) not in valid_moves:
                print("Please enter a move from the valid move list.")
            else: 
                break
        except:
            print("Please enter an integer.")

    if inp.lower() == 'q':
        sys.exit()

    return int(inp)

if __name__ == "__main__":
    main()
