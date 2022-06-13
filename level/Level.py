import os
import pygame
from random import choice
import pygame.sprite
import pygame.math
from random import randint
from objects.friendly.Player import Player
from objects.main.Solid import Solid
from objects.enemy.Turret import Turret
from objects.enemy.Ninja import Ninja
from objects.enemy.Swordsman import Swordsman
from objects.enemy.StrongSwordsman import StrongSwordsman
from objects.enemy.Skeleton import Skeleton
from companion.Companion import Companion
from ui.UI import UI
from menu.EscMenu import EscMenu
from menu.DeathScreen import DeathScreen
from config.Config import *
from level.Support import *
from level.Camera import *


class Level:
    """ """
    def __init__(self, locale, game):

        # settings
        self.game = game
        self.game_state = "active"
        self.locale = locale

        self.display_surface = pygame.display.get_surface()
        # sprite group setup
        self.visible = YSortCameraGroup()
        self.obstacle = pygame.sprite.Group()
        self.entity = pygame.sprite.Group()

        self.bullets = YSortBulletsCameraGroup()

        # Companion
        self.companion = Companion(screen=self.display_surface, level=self)

        # User Interface
        self.ui = UI()
        self.esc_menu = EscMenu(self)
        self.death_screen = DeathScreen(self)

        # Buttons events
        self.buttons_event = None

        self.shield = pygame.sprite.Group()
        self.cold_steels = pygame.sprite.Group()
        # self.create_map()

    def create_map(self):
        """ Create a map."""

        layouts = {
            'boundary': import_csv_layout(LEVEL_0_FLOORBLOCKS),
            'grass': import_csv_layout(LEVEL_0_GRASS),
            'object': import_csv_layout(LEVEL_0_OBJECTS),
            'player': import_csv_layout(LEVEL_0_PLAYER),
            'entities': import_csv_layout(LEVEL_0_ENTITIES),
        }
        graphics = {
            'grass': import_folder(GRASS_PICS_FOLDER),
            'objects': import_folder(OBJECTS_PICS_FOLDER),
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
                            random_grass_image = graphics['grass'][f'{col}.png']
                            random_grass_image = pygame.transform.scale(random_grass_image, (TILESIZE, TILESIZE))
                            Solid((x, y), [self.visible, self.obstacle], 'grass', random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][f'{col}.png']
                            surf = pygame.transform.scale(surf, (2 * TILESIZE, 2 * TILESIZE))
                            Solid((x, y), [self.visible, self.obstacle], 'object', surf)
                            pass
                        if style == 'player':
                            self.player = Player(self, (self.visible, self.entity,), (x, y))
                        if style == 'entities':
                            tmp = randint(1,5)
                            if tmp == 1:
                                Skeleton(self, (x, y))
                            elif tmp == 2:
                                Ninja(self, (x, y))
                            elif tmp == 3:
                                Turret(self, (x, y))
                            elif tmp == 4:
                                Swordsman(self, (x, y))
                            else:
                                StrongSwordsman(self, (x, y))
                            # if col == '45':
                            #     Skeleton(self, (x, y))
                            #     # Ninja(self, (x, y))
                            # elif col == '46':
                            #     Turret(self, (x, y))
                            # elif col == '47':
                            #     Swordsman(self, (x, y))
                            # else:
                            #     Skeleton(self, (x, y))

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
                print(obstacle)
                if bullet.owner != obstacle:
                    if obstacle.sprite_type != 'invisible':
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
        """ """
        if self.player.health <= 0:
            self.game_state = "death"

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
        elif self.game_state == "death":
            self.death_screen.display()

        # self.enemy.enemy_update(self.player)

    def update_locale(self, lang):
        self.death_screen.update_locale(lang)
        self.esc_menu.update_locale(lang)
        self.companion.update_locale(lang)
