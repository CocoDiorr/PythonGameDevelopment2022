"""This module is used to operate with base Enemy class."""
import pygame
from Zelda.objects.main.Entity import Entity
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon


class Enemy(Entity):
    """Base enemy class."""

    def __init__(
        self,
        level: "Level",
        groups: tuple,
        animations_path: str,
        sounds: dict[str, set[str]],
        position: pygame.math.Vector2,
        abs_accel: int,
        max_speed: int,
        health: int,
        attack_radius: int,
        notice_radius: int,
    ):
        """
        Create base enemy.

        :param level: Level
        :param groups: tuple
        :param animations_path: path to animation sheet
        :param sounds: player sounds
        :param position: position where enemy is created
        :param abs_accel: enemy acceleration
        :param max_speed: enemy maximum speed
        :param health: amount of health
        :param attack_radius: radius where enemy attacks player
        :param notice_radius: radius where enemy notices player
        """
        super().__init__(
            level,
            groups,
            animations_path,
            sounds,
            position,
            abs_accel,
            max_speed,
            health,
        )
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
        """Get distance from enemy to player."""
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

    def equip_weapon(self, weapon: "Weapon"):
        """
        Equip enemy with weapon.

        :param weapon: weapon to equip with
        """
        self.weapon = weapon

    def update(self, dt: float):
        """
        Update enemy position and weapon using.

        :param dt: delta time for main loop updating

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

    def kill(self):
        """Destroy enemy."""
        self.level.player.get_dust(self)
        super().kill()
