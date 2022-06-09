def get_umbeatable_ai_coordinates(board, current_player):
  """
  Should return a tuple of 2 numbers. 
  Each number should be between 0-2.
  The chosen number should be only a free coordinate from the board.
  The chosen coordinate should always stop the other player from winning or
  maximize the current player's chances to win.
  If the board is full (all spots taken by either X or O) than "None"
  should be returned.
  """
  pass


if __name__ == "__main__":
  # run this file to test you have implemented correctly the function
  board_1 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print(get_umbeatable_ai_coordinates(board_1, "X")) # the printed coordinate should always be (0, 0)

  board_2 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print(get_umbeatable_ai_coordinates(board_2, "O")) # the printed coordinate should always be (1, 1)

  board_3 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print(get_umbeatable_ai_coordinates(board_3, "X")) # the printed coordinate should be either (0, 2) or (2, 0)