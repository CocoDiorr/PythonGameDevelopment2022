import os
import pygame
import pygame.sprite
import pygame.math
from objects.friendly.Player import Player
from objects.main.Solid import Solid
from objects.weapon.ShootingWeapon import Weapon
from objects.weapon.ColdSteel import ColdSteel
from objects.enemy.Enemy import Enemy
from objects.enemy.Turret import Turret
from objects.enemy.FastShooter import FastShooter
from objects.enemy.Swordsman import Swordsman
from companion.Companion import Companion
from ui.UI import UI
from config.Config import *


class Level:
    """ """
    def __init__(self):

        # settings
        self.game_state = "active"

        self.display_surface = pygame.display.get_surface()
        self.visible = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.entity = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()


        # Companion
        self.companion = Companion(screen=self.display_surface, level=self)

        # User Interface
        self.ui = UI()

        #self.events = []
        self.shield = pygame.sprite.Group()
        self.cold_steels = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        """ """
        self.player = Player(self, (self.visible, self.entity,), (50, 50))
        Solid(self, (self.visible, self.obstacle,), SOLID_PATH, (400, 400))
        turret = Turret(self, (400, 500))
        swordsman = Swordsman(self, (400, 50))
        fast_shooter = FastShooter(self, (400, 150))

    def bullets_update(self):
        """ """
        self.bullets.update()

        entity_collide = pygame.sprite.groupcollide(self.bullets, self.entity, False, False)
        for bullet, entities in entity_collide.items():
            for entity in entities:
                if entity != bullet.weapon.owner:  # mb later change on enemy group and player
                    bullet.kill()
                    entity.get_hit(bullet.damage)

        cold_steel_collide = pygame.sprite.groupcollide(self.cold_steels, self.entity, False, False)
        for cold_steel, entities in cold_steel_collide.items():
            if any(cold_steel.uses):
                for entity in entities:
                    if entity != cold_steel.owner:
                        entity.get_hit(cold_steel.damage)

        shield_collide = pygame.sprite.groupcollide(self.shield, self.bullets, False, False)
        for shield, bullets in shield_collide.items():
            if any(shield.uses):
                for bullet in bullets:
                    if bullet.weapon.owner != shield.owner:
                        shield.redirect_bullet(bullet)

        obstacles_collide = pygame.sprite.groupcollide(self.bullets, self.obstacle, False, False)
        for bullet, obstacles in obstacles_collide.items():
            for obstacle in obstacles:
                if bullet.weapon.owner != obstacle:
                    bullet.kill()
                    continue

    def companion_call(self):
        """ """
        if self.game_state != "companion":
            self.game_state = "companion"
        else:
            self.game_state = "active"

    def run(self, dt):
        """

        :param dt: 

        """
        self.visible.draw(self.display_surface)
        self.bullets.draw(self.display_surface)
        if self.game_state == "active":
            self.visible.update(dt)
            self.bullets_update()
        elif self.game_state == "companion":
            self.companion.display()
        self.ui.display(self.player)
        # self.enemy.enemy_update(self.player)
