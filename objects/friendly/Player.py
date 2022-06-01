import pygame
import pygame.sprite
import pygame.key
import pygame.mouse
import pygame.math
from config.Config import *
from objects.main.Entity import Entity
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon
from companion.Companion import Companion


class Player(Entity):
    def __init__(self, level, groups, position):
        super().__init__(level, groups, PLAYER_SPRITE_PATH, position, PLAYER_ABS_ACCEL, PLAYER_MAX_SPEED, PLAYER_HEALTH) # move constants from config to __init__ (to create player with certain health, weapon, etc, in new location)
        self.weapons = [Weapon(self.level, self, BULLET_SPEED, BULLET_DAMAGE, BULLET_RANGE, BULLET_SPRITE_PATH, WEAPON_COOLDOWN)]  # TODO: move to inventory later
        self.curr_weapon = 0    # index of self.weapons array
        self.companion = self.level.companion

        # companion cooldown
        self.companion_time = None
        self.can_call_companion = True

    def input(self):
        keys = pygame.key.get_pressed()
        #event = pygame.event.get()

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
        elif keys[pygame.K_h]:
            if self.can_call_companion:
                self.can_call_companion = False
                self.companion_time = pygame.time.get_ticks()
                if self.companion.to_show == 1 or self.companion.to_show == 0:
                    self.companion.to_show = -1
                    self.companion.to_move = -1
                elif self.companion.to_show == -1:
                    self.companion.to_show = 1
                    self.companion.to_move = 1
        else:
            self.accel.x = 0

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
        #         if self.companion.to_show == 1 or self.companion.to_show == 0:
        #             self.companion.to_show = -1
        #             self.companion.to_move = -1
        #         elif self.companion.to_show == -1:
        #             self.companion.to_show = 1
        #             self.companion.to_move = 1

        mouse = pygame.mouse.get_pressed()
        self.look_angle = pygame.math.Vector2(pygame.mouse.get_pos()) - self.pos
        if mouse[0]:
            self.weapons[self.curr_weapon].spawn_bullet(self.look_angle)

    def update_weapons(self, dt):
        for weapon in self.weapons:
            weapon.update(dt)

    def companion_cooldown(self):
        if not self.can_call_companion:
            curr_time = pygame.time.get_ticks()
            if curr_time - self.companion_time >= 1000:
                self.can_call_companion = True

    def update(self, dt):
        self.input()
        self.companion_cooldown()
        self.update_weapons(dt)
        self.companion.draw(self.level.display_surface)
        self.companion.move()

        self.move()

    # def get_hit(self, damage):  # overload later for invincible time
    #     return super().get_hit(damage)
