from Pieces import Piece
import pygame

class X(Piece):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, screen): 
        grid = ['', 160, 400, 635]
        point = grid[self.x], grid [self.y]
        left_start, right_start, width = (point[0]-87.5, point[1]-87.5), (point[0]+87.5, point[1]-87.5), 30
        left_end, right_end = left_start, right_start 
        i = 1
        #120.2
        while i < 175.1:
            pygame.draw.line(screen, (255, 255, 255), left_start, (left_end[0]+i,left_end[1]+i), width)
            pygame.draw.line(screen, (255, 255, 255), right_start, (right_end[0]-i,right_end[1]+i), width)
            pygame.draw.circle(screen, (0, 0, 0), left_start, width//2+1)
            pygame.draw.circle(screen, (0, 0, 0), right_start, width//2+1)
            pygame.draw.circle(screen, (0, 0, 0), (left_end[0]+i,left_end[1]+i), width//2+1)
            pygame.draw.circle(screen, (0, 0, 0), (right_end[0]-i,right_end[1]+i), width//2+1)
            pygame.display.update()  
            i += 0.1
    
