import random

import pygame
from Map import Map
from Player import Player
from Enemy import Enemy
import pygame


class GameEngine:
    def __init__(self,parameters):
        self.map = Map(parameters["map_width"],parameters["map_height"])
        self.player = Player(parameters["entity_width"], parameters["entity_height"], 0,0,
                             parameters["player_velocity"])

        self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])
        self.cleared_level = False
        self.entered_new_level = True

        self.enemies = []
        which = bool(random.randint(0, 1))
        self.first_enemy = Enemy(parameters["entity_width"], parameters["entity_height"], 100,300, which)
        self.second_enemy = Enemy(parameters["entity_width"], parameters["entity_height"], 200, 300, not which)
        self.enemies.append(self.first_enemy)
        self.enemies.append(self.second_enemy)
        self.enemy_is_dead = False


    def render(self,surf):
        self.map.render_map(surf)
        self.player.render(surf)
        self.map.render_back_wall(surf)
        if self.enemy_is_dead:
            for enemy in self.enemies:
                enemy.render_dead(surf)
        else:
            for enemy in self.enemies:
                enemy.render(surf)

    def run(self, clock,surf,show_menu):
        running = True
        # dest = [self.player.img_pos[0] + self.player.width/2, self.player.img_pos[1] + self.player.height/2]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return show_menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.entered_new_level:
                        self.cleared_level = True
                        self.enemy_is_dead = True
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        show_menu = True
                        self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])
                        self.cleared_level = False
                        self.entered_new_level = True
                        return show_menu
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     dest[0],dest[1] = pygame.mouse.get_pos()

            if self.entered_new_level:
                dest_x,dest_y = self.map.player_shooting_pos
                self.enemy_is_dead = False
                if self.player.move_to(dest_x,dest_y):
                    self.entered_new_level = False

            if self.cleared_level:
                dest_x,dest_y = self.map.player_end_pos
                if self.player.move_to(dest_x,dest_y):
                    self.cleared_level = False
                    self.entered_new_level = True
                    self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])

            self.render(surf)

            # self.player.move_to(dest[0],dest[1])
            pygame.display.update()
            clock.tick(60)
        return show_menu

