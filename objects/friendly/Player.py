import pygame
import pygame.sprite
import pygame.key
import pygame.mouse
import pygame.math
from config.Config import *
from objects.main.Entity import Entity
from objects.weapon.Bullet import Bullet
from objects.weapon.ShootingWeapon import ShootingWeapon
from objects.weapon.Bow import Bow
from objects.weapon.Shield import Shield


class Player(Entity):
    """ """
    def __init__(self, level, groups, position):
        super().__init__(level, groups, PLAYER_SPRITE_PATH, PLAYER_SIZE, position, PLAYER_ABS_ACCEL, PLAYER_MAX_SPEED, PLAYER_HEALTH, max_health=PLAYER_MAX_HEALTH, energy=PLAYER_ENERGY, max_energy=PLAYER_MAX_ENERGY) # move constants from config to __init__ (to create player with certain health, weapon, etc, in new location)
        self.weapons = [Bow(self.level, self),]
        # self.weapons = [ShootingWeapon(self.level, SHOOTING_WEAPON_SPRITE_PATH, self, SHOOTING_WEAPON_DISTANCE, WEAPON_COOLDOWN, BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH )]  # TODO: move to inventory later
        self.curr_weapon = 0    # index of self.weapons array
        self.shield = Shield(self.level, (self.level.shield, self.level.visible), SHIELD_SPRITE_PATH, self, SHIELD_DISTANCE, SHIELD_COOLDOWN)
        self.dust = 1500

    def input(self):
        """ """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.accel.y = -1
            self.status = 'up'
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.accel.y = 1
            self.status = 'down'
        else:
            self.accel.y = 0

        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self.accel.x = 1
            self.status = 'right'
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.accel.x = -1
            self.status = 'left'
        else:
            self.accel.x = 0


        # self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - self.pos
        # self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - pygame.math.Vector2(pygame.display.get_surface().get_size()[0]//2, pygame.display.get_surface().get_size()[1]//2)

        if keys[pygame.K_LSHIFT]:
            self.sprint_on()
        else:
            self.sprint_off()

        # self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - self.pos
        self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - pygame.math.Vector2(pygame.display.get_surface().get_size()[0]//2, pygame.display.get_surface().get_size()[1]//2)
        if self.look_angle.length() != 0:
            self.look_angle = self.look_angle.normalize()

        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            self.weapons[self.curr_weapon].spawn_bullet(self.look_angle)
        if mouse[2]:
            self.shield.reflect_bullets()

    def update_weapons(self, dt):
        """

        :param dt: 

        """
        for weapon in self.weapons:
            weapon.update(dt)

    def update(self, dt):
        """

        :param dt: 

        """
        self.input()
        self.update_weapons(dt)
        self.move(self.sprint)

    # def get_hit(self, damage):  # overload later for invincible time
    #     return super().get_hit(damage)
