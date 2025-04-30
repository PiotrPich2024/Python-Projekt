import pygame
from button_class import Button
from text_font import TextFont

class GameOver:
    def __init__(self,width,height):
        self.h = height
        self.w = width
        self.img = pygame.image.load('./Pixel art/GameOverScreen.png').convert_alpha()
        self.img = pygame.transform.scale(self.img,(width,height))
        self.transparency = 0
        self.pace_of_change = 1

        self.game_over_font = TextFont(36,48,3)
        self.buttons_font = TextFont(12,16,1)

        self.x_mult = width/640
        self.y_mult = height/480
        self.game_over_pos = (158 * self.x_mult, 330 * self.y_mult)
        self.play_again_pos = (260 * self.x_mult,387* self.y_mult)
        self.yes_pos = (280 * self.x_mult,408*self.y_mult)
        self.no_pos =  (336 * self.x_mult,408*self.y_mult)

        self.text_transparency = 0

        self.temp_surf_over = pygame.Surface((324,48))
        self.temp_surf_play_again = pygame.Surface((120,16))
        self.temp_surf_yes = pygame.Surface((36,16))
        self.temp_surf_no = pygame.Surface((24,16))

        self.yes_button = Button(self.temp_surf_yes,self.yes_pos)
        self.no_button = Button(self.temp_surf_no,self.no_pos)

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
        self.buttons_font.render_string("yes", surf, self.yes_pos)
        self.buttons_font.render_string("no", surf, self.no_pos)

    def reset(self):
        self.transparency = 0
        self.text_transparency = 0

    def play_again(self,mouse_pos):
        if self.yes_button.is_clicked(mouse_pos):
            return 0
        elif self.no_button.is_clicked(mouse_pos):
            return 3
        return 2