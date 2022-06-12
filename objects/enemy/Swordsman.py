from objects.weapon.ColdSteel import ColdSteel
from objects.enemy.Enemy import Enemy
from config.Config import *


class Swordsman(Enemy):
    """Enemy swordsman class."""
    def __init__(self, level, position: tuple):
        """
        Create swordsman.

        :param level: Level
        :param position: tuple: position where swordsman is created
        """
        super().__init__(level, (level.visible, level.entity), SWORDSMAN_ANIMATION, position, SWORDSMAN_ABS_ACCEL, SWORDSMAN_MAX_SPEED, SWORDSMAN_HEALTH, SWORDSMAN_ATTACK_RADIUS, SWORDSMAN_NOTICE_RADIUS)
        self.equip_weapon(ColdSteel(level, (level.visible, level.cold_steels), SWORD_SPRITE_PATH, self, SWORD_DISTANCE, SWORD_COOLDOWN, SWORD_DAMAGE))

