import pygame

from Game.font.text_font import TextFont
from Game.screens.screen_elements.button_class import Button
from Game.screens.screen_elements.super_button import SuperButton


class GameOver:
    def __init__(self,width,height):
        self.h = height
        self.w = width
        self.img = pygame.image.load('./pixel_art/GameOverScreen.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(width,height))
        self.transparency = 0
        self.pace_of_change = 1

        self.game_over_font = TextFont(36,48,3)
        self.buttons_font = TextFont(12,16,1)

        self.x_mult = width/640
        self.y_mult = height/480
        self.game_over_pos = (158 * self.x_mult, 330 * self.y_mult)
        self.play_again_pos = (260 * self.x_mult,387* self.y_mult)
        self.yes_pos = (240 * self.x_mult,408*self.y_mult)
        self.no_pos =  (360 * self.x_mult,408*self.y_mult)

        self.text_transparency = 0

        self.temp_surf_over = pygame.Surface((324,48))
        self.temp_surf_play_again = pygame.Surface((120,16))

        self.button_width = 60
        self.button_height = 40

        # yes button surfaces
        self.yes_button_img = pygame.image.load('./pixel_art/buttons/game_over/yes/default.png').convert()
        self.yes_button_img = pygame.transform.scale(self.yes_button_img,
                                                        (self.button_width, self.button_height))
        self.yes_button_hover_img = pygame.image.load('./pixel_art/buttons/game_over/yes/hover.png')
        self.yes_button_hover_img = pygame.transform.scale(self.yes_button_hover_img,
                                                              (self.button_width, self.button_height))
        self.yes_button_clicked_img = pygame.image.load('./pixel_art/buttons/game_over/yes/clicked.png')
        self.yes_button_clicked_img = pygame.transform.scale(self.yes_button_clicked_img,
                                                                (self.button_width, self.button_height))

        # no button surfaces
        self.no_button_img = pygame.image.load('./pixel_art/buttons/game_over/no/default.png').convert()
        self.no_button_img = pygame.transform.scale(self.no_button_img,
                                                     (self.button_width, self.button_height))
        self.no_button_hover_img = pygame.image.load('./pixel_art/buttons/game_over/no/hover.png')
        self.no_button_hover_img = pygame.transform.scale(self.no_button_hover_img,
                                                           (self.button_width, self.button_height))
        self.no_button_clicked_img = pygame.image.load('./pixel_art/buttons/game_over/no/clicked.png')
        self.no_button_clicked_img = pygame.transform.scale(self.no_button_clicked_img,
                                                             (self.button_width, self.button_height))

        self.yes_button = SuperButton(self.yes_button_img, self.yes_button_hover_img
                                      , self.yes_button_clicked_img,self.yes_pos)
        self.no_button = SuperButton(self.no_button_img, self.no_button_hover_img
                                      , self.no_button_clicked_img,self.no_pos)

    def fade_in(self):
        self.transparency = min(self.transparency + self.pace_of_change, 255)
        if self.transparency >= 200:
            self.text_transparency = min(self.transparency + self.pace_of_change, 255)

    def render(self,surf):
        self.fade_in()
        self.img.set_alpha(self.transparency)
        surf.blit(self.img,(0,0))
        self.game_over_font.render_string("game over", surf, self.game_over_pos)
        self.buttons_font.render_string("play again", surf, self.play_again_pos)
        self.yes_button.render(surf)
        self.no_button.render(surf)

    def reset(self):
        self.transparency = 0
        self.text_transparency = 0

    def play_again(self,mouse_pos, mouse_pressed):
        if self.yes_button.update(mouse_pos, mouse_pressed):
            return 0
        elif self.no_button.update(mouse_pos, mouse_pressed):
            return 3
        return 2