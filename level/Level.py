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
from menu.EscMenu import EscMenu
from config.Config import *
from level.Support import *
from level.Camera import *


class Level:
    """"""
    def __init__(self, locale, game):

        # settings
        self.game = game
        self.game_state = "active"
        self.locale = locale

        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible = YSortCameraGroup() # pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.entity = pygame.sprite.Group()

        self.bullets = YSortBulletsCameraGroup() # pygame.sprite.Group()

        # Companion
        self.companion = Companion(screen=self.display_surface, level=self)

        # User Interface
        self.ui = UI()
        self.esc_menu = EscMenu(self)

        self.buttons_event = None
        self.shield = pygame.sprite.Group()
        self.cold_steels = pygame.sprite.Group()

        #self.create_map()

    def create_map(self):

        layouts = {
            'boundary': import_csv_layout(LEVEL_0_FLOORBLOCKS),
            'grass': import_csv_layout(LEVEL_0_GRASS),
            'object': import_csv_layout(LEVEL_0_OBJECTS),
            'player': import_csv_layout(LEVEL_0_PLAYER),
            'entities': import_csv_layout(LEVEL_0_ENTITIES),
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Solid((x, y), [self.obstacle], 'invisible')
                        if style == 'grass':
                            # create a grass tile
                            pass
                        if style == 'object':
                            # create an object tile
                            pass
                        if style == 'player':
                            self.player = Player(self, (self.visible, self.entity,), (x, y))
                        if style == 'entities':
                            if col == '2':
                                FastShooter(self, (x, y))
                            elif col == '1':
                                Turret(self, (x, y))
                            elif col == '0':
                                Swordsman(self, (x, y))

        self.companion.player = self.player


    def bullets_update(self):
        """ """
        self.bullets.update()

        entity_collide = pygame.sprite.groupcollide(self.bullets, self.entity, False, False)
        for bullet, entities in entity_collide.items():
            for entity in entities:
                if entity != bullet.owner:  # mb later change on enemy group and player
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
                    if bullet.owner != shield.owner:
                        shield.redirect_bullet(bullet)

        obstacles_collide = pygame.sprite.groupcollide(self.bullets, self.obstacle, False, False)
        for bullet, obstacles in obstacles_collide.items():
            for obstacle in obstacles:
                if bullet.owner != obstacle:
                    bullet.kill()
                    continue

    def companion_call(self):
        """ """
        self.companion.companion_state = "greeting"
        if self.game_state != "companion":
            self.game_state = "companion"
        else:
            self.game_state = "active"

    def esc_menu_call(self):
        """ """
        if self.game_state != "esc":
            self.game_state = "esc"
        else:
            self.game_state = "active"

    def death(self):
        if self.player.health <= 0:
            self.game.game_state = "start"
            self.game.__init__()

    def run(self, dt):

        """

        :param dt:

        """
        # self.visible.draw(self.display_surface)
        self.visible.custom_draw(self.player)
        # self.bullets.draw(self.display_surface)
        self.bullets.custom_draw(self.player)
        self.ui.display(self.player)
        if self.game_state == "active":
            self.visible.update(dt)
            self.bullets_update()
            self.death()
        elif self.game_state == "companion":
            self.companion.display()
        elif self.game_state == "esc":
            self.esc_menu.display()

        # self.enemy.enemy_update(self.player)
