import pygame
import pygame.display
import pygame.mixer
from audio.soundpack.SoundPack import MusicPack
from config.Config import *
from level.Level import Level
from menu.StartMenu import StartMenu

class Game:
    """ """
    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_RESOLUTION)
        self.clock = pygame.time.Clock()
        self.running = True
        self.locale = 'ru'
        self.volume = VOLUME
        self.music = MusicPack(GAME_MUSIC, self.volume)
        self.level = Level(self.locale, self)
        self.start_menu = StartMenu(self)
        self.game_state = "start" # "play"

    def run(self):
        """ """
        pygame.mixer.init()
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
                                pygame.mixer.music.pause()
                            elif self.level.game_state == "companion":
                                self.level.companion_call()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.game_state == "start":
                            self.start_menu.buttons_event = event
                        if self.game_state == "play":
                            if self.level.game_state in ("companion", "esc"):
                                self.level.buttons_event = event

                #elif self.game_state == "start":



            dt = self.clock.tick(FPS) / 1000
            self.screen.fill(BACKGROUND_COLOR)
            if self.game_state == "start":
                if self.level.game_state != "esc":
                    pygame.mixer.music.unpause()
                    self.music.play("start_menu")
                self.start_menu.display()
            if self.game_state == "play":
                if self.level.game_state != "esc":
                    pygame.mixer.music.unpause()
                    self.music.play("level")
                self.level.run(dt)
            pygame.display.update()
        pygame.mixer.quit()
