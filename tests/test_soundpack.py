import os
import unittest
from unittest.mock import MagicMock
import pygame
from Zelda.audio.soundpack.SoundPack import SoundPack, MusicPack

# python -m unittest discover -s tests

class FakeSoundFactory:
    def __init__(self):
        self.sounds = []
        self.called = 0

    def get_sound(self, sound):
        self.called += 1
        s = MagicMock()
        s.play = MagicMock()
        self.sounds.append(s)
        return self.sounds[-1]


class TestSoundPack(unittest.TestCase):
    def setUp(self):
        self.factory = FakeSoundFactory()
        pygame.mixer.Sound = self.factory.get_sound

    def test_01_empty_sounds(self):
        sp = SoundPack(dict(), 1)
        sp.play("hit")
        assert self.factory.called == 0

    def test_02_missing_sound(self):
        sp = SoundPack(
            {
                "hit": {"a",},
            },
            1
        )
        sp.play("click")
        for sound in self.factory.sounds:
            sound.play.assert_not_called()

    def test_03_correct_work(self):
        sp = SoundPack(
            {
                "hit": {"a",},
            },
            1
        )
        sp.play("hit")
        assert len(self.factory.sounds) == 1
        assert len(sp.sounds) == 1
        self.factory.sounds[0].play.assert_called_once()
    
    def test_04_multiple_actions(self):
        sp = SoundPack(
            {
                "hit": {"a",},
                "click": {"b",},
            },
            1
        )
        sp.play("hit")
        sp.play("click")
        assert len(self.factory.sounds) == 2
        assert len(sp.sounds) == 2
        self.factory.sounds[0].play.assert_called_once()
        self.factory.sounds[1].play.assert_called_once()
    
    def test_05_multiple_sounds(self):
        sp = SoundPack(
            {
                "hit": {"a", "b"},
            },
            1
        )
        sp.play("hit")
        assert len(self.factory.sounds) == 2
        assert len(sp.sounds) == 1
        assert self.factory.sounds[0].play.call_count + self.factory.sounds[1].play.call_count == 1



class TestMusicPack(unittest.TestCase):
    def setUp(self):
        pygame.mixer.music.set_volume = MagicMock()
        self.volume = 0
        pygame.mixer.music.unload = MagicMock()
        pygame.mixer.music.load = MagicMock()
        pygame.mixer.music.play = MagicMock()
        pygame.mixer.music.pause = MagicMock()
        pygame.mixer.music.unpause = MagicMock()
        self.apath = os.path.join("q", "w", "e")
        self.bpath = os.path.join("z", "x", "c")
        self.music = {
            "a": self.apath,
            "b": self.bpath,
        }
    
    def test_01_correct_work(self):
        mp = MusicPack(self.music, self.volume)
        pygame.mixer.music.set_volume.assert_called_once_with(self.volume)
        mp.play("a")
        pygame.mixer.music.load.assert_called_once_with(self.apath)
    
    def test_02_test_same_music(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        pygame.mixer.music.load.assert_called_once_with(self.apath)
        mp.play("a")
        pygame.mixer.music.load.assert_called_once_with(self.apath)
        pygame.mixer.music.play.assert_called_once()

    def test_02_test_change_music(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        mp.play("b")
        assert pygame.mixer.music.load.call_count == 2
        assert pygame.mixer.music.play.call_count == 2

    def test_03_pause(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        mp.pause()
        pygame.mixer.music.pause.assert_called_once()
    
    def test_04_unpause(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        mp.pause()
        pygame.mixer.music.pause.assert_called_once()
        mp.unpause()
        pygame.mixer.music.unpause.assert_called_once()


    def test_05_several_unpauses(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        mp.pause()
        pygame.mixer.music.pause.assert_called_once()
        mp.unpause()
        mp.unpause()
        mp.unpause()
        mp.unpause()
        pygame.mixer.music.unpause.assert_called_once()

    def test_06_playing_unpause(self):
        mp = MusicPack(self.music, self.volume)
        mp.play("a")
        mp.unpause()
        pygame.mixer.music.unpause.assert_not_called()
