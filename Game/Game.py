import pygame
from GameEngine import GameEngine
import json


class Game:
    def __init__(self,size_id):
        pygame.init()
        pygame.display.set_caption('game')


        with open('../Parameters.JSON','r') as file:
            data = json.load(file)
        self.parameters = next((item for item in data['sizes'] if item['size_id'] == size_id),None)
        if not self.parameters:
            raise ValueError(f"Nie znaleziono size_id {size_id} w pliku JSON")

        self.screen = pygame.display.set_mode((self.parameters["map_width"], self.parameters["map_height"]))
        self.clock = pygame.time.Clock()

        self.GameEngine = GameEngine(self.parameters)


    def run(self):
        # dest = [self.GameEngine.player.img_pos[0]/2,self.GameEngine.player.img_pos[1]/2]


        self.GameEngine.run(self.clock,self.screen)


        pygame.quit()

if __name__ == '__main__':
    game = Game(0)
    game.run()