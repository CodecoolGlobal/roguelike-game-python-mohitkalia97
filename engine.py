from os import initgroups
#from main import BOARD_WIDTH, BOARD_HEIGHT
import util
#from random import choice, random
import sys
import main
import time
import random


def create_board_one(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    wall = "X"
    board = []
    upper = wall * width
    door = "#"

    for row in range(height):
        line = []
        if row == 0 or row == height-1:
            board.append(upper)
        else:
            for col in range(width):
                if col == width - 1 and row == 1 or col == width - 1 and row == 2:
                    line.append(door)
                elif col == 0 or col == width - 1:
                    line.append(wall)
                elif row == 9 and col in range(1, 26):
                    line.append(wall)
                elif row == 3 and col in range(10, 40):
                    line.append(wall)
                elif col == 25 and row in range(13, 50):
                    line.append(wall)
                elif col == 12 and row in range(9, 17):
                    line.append(wall)
                else:
                    line.append(' ')
            board.append(line)
    return board

def create_board_two(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''

    wall = "X"
    board = []
    upper = wall * width
    door = "#"

    for row in range(height):
        line = []
        if row == 0 or row == height-1:
            board.append(upper)
        else:
            for col in range(width):
                if col == width - 1 and row == 1 or col == width - 1 and row == 2:
                    line.append(door)
                elif col == 0 or col == width - 1:
                    line.append(wall)
                elif row == 9 and col in range(15, 30):
                    line.append(wall)
                elif col == 15 and row in range(9, 17):
                    line.append(wall)
                elif col == 5 and row in range(3, 30):
                    line.append(wall)
                else:
                    line.append(' ')
            board.append(line)
    return board

def create_board_three(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''

    wall = "X"
    board = []
    upper = wall * width

    for row in range(height):
        line = []
        if row == 0 or row == height-1:
            board.append(upper)
        else:
            for col in range(width):
                if col == 0 or col == width - 1:
                    line.append(wall)
                else:
                    line.append(' ')
            board.append(line)
    return board


def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    board[player['position_y']][player['position_x']] = player['Player_icon']
    return board
    
    
def check_movement(board, player, enemy, level):
    """Move the player and check collisions with the walls
    Args:
    y, x: current coordinates of the player
    board: list of lists representing our map
    Returns:
    position: tuple with user current position
    """
    wall = ['X', '#']
    position = ()

    while True:
        char = util.key_pressed()

        if board[player["position_y"]][player["position_x"] + 1] in wall[1]:
            level += 1
            main.main_game(level)
            return level

        if char == 'd' and board[player["position_y"]][player["position_x"]+1] not in wall:
            #check_for_door(board, player)
            board[player["position_y"]][player["position_x"]] = ' '
            player["position_x"] = player["position_x"] + 1
            check_board_items(board, player)
            check_for_enemy(board, player, enemy)
            position = (player["position_y"], player["position_x"])
            return False

        elif char == 'a' and board[player["position_y"]][player["position_x"]-1] not in wall:
            #check_for_door(board, player)
            board[player["position_y"]][player["position_x"]] = ' '
            player["position_x"] = player["position_x"] - 1
            check_board_items(board, player)
            check_for_enemy(board, player, enemy)
            position = (player["position_y"], player["position_x"])
            return False

        elif char == 'w' and board[player["position_y"]-1][player["position_x"]] not in wall:
            #check_for_door(board, player)
            board[player["position_y"]][player["position_x"]] = ' '
            player["position_y"] = player["position_y"] - 1
            check_board_items(board, player)
            check_for_enemy(board, player, enemy)
            position = (player["position_y"], player["position_x"])
            return False

        elif char == 's' and board[player["position_y"]+1][player["position_x"]] not in wall:
            #check_for_door(board, player)
            board[player["position_y"]][player["position_x"]] = ' '
            player["position_y"] = player["position_y"] + 1
            check_board_items(board, player)
            check_for_enemy(board, player, enemy)
            position = (player["position_y"], player["position_x"])
            return False

        elif char == 'q':
            sys.exit()
        else:
            return position


def place_items(board):
    obstacles = ["C", "T", "H", "X", "#", "E"]
    items = ["H", "C", "T"]
    for index in range(3):
        item_pos_x = random.randint(2, 18)
        item_pos_y = random.randint(2, 28)
        if board[item_pos_x][item_pos_y] not in obstacles:
            board[item_pos_x][item_pos_y] = items[index]
    return board

def check_board_items(board, player):
    items_on_board = ["H", "C", "T"]
    position = board[player["position_y"]][player["position_x"]]

    if position in items_on_board:
        if position == "H":  #Heart_DJ durch Emoji bzw. Buchstaben ersetzen
            player["Inventory"]["Heart_DJ"] += 1
        elif position == "C":
            player["Inventory"]["Compass"] += 1
        elif position == "T":
            player["Inventory"]["Trident"] += 1

def check_for_enemy(board, player, enemy):
    interaction = random.choice(["WIN!", "LOSE!"])
    position = board[player["position_y"]][player["position_x"]]
    if position == "E":
        print(interaction)
        if interaction == "LOSE!":
            player["HP"] -= 1
            time.sleep(1)
        else:
            time.sleep(1)




def place_enemy(board, enemy):
    board[enemy["enemy_position_y"]][enemy["enemy_position_x"]] = enemy["Enemy_icon"]
    return board