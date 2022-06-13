"""This module is used to operate with Player."""
import pygame
import pygame.sprite
import pygame.key
import pygame.mouse
import pygame.math
from Zelda.config.Config import *
from Zelda.objects.main.Entity import Entity
from Zelda.objects.weapon.Bullet import Bullet
from Zelda.objects.weapon.ColdSteel import ColdSteel
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon
from Zelda.objects.weapon.Bow import Bow
from Zelda.objects.weapon.Shield import Shield
from Zelda.objects.enemy.Enemy import Enemy


class Player(Entity):
    """Player class."""

    def __init__(self, level: "Level", groups: tuple, position: pygame.math.Vector2):
        """
        Init player.

        :param level: Level
        :param groups: tuple
        :param position: position where to create player
        """
        super().__init__(
            level,
            groups,
            PLAYER_ANIMATION_PATH,
            PLAYER_SOUNDS,
            position,
            PLAYER_ABS_ACCEL,
            PLAYER_MAX_SPEED,
            PLAYER_HEALTH,
            max_health=PLAYER_MAX_HEALTH,
            energy=PLAYER_ENERGY,
            max_energy=PLAYER_MAX_ENERGY,
        )  # move constants from config to __init__ (to create player with certain health, weapon, etc, in new location)
        self.weapons = [
            Bow(self.level, self),
        ]
        self.curr_weapon = 0  # index of self.weapons array
        self.shield = Shield(self.level, self)
        self.dust = 1500

    def input(self):
        """Input from keyboard and mouse."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.accel.y = -1
            self.status = "up"
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.accel.y = 1
            self.status = "down"
        else:
            self.accel.y = 0

        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.accel.x = 1
            self.status = "right"
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.accel.x = -1
            self.status = "left"
        else:
            self.accel.x = 0

        if keys[pygame.K_LSHIFT]:
            self.sprint_on()
        else:
            self.sprint_off()

        self.look_angle = pygame.math.Vector2(
            pygame.mouse.get_pos()
        ) - pygame.math.Vector2(
            pygame.display.get_surface().get_size()[0] // 2,
            pygame.display.get_surface().get_size()[1] // 2,
        )
        if self.look_angle.length() != 0:
            self.look_angle = self.look_angle.normalize()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.weapons[self.curr_weapon].spawn_bullet(self.look_angle)
        if mouse[2]:
            self.shield.reflect_bullets()

    def update_weapons(self, dt: float):
        """
        Update position and using of player weapons.

        :param dt: delta time for main loop updating
        """
        for weapon in self.weapons:
            weapon.update(dt)

    def update(self, dt: float):
        """
        Update player position and weapons.

        :param dt: delta time for main loop updating
        """
        self.sounds.update_volume(self.level.game.sounds_volume)
        self.set_animation_state()
        self.animate()
        self.input()
        self.update_weapons(dt)
        self.move(self.sprint)

    def get_dust(self, enemy: Enemy):
        """
        Add dust to pay for stories.

        :param enemy: killed enemy
        """
        if hasattr(enemy, "weapon") and not (enemy.weapon is None):
            self.sounds.play("dust")
            if isinstance(enemy.weapon, ShootingWeapon):
                self.dust += int(
                    (
                        GET_DUST_HEALTH_MULTIPLIER * enemy.max_health
                        + GET_DUST_WEAPON_MULTIPLIER
                        * enemy.weapon.bullet_damage
                        / enemy.weapon.cooldown
                    )
                    * GET_DUST_MULTIPLIER
                )
            elif isinstance(enemy.weapon, ColdSteel):
                self.dust += int(
                    (
                        GET_DUST_HEALTH_MULTIPLIER * enemy.max_health
                        + GET_DUST_WEAPON_MULTIPLIER
                        * enemy.weapon.damage
                        / enemy.weapon.cooldown
                    )
                    * GET_DUST_MULTIPLIER
                )
