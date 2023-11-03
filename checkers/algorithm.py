import pygame
from copy import deepcopy
import random

def dict_of_moves(game):
    list = []
    for row in game.board.board:
        for piece in row:
            if piece != 0:
                if piece.colour == game.turn and game.available_moves(piece.row, piece.col) != []:
                    list.append({piece: game.available_moves(piece.row, piece.col)})
    return list



def move_random_piece(game, dict_of_moves):
    selection = random.choice(dict_of_moves)
    piece = list(selection.keys())[0]
    move = random.choice(selection[piece])
    game.select_piece(piece.row, piece.col)
    game.move(move[0], move[1])

#red wants to maximise game_state

def findmax(board, start, move):
    print("move is ", start, move)
    tempboard = deepcopy(board)
    tempboard.move(tempboard.board[start[0]][start[1]], move[0], move[1])
    available_moves = tempboard.list_of_moves()
    list_of_states = []
    for moves in available_moves:
        start = moves[0]
        for end in moves[1]:
            print("start:",start)
            print("end", end)
            tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
            list_of_states.append(tempboard.check_game_state())
            tempboard = deepcopy(board)
    return max(list_of_states)

def minmax(input_board):
    board = deepcopy(input_board)
    possible_moves = board.dict_of_moves()
    best_piece = []
    best_move = []
    state = -1000
    for piece, moves in possible_moves.items():
        for move in moves:
            piece_row, piece_col = piece.row, piece.col
            newstate = findmax(board, [piece.row, piece.col], move)
            if newstate>state:
                state = newstate
                best_piece = [piece_row, piece_col]
                best_move = move
            board = deepcopy(input_board)

    print("best move is ", best_piece, best_move[0], best_move[1])
    return [best_piece, best_move[0], best_move[1]]






