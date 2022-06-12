import pygame
import os
from config.Config import WINDOW_RESOLUTION, MENU
from menu.StartMenu import Item


class EscMenu:
    def __init__(self, level):
        self.level = level
        #self.buttons_event = None

        self.locale = self.level.locale
        #pics_path = os.path.join("pics", "menu")
        self.surface = pygame.display.get_surface()

        self.transp_bg = pygame.Surface(WINDOW_RESOLUTION, pygame.SRCALPHA)
        self.transp_bg.fill((0, 0, 0, 128))

        self.bg_rect = pygame.Rect(WINDOW_RESOLUTION[0] * 0.25, WINDOW_RESOLUTION[1] * 0.2, WINDOW_RESOLUTION[0] * 0.5, WINDOW_RESOLUTION[1] * 0.6)

        self.buttons = []
        self.buttons.append(
            Item("play.png", "play_hovered.png",\
                 int(WINDOW_RESOLUTION[0] * 0.4), int(self.bg_rect.h * 0.4),\
                 (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.26)),\
                 self.level, self.play_button_call, None, 1, 2)
        )
        self.buttons.append(
            Item("exit.png", "exit_hovered.png",\
                 int(WINDOW_RESOLUTION[0] * 0.3), int(self.bg_rect.h * 0.3),\
                 (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.56)),\
                 self.level, self.exit_button_call, None, 2, 2)
        )

    def exit_button_call(self):
        self.level.game_state = "active"
        #self.level.game.game_state = "start"
        self.level.game.__init__(self.level.game.locale, self.level.game.volume)
        #self.level.game.run()

    def play_button_call(self):
        self.level.game_state = "active"

    def display(self):
        self.surface.blit(self.transp_bg, (0, 0))

        pygame.draw.rect(self.surface, "#FFBC42", self.bg_rect, 0, 20)
        pygame.draw.rect(self.surface, "#3D0814", self.bg_rect, 10, 20)

        for button in self.buttons:
            button.display(self.surface)

    def update_locale(self, lang):
        for button in self.buttons:
            button.update_locale(lang)
