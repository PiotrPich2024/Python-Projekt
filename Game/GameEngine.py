import pygame
from Map import Map
from Player import Player
from Enemy import Enemy
from show_screen import ShowScreen
from text_font import TextFont
from enum import Enum
from random import randint
from heart_points import HP

class Method(Enum):
    kill = 1
    spare = 0

class GameEngine:
    def __init__(self,parameters):
        self.parameters = parameters
        self.map = Map(parameters["map_width"],parameters["map_height"])
        self.player = Player(parameters["entity_width"], parameters["entity_height"], 0,0,
                             parameters["player_velocity"])

        self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])
        self.cleared_level = False
        self.entered_new_level = True

        self.enemies_start_pos = (30,300)
        self.enemies_gap = parameters["entity_width"] + 20
        self.enemies = []
        self.enemies_are_dead = []
        self.alive_ones = []
        self.text_font = TextFont(12,16,2)

        # logika gracza
        self.chosen_enemy = 0
        self.method = Method.kill
        self.score = 0

        self.fps = 60

        # obsluga hp
        self.hp = HP(3,32,32,(0,0))


    def chose_next(self):
        if len(self.alive_ones) == 1:
            self.chosen_enemy = self.alive_ones[0]
            return
        elif len(self.alive_ones) < 1:
            return
        go_to = self.chosen_enemy
        n = len(self.alive_ones)
        for i in range(n-1,-1,-1):
            index = self.alive_ones[i]
            if index <= self.chosen_enemy:
                break
            go_to = index

        if go_to == self.chosen_enemy:
            self.chosen_enemy = self.alive_ones[0]
        else:
            self.chosen_enemy = go_to

    def chose_prev(self):
        if len(self.alive_ones) == 1:
            self.chosen_enemy = self.alive_ones[0]
            return
        elif len(self.alive_ones) < 1:
            return
        go_to = self.chosen_enemy
        n = len(self.alive_ones)
        for index in self.alive_ones:
            if index >= self.chosen_enemy:
                break
            go_to = index


        if go_to == self.chosen_enemy:
            self.chosen_enemy = self.alive_ones[n-1]
        else:
            self.chosen_enemy = go_to

    def render(self,surf):
        self.map.render_map(surf)
        self.player.render(surf)
        self.map.render_back_wall(surf)
        for i in range(len(self.enemies)):
            if self.enemies_are_dead[i]:
                self.enemies[i].render_dead(surf)
            else:
                if i == self.chosen_enemy:
                    self.enemies[i].render_choose(surf,bool(self.method.value))
                else:
                    self.enemies[i].render(surf)
        temp_surf = pygame.Surface((180,20))
        self.text_font.render_string(f"score={self.score}",temp_surf,pos=(0,0))
        surf.blit(temp_surf,(440,20))
        # testowanie polepszonej wersji textfont
        text_surf = pygame.Surface((200,300))
        self.text_font.render_string("sigma sigma boy sigma boy, nie wiem co tu innego pisac hellu",text_surf,pos=(0,50))
        surf.blit(text_surf,(440,100))
        self.hp.render(surf)

    def run(self, clock,surf,sc):
        running = True
        # dest = [self.player.img_pos[0] + self.player.width/2, self.player.img_pos[1] + self.player.height/2]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sc = None
                    pygame.quit()
                    return sc
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.entered_new_level:
                        if self.method == Method.spare:
                            for i in range(len(self.enemies)):
                                if i == self.chosen_enemy:
                                    continue
                                self.enemies_are_dead[i] = True
                                self.alive_ones.remove(i)
                        else:
                            self.enemies_are_dead[self.chosen_enemy] = True
                            if not self.enemies[self.chosen_enemy].is_impostor:
                                self.hp.lose_hp()
                            self.alive_ones.remove(self.chosen_enemy)
                            self.chose_next()
                        # self.cleared_level = True
                        # self.enemy_is_dead = True
                        self.player.gunshot_sound.play()
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        sc = ShowScreen.show_menu
                        self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])
                        self.cleared_level = False
                        self.entered_new_level = True
                        return sc
                    elif event.key == pygame.K_LEFT:
                        self.chose_prev()
                    elif event.key == pygame.K_RIGHT:
                        self.chose_next()
                    elif event.key == pygame.K_UP:
                        self.method = Method.kill if self.method != Method.kill else Method.spare
                    elif event.key == pygame.K_DOWN:
                        self.method = Method.spare if self.method == Method.kill else Method.kill
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     dest[0],dest[1] = pygame.mouse.get_pos()

            if not self.entered_new_level and not False in self.enemies_are_dead:
                self.cleared_level = True


            if self.entered_new_level:
                dest_x,dest_y = self.map.player_shooting_pos
                self.enemy_is_dead = False
                if self.player.move_to(dest_x,dest_y):
                    self.entered_new_level = False
                    self.enemies = [
                        Enemy(self.parameters["entity_width"], self.parameters["entity_height"], self.enemies_start_pos[0] + self.enemies_gap * i, self.enemies_start_pos[1],
                              bool(randint(0, 1))) for i in range(randint(3, 5))]
                    self.enemies_are_dead = [False for _ in range(len(self.enemies))]
                    self.alive_ones = [i for i in range(len(self.enemies))]

            if self.cleared_level:
                dest_x,dest_y = self.map.player_end_pos
                if self.player.move_to(dest_x,dest_y):
                    self.chosen_enemy = 0
                    self.score += 50
                    self.cleared_level = False
                    self.entered_new_level = True
                    self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])

            self.render(surf)

            # self.player.move_to(dest[0],dest[1])
            pygame.display.update()
            clock.tick(self.fps)
        sc = None
        return sc

