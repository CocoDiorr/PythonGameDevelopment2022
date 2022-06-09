import pygame
import pygame.display
from config.Config import *
from level.Level import Level


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.locale = 'ru'
        self.level = Level(self.locale)

    def run(self):
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.level.companion_call()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.level.buttons_event = event



            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            self.level.run(dt)
            pygame.display.update()
