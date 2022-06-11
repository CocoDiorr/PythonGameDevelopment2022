from objects.weapon.ShootingWeapon import ShootingWeapon
from config.Config import *


class Shuriken(ShootingWeapon):
    def __init__(self, level, owner):
        super().__init__(
            level,
            SHURIKEN_IMAGE_PATH,
            owner,
            SHURIKEN_DISTANCE,
            SHIELD_COOLDOWN,
            SHURIKEN_SPEED,
            SHURIKEN_DAMAGE,
            SHURIKEN_RANGE,
            SHURIKEN_IMAGE_PATH,
            0.7,
            0.7
        )
