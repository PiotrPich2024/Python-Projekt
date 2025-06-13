import pygame
from random import randint

class Enemy:
    def __init__(self,width,height,x,y,is_impostor):
        self.variant = randint(1,3)
        path = f"./pixel_art/enemy/var{self.variant}"
        self.img = pygame.image.load(path + '/enemy.png').convert_alpha()
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width = width
        self.height = height
        self.img_pos = [x,y]
        self.is_impostor = is_impostor
        self.spare_img = pygame.image.load(path + '/choose/spare.png').convert_alpha()
        self.spare_img = pygame.transform.scale(self.spare_img, (width, height))
        self.kill_img = pygame.image.load(path + '/choose/kill.png').convert_alpha()
        self.kill_img = pygame.transform.scale(self.kill_img, (width, height))

        self.death_imgs = []
        for i in range(1,5):
            temp = pygame.image.load(path + f'/death/crewmate/death_{i}.png').convert_alpha()
            if is_impostor:
                temp = pygame.image.load(path + f'/death/impostor/death_{i}.png').convert_alpha()
            temp = pygame.transform.scale(temp,(width,height))
            self.death_imgs.append(temp)

        # animacje

        # animacja śmierci
        self.current_count = 0
        self.animation_time = 2 * 60 # 2 * 60 fps

        # animacje znikania i pojawiania się
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
        if self.current_count <=  self.animation_time * 1/4:
            surf.blit(self.death_imgs[0], self.img_pos)
        elif self.current_count <= self.animation_time * 2 / 4:
            surf.blit(self.death_imgs[1], self.img_pos)
        elif self.current_count  <=  self.animation_time * 3/4:
            surf.blit(self.death_imgs[2], self.img_pos)
        else:
            surf.blit(self.death_imgs[3], self.img_pos)
            self.fade_out()
        self.current_count += 1

    def fade_out(self):
        self.death_imgs[3].set_alpha(self.dead_transpercy)
        if self.dead_transpercy > 0:
            self.dead_transpercy -= self.fade_speed
            self.dead_transpercy = max(self.dead_transpercy,0)

    def fade_in(self):
        self.img.set_alpha(self.alive_transparency)
        self.kill_img.set_alpha(self.alive_transparency)
        self.spare_img.set_alpha(self.alive_transparency)
        self.alive_transparency = min(self.alive_transparency + self.fade_speed, 255)
