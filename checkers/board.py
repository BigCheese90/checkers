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
        self.turn = RED

    def turnover(self):
        if self.turn == RED:
            self.turn = WHITE
        elif self.turn == WHITE:
            self.turn = RED
        pass


    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)




    def available_moves(self, row, col, hit=False):
        piece = self.get_piece(row, col)
        colour = piece.colour
        if colour != self.turn:
            return []

        if piece == 0:
            print("no piece at position", row, col)
            return

        u = -1 * piece.direction
        moves = []
        if 0 <= col + 1 < 8 and 0 <= row + u < 8:
            if self.board[row + u][col + 1] == 0:
                moves.append([row + u, col + 1])
            elif self.board[row + u][col + 1].colour != colour:
                if 0 <= col + 2 < 8 and 0 <= row + 2*u < 8:
                    if self.board[row + 2*u][col + 2] == 0:
                        moves.append([row + 2*u, col + 2])

        if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
            if self.board[row + u][col - 1] == 0:
                moves.append([row + u, col - 1])

            elif self.board[row + u][col - 1].colour != colour:
                if 0 <= col - 2 < 8 and 0 <= row + 2*u < 8:
                    if self.board[row + 2*u][col - 2] == 0:
                        moves.append([row + 2*u, col - 2])

        if piece.king:
            u = u *-1
            if 0 <= col + 1 < 8 and 0 <= row + u < 8:
                if self.board[row + u][col + 1] == 0:
                    moves.append([row + u, col + 1])
                elif self.board[row + u][col + 1].colour != colour:
                    if 0 <= col + 2 < 8 and 0 <= row + 2*u < 8:
                        if self.board[row + 2*u][col + 2] == 0:
                            moves.append([row + 2*u, col + 2])

            if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
                if self.board[row + u][col - 1] == 0:
                    moves.append([row + u, col - 1])

                elif self.board[row + u][col - 1].colour != colour:
                    if 0 <= col - 2 < 8 and 0 <= row + 2*u < 8:
                        if self.board[row + 2*u][col - 2] == 0:
                            moves.append([row + 2*u, col - 2])

        # if self.board[row + u][col - 1] == 0 and 0 < row + u < 8 and 0 < col - 1 < 8:
        #     moves.append([row + u, col - 1])
        # else:
        #     if self.board[row + 2*u][col - 2] == 0 and 0 < row + 2*u < 8 and 0 < col - 2 < 8:
        #         moves.append([row + 2*u, col - 2])
        # if piece.king:
        #     if self.board[row - u][col + 1] == 0 and 0 < row - u < 8 and 0 < col + 1 < 8:
        #         moves.append([row - u, col + 1])
        #     else:
        #         if self.board[row - 2 * u][col + 2] == 0 and 0 < row - 2*u < 8 and 0 < col - 2 < 8:
        #             moves.append([row - 2 * u, col + 2])
        #     if self.board[row - u][col - 1] == 0 and 0 < row - u < 8 and 0 < col - 1 < 8:
        #         moves.append([row - u, col - 1])
        #     else:
        #         if self.board[row - 2 * u][col - 2] == 0 and 0 < row - 2*u < 8 and 0 < col - 2 < 8:
        #             moves.append([row - 2 * u, col - 2])

        return moves

    def capture(self, row, col):
        self.board[row][col] = 0



    # def select_piece(self, row, col):
    #     piece = self.board[row][col]
    #
    #     if piece != 0:
    #         piece.select()
    #         piece.available_moves = self.available_moves(row, col)
    #         print("available moves are: ", piece.available_moves)
    #         self.selected_piece = piece
    #     return piece

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
