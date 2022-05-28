import pygame
from config.Config import *
from objects.main.Entity import Entity


class Player(Entity):
    def __init__(self, groups, obstacle_sprites):
        super().__init__(groups, PLAYER_ABS_ACCEL, PLAYER_MAX_SPEED, image_path="pics/red_square.jpg", obstacle_sprites=obstacle_sprites)
    
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

    def update(self):
        self.input()
        self.move()
