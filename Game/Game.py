import pygame
from GameEngine import GameEngine
import json
from Menu import Menu
from show_screen import ShowScreen


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

        sc = ShowScreen.show_menu
        pygame.mixer.music.load('./Sounds/wind__artic__cold-6195.mp3')
        while sc:
            match sc:
                case ShowScreen.show_menu:
                    pygame.mixer.music.play(-1,fade_ms=5000)
                    sc = self.Menu.show(self.clock, self.screen, sc)

                case ShowScreen.show_game:
                    pygame.mixer.music.fadeout(2500)
                    self.GameEngine = GameEngine(self.parameters)
                    sc = self.GameEngine.run(self.clock,self.screen,sc)
                case _:
                    break


if __name__ == '__main__':
    game = Game(0)
    game.run()