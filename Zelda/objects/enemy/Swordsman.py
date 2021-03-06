"""This module is used to operate with Swordsman."""
import pygame.math
from Zelda.objects.weapon.ColdSteel import ColdSteel
from Zelda.objects.enemy.Enemy import Enemy
from Zelda.config.Config import (
    SWORDSMAN_ANIMATION,
    SWORDSMAN_SOUNDS,
    SWORDSMAN_ABS_ACCEL,
    SWORDSMAN_MAX_SPEED,
    SWORDSMAN_HEALTH,
    SWORDSMAN_ATTACK_RADIUS,
    SWORDSMAN_NOTICE_RADIUS,
    SWORD_SPRITE_PATH,
    SWORD_SOUNDS,
    SWORD_DISTANCE,
    SWORD_COOLDOWN,
    SWORD_DAMAGE,
)


class Swordsman(Enemy):
    """Enemy swordsman class."""

    def __init__(self, level: "Level", position: pygame.math.Vector2):
        """
        Create swordsman.

        :param level: Level
        :param position: position where swordsman is created
        """
        super().__init__(
            level,
            (level.visible, level.entity),
            SWORDSMAN_ANIMATION,
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
                SWORD_SPRITE_PATH,
                SWORD_SOUNDS,
                self,
                SWORD_DISTANCE,
                SWORD_COOLDOWN,
                SWORD_DAMAGE,
            )
        )
