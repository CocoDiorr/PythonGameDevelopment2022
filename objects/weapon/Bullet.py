import pygame
import pygame.math
import pygame.sprite
from config.Config import *


class Bullet(pygame.sprite.Sprite):
    """ """
    def __init__(self, level, groups, image_path, size, position, speed: pygame.math.Vector2, damage, ran, weapon):
        super().__init__(groups)
        self.level = level
        self.weapon = weapon
        self.size = size
        image = pygame.image.load(image_path).convert_alpha()
        self.start_image = pygame.transform.scale(image, size)
        self.image = pygame.transform.rotate(self.start_image,
                                             self.weapon.owner.look_angle.angle_to(pygame.math.Vector2(1, 0)))
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(position)
        self.rect.center = self.pos
        self.speed = speed
        self.damage = damage
        self.start_range = ran
        self.range = ran
        self.owner = self.weapon.owner

    def set_speed(self, new_speed: pygame.math.Vector2):
        """

        :param new_speed: pygame.math.Vector2: 

        """
        self.speed = new_speed

    def move(self):
        """ """
        self.pos += self.speed
        self.rect.center = self.pos
        self.range -= self.speed.length()

    def update(self):
        """ """
        self.move()
        if self.range <= 0:
            self.kill()
