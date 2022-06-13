"""This module is used to operate with Shuriken."""
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon
from Zelda.config.Config import *


class Shuriken(ShootingWeapon):
    """Shuriken weapon class."""

    def __init__(self, level: "Level", owner: "Entity"):
        """
        Init shuriken weapon.

        :param level: Level
        :param owner: Entity
        """
        super().__init__(
            level,
            SHURIKEN_IMAGE_PATH,
            SHURIKEN_SOUNDS,
            owner,
            SHURIKEN_DISTANCE,
            SHIELD_COOLDOWN,
            SHURIKEN_SPEED,
            SHURIKEN_DAMAGE,
            SHURIKEN_RANGE,
            SHURIKEN_IMAGE_PATH,
            SHURIKEN_EXTRA_SCALE,
            SHURIKEN_EXTRA_SCALE,
        )
