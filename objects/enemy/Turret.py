import pygame
import pygame.math
from objects.main.Entity import Entity
from config.Config import *


class Turret(Entity):
    def __init__(self, groups, position, angle: pygame.math.Vector2, obstacle_sprites, bullets, image_path):
        super().__init__(groups, position, 0, 0, -1, image_path, obstacle_sprites, bullets)
        if angle.length() == 0:
            angle = pygame.math.Vector2(1, 0)
        self.angle = angle.normalize()
    
    def equip_weapon(self, weapon):
        self.weapon = weapon

    def update(self, dt):
        self.weapon.spawn_bullet(self.angle)
        self.weapon.update(dt)