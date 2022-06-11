from objects.enemy.Enemy import Enemy
from config.Config import *
from objects.weapon.Bow import Bow


class Skeleton(Enemy):
    """ """
    def __init__(self, level, position):
        super().__init__(level, (level.visible, level.entity), SKELETON_ANIMATION, position, SKELETON_ABS_ACCEL, SKELETON_MAX_SPEED, SKELETON_HEALTH, SKELETON_ATTACK_RADIUS, SKELETON_NOTICE_RADIUS)
        self.equip_weapon(Bow(level, self))
