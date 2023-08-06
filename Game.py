import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.Clock()

        self.assets = {

        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


Game().run()
