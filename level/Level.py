import pygame
from objects.friendly.Player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.create_map()

    def create_map(self):
        Player(self.visible_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
