import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from config.Config import *
from objects.weapon.Bullet import Bullet

class Weapon:
    def __init__(self, level, owner, bullet_speed, bullet_damage, bullet_range, bullet_img_path, cooldown):
        self.level = level
        self.owner = owner
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullet_range = bullet_range
        self.bullet_img_path = bullet_img_path
        self.last_shoot = cooldown
        self.cooldown = cooldown
    
    def update(self, dt):
        self.last_shoot += dt

    def spawn_bullet(self, angle: pygame.math.Vector2):
        if self.last_shoot >= self.cooldown:
            self.last_shoot = 0
            if angle.length() != 0:
                angle = angle.normalize()
            if hasattr(self.owner, "speed"):
                speed = angle * (self.bullet_speed + angle.dot(self.owner.speed))   # added speed from owner, but in direction of shoot
            else:
                speed = angle * self.bullet_speed
            self.level.bullets.add(Bullet(self.level, (self.level.bullets), self.owner.pos, speed, self.bullet_damage, self.bullet_range, self, self.bullet_img_path))

