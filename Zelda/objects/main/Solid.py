"""This module is used to operate with base solid class."""
import pygame
from Zelda.config.Config import TILESIZE


class Solid(pygame.sprite.Sprite):
    """Solid objects class."""

    def __init__(
        self,
        pos: pygame.math.Vector2,
        groups: tuple,
        sprite_type: str,
        surface=pygame.Surface((TILESIZE, TILESIZE)),
    ):
        """
        Init solid object.

        :param pos: solid object position
        :param groups: can be visible, obstacle or both
        :param sprite_type: type of solid object
        :param surface: surface where to draw solid object
        """
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = surface
        if sprite_type == "object":
            self.rect = self.image.get_rect(center=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(center=pos)

        self.hitbox = self.rect.inflate(-10, -10)
