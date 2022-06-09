def display_board(board):
    row1 = (board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    row2 = (board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    row3 = (board[2][0] + " | " + board[2][1] + " | " + board[2][2])

    print("  1   2   3")
    print(f"A {row1}")
    print("  --+---+--")
    print(f"B {row2}")
    print("  --+---+--")
    print(f"C {row3}")
    print("\n")

    pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = [
      ["X", "O", "."],
      ["X", "O", "."],
      ["O", "X", "."]
    ]
    display_board(board)
    # should print 
    #     1   2   3
    # A   X | O | . 
    #    ---+---+---
    # B   X | O | .
    #    --+---+---
    # C   0 | X | . 
    #    --+---+---
