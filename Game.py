import pygame
import time
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
        return (0,0)


def game():
    running = True
    turn = 1
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
                    win = board.add_piece(x, screen)
                    if win:
                        print(win)
                        turn += 1
                        x.draw(screen)
                        if win is not True and (win[0] == 'X' or win[0] == 'O' or win[0] == 'tie'):
                            print('here')
                            time.sleep(1)
                            grid = ['', 160, 400, 635]
                            start, end, width = (grid[win[0][1].get_location()[0]], grid[win[0][1].get_location()[1]]), (grid[win[2][1].get_location()[0]], grid[win[2][1].get_location()[1]]), 40
                            pygame.draw.line(screen, (255, 255, 255), start, end, width)
                            pygame.draw.circle(screen, (255, 255, 255), (start[0], start[1]), width//2)
                            pygame.draw.circle(screen, (255, 255, 255), (end[0], end[1]), width//2)
                            screen.fill((0, 0, 0))
                            pygame.display.flip()
                            eval(f'board.{win[0]}(screen)')
                            time.sleep(2)
                            screen.fill((0, 0, 0))
                            pygame.display.flip()
                            board = Board()
                            board.draw(screen)


if __name__ == '__main__':
    game()
