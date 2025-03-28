import pygame
from Map import Map
from Player import Player


class GameEngine:
    def __init__(self):
        self.player = Player(64,64,150,150,2)
        self.map = Map(640,480)



