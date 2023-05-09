from Circles import Circle
from Xs import X
import pygame

class Board:
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
    
    def add_piece(self):
        pass