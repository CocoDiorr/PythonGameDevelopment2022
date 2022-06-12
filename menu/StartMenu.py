import pygame
import os
from audio.soundpack.SoundPack import SoundPack
from config.Config import WINDOW_RESOLUTION, BUTTON_SOUNDS


class StartMenu:
    def __init__(self, game):
        self.game = game
        self.buttons_event = None

        # settings
        self.locale = self.game.locale
        self.surface = pygame.display.get_surface()

        self.bg_images = []
        pics_path = os.path.join("pics/menu")
        for pic in os.listdir(os.path.join(pics_path, "bg")):
            self.bg_images.append(pygame.transform.scale(pygame.image.load(os.path.join(pics_path, "bg", pic)).convert_alpha(), WINDOW_RESOLUTION))

        self.cur_frame = 0
        self.times = 20
        self.frames = len(self.bg_images)

        # state
        self.start_menu_state = "options"

        # buttons

        self.buttons = []
        self.buttons.append(
            Item(os.path.join(pics_path, "play.png"), os.path.join(pics_path, "play_hovered.png"),\
                 int(0.3 * WINDOW_RESOLUTION[0]), int(0.2 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] / 2)), self, self.play_button, None, 1, 3)
        )
        self.buttons.append(
            Item(os.path.join(pics_path, "settings.png"), os.path.join(pics_path, "settings_hovered.png"),\
                 int(0.3 * WINDOW_RESOLUTION[0]), int(0.1 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.7  + 20)), self, self.settings_button, None, 2, 3)
        )
        self.buttons.append(
            Item(os.path.join(pics_path, "exit.png"), os.path.join(pics_path, "exit_hovered.png"),\
                 int(0.2 * WINDOW_RESOLUTION[0]), int(0.1 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.8 + 40)), self, self.exit_button, None, 3, 3)
        )

    def display(self):
        self.surface.blit(self.bg_images[self.cur_frame], (0,0))
        self.times -= 1
        if self.times == 0:
            self.cur_frame = (self.cur_frame + 1) % self.frames
            self.times = 20

        for button in self.buttons:
            button.display(self.surface)


    def play_button(self):
        self.game.level.create_map()
        self.game.game_state = "play"

    def settings_button(self):
        pass

    def exit_button(self):
        self.game.running = False


class Item:
    def __init__(self, image, image_hovered, w, h, midtop, parent, action, args, numb, max_numb):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(w), int(h)))
        self.rect = self.image.get_rect(midtop=midtop)
        self.image_hovered = pygame.image.load(image_hovered).convert_alpha()
        self.image_hovered = pygame.transform.scale(self.image_hovered, (int(w), int(h)))
        self.rect_hovered = self.image_hovered.get_rect(midtop=midtop)

        # Button to display
        self.button = self.image
        self.button_rect = self.rect

        # Action for button to do when pressed
        self.action = action
        self.args = args

        # Whether the button pressed or not
        self.pressed = False

        # Index of button
        self.numb = numb
        self.max_numb = max_numb

        # Parent object to go to
        self.parent = parent

        self.sounds = SoundPack(BUTTON_SOUNDS, self.parent.game.sounds_volume)


    def hover(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_rect = self.rect_hovered
            self.button = self.image_hovered
        else:
            self.button_rect = self.rect
            self.button = self.image

    def click(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if self.parent.buttons_event and not self.pressed:
                if self.args:
                    self.sounds.play("click")
                    self.action(*self.args)
                else:
                    self.sounds.play("click")
                    self.action()
                self.pressed = True
                self.parent.buttons_event = None
            else:
                self.pressed = False
        elif self.numb == self.max_numb:
            self.parent.buttons_event = None

    def display(self, surface):
        self.hover()
        self.click()
        surface.blit(self.button, self.button_rect)
