def slice_per(source, step):
    return [source[i::step]for i in range(step)]


def get_empty_board():
    board = [".", ".", ".",
             ".", ".", ".",
             ".", ".", "."]

    return(slice_per(board, 3))


pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    board = get_empty_board()
    print(board)
