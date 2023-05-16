from constants import *
import numpy as np

class Minesweeper():
    def __init__(self, length: int, width: int, difficulty: str = None):
        self.num_boxes = length*width
        self.length = length
        self.width = width

        # To make the game less trivial (and corner cases easier), at least 5x5 board 
        if length < 5 or width < 5:
            raise InvalidConfigException
        
        self.game_board = np.chararray((length, width), unicode=True)

        if difficulty is None or difficulty not in DIFFICULTIES:
            raise InvalidConfigException
        elif difficulty == "easy":
            self.visible_board = np.random.choice([0, MINE], size=(length, width), p=[0.85, 0.15])
        elif difficulty == "medium":
            self.visible_board = np.random.choice([0, MINE], size=(length, width), p=[0.8, 0.2])
        else:
            self.visible_board = np.random.choice([0, MINE], size=(length, width), p=[0.75, 0.25])

        self.populate_counts()
        self.populate_game_board()

    def populate_counts(self):
        self.count_corners()
        self.count_edges()
        self.count_rest()

    def count_corners(self):
        if self.visible_board[0,0] != MINE:
            count = 0
            count += 1 if self.visible_board[0,1] == MINE else 0
            count += 1 if self.visible_board[1,0] == MINE else 0
            count += 1 if self.visible_board[1,1] == MINE else 0
            self.visible_board[0,0] = count
        if self.visible_board[0,self.width - 1] != MINE:
            count = 0
            count += 1 if self.visible_board[0, self.width - 2] == MINE else 0
            count += 1 if self.visible_board[1, self.width - 1] == MINE else 0
            count += 1 if self.visible_board[1, self.width - 2] == MINE else 0
            self.visible_board[0,self.width - 1] = count
        if self.visible_board[self.length - 1,0] != MINE:
            count = 0
            count += 1 if self.visible_board[self.length -1, 1] == MINE else 0
            count += 1 if self.visible_board[self.length - 2, 0] == MINE else 0
            count += 1 if self.visible_board[self.length - 2, 1] == MINE else 0
            self.visible_board[self.length - 1,0] = count
        if self.visible_board[self.length - 1, self.width - 1] != MINE:
            count = 0
            count += 1 if self.visible_board[self.length -1, self.width - 2] == MINE else 0
            count += 1 if self.visible_board[self.length - 2, self.width - 1] == MINE else 0
            count += 1 if self.visible_board[self.length - 2, self.width - 2] == MINE else 0
            self.visible_board[self.length - 1, self.width - 1] = count

    def count_edges(self):
        for i in range(1, self.width-1):
            if self.visible_board[0, i] != MINE:
                count = 0
                count += 1 if self.visible_board[0, i-1] == MINE else 0
                count += 1 if self.visible_board[0, i+1] == MINE else 0
                count += 1 if self.visible_board[1, i] == MINE else 0
                count += 1 if self.visible_board[1, i-1] == MINE else 0
                count += 1 if self.visible_board[1, i+1] == MINE else 0
                self.visible_board[0,i] = count

        for i in range(1, self.width-1):
            if self.visible_board[self.length-1, i] != MINE:
                count = 0
                count += 1 if self.visible_board[self.length-1, i-1] == MINE else 0
                count += 1 if self.visible_board[self.length-1, i+1] == MINE else 0
                count += 1 if self.visible_board[self.length-2, i] == MINE else 0
                count += 1 if self.visible_board[self.length-2, i-1] == MINE else 0
                count += 1 if self.visible_board[self.length-2, i+1] == MINE else 0
                self.visible_board[self.length-1,i] = count

        for i in range(1, self.length-1):
            if self.visible_board[i, 0] != MINE:
                count = 0
                count += 1 if self.visible_board[i-1, 0] == MINE else 0
                count += 1 if self.visible_board[i+1, 0] == MINE else 0
                count += 1 if self.visible_board[i, 1] == MINE else 0
                count += 1 if self.visible_board[i-1, 1] == MINE else 0
                count += 1 if self.visible_board[i+1, 1] == MINE else 0
                self.visible_board[i,0] = count

        for i in range(1, self.length-1):
            if self.visible_board[i, self.width-1] != MINE:
                count = 0
                count += 1 if self.visible_board[i-1, self.width-1] == MINE else 0
                count += 1 if self.visible_board[i+1, self.width-1] == MINE else 0
                count += 1 if self.visible_board[i, self.width-2] == MINE else 0
                count += 1 if self.visible_board[i-1, self.width-2] == MINE else 0
                count += 1 if self.visible_board[i+1, self.width-2] == MINE else 0
                self.visible_board[i, self.width-1] = count

    def count_rest(self):
        for i in range(1, self.length-1):
            for j in range(1, self.width-1):
                if self.visible_board[i,j] != MINE:
                    count = 0 
                    count += 1 if self.visible_board[i-1, j] == MINE else 0
                    count += 1 if self.visible_board[i-1, j+1] == MINE else 0
                    count += 1 if self.visible_board[i-1, j-1] == MINE else 0
                    count += 1 if self.visible_board[i, j+1] == MINE else 0
                    count += 1 if self.visible_board[i, j-1] == MINE else 0
                    count += 1 if self.visible_board[i+1, j] == MINE else 0
                    count += 1 if self.visible_board[i+1, j-1] == MINE else 0
                    count += 1 if self.visible_board[i+1, j+1] == MINE else 0
                    self.visible_board[i,j] = count

    def populate_game_board(self):
        for i in range(self.length):
            for j in range(self.width):
                self.game_board[i,j] = '?'

    def get_visible_visible_board(self):
        return self.visible_board
    
    def get_state(self):
        return self.game_board
    
    def action_dig_for_bomb(self, x: int, y: int) -> bool:
        if x < 0 or x >= self.length or y < 0 or y >= self.width:
            raise InvalidMoveException
        
        if self.visible_board[x,y] == MINE:
            self.game_board[x,y] = "X"
            return True

        if self.visible_board[x,y] == 0:
            self.game_board[x,y] = "_"
            self.recursively_reveal(x,y)
        else:
            self.game_board[x,y] = self.visible_board[x,y]

        return False

    def recursively_reveal(self, x: int, y: int):
        print(f"recurssively looking at ({x}, {y})")
        if x > 0 and self.visible_board[x-1, y] == 0 and self.game_board[x-1,y] != "_":
            self.game_board[x-1,y] = "_"
            self.recursively_reveal(x-1, y)
        else:
            self.game_board[x-1, y] = self.visible_board[x-1, y] if self.game_board[x-1,y] != "_" else "_"

        if x > 0 and y < self.width-1 and self.visible_board[x-1, y+1] == 0 and self.game_board[x-1,y+1] != "_":
            self.game_board[x-1,y+1] = "_"
            self.recursively_reveal(x-1, y+1)
        else:
            self.game_board[x-1, y+1] = self.visible_board[x-1, y+1] if self.game_board[x-1,y+1] != "_" else "_"

        if x > 0 and y > 0 and self.visible_board[x-1, y-1] == 0 and self.game_board[x-1, y-1] != "_":
            self.game_board[x-1,y-1] = "_"
            self.recursively_reveal(x-1, y-1)
        else:
            self.game_board[x-1, y-1] = self.visible_board[x-1, y-1] if self.game_board[x-1,y-1] != "_" else "_"

        if y < self.width-1 and self.visible_board[x, y+1] == 0 and self.game_board[x, y+1] != "_":
            self.game_board[x,y+1] = "_"
            self.recursively_reveal(x, y+1)
        else:
            self.game_board[x, y+1] = self.visible_board[x, y+1] if self.game_board[x,y+1] != "_" else "_"

        if y > 0 and self.visible_board[x, y-1] == 0 and self.game_board[x, y-1] != "_":
            self.game_board[x,y-1] = "_"
            self.recursively_reveal(x, y-1)
        else:
            self.game_board[x, y-1] = self.visible_board[x, y-1] if self.game_board[x,y-1] != "_" else "_"

        if x < self.length-1 and self.visible_board[x+1, y] == 0 and self.game_board[x+1, y] != "_":
            self.game_board[x+1,y] = "_"
            self.recursively_reveal(x+1, y)
        else:
            self.game_board[x+1, y] = self.visible_board[x+1, y] if self.game_board[x+1,y] != "_" else "_"

        if x < self.length-1 and y < self.width-1 and self.visible_board[x+1, y+1] == 0 and self.game_board[x+1, y+1] != "_":
            self.game_board[x+1,y+1] = "_"
            self.recursively_reveal(x+1, y+1)
        else:
            self.game_board[x+1, y+1] = self.visible_board[x+1, y+1] if self.game_board[x+1,y+1] != "_" else "_"

        if x < self.length-1 and y > 0 and self.visible_board[x+1, y-1] == 0 and self.game_board[x+1, y-1] != "_":
            self.game_board[x+1,y-1] = "_"
            self.recursively_reveal(x+1, y-1)
        else:
            self.game_board[x+1, y-1] = self.visible_board[x+1, y-1] if self.game_board[x+1,y-1] != "_" else "_"
 
    def place_flag(self, x: int, y: int):
        self.game_board[x,y] = 'F'
