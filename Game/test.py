import pygame

pygame.init()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('game')
        self.screen =  pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load('Pixel art/map.png')
        self.img = pygame.transform.scale(self.img, (640,480))
        self.enemies = [False,False,True,False]
        self.pointEnemy = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    continue

            self.screen.blit(self.img,(100,100))
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()