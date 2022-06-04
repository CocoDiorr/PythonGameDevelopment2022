import pygame
import pygame.sprite
import pygame.key
import pygame.mouse
import pygame.math
from config.Config import *
from objects.main.Entity import Entity
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class Player(Entity):
    def __init__(self, level, groups, position):
        super().__init__(level, groups, PLAYER_SPRITE_PATH, position, PLAYER_ABS_ACCEL, PLAYER_MAX_SPEED, PLAYER_HEALTH, PLAYER_ENERGY) # move constants from config to __init__ (to create player with certain health, weapon, etc, in new location)
        self.weapons = [Weapon(self.level, self, BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, WEAPON_COOLDOWN)]  # TODO: move to inventory later
        self.curr_weapon = 0    # index of self.weapons array


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.accel.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.accel.y = 1
            self.status = 'down'
        else:
            self.accel.y = 0

        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.accel.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.accel.x = -1
            self.status = 'left'
        else:
            self.accel.x = 0

        mouse = pygame.mouse.get_pressed()
        self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - self.pos
        if mouse[0]:
            self.weapons[self.curr_weapon].spawn_bullet(self.look_angle)

    def update_weapons(self, dt):
        for weapon in self.weapons:
            weapon.update(dt)

    def update(self, dt):
        self.input()
        self.update_weapons(dt)

        self.move()

    # def get_hit(self, damage):  # overload later for invincible time
    #     return super().get_hit(damage)
