import pygame
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class Shield(Weapon):
    """ """
    def __init__(self, level, groups, image_path, owner, owner_distance, cooldown):
        # maybe change to const path, cooldown
        super().__init__(level, groups, image_path, SHIELD_SIZE, owner, owner_distance, cooldown)

    def move(self):
        self.image = pygame.transform.rotate(self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, 1)))
        super().move()

    def reflect_bullets(self):
        """ """
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True

    def redirect_bullet(self, bullet: Bullet):
        """

        :param bullet: Bullet: 

        """
        new_speed = self.owner.look_angle * bullet.speed.length() * BULLET_REFLECTION_ACCELERATION
        bullet.range += bullet.start_range
        bullet.owner = self.owner
        bullet.image = pygame.transform.rotate(bullet.start_image,
                                            self.owner.look_angle.angle_to(pygame.math.Vector2(1, 0)))
        bullet.set_speed(new_speed)
        bullet.damage *= BULLET_REFLECTION_DAMAGE_UP

