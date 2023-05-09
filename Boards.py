import pygame


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
            self.tie(screen)
        self.pieces.append(piece)
        for p in self.pieces:
            for i, pos in enumerate(self.grid):
                if p.get_location() == pos:
                    self.grid[i] = str(p)
        if self.check_win():
            self.win(screen)

        return True
    
    def check_win(self):
        rows, cols , diag = [], [], [(self.grid[0], self.grid[4], self.grid[8]), (self.grid[6], self.grid[4], self.grid[2])] 
        
        for i in range(len(self.grid)):
            if (i+1)%3 == 0: 
                rows.append((self.grid[i-2], self.grid[i-1], self.grid[i]))
        for i in range(3):
            cols.append((self.grid[i], self.grid[i+3], self.grid[i+6]))

        for row in rows:
            if row[0] == row[1] == row[2]:
                return True 
        for col in cols:
            if col[0] == col[1] == col[2]:
                return True
        for dia in diag:
            if dia[0] == dia[1] == dia[2]:
                return True
        return False
        
    def win(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), (400, 400), 400)

    def tie(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (400, 400), 400)
