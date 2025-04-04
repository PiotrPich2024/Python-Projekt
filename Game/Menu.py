import pygame
from show_screen import ShowScreen

class Menu:
    def __init__(self,width,height,play_button_pos,score_button_pos):
        self.width = width
        self.height = height

        self.play_button_pos = list(play_button_pos)
        self.score_button_pos = list(score_button_pos)

        self.img = pygame.image.load('Pixel art/Menu.png').convert()
        self.img = pygame.transform.scale(self.img, (self.width,self.height))

        self.button_height = (55 * height)/480
        self.play_button_width = (132 * width)/640
        self.score_button_width = (138*width)/640

        self.play_button_img = pygame.image.load('Pixel art/play_button.png').convert()
        self.play_button_img = pygame.transform.scale(self.play_button_img,(self.play_button_width, self.button_height))
        self.score_button_img = pygame.image.load('Pixel art/score_button.png').convert()
        self.score_button_img = pygame.transform.scale(self.score_button_img,(self.score_button_width,self.button_height))

    def render(self,surf):
        surf.blit(self.img,(0,0))
        surf.blit(self.play_button_img,self.play_button_pos)
        surf.blit(self.score_button_img,self.score_button_pos)

    def clicked_on_play(self,x,y):
        up_left = self.play_button_pos
        down_right = list([self.play_button_pos[0] + self.play_button_width, self.play_button_pos[1] + self.button_height])
        return up_left[0] < x < down_right[0] and up_left[1] < y < down_right[1]

    def clicked_on_score(self,x,y):
        up_left = self.score_button_pos
        down_right = list([self.score_button_pos[0] + self.score_button_width,
                          self.score_button_pos[1] + self.button_height])
        return up_left[0] < x < down_right[0] and up_left[1] < y < down_right[1]

    def show(self,clock,surf,sc):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sc = None
                    return sc
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    if(self.clicked_on_play(x,y)):
                        running = False
                        sc = ShowScreen.show_game

                        return sc
                    elif(self.clicked_on_score(x,y)):
                        sc = ShowScreen.show_score
                        running = False
                        return sc
            self.render(surf)
            pygame.display.update()
            clock.tick(60)
        sc = None
        return sc


