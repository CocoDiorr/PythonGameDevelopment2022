"""This module is used to operate with UI."""
import pygame
import os
from Zelda.config.Config import UI_SETTINGS, PLAYER_MAX_ENERGY, PLAYER_MAX_HEALTH


class UI:
    """UI class."""

    def __init__(self):
        """Init the UI class."""
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_SETTINGS["UI_FONT"], UI_SETTINGS["UI_FONT_SIZE"])

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, UI_SETTINGS["HEALTH_BAR_WIDTH"], UI_SETTINGS["BAR_HEIGHT"])
        self.energy_bar_rect = pygame.Rect(10, 38, UI_SETTINGS["ENERGY_BAR_WIDTH"], UI_SETTINGS["BAR_HEIGHT"])

        self.dust_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "..", "pics", "dust.png")).convert_alpha()
        self.dust_image = pygame.transform.scale(self.dust_image, (30, 30))
        self.dust_rect = self.dust_image.get_rect(bottomright=(self.display_surface.get_size()[0] - 10, self.display_surface.get_size()[1] - 20))

    def show_bar(self, current: int, max_amount: int, bg_rect: "pygame.rect", color: ...):
        """
        Draw the bar.

        :param current: current amount of something
        :param max_amount: maximum amount of somethinf
        :param bg_rect: pygame.rect
        :param color: color, RGB or hex

        """
        back_rect = pygame.Rect.inflate(bg_rect, 6, 6)
        pygame.draw.rect(self.display_surface, UI_SETTINGS["UI_COLORS"]["BG_COLOR"], back_rect, 0, 10)

        # stats converting
        ratio = current / max_amount
        current_width = bg_rect.w * ratio
        current_rect = bg_rect.copy()
        current_rect.w = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect, 0, 30)
        pygame.draw.rect(self.display_surface, UI_SETTINGS["UI_COLORS"]["BORDER_COLOR"], back_rect, 3, 10)

    def show_dust(self, dust: int):
        """
        Draw the number of dust.

        :param dust: current player's dust

        """
        text_surf = self.font.render(str(int(dust)), False, UI_SETTINGS["UI_FONT_COLOR"])
        text_rect = text_surf.get_rect(midright=self.dust_rect.midleft)

        self.display_surface.blit(self.dust_image, self.dust_rect)
        self.display_surface.blit(text_surf, text_rect)

    def display(self, player: "Player"):
        """
        Draw the bar.

        :param player: Player

        """
        self.show_bar(player.health, PLAYER_MAX_HEALTH, self.health_bar_rect, UI_SETTINGS["UI_COLORS"]["HEALTH"])
        self.show_bar(player.energy, PLAYER_MAX_ENERGY, self.energy_bar_rect, UI_SETTINGS["UI_COLORS"]["ENERGY"])

        self.show_dust(player.dust)
