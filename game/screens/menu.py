import pygame

from Game.particles.snow_generator import SnowGenerator
from Game.screens.show_screen import ShowScreen
from Game.screens.screen_elements.super_button import SuperButton


class Menu:
    def __init__(self,width,height,play_button_pos,score_button_pos):
        self.width = width
        self.height = height

        self.play_button_pos = list(play_button_pos)
        self.score_button_pos = list(score_button_pos)

        self.img = pygame.image.load('./pixel_art/Menu.png').convert()
        self.img = pygame.transform.scale(self.img, (self.width,self.height))

        self.depth_img = pygame.image.load('./pixel_art/menu_depth.png').convert_alpha()
        self.depth_img = pygame.transform.scale(self.depth_img, (self.width,self.height))

        self.button_height = (55 * height)/480
        self.play_button_width = (132 * width)/640
        self.score_button_width = (138*width)/640


        # play button surfaces
        self.play_button_img = pygame.image.load('./pixel_art/buttons/menu/play/default.png').convert()
        self.play_button_img = pygame.transform.scale(self.play_button_img,(self.play_button_width, self.button_height))
        self.play_button_hover_img = pygame.image.load('./pixel_art/buttons/menu/play/hover.png')
        self.play_button_hover_img = pygame.transform.scale(self.play_button_hover_img,
                                                             (self.play_button_width, self.button_height))
        self.play_button_clicked_img = pygame.image.load('./pixel_art/buttons/menu/play/clicked.png')
        self.play_button_clicked_img = pygame.transform.scale(self.play_button_clicked_img,
                                                               (self.play_button_width, self.button_height))

        # score button surfaces
        self.score_button_img = pygame.image.load('./pixel_art/buttons/menu/score/default.png').convert()
        self.score_button_img = pygame.transform.scale(self.score_button_img,(self.score_button_width,self.button_height))
        self.score_button_hover_img = pygame.image.load('./pixel_art/buttons/menu/score/hover.png')
        self.score_button_hover_img = pygame.transform.scale(self.score_button_hover_img,(self.score_button_width, self.button_height))
        self.score_button_clicked_img = pygame.image.load('./pixel_art/buttons/menu/score/clicked.png')
        self.score_button_clicked_img = pygame.transform.scale(self.score_button_clicked_img,
                                                             (self.score_button_width, self.button_height))

        #super buttony
        self.score_button = SuperButton(self.score_button_img,self.score_button_hover_img,self.score_button_clicked_img, self.score_button_pos)
        self.play_button = SuperButton(self.play_button_img,self.play_button_hover_img,self.play_button_clicked_img, self.play_button_pos)

        self.snow_g = SnowGenerator(self.width,self.height)

    def render(self,surf):
        surf.blit(self.img,(0,0))
        self.snow_g.render(surf)
        surf.blit(self.depth_img,(0,0))
        self.play_button.render(surf)
        self.score_button.render(surf)


    def show(self,clock,surf,sc):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                    sc = None
                    return sc
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    if(self.play_button.update((x,y),mouse_pressed)):
                        running = False
                        sc = ShowScreen.show_game
                        return sc
                    elif(self.score_button.update((x,y),mouse_pressed)):
                        sc = ShowScreen.show_score
                        running = False
                        return sc

            # jak tutaj nie bd sprawdzał dodatkowo to hover nie działa
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            self.score_button.update(mouse_pos, mouse_pressed)
            self.play_button.update(mouse_pos, mouse_pressed)

            self.render(surf)
            pygame.display.update()
            clock.tick(60)
        sc = None
        return sc


