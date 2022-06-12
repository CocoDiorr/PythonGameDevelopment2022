import pygame
import pygame.math
import pygame.sprite
import pygame.rect
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class ShootingWeapon(Weapon):
    """Shooting weapon class. Inherited from Weapon."""
    def __init__(self, level, image_path, sounds, owner, owner_distance, cooldown, bullet_speed, bullet_damage, bullet_range, bullet_img_path, extra_scale=1., bullet_extra_scale=1.): # later <bullet_speed, ..., bullet_img_path> change to prepared Bullet examplar or to fabric
        
        """
        Init shooting weapon.

        :param level: Level
        :param image_path: str: path to weapon image
        :param owner: Entity
        :param owner_distance: int: distance from weapon to owner
        :param cooldown: int: rate of attack
        :param bullet_speed: int: speed of bullet
        :param bullet_damage: int: bullet damage
        :param bullet_range: int: bullet range
        :param bullet_img_path: int: path to bullet image
        :param extra_scale: float: extra scale for special weapon images
        :param bullet_extra_scale: float:  extra scale for special bullet images
        """
        super().__init__(level, (level.visible,), image_path, sounds, owner, owner_distance, cooldown, extra_scale)
        self.bullet_speed = bullet_speed
        self.bullet_damage = bullet_damage
        self.bullet_range = bullet_range
        self.bullet_img_path = bullet_img_path
        self.bullet_extra_scale = bullet_extra_scale

    def update(self, dt: float):
        """Update shooting weapon position and using.

        :param dt: float: delta time for main loop updating
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

        :param angle: pygame.math.Vector2: direction of shot
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