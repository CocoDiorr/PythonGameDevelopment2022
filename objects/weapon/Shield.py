import pygame
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class Shield(Weapon):
    """Shield class. Inherited from Weapon."""

    def __init__(
        self,
        level: "Level",
        owner: "Entity",
    ):
        """
        Init shield.

        :param level: Level
        :param owner: Entity
        """
        super().__init__(level, (level.shield, level.visible), SHIELD_SPRITE_PATH, SHIELD_SOUNDS, owner, SHIELD_DISTANCE, SHIELD_COOLDOWN)

    def move(self):
        """Change shield position."""
        self.image = pygame.transform.rotate(
            self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, 1))
        )
        if not any(self.uses):
            self.image.set_alpha(SHIELD_ALPHA)  # later add animation
        super().move()

    def reflect_bullets(self):
        """Allow redirect bullet."""
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True

    def redirect_bullet(self, bullet: Bullet):
        """Redirect bullet to shield.owner look angle. Change bullet damage.

        :param bullet: bullet to redirect
        """
        self.sounds.play("reflect")
        new_speed = (
            self.owner.look_angle
            * bullet.speed.length()
            * BULLET_REFLECTION_ACCELERATION
        )
        bullet.range += bullet.start_range
        bullet.owner = self.owner
        bullet.image = pygame.transform.rotate(
            bullet.start_image,
            self.owner.look_angle.angle_to(pygame.math.Vector2(1, 0)),
        )
        bullet.set_speed(new_speed)
        bullet.damage *= BULLET_REFLECTION_DAMAGE_UP
