import pygame

class Map:
    def __init__(self,width,height):
        self.img = pygame.image.load('Pixel art/map.png').convert()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [0,0]
        self.wall = 10
        self.front_dors_x = (150,196)
        self.front_dors_y = (38,110)
        self.back_dors_y = 462
