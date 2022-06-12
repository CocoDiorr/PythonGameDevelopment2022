import pygame
import pygame.mixer
from random import choice


class SoundPack:
    def __init__(self, sounds, volume):
        self.sounds = dict()
        self.volume = volume
        for name, sound_set in sounds.items():
            self.sounds[name] = []
            for sound in sound_set:
                if sound is None:
                    self.sounds[name].append(None)
                else:
                    s = pygame.mixer.Sound(sound)
                    s.set_volume(self.volume)
                    self.sounds[name].append(s)

    def play(self, name):
        if not (self.sounds.get(name) is None) and self.sounds[name]:
            choice(self.sounds[name]).play()



class MusicPack:
    def __init__(self, music, volume):
        self.music = music
        self.is_playing = None
        self.is_paused = False
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    def play(self, name):
        if self.is_playing != name:
            self.is_playing = name
            pygame.mixer.music.unload()
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.music.pause()
        self.is_paused = True

    def unpause(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        pygame.mixer.music.unload()

    def update_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)