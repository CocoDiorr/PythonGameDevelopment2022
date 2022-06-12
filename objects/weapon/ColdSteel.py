from objects.weapon.Weapon import Weapon
import pygame
from config.Config import *


class ColdSteel(Weapon):
    """Class for melee weapons and cold steel."""
    def __init__(self, level, groups, image_path, sounds, owner, owner_distance, cooldown, damage):
        
        """
        Init coldsteel.

        :param level: Level
        :param groups: tuple
        :param image_path: str: path to cold steel image
        :param owner: Entity
        :param owner_distance: int: distance from weapon to owner
        :param cooldown: int: rate of attack
        :param damage: int: attack damage
        """
        super().__init__(level, groups, image_path, sounds, owner, owner_distance, cooldown)
        self.base_owner_distance = owner_distance
        self.damage = damage
        self.uses = [False, False, False]

    def hit(self):
        """Attacking action."""
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True
            self.sounds.play("hit")
            self.owner_distance += int(TILESIZE / 2)

    def move(self):
        """Change weapon position."""
        self.image = pygame.transform.rotate(
            self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, -1))
        )
        super().move()

    def update(self, dt: float):
        """Update weapon position.

        :param dt: float: delta time for main loop updating
        """
        self.last_use += dt
        self.move()
        if self.last_use >= self.cooldown / 2:
            self.owner_distance = self.base_owner_distance
        self.update_uses()
