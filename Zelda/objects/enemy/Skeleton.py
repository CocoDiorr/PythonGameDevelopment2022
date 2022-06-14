"""This module is used to operate with Skeleton."""
import pygame.math
from Zelda.objects.enemy.Enemy import Enemy
from Zelda.objects.weapon.Bow import Bow
from Zelda.config.Config import (
    SKELETON_ANIMATION,
    SKELETON_SOUNDS,
    SKELETON_ABS_ACCEL,
    SKELETON_MAX_SPEED,
    SKELETON_HEALTH,
    SKELETON_ATTACK_RADIUS,
    SKELETON_NOTICE_RADIUS,
)


class Skeleton(Enemy):
    """Enemy skeleton class."""

    def __init__(self, level, position: pygame.math.Vector2):
        """
        Create skeleton.

        :param level: Level
        :param position: position where skeleton is created
        """
        super().__init__(
            level,
            (level.visible, level.entity),
            SKELETON_ANIMATION,
            SKELETON_SOUNDS,
            position,
            SKELETON_ABS_ACCEL,
            SKELETON_MAX_SPEED,
            SKELETON_HEALTH,
            SKELETON_ATTACK_RADIUS,
            SKELETON_NOTICE_RADIUS,
        )
        self.equip_weapon(Bow(level, self))
