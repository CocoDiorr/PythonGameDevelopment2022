import pygame
import pygame.math
import pygame.sprite
from config.Config import *


class Entity(pygame.sprite.Sprite):
    """ """
    def __init__(self, level, groups, image_path, position, abs_accel, max_speed, health, max_health=None, energy=None, max_energy=None, look_angle: pygame.math.Vector2 = pygame.math.Vector2(1, 0)):
        super().__init__(groups)
        self.level = level
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(position)
        self.rect.center = self.pos
        self.accel = pygame.math.Vector2()
        self.speed = pygame.math.Vector2()
        self.max_speed = max_speed
        self.abs_accel = abs_accel
        self.speed_fade = ENTITY_SPEED_FADE
        self.health = health
        self.sprint = [False, True]
        if max_health is None:
            self.max_health = health
        else:
            self.max_health = max_health
        self.energy = energy
        if max_energy is None:
            self.max_energy = energy
        else:
            self.max_energy = max_energy
        if look_angle.length() == 0:
            look_angle = pygame.math.Vector2(1, 0)
        self.look_angle = look_angle.normalize()

    def sprint_on(self):
        self.sprint[0] = True
    def sprint_off(self):
        self.sprint[0] = False

    def move(self, sprint=False):
        """ """
        if self.accel.length() != 0:
            self.accel.scale_to_length(self.abs_accel)
        if self.accel.x == 0:
            if abs(self.speed.x) <= ENTITY_SPEED_ZERO:
                self.speed.x = 0
            self.speed.x *= self.speed_fade
        if self.accel.y == 0:
            if abs(self.speed.y) <= ENTITY_SPEED_ZERO:
                self.speed.y = 0
            self.speed.y *= self.speed_fade

        self.speed += self.accel
        if self.max_speed and self.speed.length() >= self.max_speed:
            self.speed.scale_to_length(self.max_speed)

        curr_max_speed = self.max_speed
        curr_speed = pygame.math.Vector2(self.speed)
        if not (self.energy is None):
            if self.sprint[0] and self.sprint[1] and self.energy > 0 and self.accel.length() != 0:
                self.energy = max(self.energy - ENERGY_SPEND, 0)
                curr_max_speed *= SPRINT_MULTIPLIER
                curr_speed *= SPRINT_MULTIPLIER
            else:
                self.energy = min(self.energy + ENERGY_RECOVER, self.max_energy)
                if self.energy >= MIN_SPRINT_ENERGY:
                    self.sprint[1] = True
                else:
                    self.sprint[1] = False
            if curr_max_speed and curr_speed.length() >= curr_max_speed:
                curr_speed.scale_to_length(curr_max_speed)

        self.pos.x += curr_speed.x
        self.rect.center = self.pos
        self.collision('horizontal')

        self.pos.y += curr_speed.y
        self.rect.center = self.pos
        self.collision('vertical')


    def collision(self, direction):
        """

        :param direction: 

        """
        if direction == 'horizontal':
            collided_sprite = pygame.sprite.spritecollideany(self, self.level.obstacle)
            if collided_sprite:
                if self.speed.x > 0:  # moving right
                    self.rect.right = collided_sprite.rect.left
                    self.pos = pygame.math.Vector2(self.rect.center)
                if self.speed.x < 0:  # moving left
                    self.rect.left = collided_sprite.rect.right
                    self.pos = pygame.math.Vector2(self.rect.center)

        if direction == 'vertical':
            collided_sprite = pygame.sprite.spritecollideany(self, self.level.obstacle)
            if collided_sprite:
                if self.speed.y > 0:  # moving down
                    self.rect.bottom = collided_sprite.rect.top
                    self.pos = pygame.math.Vector2(self.rect.center)
                if self.speed.y < 0:  # moving up
                    self.rect.top = collided_sprite.rect.bottom
                    self.pos = pygame.math.Vector2(self.rect.center)

    def get_hit(self, damage):
        """

        :param damage: 

        """
        self.health = max(self.health - damage, 0)
        if self.health == 0:
            self.kill()
            if "weapon" in self.__dict__:
                self.weapon.kill()
            if "shield" in self.__dict__:
                self.shield.kill()
            # add for player weapons