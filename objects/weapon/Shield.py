import pygame
import pygame.sprite
import pygame.math
import pygame.transform
from config.Config import *
from objects.weapon.Bullet import Bullet

class Shield(pygame.sprite.Sprite):
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
        self.reflect = False
        self.reflect2 = False

    def move(self):
        self.image = pygame.transform.rotate(self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, 1)))
        if not self.reflect:
            self.image.set_alpha(SHIELD_ALPHA)  # later add animation
        self.rect = self.image.get_rect()
        self.pos = self.owner.pos + self.owner.look_angle * self.owner_distance
        self.rect.center = self.pos

    def reflect_bullets(self):
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.reflect = True

    def redirect_bullet(self, bullet: Bullet):
        new_speed = self.owner.look_angle * bullet.speed.length() * BULLET_REFLECTION_ACCELERATION
        bullet.set_speed(new_speed)
        bullet.damage *= BULLET_REFLECTION_DAMAGE_UP

    def update(self, dt):
        self.last_use += dt
        self.move()
        # check order of Level.bullets_update and Level.visible.update - reflect2 is necessary because of this order
        if self.reflect2:
            self.reflect = False
            self.reflect2 = False
        elif self.reflect:
            self.reflect2 = True