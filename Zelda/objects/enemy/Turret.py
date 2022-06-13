"""This module is used to operate with Turret."""
import pygame.math
from Zelda.objects.enemy.Enemy import Enemy
from Zelda.config.Config import *
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon
from Zelda.objects.weapon.Bow import Bow


class Turret(Enemy):
    """Enemy turret class."""

    def __init__(self, level: "Level", position: pygame.math.Vector2):
        """
        Create turret.

        :param level: Level
        :param position: position where turret is created
        """
        super().__init__(level, (level.visible, level.obstacle, level.entity), TURRET_ANIMATION, TURRET_SOUNDS, position, 0, 0, TURRET_HEALTH, TURRET_ATTACK_RADIUS, TURRET_NOTICE_RADIUS)
        self.equip_weapon(Bow(level, self))
