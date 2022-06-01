import pygame
from sys import exit
from os import path
import ipsedixit

class Companion(pygame.sprite.Sprite):
    """Companion class."""
    def __init__(self, player=None):
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
        #self.image = pygame.image.load('../pics/cat/sitting.png').convert_alpha()
        self.image = pygame.image.load(path.join('pics', 'cat', 'sitting.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect(midbottom=(850, 300))
        self.to_show = 0  # 0 - stop, 1 -> hide, -1 -> show up
        self.to_move = 0
        self.player = player

        # companion cooldown
        self.call = None
        self.available = True


    def input(self):
        pass



    def move(self):
        """Makes the cat move."""
        self.rect.x += 4 * self.to_move
        self.stop()

    def stop(self):
        """Stop the cat."""
        if self.rect.x < 680 or self.rect.x > 850:
            self.to_move = 0

    def handle_event(self, event):
        """
        Handling the 'h' key pressing
        If the 'h' key is pressed then:
            - if to_show == 0 or 1 -> to_show = -1 and the cat shows up
            - if to_show == -1 -> to_show = 1 and the cat hides
        """
        if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            if self.to_show == 1 or self.to_show == 0:
                self.to_show = -1
                self.to_move = -1
            elif self.to_show == -1:
                self.to_show = 1
                self.to_move = 1

    def draw(self, screen):
        """Display cat on the screen."""
        screen.blit(self.image, self.rect)


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
