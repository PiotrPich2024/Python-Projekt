import pygame
from Map import Map
from Player import Player
import pygame


class GameEngine:
    def __init__(self,parameters):
        self.map = Map(parameters["map_width"],parameters["map_height"])
        self.player = Player(parameters["player_width"], parameters["player_height"], 0,0,
                             parameters["player_velocity"])

        self.player.appear_at(self.map.player_start_pos[0], self.map.player_start_pos[1])
        self.cleared_level = False
        self.entered_new_level = True



    def render(self,surf):
        self.map.render_map(surf)
        self.player.render(surf)
        self.map.render_back_wall(surf)

    def run(self, clock,surf):
        running = True
        # dest = [self.player.img_pos[0] + self.player.width/2, self.player.img_pos[1] + self.player.height/2]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.cleared_level = True
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     dest[0],dest[1] = pygame.mouse.get_pos()

            if self.entered_new_level:
                dest_x,dest_y = self.map.player_shooting_pos
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

