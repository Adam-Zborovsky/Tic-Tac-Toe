import pygame
from Boards import Board
from Circles import Circle
from Xs import X
SCREEN_SIZE = (900, 800)


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
    grid = ['', 160, 400, 635]
    pieces = []

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = set_position()
                if pos_x and pos_y:
                    if turn:
                        x = X(grid[pos_x],grid[pos_y])
                        turn -= 1
                    else:
                        x = Circle(grid[pos_x],grid[pos_y])
                        turn += 1
                    board.add_piece(x)
                    x.draw(screen)
            board.check_win()

if __name__ == '__main__':
    game()
