import pygame
from math import sqrt

class Snow:
    def __init__(self,pos,width,height,direction,velocity):
        self.pos = list(pos)
        self.width = width
        self.height = height
        self.direction_x = direction[0]
        self.direction_y = direction[1]
        self.velocity = velocity
        self.img = pygame.image.load('../../pixel_art/particles/snow.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(width,height))

        self.max_transparency = 255
        self.min_transparency = 100

        self.transparency = 255
        self.change_speed = 5

        self.multiplier = -1

        c = sqrt(self.direction_x ** 2 + self.direction_y ** 2)
        self.d_x = self.direction_x/c
        self.d_y = self.direction_y/c

    def animate(self):
        self.pos[0] += self.d_x * self.velocity
        self.pos[1] += self.d_y * self.velocity
        self.transparency + self.multiplier * self.change_speed
        if self.max_transparency <= self.transparency <= self.min_transparency:
            self.multiplier *= -1
        self.img.set_alpha(self.transparency)

    def render(self,surf):
        self.animate()
        surf.blit(self.img,self.pos)


