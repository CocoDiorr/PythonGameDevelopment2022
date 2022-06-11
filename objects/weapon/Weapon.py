import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from config.Config import *


class Weapon(pygame.sprite.Sprite):
    """Basic weapon class."""

    def __init__(
        self, level, groups, image_path, owner, owner_distance, cooldown, extra_scale=1
    ):
        super().__init__(groups)
        self.level = level
        self.start_image = pygame.image.load(image_path).convert_alpha()
        width, height = self.start_image.get_width(), self.start_image.get_height()
        self.start_image = pygame.transform.scale(self.start_image, (width * SCALE * extra_scale, height * SCALE * extra_scale))
        self.image = self.start_image
        self.rect = self.image.get_rect()
        self.owner = owner
        self.owner_distance = owner_distance
        self.last_use = cooldown
        self.cooldown = cooldown

        # check order of Level.bullets_update and Level.visible.update - self.uses is necessary because of this order
        self.uses = [False, False]

    def update(self, dt):
        """Update weapon position and using.

        :param dt: delta time for main loop updating

        """
        self.last_use += dt
        self.move()
        self.update_uses()

    def move(self):
        """Change weapon position.

        :return:


        """

        self.rect = self.image.get_rect()
        self.pos = self.owner.pos + self.owner.look_angle * self.owner_distance
        self.rect.center = self.pos

    def update_uses(self):
        """Update weapon using.

        :return:


        """
        if all(self.uses):
            self.uses = [False for _ in self.uses]
        elif any(self.uses):
            false_index = self.uses.index(False)
            self.uses[false_index] = True
