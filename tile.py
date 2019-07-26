import pygame


class Tile:

    def __init__(self):
        self.piece = None
        self.rep = 'T'

    def __str__(self):
        return self.rep
