winner = None


def check_rows(board):
    row1 = board[0][0] == board[1][0] == board[2][0] != "."
    row2 = board[0][1] == board[1][1] == board[2][1] != "."
    row3 = board[0][2] == board[1][2] == board[2][2] != "."

    if row1 or row2 or row3:
        if row1:
            return board[0][0]
        elif row2:
            return board[0][1]
        elif row3:
            return board[0][2]
        else:
            return None


def check_columns(board):
    column1 = board[0][0] == board[0][1] == board[0][2] != "."
    column2 = board[1][0] == board[1][1] == board[1][2] != "."
    column3 = board[2][0] == board[2][1] == board[2][2] != "."

    if column1 or column2 or column3:
        if column1:
            return board[0][0]
        elif column2:
            return board[1][0]
        elif column3:
            return board[2][0]
        else:
            return None


def check_diagonals(board):
    diagonal1 = board[0][0] == board[1][1] == board[2][2] != "."
    diagonal2 = board[2][0] == board[1][1] == board[0][2] != "."

    if diagonal1 or diagonal2:
        if diagonal1:
            return board[0][0]
        elif diagonal2:
            return board[2][0]
        else:
            return None


def check_for_winner(board):
    global winner
    row_winner = check_rows(board)
    column_winner = check_columns(board)
    diagonal_winner = check_diagonals(board)

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return winner


def get_winning_player(board):

    check_for_winner(board)
    if winner == "X" or winner == "O":
        return winner
    elif winner is None:
        return None


pass


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    ["X", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_winning_player(board_1)) # should return "X"

  board_2 = [
    ["X", "O", "O"],
    ["X", "O", "."],
    ["O", "X", "X"],
  ]
  print(get_winning_player(board_2)) # should return "O"

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_winning_player(board_3)) # should return None