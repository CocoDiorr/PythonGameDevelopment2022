import pygame
import pygame.sprite
from objects.friendly.Player import Player
from objects.main.red_square import Square
from objects.enemy.Enemy import Enemy
from config.Config import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.entity_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        self.player = Player((self.visible_sprites, self.entity_sprites,), (50, 50), self.obstacle_sprites, self.bullets)
        Square((self.visible_sprites, self.obstacle_sprites,), (400, 400))   # TODO: turn to solid object (make class)
        self.enemy = Enemy((self.visible_sprites, self.entity_sprites), (400, 50), BASE_ENEMY_ABS_ACCEL, BASE_ENEMY_MAX_SPEED, "rectangle", BASE_ENEMY_HEALTH, self.obstacle_sprites, self.bullets, self.player)

    def bullets_update(self):
        self.bullets.update()
        obstacles_collide = pygame.sprite.groupcollide(self.bullets, self.obstacle_sprites, False, False)
        for bullet, obstacles in obstacles_collide.items():
            bullet.kill()
        entity_collide = pygame.sprite.groupcollide(self.bullets, self.entity_sprites, False, False)
        for bullet, entities in entity_collide.items():
            for entity in entities:
                if entity != bullet.weapon.owner:
                    bullet.kill()
                    entity.get_hit(bullet.damage)
            



    def run(self, dt):
        self.visible_sprites.draw(self.display_surface)
        self.bullets.draw(self.display_surface)
        self.visible_sprites.update(dt)
        # self.enemy.enemy_update(self.player)
        self.bullets_update()


