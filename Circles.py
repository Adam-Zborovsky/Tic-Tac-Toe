from Pieces import Piece
import pygame
import time

class Circle(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        i = 0
        while i < 95.1:
            pygame.display.update()    
            pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), 1 + i - 15.01)
            pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 1 + i, width = 15)
            i += 0.1