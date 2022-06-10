import pygame
from config.Config import UI_SETTINGS, PLAYER_MAX_ENERGY, PLAYER_MAX_HEALTH

class UI:
    """ """
    def __init__(self):
        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_SETTINGS["UI_FONT"], UI_SETTINGS["UI_FONT_SIZE"])

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, UI_SETTINGS["HEALTH_BAR_WIDTH"], UI_SETTINGS["BAR_HEIGHT"])
        self.energy_bar_rect = pygame.Rect(10, 38, UI_SETTINGS["ENERGY_BAR_WIDTH"], UI_SETTINGS["BAR_HEIGHT"])

    def show_bar(self, current, max_amount, bg_rect, color):
        """

        :param current: 
        :param max_amount: 
        :param bg_rect: 
        :param color: 

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

    def display(self, player):
        """

        :param player: 

        """
        self.show_bar(player.health, player.max_health, self.health_bar_rect, UI_SETTINGS["UI_COLORS"]["HEALTH"])
        self.show_bar(player.energy, player.max_energy, self.energy_bar_rect, UI_SETTINGS["UI_COLORS"]["ENERGY"])
