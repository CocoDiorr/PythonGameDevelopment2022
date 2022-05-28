import pygame
import pygame.display
from config.Config import *
from level.Level import Level


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            self.level.run(dt)
            pygame.display.update()
