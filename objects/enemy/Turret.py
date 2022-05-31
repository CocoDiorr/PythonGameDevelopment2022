import pygame
import pygame.math
from objects.main.Entity import Entity
from config.Config import *


class Turret(Entity):
    def __init__(self, groups, position, angle: pygame.math.Vector2, obstacle_sprites, bullets, image_path):
        super().__init__(groups, position, 0, 0, -1, image_path, obstacle_sprites, bullets, look_angle=angle)
    
    def equip_weapon(self, weapon):
        self.weapon = weapon

    def update(self, dt):
        self.weapon.spawn_bullet(self.look_angle)
        self.weapon.update(dt)