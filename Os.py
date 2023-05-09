from Pieces import Piece
import pygame

class O(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen):
        grid = ['', 160, 400, 635]
        point = grid[self.x], grid [self.y]
        i = 0
        while i < 95.1:
            pygame.display.update()    
            pygame.draw.circle(screen, (0, 0, 0), point, 1 + i - 15.01)
            pygame.draw.circle(screen, (255, 255, 255), point, 1 + i, width = 15)
            i += 0.1
            