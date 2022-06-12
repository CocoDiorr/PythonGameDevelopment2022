"""
This module is used to pull individual sprites from sprite sheets.
"""
import pygame
from config.Config import *


class SpriteSheet(object):
    """Class used to grab images out of a sprite sheet."""

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, x, y, width, height, colour):
        """

        :param x: param y:
        :param width: param height:
        :param colour: 
        :param y: 
        :param height: 

        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (SCALE * width, SCALE * height))
        image.set_colorkey(colour)

        return image

    # def get_image(self, x, y, width, height):
    #     """ Grab a single image out of a larger spritesheet
    #         Pass in the x, y location of the sprite
    #         and the width and height of the sprite. """
    #
    #     # Create a new blank image
    #     image = pygame.Surface((width, height)).convert_alpha()
    #
    #     # Copy the sprite from the large sheet onto the smaller image
    #     image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
    #
    #     # Assuming black works as the transparent color
    #     image.set_colorkey(BLACK)
    #
    #     # Return the image
    #     return image

    def get_animations(self) -> dict[str, list]:
        """ """
        animations = {'down': [], 'up': [], 'left': [], 'right': [],
                      'down_idle': [], 'up_idle': [], 'left_idle': [], 'right_idle': []}
        states = ('down', 'up', 'left', 'right')
        separating = (0, 16, 32, 48)
        for state, hor in zip(states, separating):
            animations[state + '_idle'] = [self.get_image(hor, separating[0], 16, 16, BLACK)]
            for vert in separating:
                animations[state].append(self.get_image(hor, vert, 16, 16, BLACK))
        return animations

    # def get_idle_list(self, horizontal) -> list:
    #     image_list = []
    #     for i, hor in enumerate(horizontal):
    #         image_list.append(self.get_image(hor[0], 1, hor[1] - hor[0], 15))
    #
    #     return image_list
