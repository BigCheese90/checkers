import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, HEIGHT, WIDTH
from .board import Board
class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def _init(self):
        self. selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select_piece(self, x, y):
        self.board.select_piece(x, y)
        return self.board

    def reset(self):
        self._init()
        pass