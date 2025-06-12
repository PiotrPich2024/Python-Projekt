import pygame

from Game.font.text_font import TextFont
from Game.screens.screen_elements.super_button import SuperButton


class StopMenuInfo:
    menu_width = 220
    menu_height = 400
    menu_pos_x = 210
    menu_pos_y = 40

    rect_width = 200
    score_height = 180
    button_height = 85

    score_text_padding = 50

    padding = 10


class StopMenu:
    def __init__(self,width,height,pos,score):
        self.menu_pos = list(pos)
        self.height = height
        self.width = width
        self.score = score
        self.score_font = TextFont(18,24,2)
        self.button_font = TextFont(12,16,1)

        self.img = pygame.image.load("./pixel_art/stop_menu_screen.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

        self.item_width = width * StopMenuInfo.rect_width/StopMenuInfo.menu_width
        self.score_height = height * StopMenuInfo.score_height/StopMenuInfo.menu_height
        self.button_height = height * StopMenuInfo.button_height/StopMenuInfo.menu_height

        # go back to menu button surfaces
        self.go_back_button_img = pygame.image.load('./pixel_art/buttons/stop_menu/go_back/default.png').convert()
        self.go_back_button_img = pygame.transform.scale(self.go_back_button_img,
                                                      (self.item_width, self.button_height))
        self.go_back_button_hover_img = pygame.image.load('./pixel_art/buttons/stop_menu/go_back/hover.png')
        self.go_back_button_hover_img = pygame.transform.scale(self.go_back_button_hover_img,
                                                            (self.item_width, self.button_height))
        self.go_back_button_clicked_img = pygame.image.load('./pixel_art/buttons/stop_menu/go_back/clicked.png')
        self.go_back_button_clicked_img = pygame.transform.scale(self.go_back_button_clicked_img,
                                                              (self.item_width, self.button_height))

        # resume button surfaces
        self.resume_button_img = pygame.image.load('./pixel_art/buttons/stop_menu/resume/default.png').convert()
        self.resume_button_img = pygame.transform.scale(self.resume_button_img,
                                                         (self.item_width, self.button_height))
        self.resume_button_hover_img = pygame.image.load('./pixel_art/buttons/stop_menu/resume/hover.png')
        self.resume_button_hover_img = pygame.transform.scale(self.resume_button_hover_img,
                                                               (self.item_width, self.button_height))
        self.resume_button_clicked_img = pygame.image.load('./pixel_art/buttons/stop_menu/resume/clicked.png')
        self.resume_button_clicked_img = pygame.transform.scale(self.resume_button_clicked_img,
                                                                 (self.item_width, self.button_height))


        self.padding = height * StopMenuInfo.padding/StopMenuInfo.menu_height

        self.text_padding = height * StopMenuInfo.score_text_padding/StopMenuInfo.menu_height

        self.item_pos_x = pos[0] + self.padding
        self.score_pos_y = pos[1] + self.padding
        self.resume_pos_y = self.score_pos_y + self.padding + self.score_height
        self.go_to_pos_y = self.resume_pos_y + self.button_height + self.padding

        self.go_back_button = SuperButton(self.go_back_button_img, self.go_back_button_hover_img,
                                          self.go_back_button_clicked_img, (self.item_pos_x,self.go_to_pos_y))
        self.resume_button = SuperButton(self.resume_button_img,self.resume_button_hover_img,
                                         self.resume_button_clicked_img, (self.item_pos_x,self.resume_pos_y))

    def render(self,surf):
        surf.blit(self.img,self.menu_pos)
        self.go_back_button.render(surf)
        self.resume_button.render(surf)
        self.score_font.render_string("score", surf, (
                                    self.menu_pos[0] + self.padding + self.text_padding,
                                    self.menu_pos[1] + self.padding + self.text_padding))
        self.score_font.render_string(f"{self.score}", surf,
                                      (self.menu_pos[0] + self.padding + self.text_padding,
                                       self.menu_pos[1] + 24 + 2 * self.padding + self.text_padding))


    def show(self,clock,surf,sc):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sc = None
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    if self.resume_button.update((x,y),mouse_pressed):
                        running = False
                        return 1
                    elif self.go_back_button.update((x,y),mouse_pressed):
                        running = False
                        return 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        return 1

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            self.resume_button.update(mouse_pos, mouse_pressed)
            self.go_back_button.update(mouse_pos, mouse_pressed)

            self.render(surf)
            pygame.display.update()
            clock.tick(60)
        return 0








