import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from audio.soundpack.SoundPack import SoundPack
from config.Config import *


class Weapon(pygame.sprite.Sprite):
    """ """
    def __init__(self, level, groups, image_path, image_size, sounds, owner, owner_distance, cooldown):
        super().__init__(groups)
        self.level = level
        self.start_image = pygame.image.load(image_path).convert_alpha()
        self.start_image = pygame.transform.scale(self.start_image, image_size)
        self.image = self.start_image
        self.rect = self.image.get_rect()
        self.sounds = SoundPack(sounds, self.level.game.sounds_volume)
        self.owner = owner
        self.owner_distance = owner_distance
        self.last_use = cooldown
        self.cooldown = cooldown

        # check order of Level.bullets_update and Level.visible.update - self.uses is necessary because of this order
        self.uses = [False, False]

    def update(self, dt):
        """

        :param dt: 

        """
        self.last_use += dt
        self.move()
        self.update_uses()

    def move(self):
        """ """
        if not any(self.uses):
            self.image.set_alpha(SHIELD_ALPHA)  # later add animation
        self.rect = self.image.get_rect()
        self.pos = self.owner.pos + self.owner.look_angle * self.owner_distance
        self.rect.center = self.pos

    def update_uses(self):
        """ """
        if all(self.uses):
            self.uses = [False for _ in self.uses]
        elif any(self.uses):
            false_index = self.uses.index(False)
            self.uses[false_index] = True


