import pygame
from config.Config import PLAYER_SPEED
from objects.main.Entity import Entity


class Player(Entity):
    def __init__(self, groups, obstacle_sprites):
        super().__init__(groups, PLAYER_SPEED, image_path="pics/red_square.jpg", obstacle_sprites=obstacle_sprites)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.move()
