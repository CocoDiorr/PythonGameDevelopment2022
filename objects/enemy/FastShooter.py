from objects.enemy.Enemy import Enemy
from config.Config import *
from objects.weapon.ShootingWeapon import ShootingWeapon


class FastShooter(Enemy):
    """ """
    def __init__(self, level, position):
        super().__init__(level, (level.visible, level.entity), FAST_SHOOTER_ANIMATION, position, FAST_SHOOTER_ABS_ACCEL, FAST_SHOOTER_MAX_SPEED, FAST_SHOOTER_HEALTH, FAST_SHOOTER_ATTACK_RADIUS, FAST_SHOOTER_NOTICE_RADIUS)
        self.equip_weapon(ShootingWeapon(level, SHOOTING_WEAPON_SPRITE_PATH, self, SHOOTING_WEAPON_DISTANCE, 0.5 * WEAPON_COOLDOWN, 0.8 * BULLET_SPEED, 0.5 * BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH))
