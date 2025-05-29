import pygame
import json
from Game.font.text_font import TextFont
from Game.screens.screen_elements.button_class import Button
from Game.screens.show_screen import ShowScreen

class ImageInfo:
    width = 640
    height = 480
    score_start_height = 70
    score_start_width = 220
    big_gap = 100
    small_gap = 50

class ScoreScreen:
    def __init__(self,width,height, scores):
        self.width = width
        self.height = height
        self.img = pygame.image.load('./pixel_art/ScoreMenu.png').convert()
        self.img = pygame.transform.scale(self.img, (self.width,self.height))

        with open('Scores.JSON', 'r') as file:
            data = json.load(file)

        self.best_score = scores['first']
        self.second_score = scores['second']
        self.third_score = scores['third']

        self.bigger_font = TextFont(36, 48, 3)
        self.middle_font = TextFont(24,32,2)
        self.smaller_font = TextFont(12, 16, 1)

        self.font_start_pos = (self.width / ImageInfo.width * ImageInfo.score_start_width,
                               self.height / ImageInfo.height * ImageInfo.score_start_height)

        self.big_gap = self.height / ImageInfo.height * ImageInfo.big_gap
        self.small_gap = self.width / ImageInfo.width * ImageInfo.small_gap

        temp_surf = pygame.Surface((72,16))

        self.go_back_button = Button(temp_surf,(self.font_start_pos[0] + 50, self.font_start_pos[1] + 300))

        self.temp_surf_score = pygame.Surface((324, 48))
        self.temp_surf_1 = pygame.Surface((120, 16))
        self.temp_surf_2 = pygame.Surface((36, 16))
        self.temp_surf_3 = pygame.Surface((24, 16))



    def render(self, surf):
        surf.blit(self.img,(0,0))
        self.bigger_font.render_string("scores", surf, self.font_start_pos)
        self.middle_font.render_string(f"1st. {self.best_score}",surf, (self.font_start_pos[0], self.font_start_pos[1] + 100))
        self.middle_font.render_string(f"2nd. {self.second_score}",surf, (self.font_start_pos[0], self.font_start_pos[1] + 150))
        self.middle_font.render_string(f"3rd. {self.third_score}",surf, (self.font_start_pos[0], self.font_start_pos[1] + 200))
        self.smaller_font.render_string("return",surf,(self.font_start_pos[0] + 50, self.font_start_pos[1] + 300))


    def show(self, clock,surf):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return None
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.go_back_button.is_clicked(pygame.mouse.get_pos()):
                        return ShowScreen.show_menu

            self.render(surf)
            pygame.display.update()
            clock.tick(60)
        return None



