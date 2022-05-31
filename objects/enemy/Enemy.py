import pygame
from objects.main.Entity import Entity
from config.Config import *


class Enemy(Entity):
    def __init__(self, level, groups, position, abs_accel, max_speed, enemy_name, health):
        super().__init__(level, groups, position, abs_accel, max_speed, health, BASE_ENEMY_SPRITE_PATH)
        self.enemy_name = enemy_name
        self.sprite_type = "enemy"

    def get_player_direction(self):
        enemy_vector = self.pos
        player_vector = self.level.player.pos
        distance = (player_vector - enemy_vector).magnitude()

        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()
        return direction

    def update(self, dt):
        self.accel = self.get_player_direction()
        self.move()
