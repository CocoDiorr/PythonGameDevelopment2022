import pygame
import pygame.sprite
import pygame.math
from objects.friendly.Player import Player
from objects.main.Solid import Solid
from objects.weapon.Weapon import Weapon
from objects.enemy.Enemy import Enemy
from objects.enemy.Turret import Turret
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
        Solid((self.visible_sprites, self.obstacle_sprites,), (400, 400), "pics/red_square.jpg")
        turret = Turret((self.visible_sprites, self.obstacle_sprites,), (400, 500), pygame.math.Vector2(-1, 0), self.obstacle_sprites, self.bullets, "pics/red_square.jpg")
        turret.equip_weapon(Weapon(turret, self.bullets, BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, 4 * WEAPON_COOLDOWN))
        self.enemy = Enemy((self.visible_sprites, self.entity_sprites), (400, 50), BASE_ENEMY_ABS_ACCEL, BASE_ENEMY_MAX_SPEED, "rectangle", BASE_ENEMY_HEALTH, self.obstacle_sprites, self.bullets, self.player)

    def bullets_update(self):
        self.bullets.update()
        obstacles_collide = pygame.sprite.groupcollide(self.bullets, self.obstacle_sprites, False, False)
        for bullet, obstacles in obstacles_collide.items():
            for obstacle in obstacles:
                if bullet.weapon.owner != obstacle:
                    bullet.kill()
                    continue
        entity_collide = pygame.sprite.groupcollide(self.bullets, self.entity_sprites, False, False)
        for bullet, entities in entity_collide.items():
            for entity in entities:
                if entity != bullet.weapon.owner:   # mb later change on enemy group and player
                    bullet.kill()
                    entity.get_hit(bullet.damage)
            



    def run(self, dt):
        self.visible_sprites.draw(self.display_surface)
        self.bullets.draw(self.display_surface)
        self.visible_sprites.update(dt)
        # self.enemy.enemy_update(self.player)
        self.bullets_update()


