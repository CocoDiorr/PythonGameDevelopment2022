import pygame
import pygame.display
from config.Config import *
from level.Level import Level
from menu.StartMenu import StartMenu

class Game:
    """ """
    def __init__(self, locale='en', volume=0.2):
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.locale = locale
        self.level = Level(self.locale, self)
        self.volume = volume
        self.game_state = "start" # "play"
        self.start_menu = StartMenu(self)

    def run(self):
        """ """
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        if self.game_state == "play":
                            self.level.companion_call()

                    if event.key == pygame.K_ESCAPE:
                        if self.game_state == "play":
                            if self.level.game_state in ("active", "esc"):
                                self.level.esc_menu_call()
                            elif self.level.game_state == "companion":
                                self.level.companion_call()
                        else:
                            if self.start_menu.settings_on:
                                self.start_menu.settings_button()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.game_state == "start":
                            self.start_menu.buttons_event = event
                        if self.game_state == "play":
                            if self.level.game_state in ("companion", "esc"):
                                self.level.buttons_event = event

                #elif self.game_state == "start":



            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            if self.game_state == "start":
                self.start_menu.display()
            if self.game_state == "play":
                self.level.run(dt)
            pygame.display.update()

    def update_locale(self, lang):
        self.locale = lang
        self.level.update_locale(lang)
        self.start_menu.update_locale(lang)
