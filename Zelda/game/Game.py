"""This module is used to operate with the Game."""
import pygame
import pygame.display
import pygame.mixer
from Zelda.audio.soundpack.SoundPack import MusicPack
from Zelda.config.Config import *
from Zelda.level.Level import Level
from Zelda.menu.StartMenu import StartMenu


class Game:
    """Game class."""
    def __init__(self, locale: str = 'en', music_volume: float = MUSIC_VOLUME, sounds_volume: float = SOUNDS_VOLUME):
        """
        Init base weapon.

        :param locale: name of locale ('en' or 'ru')
        :param music_volume: game music volume
        :param sounds_volume: game sounds volume

        """
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.locale = locale
        self.music_volume = music_volume
        self.music = MusicPack(GAME_MUSIC, music_volume)
        self.sounds_volume = sounds_volume
        self.level = Level(self.locale, self)
        self.game_state = "start"
        self.start_menu = StartMenu(self)

    def run(self):
        """Run the game."""
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        while self.running:
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        if self.game_state == "play":
                            self.level.companion_call()

                    if event.key == pygame.K_ESCAPE:
                        if self.game_state == "play":
                            if self.level.game_state in ("active", "esc"):
                                self.level.esc_menu_call()
                                self.music.pause()
                            elif self.level.game_state == "companion":
                                self.level.companion_call()
                        else:
                            if self.start_menu.settings_on:
                                self.start_menu.settings_button()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.game_state == "start":
                            self.start_menu.buttons_event = event
                        if self.game_state == "play":
                            if self.level.game_state in ("companion", "esc"):
                                self.level.buttons_event = event

            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            if self.game_state == "start":
                if self.level.game_state != "esc":
                    self.music.unpause()
                    self.music.play("start_menu")
                self.start_menu.display()
            if self.game_state == "play":
                if self.level.game_state != "esc":
                    self.music.unpause()
                    self.music.play("level")
                self.level.run(dt)
            pygame.display.update()
        pygame.mixer.quit()

    def update_locale(self, lang: str):
        """
        Update the language of locale and game start menu.

        :param lang: language of the game

        """
        self.locale = lang
        self.level.update_locale(lang)
        self.start_menu.update_locale(lang)
