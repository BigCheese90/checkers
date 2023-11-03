import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, HEIGHT, WIDTH
from .board import Board
import random



class Game:
    def __init__(self,win):
        self._init()
        self.win = win
        self.selected = None

    def _init(self):
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select_piece(self, row, col):
        piece = self.board.board[row][col]
        if piece != 0:
            piece.select()
            self.selected = piece
            piece.available_moves = self.board.available_moves(row, col)
            print("available moves are: ", piece.available_moves)
        return

    def deselect(self):
        piece = self.selected
        piece.deselect()
        self.selected = None

    def reset(self):
        self._init()

    def move(self,row, col):
        if self.selected != (0 or None):
            piece = self.selected
            if [row, col] in piece.available_moves:
                print("Move starts at ", piece.row, piece.col)

                if abs(row - piece.row) == 2:
                    self.board.move(self.selected, row, col)
                    piece.available_moves = self.available_moves(row, col, hit=True)
                    if piece.available_moves == []:
                        self.change_turn()
                        self.deselect()
                else:
                    self.board.move(self.selected, row, col)
                    self.change_turn()
                    self.deselect()

            else:
                print("move impossible")


    def capture(self, row, col):
        self.board.capture(row,col)

    def change_turn(self):
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED
        print("it is ", self.turn, " turn now")


    def available_moves(self, row, col, hit=False):
        piece = self.board.get_piece(row, col)
        colour = piece.colour

        if colour != self.turn:
            return []
        if piece == 0:
            print("no piece at position", row, col)
            return

        u = -1 * piece.direction
        moves = []

        board = self.board.board

        if 0 <= col + 1 < 8 and 0 <= row + u < 8:
            if board[row + u][col + 1] == 0:
                if hit == False:
                    moves.append([row + u, col + 1])
            elif board[row + u][col + 1].colour != colour:
                if 0 <= col + 2 < 8 and 0 <= row + 2*u < 8:
                    if board[row + 2*u][col + 2] == 0:
                        moves.append([row + 2*u, col + 2])

        if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
            if board[row + u][col - 1] == 0:
                if hit == False:
                    moves.append([row + u, col - 1])

            elif board[row + u][col - 1].colour != colour:
                if 0 <= col - 2 < 8 and 0 <= row + 2*u < 8:
                    if board[row + 2*u][col - 2] == 0:
                        moves.append([row + 2*u, col - 2])

        if piece.king:
            u = u *-1
            if 0 <= col + 1 < 8 and 0 <= row + u < 8:
                if board[row + u][col + 1] == 0:
                    if hit == False:
                        moves.append([row + u, col + 1])
                elif board[row + u][col + 1].colour != colour:
                    if 0 <= col + 2 < 8 and 0 <= row + 2*u < 8:
                        if board[row + 2*u][col + 2] == 0:
                            moves.append([row + 2*u, col + 2])

            if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
                if board[row + u][col - 1] == 0:
                    if hit == False:
                        moves.append([row + u, col - 1])
                elif board[row + u][col - 1].colour != colour:
                    if 0 <= col - 2 < 8 and 0 <= row + 2*u < 8:
                        if board[row + 2*u][col - 2] == 0:
                            moves.append([row + 2*u, col - 2])

        return moves



    def dict_of_moves(self):
        list = []
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.colour == self.turn and self.available_moves(piece.row, piece.col) != []:
                        list.append(piece)#, self.available_moves(piece.row, piece.col)])
        return list

    def select_random_piece(self, dict_of_moves):
        piece = random.choice(list_of_pieces)
        self.select_piece(piece.row, piece.col)
        move = random.choice(piece.available_moves)
        self.move(move[0], move[1])


