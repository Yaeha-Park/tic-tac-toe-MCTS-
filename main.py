#!/usr/bin/python3 
from TTT import ttt

def main():
    run_cli_human_game()

def run_cli_human_game():
    game = ttt()
    inp = get_user_input(game.get_valid_moves())

def get_user_input(valid_moves):
    print(f"Please make a move. Valid moves: {valid_moves}")
    while (True):
        try: 
            inp = input("> ")
            if int(inp) not in valid_moves:
                print("Please enter a move from the valid move list.")
            else: 
                break
        except:
            print("Please enter an integer.")

    return int(inp)

if __name__ == "__main__":
    main()
