import pygame
from config.Config import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, speed, image_path):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.direction = pygame.math.Vector2()
        self.speed = speed

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def collision(self,direction):

        pass
