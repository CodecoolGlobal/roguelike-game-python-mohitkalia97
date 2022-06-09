from TTT_Boss.function0 import display_board
from TTT_Boss.function1 import get_menu_option
from TTT_Boss.function2 import get_empty_board
from TTT_Boss.function3 import get_human_coordinates
from TTT_Boss.function4 import get_random_ai_coordinates
from TTT_Boss.function5 import get_umbeatable_ai_coordinates
from TTT_Boss.function6 import get_winning_player
from TTT_Boss.function7 import is_board_full
from time import sleep

HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def main_menu():
    game_mode = 3
    board = get_empty_board()
    is_game_running = True
    round = 0

    while is_game_running:
        current_player = 'X'

        if round % 2 == 0:
            current_player = "X"
        else:
            current_player = "O"
        round += 1

        if game_mode == 1:
            display_board(board)
            x, y = get_human_coordinates(board, current_player)
            print("\n")
            board[x][y] = current_player

        if game_mode == 2:
            display_board(board)
            x, y = get_random_ai_coordinates(board, current_player)
            board[x][y] = current_player
            sleep(0.5)

        if game_mode == 3:
            display_board(board)
            if round % 2 != 0:
                x, y = get_human_coordinates(board, current_player)
                print("\n")
            else:
                x, y = get_random_ai_coordinates(board, current_player)
            board[x][y] = current_player
            sleep(0.5)

        if game_mode == 4:
            print("Not included in your current tictactoe subscription. Upgrade to tictactoe premium to get access!")
            break

        if is_board_full(board) is True and get_winning_player(board) is None:
            board[x][y] = current_player
            display_board(board)
            print("Draw!")
            break

        if get_winning_player(board) is None:
            continue

        elif get_winning_player(board) == "X":
            board[x][y] = current_player
            display_board(board)
            print("Player 'X' won!")
            break

        elif get_winning_player(board) == "O":
            board[x][y] = current_player
            display_board(board)
            print("Player 'O' won!")
            break


if __name__ == '__main__':
    main_menu()
