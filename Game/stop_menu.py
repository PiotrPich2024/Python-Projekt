import pygame
from text_font import TextFont

class StopMenuInfo:
    menu_widht = 220
    menu_height = 400
    menu_pos_x = 210
    menu_pos_y = 40

    rect_width = 200
    score_height = 180
    button_height = 85

    padding = 10


class StopMenu:
    def __init__(self,width,height,pos,score):
        self.menu_pos = list(pos)
        self.height = height
        self.width = width
        self.score = score
        self.score_font = TextFont(18,24,2)
        self.button_font = TextFont(12,16,1)

        self.item_width = width * StopMenuInfo.rect_width/StopMenuInfo.menu_widht
        self.score_height = height * StopMenuInfo.score_height/StopMenuInfo.menu_height
        self.button_height = height * StopMenuInfo.button_height/StopMenuInfo.menu_height

        self.padding = height * StopMenuInfo.padding/StopMenuInfo.menu_height

        self.item_pos_x = pos[0] + self.padding
        self.score_pos_y = pos[1] + self.padding
        self.resume_pos_y = self.score_pos_y + self.padding + self.score_height
        self.return_pos_y = self.resume_pos_y + self.button_height + self.padding

    def render(self,surf):
        temp_surf = pygame.Surface((self.width,self.height))
        temp_score = pygame.Surface((self.item_width,self.score_height))
        temp_res = pygame.Surface((self.item_width,self.button_height))
        temp_ret = pygame.Surface((self.item_width,self.button_height))
        temp_surf.fill(pygame.Color("blue"))
        temp_res.fill(pygame.Color("black"))
        temp_ret.fill(pygame.Color("black"))
        self.score_font.render_string(f"SCORE {self.score}",temp_score,(10,40))
        self.button_font.render_string("return",temp_ret,(10,20))
        self.button_font.render_string("resume",temp_res,(10,20))
        surf.blit(temp_surf,self.menu_pos)
        surf.blit(temp_score,(self.item_pos_x,self.score_pos_y))
        surf.blit(temp_res,(self.item_pos_x,self.resume_pos_y))
        surf.blit(temp_ret,(self.item_pos_x,self.return_pos_y))


    def clicked_on_resume(self,x,y):
        upper_left = (self.item_pos_x,self.resume_pos_y)
        bottom_right = (upper_left[0]+self.item_width, upper_left[1]+self.button_height)
        return upper_left[0] <= x <= bottom_right[0] and upper_left[1] <= y <= bottom_right[1]

    def clicicked_on_return(self,x,y):
        upper_left = (self.item_pos_x, self.return_pos_y)
        bottom_right = (upper_left[0] + self.item_width, upper_left[1] + self.button_height)
        return upper_left[0] <= x <= bottom_right[0] and upper_left[1] <= y <= bottom_right[1]


    def show(self,clock,surf,sc):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sc = None
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.clicked_on_resume(x,y):
                        running = False
                        return 1
                    elif self.clicicked_on_return(x,y):
                        running = False
                        return 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        return 1
            self.render(surf)
            pygame.display.update()
            clock.tick(60)
        return 0








