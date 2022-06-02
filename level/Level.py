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
        self.visible = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.entity = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.shield = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        self.player = Player(self, (self.visible, self.entity,), (50, 50))
        Solid(self, (self.visible, self.obstacle,), SOLID_PATH, (400, 400))
        turret = Turret(self, (self.visible, self.obstacle, self.entity), TURRET_PATH, (400, 500), TURRET_HEALTH, TURRET_ATTACK_RADIUS, TURRET_NOTICE_RADIUS)
        turret.equip_weapon(Weapon(self, turret, 0.5 * BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, 4 * WEAPON_COOLDOWN))
        self.enemy = Enemy(self, (self.visible, self.entity), BASE_ENEMY_SPRITE_PATH, (400, 50), BASE_ENEMY_ABS_ACCEL, BASE_ENEMY_MAX_SPEED, BASE_ENEMY_HEALTH, BASE_ENEMY_ATTACK_RADIUS, BASE_ENEMY_NOTICE_RADIUS)
        self.enemy.equip_weapon(Weapon(self, self.enemy, BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, 4 * WEAPON_COOLDOWN))

    def bullets_update(self):
        self.bullets.update()
        entity_collide = pygame.sprite.groupcollide(self.bullets, self.entity, False, False)
        for bullet, entities in entity_collide.items():
            for entity in entities:
                if entity != bullet.weapon.owner:  # mb later change on enemy group and player
                    bullet.kill()
                    entity.get_hit(bullet.damage)
        shield_collide = pygame.sprite.groupcollide(self.shield, self.bullets, False, False)
        for shield, bullets in shield_collide.items():
            if shield.reflect:
                for bullet in bullets:
                    if bullet.weapon.owner != shield.owner:
                        shield.redirect_bullet(bullet)
        obstacles_collide = pygame.sprite.groupcollide(self.bullets, self.obstacle, False, False)
        for bullet, obstacles in obstacles_collide.items():
            for obstacle in obstacles:
                if bullet.weapon.owner != obstacle:
                    bullet.kill()
                    continue
            



    def run(self, dt):
        self.visible.draw(self.display_surface)
        self.bullets.draw(self.display_surface)
        self.visible.update(dt)
        self.bullets_update()


