def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    for i in range(len(board)):
        print(" ".join(board[i]))
