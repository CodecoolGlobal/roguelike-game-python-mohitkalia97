import random
from TTT_Boss.function7 import is_board_full


def get_random_ai_coordinates(board, current_player):
    row = 3
    column = 3
    allowed_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    ai_move = random.choice(allowed_moves)

    while is_board_full(board) is False:
        if 'a' in ai_move:
            row = 0
        elif 'b' in ai_move:
            row = 1
        elif 'c' in ai_move:
            row = 2
        if '1' in ai_move:
            column = 0
        elif '2' in ai_move:
            column = 1
        elif '3' in ai_move:
            column = 2
        if board[row][column] != ".":
            return get_random_ai_coordinates(board, current_player)
        return (row, column)


pass


if __name__ == "__main__":
    board_1 = [
        ["O", "O", "."],
        [".", "O", "."],
        ["X", "X", "O"],
      ]
    print(get_random_ai_coordinates(board_1, "X"))
    print(get_random_ai_coordinates(board_1, "X"))
    print(get_random_ai_coordinates(board_1, "X"))

    board_2 = [
        ["O", "X", "X"],
        ["X", "O", "X"],
        ["X", "O", "X"],
      ]
    print(get_random_ai_coordinates(board_2, "O"))
    