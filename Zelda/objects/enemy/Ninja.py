"""This module is used to operate with Ninja."""
import pygame.math
from Zelda.objects.weapon.Shuriken import Shuriken
from Zelda.objects.enemy.Enemy import Enemy
from Zelda.config.Config import (
    NINJA_ANIMATION,
    FAST_SHOOTER_SOUNDS,
    NINJA_ABS_ACCEL,
    NINJA_MAX_SPEED,
    NINJA_HEALTH,
    NINJA_ATTACK_RADIUS,
    NINJA_NOTICE_RADIUS,
)


class Ninja(Enemy):
    """Enemy ninja class."""

    def __init__(self, level: "Level", position: pygame.math.Vector2):
        """
        Create ninja.

        :param level: Level
        :param position: position where ninja is created
        """
        super().__init__(
            level,
            (level.visible, level.entity),
            NINJA_ANIMATION,
            FAST_SHOOTER_SOUNDS,
            position,
            NINJA_ABS_ACCEL,
            NINJA_MAX_SPEED,
            NINJA_HEALTH,
            NINJA_ATTACK_RADIUS,
            NINJA_NOTICE_RADIUS,
        )
        self.equip_weapon(Shuriken(level, self))
