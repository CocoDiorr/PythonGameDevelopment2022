import pygame
import pygame.math
from objects.main.Entity import Entity
from config.Config import *


class Turret(Entity):
    def __init__(self, level, groups, position, angle: pygame.math.Vector2, image_path):
        super().__init__(level, groups, position, 0, 0, -1, image_path, look_angle=angle)
    
    def equip_weapon(self, weapon):
        self.weapon = weapon

    def update(self, dt):
        self.weapon.spawn_bullet(self.look_angle)
        self.weapon.update(dt)