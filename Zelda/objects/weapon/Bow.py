"""This module is used to operate with Bow."""
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon
from Zelda.config.Config import *

# from level.Level import Level
# from objects.friendly.Player import Player


class Bow(ShootingWeapon):
    """Bow Class. Inherited from ShootingWeapon."""

    def __init__(self, level: "Level", owner: "Entity"):
        # later <bullet_speed, ..., bullet_img_path> change to prepared Bullet examplar or to fabric
        """
        Init bow weapon.

        :param level: Level
        :param owner: Entity
        """
        super().__init__(
            level,
            BOW_IMAGE_PATH,
            BOW_SOUNDS,
            owner,
            BOW_DISTANCE,
            BOW_COOLDOWN,
            ARROW_SPEED,
            ARROW_DAMAGE,
            ARROW_RANGE,
            ARROW_IMAGE_PATH,
        )
