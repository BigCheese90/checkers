import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.game import Game
from checkers.constants import transform_x_y

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

FPS = 60


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)
    board = game.board
    print(game.list_of_moves())

    i=0


    while run:
        clock.tick(FPS)
        i+=1
        if i % 6 == 1:
            game.select_random_piece(game.list_of_moves())

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
