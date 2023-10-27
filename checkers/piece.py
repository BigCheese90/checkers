from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN, BLUE
import pygame

class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = 0
        self.y = 0
        self.selected = False
        self.calc_pos()
        self.available_moves = []


        if self.colour == RED:
            self.direction = 1
        else:
            self.direction = -1


    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        if not self.selected:
            pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        else:
            pygame.draw.circle(win, BLUE, (self.x, self.y), radius + self.OUTLINE + 2)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        if row == 7 or row == 0:
            self.make_king()


    def __repr__(self):
        return str(self.colour)


