class Piece:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_location(self):
        return self.x, self.y
    
    def set_location(self ,x ,y):
        self.x = x 
        self.y = y

    def __str__(self):
        return self.__class__.__name__