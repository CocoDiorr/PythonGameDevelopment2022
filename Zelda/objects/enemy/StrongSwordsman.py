"""This module is used to operate with StrongSwordsman."""
import pygame.math
from Zelda.objects.weapon.ColdSteel import ColdSteel
from Zelda.objects.enemy.Enemy import Enemy
from Zelda.config.Config import *


class StrongSwordsman(Enemy):
    """Enemy strong swordsman class."""

    def __init__(self, level, position: pygame.math.Vector2):
        """
        Create strong swordsman.

        :param level: Level
        :param position: position where strong swordsman is created
        """
        super().__init__(
            level,
            (level.visible, level.entity),
            STRONG_SWORDSMAN_ANIMATION,
            SWORDSMAN_SOUNDS,
            position,
            SWORDSMAN_ABS_ACCEL,
            SWORDSMAN_MAX_SPEED,
            SWORDSMAN_HEALTH,
            SWORDSMAN_ATTACK_RADIUS,
            SWORDSMAN_NOTICE_RADIUS,
        )
        self.equip_weapon(
            ColdSteel(
                level,
                (level.visible, level.cold_steels),
                STRONG_SWORD_SPRITE_PATH,
                SWORD_SOUNDS,
                self,
                SWORD_DISTANCE,
                SWORD_COOLDOWN,
                STRONG_SWORD_DAMAGE,
            )
        )
