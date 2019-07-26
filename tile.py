

class Tile:

    def __init__(self):
        self.rep = '.'

    def __str__(self):
        return str(self.rep)


class GameTile(object):

    def __init__(self):
        self.rep = None
        self.piece = []

    def __str__(self):
        self.rep = 'T' if len(self.piece) == 0 else 'P'
        return self.rep

    def put_piece(self, piece):
        self.piece.append(piece)

    def remove_piece(self):
        return self.piece.pop()
