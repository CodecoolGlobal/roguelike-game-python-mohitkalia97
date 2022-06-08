import util
import engine
import ui
import random

PLAYER_ICON = '@'
PLAYER_START_X = 1
PLAYER_START_Y = 18
position_x = 1
position_y = 18
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
key = ""
ENEMY_ICON = 'E'
inventory = {"Heart_DJ": 0, "Compass": 0, "Trident": 0}
level = 1

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {"Player_icon": PLAYER_ICON, "position_x": position_x, "position_y": position_y, "Inventory": inventory}
    return player

def create_enemy():
    enemy_position_x = random.randint(2, 28)
    enemy_position_y = random.randint(2, 18)
    enemy = {"Enemy_icon": ENEMY_ICON, "enemy_position_x": enemy_position_x, "enemy_position_y": enemy_position_y}
    return enemy


def main_game(level):
    obstacles = ["C", "T", "H", "X", "#", "E"]
    player = create_player()
    if level == 1:
        board = engine.create_board_one(BOARD_WIDTH, BOARD_HEIGHT)
    elif level == 2:
        board = engine.create_board_two(BOARD_WIDTH, BOARD_HEIGHT)
    elif level == 3:
        board = engine.create_board_three(BOARD_WIDTH, BOARD_HEIGHT)
    engine.place_items(board)
    for i in range(3):
        enemy = create_enemy()
        if board[enemy["enemy_position_y"]][enemy["enemy_position_x"]] not in obstacles:
            engine.place_enemy(board, enemy)

    util.clear_screen()

    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        ui.display_board(board)
        line = ""
        for item, value in player["Inventory"].items():
            line += f"{item}: {value} "
        print(line)
        engine.check_movement(board, player, enemy, level)
        util.clear_screen()


def main():
    #level = 1
    #while level <= 3:
    main_game(level)
    #    level += 1

if __name__ == '__main__':
    main()