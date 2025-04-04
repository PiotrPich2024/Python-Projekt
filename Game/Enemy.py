import pygame

class Enemy:
    def __init__(self,width,height,x,y,is_impostor):
        self.img = pygame.image.load('Pixel art/Enemy/enemy.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [x,y]
        self.is_impostor = is_impostor
        self.spare_img = pygame.image.load('Pixel art/Enemy/enemy_spare.png').convert_alpha()
        self.spare_img = pygame.transform.scale(self.spare_img, (width, height))
        self.kill_img = pygame.image.load('Pixel art/Enemy/enemy_kill.png').convert_alpha()
        self.kill_img = pygame.transform.scale(self.kill_img, (width, height))

        self.dead_img = pygame.image.load('Pixel art/Enemy/enemy_crewmate.png').convert_alpha()
        if is_impostor:
            self.dead_img = pygame.image.load('Pixel art/Enemy/enemy_impostor.png').convert_alpha()
        self.dead_img = pygame.transform.scale(self.dead_img, (width, height))

    def render(self,surf):
        surf.blit(self.img,self.img_pos)

    def render_choose(self,surf,to_kill):
        if to_kill:
            surf.blit(self.kill_img, self.img_pos)
        else:
            surf.blit(self.spare_img, self.img_pos)

    def render_dead(self,surf):
        surf.blit(self.dead_img, self.img_pos)

