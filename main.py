from environment import Minesweeper


if __name__ == "__main__":
    game = Minesweeper(5, 5, "easy")
    print(game.get_board())