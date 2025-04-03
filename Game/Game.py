import pygame
from GameEngine import GameEngine
import json
from Menu import Menu


class Game:
    def __init__(self,size_id):
        pygame.init()
        pygame.display.set_caption('FREQUENCIES OF FEAR')
        gameIcon = pygame.image.load('Pixel art/logo.png')
        pygame.display.set_icon(pygame.transform.scale(gameIcon,(32,32)))


        with open('../Parameters.JSON','r') as file:
            data = json.load(file)
        self.parameters = next((item for item in data['sizes'] if item['size_id'] == size_id),None)
        if not self.parameters:
            raise ValueError(f"Nie znaleziono size_id {size_id} w pliku JSON")

        self.screen = pygame.display.set_mode((self.parameters["map_width"], self.parameters["map_height"]))
        self.clock = pygame.time.Clock()

        self.GameEngine = GameEngine(self.parameters)
        self.Menu = Menu(self.parameters["menu_width"],self.parameters["menu_height"],self.parameters["play_button_pos"],self.parameters["score_button_pos"])


    def run(self):
        # dest = [self.GameEngine.player.img_pos[0]/2,self.GameEngine.player.img_pos[1]/2]
        show_game = False
        show_menu = True
        show_score = False

        while show_game or show_menu or show_score:
            if show_menu:
                show_game, show_score = self.Menu.show(self.clock,self.screen,show_game,show_score)

            if(show_game):
                self.GameEngine.run(self.clock,self.screen,show_menu)
                show_game = False


        pygame.quit()

if __name__ == '__main__':
    game = Game(0)
    game.run()