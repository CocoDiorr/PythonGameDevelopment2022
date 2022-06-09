import pygame
from config.Config import COMPANION_BUTTON, COMPANION_COLORS


class Button:
    """ """
    def __init__(self, pos, text, action=None, args=None):
        #self.rect = pygame.Rect(l, t, w, h)
        self.x, self.y = pos
        self.action = action
        self.args = args
        self.pressed = False
        self.font = pygame.font.Font(COMPANION_BUTTON["FONT"], COMPANION_BUTTON["FONT_SIZE"])
        self.text_surface = self.font.render(text, 0, COMPANION_BUTTON["FONT_COLOR"])
        self.rect = self.text_surface.get_rect(left=self.x - 10, top=self.y - 10,\
                                          w=self.text_surface.get_size()[0] + 20,\
                                          h=self.text_surface.get_size()[1] + 20)
        self.text_rect = self.rect


    def hover(self):
        """ """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text_rect = pygame.Rect.inflate(self.rect, 20, 20)
        else:
            self.text_rect = self.rect

    def click(self):
        """ """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and not self.pressed:
                if self.args:
                    self.action(*self.args)
                else:
                    self.action()
                self.pressed = True
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.pressed = False

    def display(self, surface):
        """

        :param surface: 

        """
        #self.input()
        self.hover()
        self.click()
        pygame.draw.rect(surface, COMPANION_BUTTON["MAIN_COLOR"], self.text_rect, 0, 10)
        pygame.draw.rect(surface, COMPANION_BUTTON["OUTLINE_COLOR"], self.text_rect, 10, 10)
        surface.blit(self.text_surface, (self.x, self.y))
