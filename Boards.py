import pygame
import time


class Board:
    def __init__(self):
        self.pieces = []
        self.grid = [(1,1), (2,1), (3,1),
                (1,2), (2,2), (3,2),
                (1,3), (2,3), (3,3)]

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
    
    def add_piece(self, piece, screen):
        if piece.get_location() not in self.grid:
            return False
        if len(self.pieces) == 8:
            return 'tie'
        self.pieces.append(piece)
        for p in self.pieces:
            for i, pos in enumerate(self.grid):
                if p.get_location() == pos:
                    self.grid[i] = (str(p), p)
        
        win = self.check_win()
        if win and not isinstance(win[0][1], int) and not isinstance(win[1][1], int) and not isinstance(win[2][1], int):
            return win

        return True
    
    def check_win(self):
        rows, cols , diag = [], [], [(self.grid[0], self.grid[4], self.grid[8]), (self.grid[6], self.grid[4], self.grid[2])] 
        
        for i in range(len(self.grid)):
            if (i+1)%3 == 0: 
                rows.append((self.grid[i-2], self.grid[i-1], self.grid[i]))
        for i in range(3):
            cols.append((self.grid[i], self.grid[i+3], self.grid[i+6]))

        for row in rows:
            if row[0][0] == row[1][0] == row[2][0]:
                return row
        for col in cols:
            if col[0][0] == col[1][0] == col[2][0]:
                return col
        for dia in diag:
            if dia[0][0] == dia[1][0] == dia[2][0]:
                return dia
        return False
        
    def win(self, screen):
        pygame.font.init()
        screen.blit(pygame.font.SysFont("David", 200).render('O Won', True, (255, 255, 255)), (115, 100))
        pygame.display.update()
        
    def X(self, screen):
        pygame.font.init()
        screen.blit(pygame.font.SysFont("David", 200).render('X Won', True, (255, 255, 255)), (115, 100))
        pygame.display.flip()

    def tie(self, screen):
        pygame.font.init()
        screen.blit(pygame.font.SysFont("David", 200).render('Its a Tie', True, (255, 255, 255)), (100, 100))
        pygame.display.flip()
