import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, HEIGHT, WIDTH
from .piece import Piece
from icecream import ic
from typing import Dict, Any, Union, List


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()
        self.turn = RED
        self.last_action = "Move"

    def turnover(self):
        if self.turn == RED:
            self.turn = WHITE
        elif self.turn == WHITE:
            self.turn = RED
        pass

    def check_game_state(self):
        return self.red_left + self.red_kings - self.white_left - self.white_kings

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        print("move ", piece, "to" , row, col)
        if abs(row - piece.row) == 2:
            self.capture((row + piece.row) // 2, (col + piece.col) // 2)
            piece.move(row, col)
            piece.available_moves = self.available_captures(row, col)
            if piece.available_moves == []:
                self.turnover()
                self.last_action = "Move"
            else:
                self.last_action = piece
        else:
            piece.move(row, col)
            self.turnover()
        if (row == 7 or row == 0) and piece.king == False:
            piece.make_king()
            if piece.colour == RED:
                self.red_kings = self.red_kings + 1

            if piece.colour == WHITE:
                self.white_kings = self.white_kings + 1


    def get_pieces(self):
        piece_list = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.colour == self.turn:
                    piece_list.append(piece)
        return piece_list

    def dict_of_moves(self):
        dict_of_moves = {}
        for row in self.board:
            for piece in row:
                if piece != 0:
                    if piece.colour == self.turn and self.available_moves(piece.row, piece.col) != []:
                        dict_of_moves[piece] = self.available_moves(piece.row, piece.col)

        return dict_of_moves

    def list_of_moves(self):
        list_of_moves = []
        if self.last_action != "Move":
            piece = self.last_action
            moves = self.available_moves(piece.row, piece.col)
            if piece.colour == self.turn and moves != []:
                for i in moves:
                    list_of_moves.append([[piece.row, piece.col], i])
            return list_of_moves

        for row in self.board:
            for piece in row:
                if piece != 0:
                    moves = self.available_moves(piece.row, piece.col)
                    if piece.colour == self.turn and moves != []:
                        for i in moves:
                            list_of_moves.append([[piece.row, piece.col], i])

        return list_of_moves

    def available_moves(self, row, col):
        piece = self.get_piece(row, col)
        if piece == self.last_action:
            return piece.available_moves
        try:
            colour = piece.colour
        except:
            print("error")
            print(piece, row, col)
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
                if 0 <= col + 2 < 8 and 0 <= row + 2 * u < 8:
                    if self.board[row + 2 * u][col + 2] == 0:
                        moves.append([row + 2 * u, col + 2])

        if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
            if self.board[row + u][col - 1] == 0:
                moves.append([row + u, col - 1])

            elif self.board[row + u][col - 1].colour != colour:
                if 0 <= col - 2 < 8 and 0 <= row + 2 * u < 8:
                    if self.board[row + 2 * u][col - 2] == 0:
                        moves.append([row + 2 * u, col - 2])

        if piece.king:
            u = u * -1
            if 0 <= col + 1 < 8 and 0 <= row + u < 8:
                if self.board[row + u][col + 1] == 0:
                    moves.append([row + u, col + 1])
                elif self.board[row + u][col + 1].colour != colour:
                    if 0 <= col + 2 < 8 and 0 <= row + 2 * u < 8:
                        if self.board[row + 2 * u][col + 2] == 0:
                            moves.append([row + 2 * u, col + 2])

            if 0 <= col - 1 <= 8 and 0 <= row + u < 8:
                if self.board[row + u][col - 1] == 0:
                    moves.append([row + u, col - 1])

                elif self.board[row + u][col - 1].colour != colour:
                    if 0 <= col - 2 < 8 and 0 <= row + 2 * u < 8:
                        if self.board[row + 2 * u][col - 2] == 0:
                            moves.append([row + 2 * u, col - 2])

        return moves

    def available_captures(self, row, col):
        piece = self.get_piece(row, col)
        colour = piece.colour
        u = -1 * piece.direction
        moves = []
        if 0 <= col + 2 < 8 and 0 <= row + 2 * u < 8 and self.board[row + 2 * u][col + 2] == 0:
            if self.board[row + u][col + 1] != 0 and self.board[row + u][col + 1].colour != colour:
                moves.append([row + 2*u, col +2])

        if 0 <= col - 2 < 8 and 0 <= row + 2 * u < 8 and self.board[row + 2 * u][col - 2] == 0:
            if self.board[row + u][col - 1] != 0 and self.board[row + u][col - 1].colour != colour:
                moves.append([row + 2 * u, col - 2])

        if not piece.king:
            return moves

        u = u*-1
        if 0 <= col + 2 < 8 and 0 <= row + 2 * u < 8 and self.board[row + 2 * u][col + 2] == 0:
            if self.board[row + u][col + 1] != 0 and self.board[row + u][col + 1].colour != colour:
                moves.append([row + 2*u, col +2])

        if 0 <= col - 2 < 8 and 0 <= row + 2 * u < 8 and self.board[row + 2 * u][col - 2] == 0:
            if self.board[row + u][col - 1] != 0 and self.board[row + u][col - 1].colour != colour:
                moves.append([row + 2 * u, col - 2])

        return moves


    def capture(self, row, col):
        piece = self.board[row][col]
        if piece.colour == RED:
            self.red_left = self.red_left - 1
            if piece.king:
                self.red_kings = self.red_kings - 1
        if piece.colour == WHITE:
            self.white_left = self.white_left - 1
            if piece.king:
                self.white_kings = self.white_kings - 1

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

    def get_piece(self, row, col):
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
