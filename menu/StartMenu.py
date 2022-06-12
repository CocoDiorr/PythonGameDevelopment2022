import pygame
import os
from config.Config import WINDOW_RESOLUTION, UI_SETTINGS, AUDIO, DEFAULT_LOCALE, MENU

import gettext
translation = gettext.translation("StartMenu", os.path.join("locale", "start_menu"), languages=[DEFAULT_LOCALE])
_ = translation.gettext


class StartMenu:
    def __init__(self, game):
        self.game = game
        self.buttons_event = None
        self.settings_on = False
        self.font = pygame.font.Font(UI_SETTINGS["UI_FONT"], MENU["FONT_SIZE"])

        # settings
        self.locale = self.game.locale
        self.surface = pygame.display.get_surface()

        # Audio
        self.bg_music = pygame.mixer.Sound(AUDIO["START_MENU"])
        self.bg_music.set_volume(self.game.volume)


        # Background
        self.bg_images = []
        #self.pics_path = os.path.join("pics", "menu")
        for pic in os.listdir(os.path.join(MENU["PICS_PATH"], "bg")):
            self.bg_images.append(pygame.transform.scale(pygame.image.load(os.path.join(MENU["PICS_PATH"], "bg", pic)).convert_alpha(), WINDOW_RESOLUTION))

        self.cur_frame = 0
        self.times = 20
        self.frames = len(self.bg_images)

        # Name above
        # self.vmik = pygame.image.load(os.path.join(MENU["PICS_PATH"], "VMIK_name.png"))
        # self.vmik_

        # state
        self.start_menu_state = "options"

        # buttons

        self.buttons = []
        self.buttons.append(
            Item("play.png", "play_hovered.png",\
                 int(0.3 * WINDOW_RESOLUTION[0]), int(0.2 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] / 2)), self, self.play_button, None, 1, 3)
        )
        self.buttons.append(
            Item("settings.png", "settings_hovered.png",\
                 int(0.3 * WINDOW_RESOLUTION[0]), int(0.1 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.7  + 20)), self, self.settings_button, None, 2, 3)
        )
        self.buttons.append(
            Item("exit.png", "exit_hovered.png",\
                 int(0.2 * WINDOW_RESOLUTION[0]), int(0.1 * WINDOW_RESOLUTION[1]),\
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.8 + 40)), self, self.exit_button, None, 3, 3)
        )
        self.buttons.append(
            LangButton("USA.png", "USA_hovered.png",\
                 int(WINDOW_RESOLUTION[0] * 0.1), int(WINDOW_RESOLUTION[1] * 0.1),\
                (int(WINDOW_RESOLUTION[0] * 0.40), int(WINDOW_RESOLUTION[1] * 0.7)), self, self.lang_button, ('en',), 2, 3, 'en')

        )
        self.buttons.append(
            LangButton("Russia.png", "Russia_hovered.png",\
                 int(WINDOW_RESOLUTION[0] * 0.1), int(WINDOW_RESOLUTION[1] * 0.1),\
                (int(WINDOW_RESOLUTION[0] * 0.6), int(WINDOW_RESOLUTION[1] * 0.7)), self, self.lang_button, ('ru',), 2, 3, 'ru')

        )

        #self.volume_rect = pygame.Rect(int(WINDOW_RESOLUTION[0] * 0.4), int(WINDOW_RESOLUTION[1] * 0.1), int(WINDOW_RESOLUTION[0] * 0.3), int(WINDOW_RESOLUTION[1] * 0.15))

    def display(self):
        self.surface.blit(self.bg_images[self.cur_frame], (0,0))
        self.times -= 1
        if self.times == 0:
            self.cur_frame = (self.cur_frame + 1) % self.frames
            self.times = 20

        if not self.settings_on:
            #pygame.draw.rect(self.surface, )
            for button in self.buttons[:3]:
                button.display(self.surface)
        else:
            text_surf_1 = self.font.render(_("Volume"), 0, MENU["FONT_COLOR"])
            text_rect_1 = text_surf_1.get_rect(midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.05)))
            self.surface.blit(text_surf_1, text_rect_1)

            text_surf_2 = self.font.render(_("Choose language"), 0, MENU["FONT_COLOR"])
            text_rect_2 = text_surf_2.get_rect(midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.6)))
            self.surface.blit(text_surf_2, text_rect_2)
            for button in self.buttons[3:]:
                button.display(self.surface)
        self.bg_music.play(loops = -1)

    def play_button(self):
        self.game.level.create_map()
        self.game.game_state = "play"
        #self.bg_music.pause()

    def settings_button(self):
        self.settings_on = not self.settings_on

    def exit_button(self):
        self.game.running = False

    def lang_button(self, lang):
        #self.game.locale = lang
        self.game.update_locale(lang)

    def update_locale(self, lang):
        for button in self.buttons[:3]:
            button.update_locale(lang)


class Item:
    def __init__(self, image, image_hovered, w, h, midtop, parent, action, args, numb, max_numb):

        # Parent object to go to
        self.parent = parent
        self.locale = self.parent.locale

        self.image_name = image
        self.image_hovered_name = image_hovered

        self.image_path = os.path.join(MENU["PICS_PATH"], self.locale, image)
        self.image_hovered_path = os.path.join(MENU["PICS_PATH"], self.locale, image_hovered)


        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (w, h))
        self.rect = self.image.get_rect(midtop=midtop)
        self.image_hovered = pygame.image.load(self.image_hovered_path).convert_alpha()
        self.image_hovered = pygame.transform.scale(self.image_hovered, (w, h))
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
                    self.action(*self.args)
                else:
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

    def update_locale(self, lang):
        global translation
        global _

        translation = gettext.translation("StartMenu", os.path.join("locale", "start_menu"), languages=[lang])
        translation.install()
        _ = translation.gettext

        self.image_path = os.path.join(MENU["PICS_PATH"], lang, self.image_name)
        self.image_hovered_path = os.path.join(MENU["PICS_PATH"], lang, self.image_hovered_name)

        self.locale = lang

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))

        self.image_hovered = pygame.image.load(self.image_hovered_path).convert_alpha()
        self.image_hovered = pygame.transform.scale(self.image_hovered, (self.rect.w, self.rect.h))


class LangButton(Item):
    def __init__(self, image, image_hovered, w, h, midtop, parent, action, args, numb, max_numb, lang):
        super().__init__(image, image_hovered, w, h, midtop, parent, action, args, numb, max_numb)
        self.lang = lang

    def display(self, surface):
        self.hover()
        self.click()
        if self.parent.game.locale == self.lang:
            surface.blit(self.image_hovered, self.rect_hovered)
            #print(self.parent.game.locale)
        else:
            surface.blit(self.button, self.button_rect)
