import player_piece


class Tile:

    def __init__(self):
        self.rep = '.'

    def __str__(self):
        return str(self.rep)


class GameTile:

    def __init__(self, tag):
        self.rep = 'T'
        self.tag = tag
        self.piece = []

    def __str__(self):
        return str(self.rep)

    def get_piece(self, piece):
        self.piece.append(piece)

    def remove_piece(self):
        return self.piece.pop()
