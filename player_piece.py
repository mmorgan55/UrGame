class PlayerPiece(object):
    def __init__(self, start):
        self.moves = [(3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 0), (5, 0), (6, 1), (7, 1),
                      (7, 0), (6, 0)]
        self.currentSpot = start

        self.row, self.col = self.moves[self.currentSpot]
        self.last_row = None
        self.last_col = None

    def move(self, num):
        self.last_row, self.last_col = self.moves[self.currentSpot]
        self.currentSpot += num
        self.row, self.col = self.moves[self.currentSpot]
