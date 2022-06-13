import pygame.math

from objects.weapon.Shuriken import Shuriken
from objects.enemy.Enemy import Enemy
from config.Config import *


class Ninja(Enemy):
    """Enemy ninja class."""
    def __init__(self, level: "Level", position: pygame.math.Vector2):
        """
        Create ninja.

        :param level: Level
        :param position: position where ninja is created
        """
        super().__init__(level, (level.visible, level.entity), NINJA_ANIMATION, FAST_SHOOTER_SOUNDS, position, NINJA_ABS_ACCEL, NINJA_MAX_SPEED, NINJA_HEALTH, NINJA_ATTACK_RADIUS, NINJA_NOTICE_RADIUS)
        self.equip_weapon(Shuriken(level, self))
