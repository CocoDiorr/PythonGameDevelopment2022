import pygame
from objects.friendly.Player import Player
from objects.main.red_square import Square
from objects.enemy.Enemy import Enemy
from config.Config import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        self.player = Player((self.visible_sprites,), self.obstacle_sprites)
        Square((self.visible_sprites, self.obstacle_sprites), (400, 400))
        self.enemy = Enemy((self.visible_sprites,), BASE_ENEMY_ABS_ACCEL, BASE_ENEMY_MAX_SPEED, "rectangle", 100, (400, 0), self.obstacle_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.enemy.enemy_update(self.player)



