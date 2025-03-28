import pygame
from GameEngine import GameEngine

pygame.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('game')
        self.screen =  pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.GameEngine = GameEngine()

    def run(self):
        running = True
        dest = [150, 150]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dest[0],dest[1] = pygame.mouse.get_pos()

            self.screen.blit(self.GameEngine.map.img,self.GameEngine.map.img_pos)

            self.screen.blit(self.GameEngine.player.img, self.GameEngine.player.img_pos)
            self.GameEngine.player.move_to(dest[0],dest[1])
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()