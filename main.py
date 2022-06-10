import util
import engine
import ui
import random
import sys
import time
from ART import logo, girls, intro

PLAYER_ICON = '😡'
PLAYER_START_X = 1
PLAYER_START_Y = 18
position_x = 1
position_y = 18
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
key = ""
ENEMY_ICON = '💀'
Inventory = {"💝": 0, "🧭": 0, "🔱": 0}
level = 1
HITPOINTS = 3
AMOUNT_OF_ENEMIES = 5


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    player = {
        "Player_icon": PLAYER_ICON,
        "position_x": position_x,
        "position_y": position_y,
        "Inventory": Inventory,
        "HP": HITPOINTS,
        }
    return player


def create_enemy():
    enemy_position_x = random.randint(2, 28)
    enemy_position_y = random.randint(2, 18)
    enemy = {"Enemy_icon": ENEMY_ICON, "enemy_position_x": enemy_position_x, "enemy_position_y": enemy_position_y}
    return enemy


def main_game(level, player, Inventory):
    obstacles = ["🧭", "🔱", "💝", "🟦", "💀", "😡", "🌊"]
    player["position_y"] = 18
    player["position_x"] = 1
    if level == 1:
        board = engine.create_board_one(BOARD_WIDTH, BOARD_HEIGHT)
        util.clear_screen()
        print(intro)
        time.sleep(1)
    elif level == 2:
        board = engine.create_board_two(BOARD_WIDTH, BOARD_HEIGHT)
    elif level == 3:
        board = engine.create_board_three(BOARD_WIDTH, BOARD_HEIGHT)
        board[10][15] = "🥸 "
    if level != 3:
        engine.place_items(board)
    for i in range(AMOUNT_OF_ENEMIES):
        enemy = create_enemy()
        if board[enemy["enemy_position_y"]][enemy["enemy_position_x"]] not in obstacles and level != 3:
            engine.place_enemy(board, enemy)

    util.clear_screen()

    is_running = True
    while is_running:
        engine.put_player_on_board(board, player)
        print(f"Level: {level}")
        ui.display_board(board)
        line = ""
        for item, value in player["Inventory"].items():
            line += f"{item}: {value} "
        print()
        print(line)
        print(f'HP: {player["HP"]}')
        engine.check_movement(board, player, enemy, level, Inventory)
        util.clear_screen()

        if player["HP"] == 0:
            is_running = False
            engine.dead()


def main():
    util.clear_screen()
    player = create_player()
    is_running2 = True
    while is_running2:
        util.clear_screen()
        print(logo + girls)
        print("[P]lay Game")
        print("[E]xit")
        key = util.key_pressed()
        if key.upper() == "P":
            is_running2 = False
            main_game(level, player, Inventory)
        elif key.upper() == "E":
            util.clear_screen()
            sys.exit(0)
        else:
            KeyError("invalid input!")


if __name__ == '__main__':
    main()
