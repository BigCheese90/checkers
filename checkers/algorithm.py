import pygame
from copy import deepcopy
import random
from .constants import WHITE, RED

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

def findmax(board, start, move, colour, n):
    print("move is ", start, move)
    board = deepcopy(board)
    board.move(board.board[start[0]][start[1]], move[0], move[1])
    print("available moves are :", board.list_of_moves())
    available_moves = board.list_of_moves()
    random.shuffle(available_moves)
    print("shuffled moves are :", available_moves)
    #available_moves = random.shuffle(available_moves)
    list_of_states = []
    for moves in available_moves:
        start = moves[0]
        end = moves[1]
        tempboard = deepcopy(board)
        print("start:",start)
        print("end", end)
        tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
        list_of_states.append(tempboard.check_game_state())
    if colour == RED:
        best_move = max(list_of_states)
    else:
        print("lol")
        best_move = min(list_of_states)

    return best_move

def minmax(input_board):
    turn = input_board.turn
    board = deepcopy(input_board)
    possible_moves = board.list_of_moves()
    best_piece = []
    best_move = []
    state = -1000
    random.shuffle(possible_moves)
    for move in possible_moves:
        piece_row, piece_col = move[0][0], move[0][1]
        newstate = findmax(board, [piece_row, piece_col], move[1], turn)
        if turn == WHITE:
            newstate = newstate*-1
        if newstate > state:
            state = newstate
            best_piece = [piece_row, piece_col]
            best_move = move[1]
        board = deepcopy(input_board)

    # for piece, moves in possible_moves.items():
    #     for move in moves:
    #         piece_row, piece_col = piece.row, piece.col
    #         newstate = findmax(board, [piece.row, piece.col], move, turn)
    #         if turn == WHITE:
    #             newstate = newstate*-1
    #         if newstate > state:
    #             state = newstate
    #             best_piece = [piece_row, piece_col]
    #             best_move = move
    #         board = deepcopy(input_board)

    print("best move is ", best_piece, best_move[0], best_move[1])
    return [best_piece, best_move[0], best_move[1]]




def find_opponent_move(board):
    available_moves = board.list_of_moves()
    if board.turn == WHITE:
        maxEval = float("inf")
        best_board = board
        for move in available_moves:
            start = move[0]
            end = move[1]
            tempboard = deepcopy(board)
            tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
            game_state = tempboard.check_game_state()
            if game_state < maxEval:
                best_board = tempboard

    else:
        maxEval = float("-inf")
        best_board = board
        for move in available_moves:
            start = move[0]
            end = move[1]
            tempboard = deepcopy(board)
            tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
            game_state = tempboard.check_game_state()
            if game_state > maxEval:
                best_board = tempboard

    return best_board


def findmax_two(board, n=0):

    if board.turn == RED:
        available_moves = board.list_of_moves()
        list_of_states = []
        maxEval = float("-inf")
        best_move = None

        for moves in available_moves:
            start = moves[0]
            end = moves[1]
            tempboard = deepcopy(board)
            tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])


            if n > 0:
                best_move, game_state = findmax_two(tempboard, n-1)
            else:
                game_state = tempboard.check_game_state()

            if game_state > maxEval:
                best_move = moves
                maxEval = game_state
                print(game_state, best_move)
        return best_move, maxEval


def minimax_red(board, n=0, maxEval = float("-inf")):

    available_moves = board.list_of_moves()
    best_move = None
    best_score = float("-inf")
    for move in available_moves:
        start = move[0]
        end = move[1]
        tempboard = deepcopy(board)
        tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
        while True:
            tempboard = find_opponent_move(tempboard)
            if tempboard.turn == RED:
                break

        if n == 0:
            game_state = tempboard.check_game_state()
            if game_state > maxEval:
                maxEval = game_state
                best_move = move

            #print(game_state)

        else:
            maxEval, best_moves = minimax_red(tempboard, n-1, maxEval)
            # print("score: ", maxEval)
            # print("move: ", move)
            if maxEval > best_score:
                best_score = maxEval
                best_move = move


    return maxEval, best_move

def minimax_white(board, n=0, maxEval = float("+inf")):

    available_moves = board.list_of_moves()
    best_move = None
    best_score = float("+inf")
    for move in available_moves:
        start = move[0]
        end = move[1]
        tempboard = deepcopy(board)
        tempboard.move(tempboard.board[start[0]][start[1]], end[0], end[1])
        while True:
            tempboard = find_opponent_move(tempboard)
            if tempboard.turn == WHITE:
                break

        if n == 0:
            game_state = tempboard.check_game_state()
            if game_state < maxEval:
                maxEval = game_state
                best_move = move

            #print(game_state)

        else:
            maxEval, best_moves = minimax_white(tempboard, n-1, maxEval)
            # print("score: ", maxEval)
            # print("move: ", move)
            if maxEval < best_score:
                best_score = maxEval
                best_move = move


    return maxEval, best_move

#print(find_all_moves(board))

def minimax(board):
    available_moves = board.list_of_moves()