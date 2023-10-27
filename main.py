import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    board = game.board

    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    if board.selected_piece == None:
                        board.select_piece(x, y)
                    else:
                        piece = board.selected_piece
                        board.move(piece, x, y, coordinates=True)
                if event.button == 2:
                    x, y = event.pos

                    board.capture(x, y, coordinates=True)

                if event.button == 3:
                    if board.selected_piece != None:
                        board.deselect()


                    print("Left mouse button clicked at (x, y):", x, y)
                pass


        game.update()

    pygame.quit()



main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    (print('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
