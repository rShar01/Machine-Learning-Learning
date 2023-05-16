from environment import Minesweeper


if __name__ == "__main__":
    game = Minesweeper(10, 7, "easy")
    print("--- STARTING GAME ---")
    while True:
        print("--- Curret Board ---")
        print(game.get_state())
        choice = input("Enter 'b' to dig for bombs and 'f' to place a flag:")
        x = int(input("Enter the x coordinate (0 indexed):"))
        y = int(input("Enter the y coordinate (0 indexed):"))

        if choice == 'b':
            found_bomb = game.action_dig_for_bomb(x,y)
            if found_bomb:
                break
        else:
            game.place_flag(x,y)


    print("---- GAME OVER ----")
    print("final board:")
    print(game.get_state())