import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class ShootingWeapon(Weapon):
    def __init__(self, level, image_path, owner, owner_distance, cooldown, bullet_speed, bullet_damage, bullet_range, bullet_img_path): # later <bullet_speed, ..., bullet_img_path> change to prepared Bullet examplar or to fabric
        super().__init__(level, (level.visible,), image_path, owner, owner_distance, cooldown)
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullet_range = bullet_range
        self.bullet_img_path = bullet_img_path

    def update(self, dt):
        super().update(dt)

    def spawn_bullet(self, angle: pygame.math.Vector2):
        if self.last_use >= self.cooldown:
            self.last_use = 0
            if angle.length() != 0:
                angle = angle.normalize()
            if hasattr(self.owner, "speed"):
                speed = angle * (self.bullet_speed + angle.dot(self.owner.speed))   # added speed from owner, but in direction of shoot
            else:
                speed = angle * self.bullet_speed
            self.level.bullets.add(Bullet(self.level, (self.level.bullets,), self.bullet_img_path, self.rect.center, speed, self.bullet_damage, self.bullet_range, self))
