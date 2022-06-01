import pygame
import pygame.math
from objects.enemy.Enemy import Enemy
from config.Config import *

# Пока в таком виде. Если не будет разных видов турелей,
# можно убрать все, кроме level и position, а остальное на константы заменить.

class Turret(Enemy):
    def __init__(self, level, groups, image_path, position, health, attack_radius, notice_radius):
        super().__init__(level, groups, image_path, position, 0, 0, health, attack_radius, notice_radius)
