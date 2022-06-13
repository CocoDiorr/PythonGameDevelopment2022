"""This module is used to implement camera and draw moving map."""
import pygame
from Zelda.config.Config import *


class YSortCameraGroup(pygame.sprite.Group):
    """Make camera draw the map, obstacles and visibles with offset."""

    def __init__(self):
        """Init camera for map, obstacles and visibles with offset."""
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load(LEVEL_0_PIC_PATH).convert()
        self.floor_surf = pygame.transform.scale2x(self.floor_surf)
        self.floor_surf = pygame.transform.scale2x(self.floor_surf)
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player: "Player"):
        """
        Draw the map, obstacles and visibles.

        :param player: Player

        """
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width + int(TILESIZE/2)
        self.offset.y = player.rect.centery - self.half_height + int(TILESIZE/2)

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        self.offset.x -= int(TILESIZE/2)
        self.offset.y -= int(TILESIZE / 2)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)


class YSortBulletsCameraGroup(pygame.sprite.Group):
    """Make camera draw bullets with offset."""

    def __init__(self):
        """Init camera for bullets with offset."""
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player: "Player"):
        """
        Draw bullets.

        :param player: Player

        """
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
