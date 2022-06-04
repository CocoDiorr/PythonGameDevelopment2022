import pygame
import pygame.sprite
import pygame.math
import pygame.transform
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.MeleeWeapon import MeleeWeapon


class Shield(MeleeWeapon):
    def __init__(self, level, groups, image_path, owner, owner_distance, cooldown):
        super().__init__(level, groups, image_path, owner, owner_distance, cooldown)
        self.reflect2 = False

    def reflect_bullets(self):
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.use = True

    def redirect_bullet(self, bullet: Bullet):
        new_speed = self.owner.look_angle * bullet.speed.length() * BULLET_REFLECTION_ACCELERATION
        bullet.set_speed(new_speed)
        bullet.damage *= BULLET_REFLECTION_DAMAGE_UP

    def update(self, dt):
        super().update(dt)
        self.move()
        # check order of Level.bullets_update and Level.visible.update - reflect2 is necessary because of this order
        if self.reflect2:
            self.use = False
            self.reflect2 = False
        elif self.use:
            self.reflect2 = True
