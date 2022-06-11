import pygame
from sys import exit
from os import path
from config.Config import COMPANION_FONT, COMPANION_FONT_SIZE, WINDOW_RESOLUTION,\
                          COMPANION_SIZE, COMPANION_IMAGE, COMPANION_COLORS,\
                          COMPANION_BUTTON
from button.Button import Button
import ipsedixit


class Companion(pygame.sprite.Sprite):
    """Companion class."""
    def __init__(self, screen, level, player=None):
        """
        Initialize the Companion:

            * self.image -- image/surface of the companion
            * self.rect -- corresponding rect to the companion
            * self.to_show -- state of the companion:
                -  0 - initial state
                -  1 - hides
                - -1 - shows up
            * self.to_move -- state of moving:
                -  0 - stays in the place
                -  1 - hides
                - -1 - shows up
        """
        super().__init__()
        self.image = pygame.image.load(COMPANION_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, COMPANION_SIZE)
        self.rect = self.image.get_rect(midbottom=(WINDOW_RESOLUTION[0] - COMPANION_SIZE[0] / 2, WINDOW_RESOLUTION[1]))
        self.font = pygame.font.Font(COMPANION_FONT, COMPANION_FONT_SIZE)
        self.companion_state = "greeting"
        self.player = player
        self.screen = screen
        self.level = level
        self.locale = self.level.locale

        # companion outline
        self.fill_box = pygame.Rect(self.rect.left - 5, self.rect.top - 5, self.rect.w + 5, self.rect.h + 5)

        # message textbox
        self.hi_msg_1 = "Hi, haven't seen you in a while ! <3"
        self.hi_msg_2 = "Do you want a story ?"

        # companion cooldown
        self.call = None
        self.available = True


    def show_msg(self, screen, msg):
        """

        :param screen: 
        :param msg: 

        """

        words = [word.split(' ') for word in msg.splitlines()]
        space = self.font.size(' ')[0]

        max_width, max_height = 30, self.fill_box.h
        x, y = self.fill_box.left, self.fill_box.top + self.fill_box.height - 40
        box_width, box_height = 20, 20
        surfaces = []

        for line in words[::-1]:
            tmp_width, tmp_height = 0, 0
            for word in line[::-1]:
                word_surface = self.font.render(word, 0, COMPANION_COLORS["FONT_COLOR"])
                word_width, word_height = word_surface.get_size()

                if word_height >= tmp_height:
                    tmp_height = word_height
                tmp_width += word_width + space

                if x - word_width < max_width:
                    x = self.fill_box.left
                    y -= word_height
                    box_height += word_height
                x = x - word_width - space
                surfaces.append((word_surface, (x,y)))
            tmp_width -= space



            if tmp_width > box_width:
                box_width = tmp_width
            box_height += tmp_height

            x = self.fill_box.left
            y -= tmp_height

        text_box = pygame.Rect(self.fill_box.left - box_width - 20, WINDOW_RESOLUTION[1] - box_height - 20, box_width + 30, box_height + 20)

        pygame.draw.rect(screen, COMPANION_COLORS["MAIN_COLOR"], text_box, 0, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["OUTLINE_COLOR"], text_box, 10, 20)
        screen.blits(surfaces)

    def yes_button(self, companion):
        """

        :param companion:

        """
        companion.companion_state = "trade"

    def no_button(self,level):
        """

        :param level: 

        """
        level.game_state = "active"


    def greeting(self, screen):
        """

        :param screen: 

        """
        #self.show_msg(self.screen, self.hi_msg)
        text_surface_1 = self.font.render(self.hi_msg_1, 0, COMPANION_COLORS["FONT_COLOR"])
        text_surface_2 = self.font.render(self.hi_msg_2, 0, COMPANION_COLORS["FONT_COLOR"])

        greet_rect = pygame.Rect(self.fill_box.left - text_surface_1.get_size()[0] - 20,\
                                 self.fill_box.top,\
                                 text_surface_1.get_size()[0] + 30,\
                                 self.fill_box.height)
        gradient_rect = pygame.Rect.inflate(greet_rect, -5, -5)

        pygame.draw.rect(screen, COMPANION_COLORS["MAIN_COLOR"], greet_rect, 0, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["OUTLINE_COLOR"], greet_rect, 10, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["GRADIENT"], gradient_rect, 3, 20)
        screen.blit(text_surface_1, (greet_rect.left + 15, greet_rect.top + 20))
        screen.blit(text_surface_2, (greet_rect.left + 15, greet_rect.top + 30 + text_surface_1.get_size()[1]))

        yes = Button(self.level, (greet_rect.left + greet_rect.w * 0.2, greet_rect.top + greet_rect.h * 9 / 16),\
                     greet_rect.w * 0.25, greet_rect.h * 0.35, "Yes", self.yes_button, (self,), 1, 2)
        no = Button(self.level, (greet_rect.left + greet_rect.w * 0.55, greet_rect.top + greet_rect.h * 9 / 16),\
                    greet_rect.w * 0.25, greet_rect.h * 0.35, "No", self.no_button, (self.level,), 2, 2)

        yes.display(screen)
        no.display(screen)

    def trade_button(self, companion, name):
        """
		
        :param companion:
        :param name:
		
        """
        if companion.player.dust >= int(name):
            companion.companion_state = "story"
            companion.player.dust -= int(name)
            companion.txt = path.join("texts", companion.locale , f"{name}.txt")
            with open(companion.txt, "r") as f:
                companion.generator = ipsedixit.Generator(f.read())
            companion.tell = companion.generator.paragraphs(1)

    def trade(self, screen):
        """

        :param screen:

        """
        text_surface = self.font.render("How much would you pay ?", 0, COMPANION_COLORS["FONT_COLOR"])

        trade_rect = pygame.Rect(self.fill_box.left - text_surface.get_size()[0] * 2 + 4,\
                                 self.fill_box.top,\
                                 text_surface.get_size()[0] * 2,\
                                 self.fill_box.height)
        gradient_rect = pygame.Rect.inflate(trade_rect, -5, -5)

        pygame.draw.rect(screen, COMPANION_COLORS["MAIN_COLOR"], trade_rect, 0, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["OUTLINE_COLOR"], trade_rect, 10, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["GRADIENT"], gradient_rect, 3, 20)

        screen.blit(text_surface, (trade_rect.left + trade_rect.width / 4, trade_rect.top + 10))
        buttons = []
        buttons.append(Button(self.level, (trade_rect.left + trade_rect.w * 0.25,\
                              trade_rect.top + trade_rect.h / 4 + 15),\
                              trade_rect.w * 0.25, trade_rect.h * 0.25, "100", self.trade_button, (self, "100"), 1, 4))
        buttons.append(Button(self.level, (trade_rect.left + trade_rect.w * 0.55,\
                              trade_rect.top + trade_rect.h / 4 + 15), \
                              trade_rect.w * 0.25, trade_rect.h * 0.25, "300", self.trade_button, (self, "300"), 2, 4))
        buttons.append(Button(self.level, (trade_rect.left + trade_rect.w * 0.25,\
                              trade_rect.top + trade_rect.h / 2 + 35),\
                              trade_rect.w * 0.25, trade_rect.h * 0.25, "500", self.trade_button, (self, "500"), 3, 4))
        buttons.append(Button(self.level, (trade_rect.left + trade_rect.w * 0.55,\
                              trade_rect.top + trade_rect.h / 2 + 35),\
                              trade_rect.w * 0.25, trade_rect.h * 0.25, "1000", self.trade_button, (self, "1000"), 4, 4))

        for button in buttons:
            button.display(screen)

    def story(self):
        """ """
        self.show_msg(self.screen, *self.tell)

    def display(self):
        """ """
        pygame.draw.rect(self.screen, COMPANION_COLORS["MAIN_COLOR"], self.fill_box, 0, 20)
        pygame.draw.rect(self.screen, COMPANION_COLORS["OUTLINE_COLOR"], self.fill_box, 10, 20)
        gradient_rect = pygame.Rect.inflate(self.fill_box, -5, -5)
        pygame.draw.rect(self.screen, COMPANION_COLORS["GRADIENT"], gradient_rect, 3, 20)

        if self.companion_state == "greeting":
            self.greeting(self.screen)
        elif self.companion_state == "trade":
            self.trade(self.screen)
        elif self.companion_state == "story":
            self.story()

        self.screen.blit(self.image, self.rect)
