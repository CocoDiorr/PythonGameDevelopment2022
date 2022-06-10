from objects.weapon.Weapon import Weapon


class ColdSteel(Weapon):
    """ """
    def __init__(self, level, groups, image_path, owner, owner_distance, cooldown, damage):
        super().__init__(level, groups, image_path, owner, owner_distance, cooldown)
        self.damage = damage
        self.uses = [False, False, False]

    def hit(self):
        """ """
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True

    def update(self, dt):
        """

        :param dt: 

        """
        self.last_use += dt
        self.move()
        self.update_uses()

