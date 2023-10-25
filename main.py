import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    piece = board.get_piece(0, 1)
    board.move(piece, 5, 4)
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

                    board.available_moves(x, y, coordinates=True)

                if event.button == 3:
                    if board.selected_piece != None:
                        board.deselect()


                    print("Left mouse button clicked at (x, y):", x, y)
                pass


        board.draw(WIN)
        pygame.display.update()

    pygame.quit()



main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    (print('PyCharm'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
