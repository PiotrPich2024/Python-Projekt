import pygame

class Enemy:
    def __init__(self,width,height,x,y,is_impostor):
        self.img = pygame.image.load('./pixel_art/enemy/enemy.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [x,y]
        self.is_impostor = is_impostor
        self.spare_img = pygame.image.load('./pixel_art/enemy/enemy_spare.png').convert_alpha()
        self.spare_img = pygame.transform.scale(self.spare_img, (width, height))
        self.kill_img = pygame.image.load('./pixel_art/enemy/enemy_kill.png').convert_alpha()
        self.kill_img = pygame.transform.scale(self.kill_img, (width, height))

        self.dead_img = pygame.image.load('./pixel_art/enemy/enemy_crewmate.png').convert_alpha()
        if is_impostor:
            self.dead_img = pygame.image.load('./pixel_art/enemy/enemy_impostor.png').convert_alpha()
        self.dead_img = pygame.transform.scale(self.dead_img, (width, height))

        # animacje
        self.dead_transpercy = 255
        self.alive_transparency = 0
        self.fade_speed = 5

    def render(self,surf):
        self.fade_in()
        surf.blit(self.img, self.img_pos)

    def render_choose(self,surf,to_kill):
        self.fade_in()
        if to_kill:
            surf.blit(self.kill_img, self.img_pos)
        else:
            surf.blit(self.spare_img, self.img_pos)


    def render_dead(self,surf):
        surf.blit(self.dead_img, self.img_pos)
        self.fade_out()

    def fade_out(self):
        self.dead_img.set_alpha(self.dead_transpercy)
        if self.dead_transpercy > 0:
            self.dead_transpercy -= self.fade_speed
            self.dead_transpercy = max(self.dead_transpercy,0)

    def fade_in(self):
        self.img.set_alpha(self.alive_transparency)
        self.kill_img.set_alpha(self.alive_transparency)
        self.spare_img.set_alpha(self.alive_transparency)
        self.alive_transparency = min(self.alive_transparency + self.fade_speed, 255)
