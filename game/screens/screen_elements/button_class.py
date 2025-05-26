import pygame

class Button:
    def __init__(self,surf,pos):
        self.width = surf.get_width()
        self.height = surf.get_height()
        self.upperLeft = list(pos)
        self.lowerRight = [pos[0] + self.width, pos[1] + self.height]
        self.surf = surf
        self.pos = pos

    def is_clicked(self,mouse_pos):
        return self.upperLeft[0] <= mouse_pos[0] <= self.lowerRight[0] and self.upperLeft[1] <= mouse_pos[1] <= self.lowerRight[1]

    def render(self,surf):
        surf.blit(self.surf,self.pos)