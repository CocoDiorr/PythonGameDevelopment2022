import pygame
import os
from Zelda.config.Config import MENU, UI_SETTINGS, WINDOW_RESOLUTION, DEFAULT_LOCALE

import gettext
translation = gettext.translation("DeathScreen", os.path.join(os.path.dirname(__file__), "..", "locale", "death_screen"), languages=[DEFAULT_LOCALE])
_ = translation.gettext


class DeathScreen:
    """ DeathScreen class. """
    def __init__(self, level: "Level"):
        """
        Init the death screen class.

        :param level: Level

        """
        self.level = level
        self.locale = self.level.locale

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_SETTINGS["UI_FONT"], MENU["FONT_SIZE"] * 2)

        self.transp_bg = pygame.Surface(WINDOW_RESOLUTION, pygame.SRCALPHA)
        self.transp_bg.fill((255, 0, 0, 128))

    def display(self):
        """ Draw the Death screen. """
        text_surf_1 = self.font.render(_("You died"), 0, MENU["FONT_COLOR"])
        text_rect_1 = text_surf_1.get_rect(midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.2)))

        text_surf_2 = self.font.render(_("Press SPACE to exit"), 0, MENU["FONT_COLOR"])
        text_rect_2 = text_surf_2.get_rect(midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.6)))

        self.display_surface.blit(self.transp_bg, (0, 0))

        self.display_surface.blit(text_surf_1, text_rect_1)
        self.display_surface.blit(text_surf_2, text_rect_2)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.level.game.game_state = "start"
            self.level.game.__init__(self.level.game.locale, self.level.game.music_volume, self.level.game.sounds_volume)

    def update_locale(self, lang: str):
        """
        Update the language of locale and Death screen.

        :param lang: language of the game

        """
        global translation
        global _
        self.locale = lang

        translation = gettext.translation("DeathScreen", os.path.join(os.path.dirname(__file__), "..", "locale", "death_screen"), languages=[lang])
        translation.install()
        _ = translation.gettext
