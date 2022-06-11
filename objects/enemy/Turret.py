from objects.enemy.Enemy import Enemy
from config.Config import *
from objects.weapon.ShootingWeapon import ShootingWeapon
from objects.weapon.Bow import Bow


class Turret(Enemy):
    """ """
    def __init__(self, level, position):
        super().__init__(level, (level.visible, level.obstacle, level.entity), TURRET_ANIMATION, position, 0, 0, TURRET_HEALTH, TURRET_ATTACK_RADIUS, TURRET_NOTICE_RADIUS)
        self.equip_weapon(Bow(level, self))
        # self.equip_weapon(ShootingWeapon(level, SHOOTING_WEAPON_SPRITE_PATH, SHOOTING_WEAPON_SIZE, self, SHOOTING_WEAPON_DISTANCE, 4 * WEAPON_COOLDOWN, 1.1 * BULLET_SPEED, 4 * BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, BULLET_SIZE))
