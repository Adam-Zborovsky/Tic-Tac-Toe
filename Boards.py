from Circles import Circle
from Xs import X
import pygame


class Board:
    def __init__(self):
        self.pieces = []

    def draw(self, screen):
        start, end, width = (282.5, 55), (282.5, 745), 15
        for i in range(2):
            pygame.draw.line(screen, (255, 255, 255), start, end, width)
            pygame.draw.circle(screen, (255, 255, 255), (start[0], start[1]), width//2)
            pygame.draw.circle(screen, (255, 255, 255), (end[0], end[1]), width//2)
            start, end = (start[0]+235, start[1]), (end[0]+235, end[1])
        start, end = (55, 282.5), (745, 282.5)
        for i in range(2):
            pygame.draw.line(screen, (255, 255, 255), start, end, width)
            pygame.draw.circle(screen, (255, 255, 255), (start[0], start[1]), width//2)
            pygame.draw.circle(screen, (255, 255, 255), (end[0], end[1]), width//2)
            start, end = (start[0], start[1]+235), (end[0], end[1]+235)
        pygame.display.flip()
    
    def add_piece(self, piece):
        self.pieces.append(piece)

    def check_win(self):
        grid = [(160,160), (400,160), (635,160)
                (160,400), (400,400), (635,400)
                (160,635), (400,635), (635,635)]
        for piece in self.pieces:
            for x, y in grid:
                if piece.get_location() ==  piece.__class__.__name__
            
