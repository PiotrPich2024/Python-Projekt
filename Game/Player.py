import pygame

class Player:
    def __init__(self,width,height,x,y,velocity):
        self.img = pygame.image.load('Pixel art/Player/player.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [x,y]
        self.velocity = velocity

    def move_to(self,dest_x,dest_y):
        x,y = self.img_pos[0]+self.width/2,self.img_pos[1]+self.height
        x_move,y_move = 0,0
        if dest_x - x != 0:
            x_move = min(self.velocity,abs(dest_x-x))
            x_move *= (dest_x - x)/abs(dest_x - x)

        if dest_y - y != 0:
            y_move = min(self.velocity,abs( dest_y - y))
            y_move *= (dest_y - y) / abs(dest_y - y)

        self.img_pos[0] += x_move
        self.img_pos[1] += y_move



