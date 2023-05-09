import pygame
from Boards import Board
from Os import O
from Xs import X
SCREEN_SIZE = (800, 800)


def set_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if 50 < mouse_x < 275 and 50 < mouse_y < 275:
        return (1,1)
    if 290 < mouse_x < 510 and 50 < mouse_y < 275:
        return (2,1)
    if 525 < mouse_x < 750 and 50 < mouse_y < 275:
        return (3,1)
    if 50 < mouse_x < 275 and 290 < mouse_y < 510:
        return (1,2)
    if 290 < mouse_x < 510 and 290 < mouse_y < 510:
        return (2,2)
    if 525 < mouse_x < 750 and 290 < mouse_y < 510:
        return (3,2)
    if 50 < mouse_x < 275 and 525 < mouse_y < 750:
        return (1,3)
    if 290 < mouse_x < 510 and 525 < mouse_y < 750:
        return (2,3)
    if 525 < mouse_x < 750 and 525 < mouse_y < 750:
        return (3,3)
    else:
        return None


def game():
    running = True
    turn = 0
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Tic Tac Toe')
    screen.fill((0, 0, 0))
    pygame.display.flip()
    board = Board()
    board.draw(screen)

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = set_position()
                if pos_x is not None and pos_y is not None:
                    if turn%2 == 1:
                        x = X(pos_x,pos_y)
                    else:
                        x = O(pos_x,pos_y)
                    if board.add_piece(x, screen):
                        turn += 1
                        x.draw(screen)

if __name__ == '__main__':
    game()
