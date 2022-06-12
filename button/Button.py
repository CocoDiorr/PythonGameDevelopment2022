import pygame
import os
from audio.soundpack.SoundPack import SoundPack
from config.Config import COMPANION_BUTTON, COMPANION_COLORS, BUTTON_SOUNDS


class Button:
    """ """
    def __init__(self, parent, pos, w, h, text, action=None, args=None, numb=None, max_numb=None):
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
        """ """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_rect = pygame.Rect.inflate(self.rect, 20, 20)
        else:
            self.text_rect = self.rect

    def click(self):
        """ """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.parent.buttons_event and not self.pressed:
                if self.args:
                    self.sounds.play("click")
                    self.action(*self.args)
                else:
                    self.sounds.play("click")
                    self.action()
                self.pressed = True
                self.parent.buttons_event = None
            else:
                self.pressed = False
        elif self.numb == self.max_numb:
            self.parent.buttons_event = None


    def display(self, surface):
        """

        :param surface: 

        """
        self.hover()
        self.click()
        pygame.draw.rect(surface, COMPANION_BUTTON["MAIN_COLOR"], self.text_rect, 0, 10)
        pygame.draw.rect(surface, COMPANION_BUTTON["OUTLINE_COLOR"], self.text_rect, 10, 10)
        surface.blit(self.text_surface, (self.rect.left + (self.rect.w - self.text_surface.get_size()[0]) // 2,\
                                         self.rect.top + (self.rect.h - self.text_surface.get_size()[1]) // 2))
