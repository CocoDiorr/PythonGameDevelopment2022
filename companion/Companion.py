import pygame
from sys import exit
from os import path
from config.Config import COMPANION_FONT, COMPANION_FONT_SIZE, WINDOW_RESOLUTION,\
                          COMPANION_SIZE, COMPANION_IMAGE, COMPANION_COLORS
import ipsedixit

class Companion(pygame.sprite.Sprite):
    """Companion class."""
    def __init__(self, screen, player=None):
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
        self.to_show = False  # 0 - stop, 1 -> hide, -1 -> show up
        self.to_move = 0
        self.player = player
        self.screen = screen

        # companion outline
        self.fill_box = pygame.Rect(self.rect.left - 5, self.rect.top - 5, self.rect.w + 5, self.rect.h + 5)

        # message textbox
        #self.msg_box = pygame.Rect(self.rect.left - 200, self.rect.top + 5, self.rect.w, self.rect.h / 2)
        self.hi_msg = "Hi, haven't seen you in a while ! \n<3 \n asfjahsjahgjhajsghkahgkshgasg \n asgsag \n asgasg"

        # companion cooldown
        self.call = None
        self.available = True


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_h]:
            if self.available:
                self.available = False
                self.call = pygame.time.get_ticks()
                self.to_show = not self.to_show
                # if self.companion.to_show == 1 or self.companion.to_show == 0:
                #     self.companion.to_show = -1
                #     self.companion.to_move = -1
                # elif self.companion.to_show == -1:
                #     self.companion.to_show = 1
                #     self.companion.to_move = 1
                #

    def cooldown(self):
        if not self.available:
            curr_time = pygame.time.get_ticks()
            if curr_time - self.call >= 500:
                self.available = True

    def show_msg(self, screen, msg):

        words = [word.split(' ') for word in msg.splitlines()]
        space = self.font.size(' ')[0]

        max_width, max_height = 20, self.fill_box.h
        x, y = self.fill_box.left, self.fill_box.top + self.fill_box.height - 30
        box_width, box_height = 20, 20
        surfaces = []

        for line in words[::-1]:
            tmp_width, tmp_height = 0, 0
            for word in line[::-1]:
                word_surface = self.font.render(word, 0, COMPANION_COLORS["COMPANION_FONT_COLOR"])
                word_width, word_height = word_surface.get_size()

                if word_height >= tmp_height:
                    tmp_height = word_height
                tmp_width += word_width + space

                if x - word_width <= max_width:
                    x = self.fill_box.left
                    y -= word_height
                x = x - word_width - space
                surfaces.append((word_surface, (x,y)))



            if tmp_width > box_width:
                box_width = tmp_width
            box_height += tmp_height

            x = self.fill_box.left
            y -= tmp_height

        text_box = pygame.Rect(self.fill_box.left - box_width - 20, WINDOW_RESOLUTION[1] - box_height - 20, box_width + 30, box_height + 20)

        pygame.draw.rect(screen, COMPANION_COLORS["COMPANION_MAIN_COLOR"], text_box, 0, 20)
        pygame.draw.rect(screen, COMPANION_COLORS["COMPANION_OUTLINE_COLOR"], text_box, 10, 20)
        screen.blits(surfaces)

    def display(self):
        self.input()
        self.cooldown()
        #if self.to_show:
        pygame.draw.rect(self.screen, COMPANION_COLORS["COMPANION_MAIN_COLOR"], self.fill_box, 0, 20)
        pygame.draw.rect(self.screen, COMPANION_COLORS["COMPANION_OUTLINE_COLOR"], self.fill_box, 10, 20)
        self.show_msg(self.screen, self.hi_msg)
        self.screen.blit(self.image, self.rect)

    #def show_msg(self, msg):


    # def move(self):
    #     """Makes the cat move."""
    #     self.rect.x += 4 * self.to_move
    #     if self.rect.x < 600 or self.rect.x > 850:
    #         self.to_move = 0
        #self.stop()

    # def stop(self):
    #     """Stop the cat."""
    #     if self.rect.x < 680 or self.rect.x > 850:
    #         self.to_move = 0

    # def handle_event(self, event):
    #     """
    #     Handling the 'h' key pressing
    #     If the 'h' key is pressed then:
    #         - if to_show == 0 or 1 -> to_show = -1 and the cat shows up
    #         - if to_show == -1 -> to_show = 1 and the cat hides
    #     """
    #     if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
    #         if self.to_show == 1 or self.to_show == 0:
    #             self.to_show = -1
    #             self.to_move = -1
    #         elif self.to_show == -1:
    #             self.to_show = 1
    #             self.to_move = 1

    # def draw(self, screen):
    #     """Display cat on the screen."""
    #     screen.blit(self.image, self.rect)




# class PopUpMessage(pygame.sprite.Sprite):
#     def __init__(self, text_generator, companion):
#         """
#         text_generator -> ipse dixit generator
#         companion -> rect to catch up to
#         """
#         self.generator = text_generator
#         self.dialogue_box = pygame.image.load('../pics/text_box/box.png').convert_alpha()
#         self.rect = self.dialogue_box.get_rect(bottomright = (companion.rect.topleft))




# pygame.init()
# screen = pygame.display.set_mode((800, 400))
# clock = pygame.time.Clock()

# Companion
#companion = Companion()


# Bg
# sky_surface = pygame.image.load('../pics/Sky.png').convert()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#
#         companion.handle_event(event)
#
#     screen.blit(sky_surface, (0, 0))
#     companion.draw(screen)
#     companion.move()
#
#
#
#     pygame.display.update()
#     clock.tick(60)
