import pygame
from objects.main.Entity import Entity
from config.Config import BASE_ENEMY_SPEED


class Enemy(Entity):
    def __init__(self, groups, speed, monster_name, health, pos, obstacle_sprites):
        super().__init__(groups, BASE_ENEMY_SPEED, image_path="pics/blue_rect.png", obstacle_sprites=obstacle_sprites)
        self.monster_name = monster_name
        self.sprite_type = "enemy"
        self.rect = self.image.get_rect(topleft=pos)

    def get_player_direction(self, player):
        enemy_vector = pygame.math.Vector2(self.rect.center)
        player_vector = pygame.math.Vector2(player.rect.center)
        distance = (player_vector - enemy_vector).magnitude()

        if distance > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()
        return direction

    def enemy_update(self, player):
        self.direction = self.get_player_direction(player)
        self.move()
