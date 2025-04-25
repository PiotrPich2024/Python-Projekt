import pygame

class HP:
    def __init__(self,no_hp,width,height,pos):
        self.width = width
        self.height = height
        self.full_img = pygame.image.load('./Pixel art/full_heart.png').convert_alpha()
        self.empty_img = pygame.image.load('./Pixel art/empty_heart.png').convert_alpha()
        self.full_img = pygame.transform.scale(self.full_img,(width,height))
        self.empty_img = pygame.transform.scale(self.empty_img, (width, height))
        self.curr_hp = no_hp
        self.no_hp = no_hp
        self.pos_x = pos[0]
        self.pos_y = pos[1]

    def render(self,surf):
        i = 0
        x_pos = 0
        while i < self.curr_hp:
            surf.blit(self.full_img,(self.pos_x + x_pos, self.pos_y))
            x_pos += self.width
            i += 1
        while i < self.no_hp:
            surf.blit(self.empty_img,(self.pos_x + x_pos, self.pos_y))
            x_pos += self.width
            i += 1

    def lose_hp(self):
        self.curr_hp = max(self.curr_hp - 1,0)