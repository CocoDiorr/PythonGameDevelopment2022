import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from audio.soundpack.SoundPack import SoundPack
from config.Config import *


class Weapon(pygame.sprite.Sprite):
    """Base weapon class."""

    def __init__(
        self, level, groups: tuple, image_path: str, sounds, owner, owner_distance: int, cooldown: int, extra_scale=1.
    ):
        """
        Init base weapon.

        :param level: Level
        :param groups: tuple
        :param image_path: str: path to weapon image
        :param owner: Entity
        :param owner_distance: int: distance from weapon to owner
        :param cooldown: int: rate of attack
        :param extra_scale: Default value = 1.: scale for special images
        """
        super().__init__(groups)
        self.level = level
        self.start_image = pygame.image.load(image_path).convert_alpha()
        width, height = self.start_image.get_width(), self.start_image.get_height()
        self.start_image = pygame.transform.scale(self.start_image, (int(width * SCALE * extra_scale), int(height * SCALE * extra_scale)))
        self.image = self.start_image
        self.rect = self.image.get_rect()
        self.sounds = SoundPack(sounds, self.level.game.sounds_volume)
        self.owner = owner
        self.owner_distance = owner_distance
        self.last_use = 0
        self.cooldown = cooldown

        # check order of Level.bullets_update and Level.visible.update - self.uses is necessary because of this order
        self.uses = [False, False]

    def update(self, dt: float):
        """Update weapon position and using.

        :param dt: float: delta time for main loop updating
        """
        self.last_use += dt
        self.move()
        self.update_uses()
        self.sounds.update_volume(self.level.game.sounds_volume)

    def move(self):
        """Change weapon position."""

        self.rect = self.image.get_rect()
        self.pos = self.owner.pos + self.owner.look_angle * self.owner_distance
        self.rect.center = self.pos

    def update_uses(self):
        """Update weapon using."""

        if all(self.uses):
            self.uses = [False for _ in self.uses]
        elif any(self.uses):
            false_index = self.uses.index(False)
            self.uses[false_index] = True
