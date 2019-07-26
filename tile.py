import pygame


class Tile:

    def __init__(self):
        self.rep = '.'

    def __str__(self):
        return str(self.rep)


class GameTile:

    def __init__(self):
        self.rep = 'T'

    def __str__(self):
        return str(self.rep)
