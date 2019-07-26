class PlayerPiece:
    def __init__(self):
        self.moveSquares = [10, 7, 4, 1, 2, 5, 8, 11, 13, 14, 16, 19, 18, 15]
        self.currentSpot = -1

    def move(self, num):
        self.currentSpot += num
        return self.moveSquares[self.currentSpot]
