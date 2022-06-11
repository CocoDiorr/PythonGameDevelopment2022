import pygame
import pygame.mixer
from random import choice

# class SoundPack:
#     def __init__(self, sounds):
#         self.sounds = sounds

#     def play_sound(self, sound_name):
#         choice(self.sounds[sound_name]).play()


class MusicPack:
    def __init__(self, music, volume):
        self.music = music
        self.is_playing = None
        self.volume = volume

    def play(self, name):
        if self.is_playing != name:
            self.is_playing = name
            pygame.mixer.music.unload()
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.set_volume(self.volume)
            pygame.mixer.music.play(-1)

    def stop(self):
        pygame.mixer.music.unload()
