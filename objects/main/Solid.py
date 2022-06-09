import pygame
from objects.weapon.ShootingWeapon import Weapon
from config.Config import *

class Solid(pygame.sprite.Sprite):
    """ """
    def __init__(self, level, groups, image_path, position):
        super().__init__(groups)
        self.level = level
        self.image = pygame.image.load(image_path).convert_alpha()
        self.pos = position
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    