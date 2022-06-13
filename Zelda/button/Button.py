"""This module is used to operate with buttons."""
from typing import Callable
import pygame
from Zelda.audio.soundpack.SoundPack import SoundPack
from Zelda.config.Config import COMPANION_BUTTON, COMPANION_COLORS, BUTTON_SOUNDS


class Button:
    """Button class."""

    def __init__(self, parent: "Level", pos: tuple[int], w: int, h: int, text: str, action: Callable[..., None] = None, args: "args" = None, numb: int = None, max_numb: int = None):
        """
        Init the button class.

        :param parent: Level
        :param pos: position, (x, y)
        :param w: width
        :param h: height
        :param text: button text
        :param action: function for the button
        :param args: args for the function
        :param numb: number of the button
        :param max_numb: number of buttons on the screen at the moment
        """
        self.parent = parent
        self.x, self.y = pos
        self.action = action
        self.args = args
        self.pressed = False
        self.font = pygame.font.Font(COMPANION_BUTTON["FONT"], COMPANION_BUTTON["FONT_SIZE"])
        self.text = text
        self.text_surface = self.font.render(text, 0, COMPANION_BUTTON["FONT_COLOR"])
        self.rect = self.text_surface.get_rect(left=self.x - 12, top=self.y - 10,\
                                               w=int(w), h=int(h))
        self.text_rect = self.rect
        self.numb = numb
        self.max_numb = max_numb
        self.sounds = SoundPack(BUTTON_SOUNDS, self.parent.game.sounds_volume)

    def hover(self):
        """Hover the button."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_rect = pygame.Rect.inflate(self.rect, 20, 20)
        else:
            self.text_rect = self.rect

    def click(self):
        """Click the button."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.parent.buttons_event and not self.pressed:
                if self.args:
                    self.sounds.update_volume(self.parent.game.sounds_volume)
                    self.sounds.play("click")
                    self.action(*self.args)
                else:
                    self.sounds.update_volume(self.parent.game.sounds_volume)
                    self.sounds.play("click")
                    self.action()
                self.pressed = True
                self.parent.buttons_event = None
            else:
                self.pressed = False
        elif self.numb == self.max_numb:
            self.parent.buttons_event = None


    def display(self, surface: "pygame.surface"):
        """
        Draw the surface on the screen.

        :param surface: "pygame.surface"

        """
        self.hover()
        self.click()
        pygame.draw.rect(surface, COMPANION_BUTTON["MAIN_COLOR"], self.text_rect, 0, 10)
        pygame.draw.rect(surface, COMPANION_BUTTON["OUTLINE_COLOR"], self.text_rect, 10, 10)
        surface.blit(self.text_surface, (self.rect.left + (self.rect.w - self.text_surface.get_size()[0]) // 2,\
                                         self.rect.top + (self.rect.h - self.text_surface.get_size()[1]) // 2))
