import pygame
import pygame.math
from config.Config import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, groups, abs_accel, max_speed, image_path, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.accel = pygame.math.Vector2()
        self.speed = pygame.math.Vector2()
        self.max_speed = max_speed
        self.abs_accel = abs_accel
        self.speed_fade = ENTITY_SPEED_FADE
        self.obstacle_sprites = obstacle_sprites

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
        if self.speed.length() >= self.max_speed:
            self.speed.scale_to_length(self.max_speed)

        self.rect.move_ip((self.speed.x, 0))
        # self.rect.x += self.speed.x   # don't work well with speed fading
        self.collision('horizontal')
        self.rect.move_ip((0, self.speed.y))
        # self.rect.y += self.speed.y
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.speed.x > 0:  # moving right
                        self.rect.right = sprite.rect.left
                    if self.speed.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.speed.y > 0:  # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.speed.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom
