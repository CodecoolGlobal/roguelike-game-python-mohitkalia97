def get_human_coordinates(board, current_player):
    row = 3
    column = 3
    allowed_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
    move = input('Choose an empty field: ')

    if move.lower() == 'quit':
        print("Goodbye!")
        quit()
    elif move.lower() not in allowed_moves:
        print('Not a valid move! Try again!')
        return get_human_coordinates(board, current_player)
    if 'a' in move.lower():
        row = 0
    elif 'b' in move.lower():
        row = 1
    elif 'c' in move.lower():
        row = 2
    if '1' in move.lower():
        column = 0
    elif '2' in move.lower():
        column = 1
    elif '3' in move.lower():
        column = 2
    if board[row][column] != ".":
        print('Place already taken! Try again!')
        return get_human_coordinates(board, current_player)
    return (row, column)


pass


if __name__ == "__main__":

    board_1 = [
        ["X", "X", "."],
        ["X", ".", "."],
        ["X", "X", "."],
    ]
    coordinates = get_human_coordinates(board_1, "X")
    print(coordinates)
