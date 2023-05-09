import pygame
from Boards import Board
from Circles import Circle
from Xs import X
SCREEN_SIZE = (900, 800)


def game():
    running = True
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill((0, 0, 0))
    pygame.display.flip()
    board = Board()
    board.draw(screen)
    pieces = []

    x= Circle(160,160)
    x.draw(screen)
    x= X(160,160)
    x.draw(screen)
    



    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.MOUSEBUTTONUP:
                pass


if __name__ == '__main__':
    game()
