import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from config.Config import *
from objects.weapon.Bullet import Bullet


class MeleeWeapon(pygame.sprite.Sprite):
    def __init__(self, level, groups, image_path, owner, owner_distance, cooldown):
        super().__init__(groups)
        self.level = level
        self.start_image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.owner = owner
        self.owner_distance = owner_distance
        self.last_use = cooldown
        self.cooldown = cooldown
        self.use = False

    def update(self, dt):
        self.last_use += dt
        self.move()

    def move(self):
        self.image = pygame.transform.rotate(self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, 1)))
        if not self.use:
            self.image.set_alpha(SHIELD_ALPHA)  # later add animation
        self.rect = self.image.get_rect()
        self.pos = self.owner.pos + self.owner.look_angle * self.owner_distance
        self.rect.center = self.pos


