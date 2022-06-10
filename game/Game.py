import pygame
import pygame.display
from config.Config import *
from level.Level import Level


class Game:
    """ """
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.level = Level()

    def run(self):
        """ """
        while self.running:
            events = pygame.event.get()
            #self.level.put_events(events)
            #self.level.events = events
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.level.companion_call()

                #if event.type == pygame.KEYDOWN and event.key == pygame.K_h:


            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            self.level.run(dt)
            pygame.display.update()
