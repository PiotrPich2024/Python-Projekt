import pygame

class Map:
    def __init__(self,width,height):
        self.img = pygame.image.load('pixel_art/map.png').convert()
        self.img = pygame.transform.scale(self.img, (width, height))

        self.width = width
        self.height = height

        self.img_pos = [0,0]
        self.back_wall_pos = [0,(height * 53)/60]
        self.img_back_wall = pygame.image.load('pixel_art/backwall.png').convert_alpha()
        self.img_back_wall = pygame.transform.scale(self.img_back_wall, (width, (height * 7)/60))


        self.player_passage = [(75*width)/320,0]
        self.door_width = width/16
        self.door_height = (36 * height)/240


        self.player_start_pos = [self.player_passage[0] + self.door_width/2,18*height/240 + self.door_height/2]
        self.player_end_pos = [self.player_passage[0] + self.door_width/2,height]
        self.player_shooting_pos = [self.player_passage[0] + self.door_width/2,2*height/5]


    def render_map(self,surf):
        surface = pygame.Surface((surf.get_width(),surf.get_height()),pygame.SRCALPHA)
        surface.blit(self.img, self.img_pos)
        surf.blit(surface,self.img_pos)


    def render_back_wall(self,surf):
        surf.blit(self.img_back_wall, self.back_wall_pos)