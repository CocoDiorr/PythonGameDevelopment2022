from objects.enemy.Enemy import Enemy
from config.Config import *
from objects.weapon.Weapon import Weapon


class Turret(Enemy):
    def __init__(self, level, position):
        super().__init__(level, (level.visible, level.obstacle, level.entity), TURRET_PATH, position, 0, 0, TURRET_HEALTH, TURRET_ATTACK_RADIUS, TURRET_NOTICE_RADIUS)
        self.equip_weapon(Weapon(level, self, 1.1 * BULLET_SPEED, 4 * BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, 4 * WEAPON_COOLDOWN))
