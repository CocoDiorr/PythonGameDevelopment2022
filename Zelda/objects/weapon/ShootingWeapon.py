"""This module is used to operate with base Shooting weapon class."""
import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from Zelda.config.Config import *
from Zelda.objects.weapon.Bullet import Bullet
from Zelda.objects.weapon.Weapon import Weapon


class ShootingWeapon(Weapon):
    """Shooting weapon class. Inherited from Weapon."""

    def __init__(self, level: "Level", image_path: str, sounds: dict[str, set[str]], owner: "Entity", owner_distance: int, cooldown: int, bullet_speed: int, bullet_damage: int, bullet_range: int, bullet_img_path: str, extra_scale=1., bullet_extra_scale=1.):
        """
        Init shooting weapon.

        :param level: Level
        :param image_path: path to weapon image
        :param owner: Entity
        :param owner_distance: distance from weapon to owner
        :param cooldown: rate of attack
        :param bullet_speed: speed of bullet
        :param bullet_damage: bullet damage
        :param bullet_range: bullet range
        :param bullet_img_path: path to bullet image
        :param extra_scale: extra scale for special weapon images
        :param bullet_extra_scale: extra scale for special bullet images
        """
        super().__init__(level, (level.visible,), image_path, sounds, owner, owner_distance, cooldown, extra_scale)
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullet_range = bullet_range
        self.bullet_img_path = bullet_img_path
        self.bullet_extra_scale = bullet_extra_scale

    def update(self, dt: float):
        """Update shooting weapon position and using.

        :param dt: delta time for main loop updating
        """
        super().update(dt)

    def move(self):
        """Change shooting weapon position."""
        self.image = pygame.transform.rotate(
            self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, 1))
        )
        super().move()

    def spawn_bullet(self, angle: pygame.math.Vector2):
        """Make a shot.

        Create bullet in shooting weapon center position.

        :param angle: direction of shot
        """
        if self.last_use >= self.cooldown:
            self.last_use = 0
            if angle.length() != 0:
                angle = angle.normalize()
            if hasattr(self.owner, "speed"):
                speed = angle * (
                    self.bullet_speed + angle.dot(self.owner.speed)
                )  # added speed from owner, but in direction of shoot
            else:
                speed = angle * self.bullet_speed
            self.sounds.play("shoot")
            self.level.bullets.add(

                Bullet(
                    self.level,
                    (self.level.bullets,),
                    self.bullet_img_path,
                    self.rect.center,
                    speed,
                    self.bullet_damage,
                    self.bullet_range,
                    self,
                    self.bullet_extra_scale,
                )
            )
