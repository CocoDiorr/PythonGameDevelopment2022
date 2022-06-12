import pygame
from objects.main.Entity import Entity
from objects.weapon.ShootingWeapon import ShootingWeapon
from config.Config import *


class Enemy(Entity):
    """Base enemy class. Inherited from Entity."""
    def __init__(self, level, groups: tuple, animations_path: str, position: tuple, abs_accel: int, max_speed: int, health: int, attack_radius: int, notice_radius: int):
        """
        Create base enemy.

        :param level: Level
        :param groups: tuple
        :param animations_path: str: path to animation sheet
        :param position: tuple: position where enemy is created
        :param abs_accel: int: enemy acceleration
        :param max_speed: int: enemy maximum speed
        :param health: int: amount of health
        :param attack_radius: int: radius where enemy attacks player
        :param notice_radius: int: radius where enemy notices player
        """
        super().__init__(level, groups, animations_path, position, abs_accel, max_speed, health)
        self.sprite_type = "enemy"
        self.status = "idle"
        self.attack_radius = attack_radius
        self.notice_radius = notice_radius

    def get_player_direction(self):
        """Get direction from enemy to player."""
        enemy_vector = self.pos
        player_vector = self.level.player.pos

        if self.get_player_distance() > 0:
            direction = (player_vector - enemy_vector).normalize()
        else:
            direction = pygame.math.Vector2()
        return direction

    def get_player_distance(self):
        """Get distance from enemy to player"""
        enemy_vector = self.pos
        player_vector = self.level.player.pos
        return (player_vector - enemy_vector).magnitude()

    def get_status(self):
        """Get enemy status: idle, move or attack."""
        distance = self.get_player_distance()
        if distance <= self.attack_radius:
            return "attack"
        elif distance <= self.notice_radius:
            return "move"
        else:
            return "idle"

    def equip_weapon(self, weapon):
        """
        Equip enemy with weapon.

        :param weapon: Weapon
        """
        self.weapon = weapon

    def update(self, dt: float):
        """
        Update enemy position and weapon using.

        :param dt: float: delta time for main loop updating

        """

        self.status = self.get_status()
        if self.status in ("move", "attack"):
            self.accel = self.get_player_direction()
            self.look_angle = self.get_player_direction()
            self.set_animation_state()
            self.animate()
            self.move()

            if self.status == "attack":
                if isinstance(self.weapon, ShootingWeapon):
                    self.weapon.spawn_bullet(self.look_angle)
                else:
                    self.weapon.hit()
            self.weapon.update(dt)
