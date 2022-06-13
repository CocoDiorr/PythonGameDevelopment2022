"""This module is used to operate with base entity class."""
import pygame
import pygame.math
import pygame.sprite
from Zelda.audio.soundpack.SoundPack import SoundPack
from Zelda.config.Config import *
from Zelda.config.SpriteSheet import SpriteSheet


class Entity(pygame.sprite.Sprite):
    """Base entity class."""

    def __init__(self, level: "Level", groups: tuple, animations_path: str, sounds: dict[str, set[str]], position: pygame.math.Vector2, abs_accel: int, max_speed: int, health: int, max_health=None, energy=None, max_energy=None, look_angle: pygame.math.Vector2 = pygame.math.Vector2(1, 0)):
        """
        Init base entity.

        :param level: Level
        :param groups: visible or obstacle gro
        :param animations_path: path to entity animation sheet
        :param sounds: entity sounds
        :param position: position where entity is created
        :param abs_accel: acceleration of entity
        :param max_speed: entity maximum speed
        :param health: entity health
        :param max_health: entity maximum health
        :param energy: entity energy, used in sprint
        :param max_energy: entity maximum energy
        :param look_angle: entity looking direction
        """
        super().__init__(groups)
        self.level = level
        self.anim_state = 'down_idle'
        self.animations = SpriteSheet(animations_path).get_animations()
        self._frame_index = 0
        self._animation_speed = ANIMATION_SPEED
        self.image = self.animations[self.anim_state][0]
        self.rect = self.image.get_rect()
        self.sounds = SoundPack(sounds, self.level.game.sounds_volume)
        self.pos = pygame.math.Vector2(position)
        self.rect.center = self.pos
        self.accel = pygame.math.Vector2()
        self.speed = pygame.math.Vector2()
        self.max_speed = max_speed
        self.abs_accel = abs_accel
        self.speed_fade = ENTITY_SPEED_FADE
        self.health = health
        self.sprint = [False, True]
        if max_health is None:
            self.max_health = health
        else:
            self.max_health = max_health
        self.energy = energy
        if max_energy is None:
            self.max_energy = energy
        else:
            self.max_energy = max_energy
        if look_angle.length() == 0:
            look_angle = pygame.math.Vector2(1, 0)
        self.look_angle = look_angle.normalize()

        self.hitbox = self.rect.inflate(-26, -26)
        self.sprite_type = 'entity'

    def sprint_on(self):
        """Start sprint."""
        self.sprint[0] = True

    def sprint_off(self):
        """Stop sprint."""
        self.sprint[0] = False

    def set_animation_state(self):
        """Animation state: down, up, left or right."""
        if self.look_angle.y > abs(self.look_angle.x):
            self.anim_state = 'down'
        elif self.look_angle.y < -abs(self.look_angle.x):
            self.anim_state = 'up'
        elif self.look_angle.x > abs(self.look_angle.y):
            self.anim_state = 'right'
        elif self.look_angle.x < -abs(self.look_angle.y):
            self.anim_state = 'left'

        if abs(self.speed.x) <= ENTITY_SPEED_ZERO and abs(self.speed.y) <= ENTITY_SPEED_ZERO:
            if 'idle' not in self.anim_state:
                self.anim_state += '_idle'

    def animate(self):
        """Animate entity walk."""
        animation = self.animations[self.anim_state]

        # loop over the frame index
        self._frame_index += self._animation_speed
        if self._frame_index >= len(animation):
            self._frame_index = 0

        # set the image
        self.image = animation[int(self._frame_index)]
        self.rect = self.image.get_rect(center = self.hitbox.center)
        # self.hitbox = self.rect.inflate(0, -26)

    def move(self, sprint=False):
        """
        Change entity position.

        :param sprint: move faster flag
        """

        if self.accel.length() != 0:
            self.accel.scale_to_length(self.abs_accel)
        if self.accel.x == 0:
            if abs(self.speed.x) <= ENTITY_SPEED_ZERO:
                self.speed.x = 0
            self.speed.x *= self.speed_fade
        if self.accel.y == 0:
            if abs(self.speed.y) <= ENTITY_SPEED_ZERO:
                self.speed.y = 0
            self.speed.y *= self.speed_fade

        self.speed += self.accel
        if self.max_speed and self.speed.length() >= self.max_speed:
            self.speed.scale_to_length(self.max_speed)

        curr_max_speed = self.max_speed
        curr_speed = pygame.math.Vector2(self.speed)
        if not (self.energy is None):
            if self.sprint[0] and self.sprint[1] and self.energy > 0 and self.accel.length() != 0:
                self.energy = max(self.energy - ENERGY_SPEND, 0)
                curr_max_speed *= SPRINT_MULTIPLIER
                curr_speed *= SPRINT_MULTIPLIER
            else:
                self.energy = min(self.energy + ENERGY_RECOVER, self.max_energy)
                if self.energy >= MIN_SPRINT_ENERGY:
                    self.sprint[1] = True
                else:
                    self.sprint[1] = False
            if curr_max_speed and curr_speed.length() >= curr_max_speed:
                curr_speed.scale_to_length(curr_max_speed)

        self.pos.x += curr_speed.x
        self.rect.center = self.pos
        self.hitbox.center = self.pos
        # self.hitbox.x = self.pos.x
        self.collision('horizontal')

        self.pos.y += curr_speed.y
        self.rect.center = self.pos
        self.hitbox.center = self.pos
        # self.hitbox.y = self.pos.y
        self.collision('vertical')

        self.rect.center = self.hitbox.center

    def collision(self, direction):
        """
        Check if entity collides with obstacles.

        :param direction: direction of collide, can be vertical or horizontal
        """
        if direction == 'horizontal':
            for sprite in self.level.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.speed.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                        self.pos = pygame.math.Vector2(self.hitbox.center)
                    if self.speed.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        self.pos = pygame.math.Vector2(self.hitbox.center)
        if direction == 'vertical':
            for sprite in self.level.obstacle:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.speed.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                        self.pos = pygame.math.Vector2(self.hitbox.center)
                    if self.speed.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        self.pos = pygame.math.Vector2(self.hitbox.center)

    def get_hit(self, damage: int):
        """
        Get hit if entity was attacked.

        :param damage: hit damage
        """
        self.health = max(self.health - damage, 0)
        self.sounds.update_volume(self.level.game.sounds_volume)
        self.sounds.play("hurt")
        if self.health == 0:
            self.kill()
            if "weapon" in self.__dict__:
                self.weapon.kill()
            if "shield" in self.__dict__:
                self.shield.kill()
