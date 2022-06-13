import pygame
import pygame.mixer
from random import choice


class SoundPack:
    """" SoundPack class. """
    def __init__(self, sounds: dict[str, set[str]], volume: float):
        """
        Init SoundPack class.

        :param sounds: dictionary of all sounds with the key of sound_names
        :param volume: sound volume

        """
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

    def play(self, name: str):
        """
        Play random music from the set of self.sounds[name].

        :param name: name of the sound_pack
        :return:

        """
        if not (self.sounds.get(name) is None) and self.sounds[name]:
            choice(self.sounds[name]).play()

    def update_volume(self, new_volume: float):
        """
        Update sound volume of the game.

        :param new_volume: new sound value
        :return:
        """
        if self.volume != new_volume:
            self.volume = new_volume
            for _, sound_list in self.sounds.items():
                for sound in sound_list:
                    sound.set_volume(self.volume)


class MusicPack:
    """ MusicPack class. """
    def __init__(self, music: dict[str, str], volume):
        """
        Init MusicPack class.

        :param music: dictionary of music
        :param volume: music volume
        """
        self.music = music
        self.is_playing = None
        self.is_paused = False
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

    def play(self, name: str):
        """
        Play the music file with the name name.

        :param name: name of music
        :return:
        """
        if self.is_playing != name:
            self.is_playing = name
            pygame.mixer.music.unload()
            pygame.mixer.music.load(self.music[name])
            pygame.mixer.music.play(-1)

    def pause(self):
        """ Pause the music. """
        pygame.mixer.music.pause()
        self.is_paused = True

    def unpause(self):
        """ Unpause the music. """
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        """Stop the music"""
        pygame.mixer.music.unload()

    def update_volume(self, volume: float):
        """
        Update music volume of the game.

        :param volume: new music value
        :return:
        """
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)