#!/usr/bin/python3 
from TTT import ttt

def main():
    run_cli_human_game()

def run_cli_human_game():
    game = ttt()
    while (game.get_winner() == None):
        game.print_board()
        inp = get_user_input(game.get_valid_moves(), game.player)
        game.make_move(inp)

    game.print_board()
    result = game.get_winner()
    if result == "Draw":
        print(result)
    else:
        print(f"{game.get_winner()} is the winner!")

def get_user_input(valid_moves, turn):
    print(f"{turn}'s move. Valid moves: {valid_moves}")
    while (True):
        try: 
            inp = input("> ")
            if inp == 'q':
                return ""
            elif int(inp) not in valid_moves:
                print("Please enter a move from the valid move list.")
            else: 
                break
        except:
            print("Please enter an integer.")

    return int(inp)

if __name__ == "__main__":
    main()
