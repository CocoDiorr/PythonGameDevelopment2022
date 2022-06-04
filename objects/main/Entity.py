import pygame
import pygame.math
import pygame.sprite
from config.Config import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, level, groups, image_path, position, abs_accel, max_speed, health, look_angle: pygame.math.Vector2 = pygame.math.Vector2(1, 0)):
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
        if look_angle.length() == 0:
            look_angle = pygame.math.Vector2(1, 0)
        self.look_angle = look_angle.normalize()

    def move(self):
        if self.accel.length() != 0:
            self.accel.scale_to_length(self.abs_accel)
        if self.accel.x == 0:
            if abs(self.speed.x) <= 1e-3:
                self.speed.x = 0
            self.speed.x *= self.speed_fade
        if self.accel.y == 0:
            if abs(self.speed.y) <= 1e-3:
                self.speed.y = 0
            self.speed.y *= self.speed_fade

        self.speed += self.accel
        if self.speed.length() >= self.max_speed and self.max_speed:
            self.speed.scale_to_length(self.max_speed)

        self.pos.x += self.speed.x
        self.rect.center = self.pos
        self.collision('horizontal')
        
        self.pos.y += self.speed.y
        self.rect.center = self.pos
        self.collision('vertical')

    def collision(self, direction):
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
        self.health -= damage
        if self.health <= 0:
            self.kill()

