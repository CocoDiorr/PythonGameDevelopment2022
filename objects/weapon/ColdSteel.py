from objects.weapon.Weapon import Weapon
import pygame

class ColdSteel(Weapon):
    """ """
    def __init__(self, level, groups, image_path, image_size, sounds, owner, owner_distance, cooldown, damage):
        super().__init__(level, groups, image_path, image_size, sounds, owner, owner_distance, cooldown)
        self.damage = damage
        self.uses = [False, False, False]

    def hit(self):
        """ """
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True
            self.sounds.play("hit")

    def move(self):
        self.image = pygame.transform.rotate(self.start_image, self.owner.look_angle.angle_to(pygame.math.Vector2(0, -1)))
        super().move()

    def update(self, dt):
        """

        :param dt: 

        """
        self.last_use += dt
        self.move()
        self.update_uses()

