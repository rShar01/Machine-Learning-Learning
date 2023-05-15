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

        if difficulty is None or difficulty not in DIFFICULTIES:
            raise InvalidConfigException
        elif difficulty == "easy":
            self.board = np.random.choice([0, MINE], size=(length, width), p=[0.85, 0.15])
        elif difficulty == "medium":
            self.board = np.random.choice([0, MINE], size=(length, width), p=[0.8, 0.2])
        else:
            self.board = np.random.choice([0, MINE], size=(length, width), p=[0.75, 0.25])

        self.populate_counts()

    def populate_counts(self):
        self.count_corners()
        self.count_edges()
        self.count_rest()

    def count_corners(self):
        if self.board[0,0] != MINE:
            count = 0
            count += 1 if self.board[0,1] == MINE else 0
            count += 1 if self.board[1,0] == MINE else 0
            count += 1 if self.board[1,1] == MINE else 0
            self.board[0,0] = count
        if self.board[0,self.width - 1] != MINE:
            count = 0
            count += 1 if self.board[0, self.width - 2] == MINE else 0
            count += 1 if self.board[1, self.width - 1] == MINE else 0
            count += 1 if self.board[1, self.width - 2] == MINE else 0
            self.board[0,self.width - 1] = count
        if self.board[self.length - 1,0] != MINE:
            count = 0
            count += 1 if self.board[self.length -1, 1] == MINE else 0
            count += 1 if self.board[self.length - 2, 0] == MINE else 0
            count += 1 if self.board[self.length - 2, 1] == MINE else 0
            self.board[self.length - 1,0] = count
        if self.board[self.length - 1, self.width - 1] != MINE:
            count = 0
            count += 1 if self.board[self.length -1, self.width - 2] == MINE else 0
            count += 1 if self.board[self.length - 2, self.width - 1] == MINE else 0
            count += 1 if self.board[self.length - 2, self.width - 2] == MINE else 0
            self.board[self.length - 1, self.width - 1] = count

    def count_edges(self):
        for i in range(1, self.width-1):
            if self.board[0, i] != MINE:
                count = 0
                count += 1 if self.board[0, i-1] == MINE else 0
                count += 1 if self.board[0, i+1] == MINE else 0
                count += 1 if self.board[1, i] == MINE else 0
                count += 1 if self.board[1, i-1] == MINE else 0
                count += 1 if self.board[1, i+1] == MINE else 0
                self.board[0,i] = count

        for i in range(1, self.width-1):
            if self.board[self.length-1, i] != MINE:
                count = 0
                count += 1 if self.board[self.length-1, i-1] == MINE else 0
                count += 1 if self.board[self.length-1, i+1] == MINE else 0
                count += 1 if self.board[self.length-2, i] == MINE else 0
                count += 1 if self.board[self.length-2, i-1] == MINE else 0
                count += 1 if self.board[self.length-2, i+1] == MINE else 0
                self.board[self.length-1,i] = count

        for i in range(1, self.length-1):
            if self.board[i, 0] != MINE:
                count = 0
                count += 1 if self.board[i-1, 0] == MINE else 0
                count += 1 if self.board[i+1, 0] == MINE else 0
                count += 1 if self.board[i, 1] == MINE else 0
                count += 1 if self.board[i-1, 1] == MINE else 0
                count += 1 if self.board[i+1, 1] == MINE else 0
                self.board[i,0] = count

        for i in range(1, self.length-1):
            if self.board[i, self.width-1] != MINE:
                count = 0
                count += 1 if self.board[i-1, self.width-1] == MINE else 0
                count += 1 if self.board[i+1, self.width-1] == MINE else 0
                count += 1 if self.board[i, self.width-2] == MINE else 0
                count += 1 if self.board[i-1, self.width-2] == MINE else 0
                count += 1 if self.board[i+1, self.width-2] == MINE else 0
                self.board[i, self.width-1] = count

    def count_rest(self):
        for i in range(1, self.length-1):
            for j in range(1, self.width-1):
                if self.board[i,j] != MINE:
                    count = 0 
                    count += 1 if self.board[i-1, j] == MINE else 0
                    count += 1 if self.board[i-1, j+1] == MINE else 0
                    count += 1 if self.board[i-1, j-1] == MINE else 0
                    count += 1 if self.board[i, j+1] == MINE else 0
                    count += 1 if self.board[i, j-1] == MINE else 0
                    count += 1 if self.board[i+1, j] == MINE else 0
                    count += 1 if self.board[i+1, j-1] == MINE else 0
                    count += 1 if self.board[i+1, j+1] == MINE else 0
                    self.board[i,j] = count


    def get_board(self):
        return self.board
