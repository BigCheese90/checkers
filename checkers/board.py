import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, HEIGHT, WIDTH
from .piece import Piece
from icecream import ic

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col, coordinates=False):
        if coordinates:
            row = row // (HEIGHT // ROWS)
            col = col // (WIDTH // COLS)
            row, col = col, row
        print([row, col])
        print(piece.available_moves)
        if [row, col] in piece.available_moves:
            print("yeah", row, piece.row)
            if row - piece.row == 2:
                ic("kill", (row - piece.row) // 2, (col - piece.col) // 2)

                self.capture((row + piece.row) // 2, (col + piece.col) // 2)

            self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
            piece.available_moves = self.available_moves(row, col)
            piece.move(row, col)
        else:
            print("move impossible")
        # print("coords are: ", col, row)
        # if self.board[row][col] != 0:
        #     print("Move to ", row, col, " not possible: ", "way blocked")
        #
        # elif piece.direction * piece.row <= piece.direction * row and not piece.king:
        #     print("Move to ", row, col, " not possible: ", "wrong direction")
        # elif (row + col) % 2 == 0:
        #     print("Move on red Squares not allowed")
        # elif abs(piece.row - row) > 1 or abs(piece.col - col) > 1:
        #     print("cannot move that far")
        #
        #
        # else:
        #     self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        #     piece.move(row, col)
        #
        # if row == ROWS-1 or row == 0:
        #     piece.make_king()
        #     if piece.colour == WHITE:
        #         self.white_kings += 1
        #     else:
        #         self.red_kings += 1

    def available_moves(self, row, col, coordinates = False):

        if coordinates == True:
            row = row // (HEIGHT // ROWS)
            col = col // (WIDTH // COLS)
            row, col = col, row
        piece = self.get_piece(row, col)
        if piece == 0:
            print("no piece at position", row, col)
            return
        moves = []
        u = -1 * piece.direction

        if self.board[row + u][col + 1] == 0 and 0 < row + u < 8 and 0 < col + 1 < 8:
            moves.append([row + u, col + 1])
        else:
            if self.board[row + 2*u][col + 2] == 0 and 0 < row + 2*u < 8 and 0 < col + 2 < 8:
                moves.append([row + 2*u, col + 2])
        if self.board[row + u][col - 1] == 0 and 0 < row + u < 8 and 0 < col - 1 < 8:
            moves.append([row + u, col - 1])
        else:
            if self.board[row + 2*u][col - 2] == 0 and 0 < row + 2*u < 8 and 0 < col - 2 < 8:
                moves.append([row + 2*u, col - 2])
        if piece.king:
            if self.board[row - u][col + 1] == 0 and 0 < row - u < 8 and 0 < col + 1 < 8:
                moves.append([row - u, col + 1])
            else:
                if self.board[row - 2 * u][col + 2] == 0 and 0 < row - 2*u < 8 and 0 < col - 2 < 8:
                    moves.append([row - 2 * u, col + 2])
            if self.board[row - u][col - 1] == 0 and 0 < row - u < 8 and 0 < col - 1 < 8:
                moves.append([row - u, col - 1])
            else:
                if self.board[row - 2 * u][col - 2] == 0 and 0 < row - 2*u < 8 and 0 < col - 2 < 8:
                    moves.append([row - 2 * u, col - 2])

        return moves

    def capture(self, row, col, coordinates=False):
        # if coordinates:
        #     row = row // (HEIGHT // ROWS)
        #     col = col // (WIDTH // COLS)
        #     row, col = col, row
        self.board[row][col] = 0

    def deselect(self):
        piece = self.selected_piece
        piece.deselect()
        self.selected_piece = None

    def select_piece(self, x, y):
        col = x // (HEIGHT // ROWS)
        row = y // (WIDTH // COLS)
        print(row , col, self.board[row][col])
        piece = self.board[row][col]

        if piece != 0:
            piece.select()
            piece.available_moves = self.available_moves(row, col)
            print("available moves are: ", piece.available_moves)
            self.selected_piece = piece
        return piece

    def get_piece(self, row,col):
        return self.board[row][col]


    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)


    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
