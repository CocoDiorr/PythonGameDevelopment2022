import pygame
from objects.main.Entity import Entity
from objects.weapon.ShootingWeapon import ShootingWeapon
from config.Config import *


class Enemy(Entity):
    """ """
    def __init__(self, level, groups, image_path, size, sounds, position, abs_accel, max_speed, health, attack_radius, notice_radius):
        super().__init__(level, groups, image_path, size, sounds, position, abs_accel, max_speed, health)
        self.sprite_type = "enemy"
        self.status = "idle"
        self.attack_radius = attack_radius
        self.notice_radius = notice_radius

    def get_player_direction(self):
        """ """
        enemy_vector = self.pos
        player_vector = self.level.player.pos

        if self.get_player_distance() > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()
        return direction

    def get_player_distance(self):
        """ """
        enemy_vector = self.pos
        player_vector = self.level.player.pos
        return (player_vector - enemy_vector).magnitude()

    def get_status(self):
        """ """
        distance = self.get_player_distance()
        if distance <= self.attack_radius:
            return "attack"
        elif distance <= self.notice_radius:
            return "move"
        else:
            return "idle"

    def equip_weapon(self, weapon):
        """

        :param weapon: 

        """
        self.weapon = weapon

    def update(self, dt):
        """

        :param dt: 

        """
        self.status = self.get_status()
        if self.status in ("move", "attack"):
            self.accel = self.get_player_direction()
            self.look_angle = self.get_player_direction()
            self.move()
            if self.status == "attack":
                if isinstance(self.weapon, ShootingWeapon):
                    self.weapon.spawn_bullet(self.look_angle)
                else:
                    self.weapon.hit()
            self.weapon.update(dt)

    def kill(self):
        self.level.player.get_dust(self)
        super().kill()