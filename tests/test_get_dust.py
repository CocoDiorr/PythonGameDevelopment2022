import unittest
from unittest.mock import MagicMock, patch
from Zelda.objects.friendly.Player import Player
from Zelda.objects.weapon.ColdSteel import ColdSteel
from Zelda.objects.weapon.ShootingWeapon import ShootingWeapon
from Zelda.config.Config import *

class TestPlayerGetDust(unittest.TestCase):
    def setUp(self):
        self.player = MagicMock()
        self.player.dust = 100
        self.player.sounds.play = MagicMock()
        self.start_dust = self.player.dust
        self.enemy = MagicMock()

    def test_01_correct_work_shooting_weapon(self):
        with patch('Zelda.objects.friendly.Player', spec=ShootingWeapon) as sw:
            self.enemy.weapon = sw
            self.enemy.max_health = 10
            self.enemy.weapon.bullet_damage = 20
            self.enemy.weapon.cooldown = 0.5
            addition = int((GET_DUST_HEALTH_MULTIPLIER * self.enemy.max_health + GET_DUST_WEAPON_MULTIPLIER * self.enemy.weapon.bullet_damage / self.enemy.weapon.cooldown) * GET_DUST_MULTIPLIER)
            Player.get_dust(self.player, self.enemy)
        assert self.player.dust == self.start_dust + addition
    
    def test_02_correct_work_cold_steel(self):
        with patch('Zelda.objects.friendly.Player', spec=ColdSteel) as cs:
            self.enemy.weapon = cs
            self.enemy.max_health = 10
            self.enemy.weapon.damage = 20
            self.enemy.weapon.cooldown = 0.5
            addition = int((GET_DUST_HEALTH_MULTIPLIER * self.enemy.max_health + GET_DUST_WEAPON_MULTIPLIER * self.enemy.weapon.damage / self.enemy.weapon.cooldown) * GET_DUST_MULTIPLIER)
            Player.get_dust(self.player, self.enemy)
        assert self.player.dust == self.start_dust + addition
    
    def test_03_no_weapon(self):
        Player.get_dust(self.player, self.enemy)

    def test_04_None_weapon(self):
        self.enemy.weapon = None
        Player.get_dust(self.player, self.enemy)
    
