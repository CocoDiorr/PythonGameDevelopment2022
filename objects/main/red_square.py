import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(*groups)
        self.image = pygame.image.load("pics/red_square.jpg").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
