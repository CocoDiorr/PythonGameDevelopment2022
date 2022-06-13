"""This module is used to operate with animations."""
import pygame
from Zelda.config.Config import *


class SpriteSheet(object):
    """Class used to grab images out of a sprite sheet."""

    def __init__(self, file_name: str):
        """
        Init the SpriteSheet class.

        :param file_name: file_name of the file, which contains images for the animations
        """
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(
        self, x: int, y: int, width: int, height: int, colour: tuple[int]
    ) -> "pygame.Surface":
        """
        Get the image.

        :param x: x coordinate
        :param width: width of the image
        :param colour: tuple of int for RGB colour
        :param y: y coordinate
        :param height: height of the image
        :return image: get the needed image

        """
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image, (SCALE * width, SCALE * height))
        image.set_colorkey(colour)

        return image

    def get_animations(self) -> dict[str, list]:
        """
        Get the animation.

        :return animations: dictionary of images

        """
        animations = {
            "down": [],
            "up": [],
            "left": [],
            "right": [],
            "down_idle": [],
            "up_idle": [],
            "left_idle": [],
            "right_idle": [],
        }
        states = ("down", "up", "left", "right")
        separating = (0, 16, 32, 48)
        for state, hor in zip(states, separating):
            animations[state + "_idle"] = [
                self.get_image(hor, separating[0], 16, 16, BLACK)
            ]
            for vert in separating:
                animations[state].append(self.get_image(hor, vert, 16, 16, BLACK))
        return animations
