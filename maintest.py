import pygame
from checkers.constants import WIDTH, HEIGHT, RED, WHITE
from checkers.board import Board
from checkers.game import Game
from checkers.constants import transform_x_y
from checkers.algorithm import *


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FPS = 60

game = Game(WIN)
board = game.board

def main():
    run = True
    clock = pygame.time.Clock()

    i=0


    while run:
        clock.tick(FPS//2)
        if game.board.turn == RED:
            best_move = minmax(board)
            print(best_move)
            #board.move(board.board[5][0], 4, 1)
            board.move(board.get_piece(best_move[0][0], best_move[0][1]), best_move[1], best_move[2])
            #game.change_turn()
            pass
        else:
            best_move = minmax(board)
            print(best_move)
            #board.move(board.board[5][0], 4, 1)
            board.move(board.get_piece(best_move[0][0], best_move[0][1]), best_move[1], best_move[2])
            #game.change_turn()
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                row, col = transform_x_y(x, y)

                if event.button == 1:  # Left mouse button
                    if game.selected == None:
                        game.select_piece(row, col)
                    else:
                        game.move(row, col)

                if event.button == 2:
                    board.capture(row, col)

                if event.button == 3:
                    print("deselect")
                    if game.selected != None:
                        game.deselect()



                    print("Left mouse button clicked at (x, y):", x, y)
                pass


        game.update()

    pygame.quit()



main()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    (print('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
