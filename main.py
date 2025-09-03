#!/usr/bin/python3 
import sys
from TTT import ttt

def main():
    game_menu()

def game_menu():
    while(True):
        print("Choose a game mode:")
        print("-------------------")
        print("Mode \t\tKey")
        print("Human opponent: 'h'")
        print("MCTS opponent: \t'm'")
        print("Quit: \t\t'q'")

        inp = input("> ").lower()
        if inp == 'h':
            run_cli_human_game()
            break
        elif inp == 'm':
            print("MCTS mode is currently not implemented, check again later.")
            input("Press ENTER to continue\n")
        elif inp == 'q':
            break
        else:
            print("Option invalid. Please enter a valid key from the table.")
            input("Press ENTER to continue\n")

def run_cli_human_game(board_size = 3):
    # Game loop
    game = ttt(board_size)
    while (game.get_winner() == None):
        game.print_board()
        inp = get_user_input(game.get_valid_moves(), game.player)
        game.make_move(inp)
    
    # Print result and winner
    game.print_board()
    result = game.get_winner()
    if result == "Draw":
        print("The game is a draw.")
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
