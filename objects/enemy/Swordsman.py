from objects.weapon.ColdSteel import ColdSteel
from objects.enemy.Enemy import Enemy
from config.Config import *


class Swordsman(Enemy):
    """ """
    def __init__(self, level, position):
        super().__init__(level, (level.visible, level.entity), SWORDSMAN_PATH, SWORDSMAN_ANIMATION, SWORDSMAN_SIZE, position, SWORDSMAN_ABS_ACCEL, SWORDSMAN_MAX_SPEED, SWORDSMAN_HEALTH, SWORDSMAN_ATTACK_RADIUS, SWORDSMAN_NOTICE_RADIUS)
        self.equip_weapon(ColdSteel(level, (level.visible, level.cold_steels), SWORD_SPRITE_PATH, SWORD_SIZE, self, SWORD_DISTANCE, SWORD_COOLDOWN, SWORD_DAMAGE))

