def get_menu_option():
    print("Welcome to Tic Tac Toe\n")
    print("1. Human vs Human")
    print("2. Random AI vs Random AI")
    print("3. Human vs Random AI")
    print("4. Human vs Unbeatable AI\n")

    while True:
        gamemode = input("Choose a gamemode: ")
        if gamemode.isdigit():
            gamemode = int(gamemode)
            if gamemode > 4 or gamemode < 1:
                print("Invalid input, try again")
            else:
                for difficulty in range(1, 5):
                    if difficulty == gamemode:
                        return difficulty
                    else:
                        difficulty += 1
        else:
            print("Invalid input, try again")


pass


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print(option)  # if the user selected 1, it should print 1
