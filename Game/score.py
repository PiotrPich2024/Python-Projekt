import pygame

class Score:
    def __init__(self, pos,width,height,score):
        self.score = score
        self.pos = list(pos)
        self.width = width
        self.height = height

