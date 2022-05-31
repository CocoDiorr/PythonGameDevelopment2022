import pygame
from objects.weapon.Weapon import Weapon
from config.Config import *

class Solid(pygame.sprite.Sprite):
    def __init__(self, groups, position, image_path):
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.pos = position
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    