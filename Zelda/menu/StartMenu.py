"""This module is used to operate with start menu."""
import pygame
import os
from typing import Callable
from Zelda.audio.soundpack.SoundPack import SoundPack
from Zelda.config.Config import (
    WINDOW_RESOLUTION,
    UI_SETTINGS,
    DEFAULT_LOCALE,
    MENU,
    BUTTON_SOUNDS,
)

import gettext

translation = gettext.translation(
    "StartMenu",
    os.path.join(os.path.dirname(__file__), "..", "locale", "start_menu"),
    languages=[DEFAULT_LOCALE],
)
_ = translation.gettext


class StartMenu:
    """StartMenu class."""

    def __init__(self, game: "Game"):
        """
        Init the Start menu.

        :param game: Game

        """
        self.game = game
        self.buttons_event = None
        self.settings_on = False
        self.font = pygame.font.Font(UI_SETTINGS["UI_FONT"], MENU["FONT_SIZE"])

        # settings
        self.locale = self.game.locale
        self.surface = pygame.display.get_surface()

        # Background
        self.bg_images = []
        for pic in os.listdir(os.path.join(MENU["PICS_PATH"], "bg")):
            self.bg_images.append(
                pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(MENU["PICS_PATH"], "bg", pic)
                    ).convert_alpha(),
                    WINDOW_RESOLUTION,
                )
            )

        self.cur_frame = 0
        self.times = 20
        self.frames = len(self.bg_images)

        # Name above
        self.vmik = pygame.image.load(
            os.path.join(MENU["PICS_PATH"], self.locale, "VMIK.png")
        ).convert_alpha()
        self.vmik = pygame.transform.scale(
            self.vmik,
            (int(WINDOW_RESOLUTION[0] * 0.5), int(WINDOW_RESOLUTION[1] * 0.2)),
        )
        self.vmik_rect = self.vmik.get_rect(
            midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.1))
        )

        # ASVK
        self.asvk = pygame.image.load(
            os.path.join(MENU["PICS_PATH"], "asvk.png")
        ).convert_alpha()
        self.asvk = pygame.transform.scale(self.asvk, (100, 100))
        self.asvk_rect = self.asvk.get_rect(topleft=(WINDOW_RESOLUTION[0] - 110, 10))

        # state
        self.start_menu_state = "options"

        # buttons
        self.buttons = []
        self.buttons.append(
            Item(
                "play.png",
                "play_hovered.png",
                int(0.3 * WINDOW_RESOLUTION[0]),
                int(0.2 * WINDOW_RESOLUTION[1]),
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] / 2)),
                self,
                self.play_button,
                None,
                1,
                3,
            )
        )
        self.buttons.append(
            Item(
                "settings.png",
                "settings_hovered.png",
                int(0.3 * WINDOW_RESOLUTION[0]),
                int(0.1 * WINDOW_RESOLUTION[1]),
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.7 + 20)),
                self,
                self.settings_button,
                None,
                2,
                3,
            )
        )
        self.buttons.append(
            Item(
                "exit.png",
                "exit_hovered.png",
                int(0.2 * WINDOW_RESOLUTION[0]),
                int(0.1 * WINDOW_RESOLUTION[1]),
                (int(WINDOW_RESOLUTION[0] / 2), int(WINDOW_RESOLUTION[1] * 0.8 + 40)),
                self,
                self.exit_button,
                None,
                3,
                3,
            )
        )
        self.buttons.append(
            LangButton(
                "USA.png",
                "USA_hovered.png",
                int(WINDOW_RESOLUTION[0] * 0.1),
                int(WINDOW_RESOLUTION[1] * 0.1),
                (int(WINDOW_RESOLUTION[0] * 0.40), int(WINDOW_RESOLUTION[1] * 0.7)),
                self,
                self.lang_button,
                ("en",),
                3,
                4,
                "en",
            )
        )
        self.buttons.append(
            LangButton(
                "Russia.png",
                "Russia_hovered.png",
                int(WINDOW_RESOLUTION[0] * 0.1),
                int(WINDOW_RESOLUTION[1] * 0.1),
                (int(WINDOW_RESOLUTION[0] * 0.6), int(WINDOW_RESOLUTION[1] * 0.7)),
                self,
                self.lang_button,
                ("ru",),
                4,
                4,
                "ru",
            )
        )

        self.music_toggle = Toggle(
            int(WINDOW_RESOLUTION[0] * 0.25),
            int(WINDOW_RESOLUTION[1] * 0.13),
            int(WINDOW_RESOLUTION[0] * 0.5),
            int(WINDOW_RESOLUTION[1] * 0.15),
            self,
            1,
            4,
            self.game.music_volume,
            1,
            "music",
            True,
        )

        self.sounds_toggle = Toggle(
            int(WINDOW_RESOLUTION[0] * 0.25),
            int(WINDOW_RESOLUTION[1] * 0.35),
            int(WINDOW_RESOLUTION[0] * 0.5),
            int(WINDOW_RESOLUTION[1] * 0.15),
            self,
            2,
            4,
            self.game.sounds_volume,
            1,
            "sounds",
            False,
        )

    def display(self):
        """Draw the Start menu."""
        self.surface.blit(self.bg_images[self.cur_frame], (0, 0))
        self.times -= 1
        if self.times == 0:
            self.cur_frame = (self.cur_frame + 1) % self.frames
            self.times = 20

        if not self.settings_on:
            self.surface.blit(self.vmik, self.vmik_rect)
            self.surface.blit(self.asvk, self.asvk_rect)
            for button in self.buttons[:3]:
                button.display(self.surface)
        else:
            self.music_toggle.display(self.surface, _("Music"))
            self.sounds_toggle.display(self.surface, _("Sounds"))

            text_surf_1 = self.font.render(_("Volume"), 0, MENU["FONT_COLOR"])
            text_rect_1 = text_surf_1.get_rect(
                midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.05))
            )
            self.surface.blit(text_surf_1, text_rect_1)

            text_surf_2 = self.font.render(_("Choose language"), 0, MENU["FONT_COLOR"])
            text_rect_2 = text_surf_2.get_rect(
                midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.6))
            )
            self.surface.blit(text_surf_2, text_rect_2)
            for button in self.buttons[3:]:
                button.display(self.surface)

    def play_button(self):
        """Call the play button."""
        self.game.level.create_map()
        self.game.game_state = "play"

    def settings_button(self):
        """Call the settings button."""
        self.settings_on = not self.settings_on

    def exit_button(self):
        """Call the exit button."""
        self.game.running = False

    def lang_button(self, lang: str):
        """
        Call the language button.

        :param lang: language of the game

        """
        self.game.update_locale(lang)

    def update_locale(self, lang: str):
        """
        Update the language of the Game.

        :param lang: language of the game

        """
        self.vmik = pygame.image.load(
            os.path.join(MENU["PICS_PATH"], lang, "VMIK.png")
        ).convert_alpha()
        self.vmik = pygame.transform.scale(
            self.vmik,
            (int(WINDOW_RESOLUTION[0] * 0.5), int(WINDOW_RESOLUTION[1] * 0.2)),
        )
        self.vmik_rect = self.vmik.get_rect(
            midtop=(WINDOW_RESOLUTION[0] // 2, int(WINDOW_RESOLUTION[1] * 0.1))
        )

        for button in self.buttons[:3]:
            button.update_locale(lang)


class Item:
    """Item class."""

    def __init__(
        self,
        image: str,
        image_hovered: str,
        w: int,
        h: int,
        midtop: tuple[int],
        parent: "Object",
        action: Callable[..., None],
        args: "args",
        numb: int,
        max_numb: int,
    ):
        """
        Init the Item class.

        :param image: name of the image
        :param image_hovered: name of the image, when hovering it
        :param w: width of the image
        :param h: height of the image
        :param midtop: midtop image coordinates
        :param parent: StartMenu or Level
        :param action: function
        :param args: args for the action
        :param numb: number of the button
        :param max_numb: number of the buttons on the screen
        """
        # Parent object to go to
        self.parent = parent
        self.locale = self.parent.locale

        self.image_name = image
        self.image_hovered_name = image_hovered

        self.image_path = os.path.join(MENU["PICS_PATH"], self.locale, image)
        self.image_hovered_path = os.path.join(
            MENU["PICS_PATH"], self.locale, image_hovered
        )

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

        self.sounds = SoundPack(BUTTON_SOUNDS, self.parent.game.sounds_volume)

    def hover(self):
        """Hover on the button."""
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            self.button_rect = self.rect_hovered
            self.button = self.image_hovered
        else:
            self.button_rect = self.rect
            self.button = self.image

    def click(self):
        """Click the button."""
        if self.button_rect.collidepoint(pygame.mouse.get_pos()):
            if self.parent.buttons_event and not self.pressed:
                if self.args:
                    self.sounds.update_volume(self.parent.game.sounds_volume)
                    self.sounds.play("click")
                    self.action(*self.args)
                else:
                    self.sounds.update_volume(self.parent.game.sounds_volume)
                    self.sounds.play("click")
                    self.action()
                self.pressed = True
                self.parent.buttons_event = None
            else:
                self.pressed = False
        elif self.numb == self.max_numb:
            self.parent.buttons_event = None

    def display(self, surface: "pygame.display"):
        """
        Draw the button on the screen.

        :param surface:

        """
        self.hover()
        self.click()
        surface.blit(self.button, self.button_rect)

    def update_locale(self, lang: str):
        """
        Update the language of the button.

        :param lang: language of the game

        """
        global translation
        global _

        translation = gettext.translation(
            "StartMenu",
            os.path.join(os.path.dirname(__file__), "..", "locale", "start_menu"),
            languages=[lang],
        )
        translation.install()
        _ = translation.gettext

        self.image_path = os.path.join(MENU["PICS_PATH"], lang, self.image_name)
        self.image_hovered_path = os.path.join(
            MENU["PICS_PATH"], lang, self.image_hovered_name
        )

        self.locale = lang

        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.w, self.rect.h))

        self.image_hovered = pygame.image.load(self.image_hovered_path).convert_alpha()
        self.image_hovered = pygame.transform.scale(
            self.image_hovered, (self.rect.w, self.rect.h)
        )


class LangButton(Item):
    """Language button. Inherited from Item class."""

    def __init__(
        self,
        image: str,
        image_hovered: str,
        w: int,
        h: int,
        midtop: tuple[int],
        parent: "Object",
        action: Callable[..., None],
        args: "args",
        numb: int,
        max_numb: int,
        lang: str,
    ):
        """
        Init the Item class.

        :param image: name of the image
        :param image_hovered: name of the image, when hovering it
        :param w: width of the image
        :param h: height of the image
        :param midtop: midtop image coordinates
        :param parent: StartMenu or Level
        :param action: function
        :param args: args for the action
        :param numb: number of the button
        :param max_numb: number of the buttons on the screen
        :param lang: current language
        """
        super().__init__(
            image, image_hovered, w, h, midtop, parent, action, args, numb, max_numb
        )
        self.lang = lang

    def display(self, surface):
        """Draw the language button."""
        self.hover()
        self.click()
        if self.parent.game.locale == self.lang:
            surface.blit(self.image_hovered, self.rect_hovered)
        else:
            surface.blit(self.button, self.button_rect)


class Toggle:
    """Toggle Class."""

    def __init__(
        self,
        l: int,  # noqa: E741
        t: int,
        w: int,
        h: int,
        parent,
        numb: int,
        max_numb: int,
        value: int,
        max_value: int,
        name: str,
        update_func: Callable[..., None] = False,
    ):
        """
        Init the Toggle class.

        :param l: left coordinate
        :param t: top coordinate
        :param w: width
        :param h: height
        :param parent:
        :param numb: number of the button
        :param max_numb: number of buttons on the screen
        :param value: current music value
        :param max_value: maximum music value
        :param name: string
        :param update_func: function for update

        """
        self.parent = parent
        self.name = name

        self.rect = pygame.Rect(l, t, w, h)
        self.font = pygame.font.Font(
            UI_SETTINGS["UI_FONT"], UI_SETTINGS["UI_FONT_SIZE"]
        )

        self.value = value
        self.max_value = max_value

        self.top = self.rect.midright + pygame.math.Vector2(-20, 10)
        self.bottom = self.rect.midleft + pygame.math.Vector2(20, 10)

        full_length = self.top[0] - self.bottom[0]
        relative_number = (self.value / self.max_value) * full_length

        self.value_rect = pygame.Rect(
            self.bottom[0] + relative_number, self.bottom[1] - 15, 40, 30
        )
        self.slider = self.value_rect

        self.update_func = update_func

    def display_bar(self, surface: "pygame.display", value: float, max_value: float):
        """
        Draw the bar.

        :param surface: pygame.display
        :param value: current volume in the game
        :param max_value: maximum volume in the game

        """
        color = "#3D0814"

        pygame.draw.line(surface, color, self.top, self.bottom, 5)
        pygame.draw.rect(surface, color, self.slider)

    def hover(self):
        """Hover on the button."""
        if self.value_rect.collidepoint(pygame.mouse.get_pos()):
            self.slider = pygame.Rect.inflate(self.value_rect, 10, 10)
        else:
            self.slider = self.value_rect

    def slide(self):
        """Slide the button."""
        mouse_pos = pygame.mouse.get_pos()
        if (
            self.slider.left - 10 <= mouse_pos[0] <= self.slider.right + 10
            and self.slider.top - 10 <= mouse_pos[1] <= self.slider.bottom + 10
        ):
            if pygame.mouse.get_pressed()[0]:
                if self.bottom[0] <= pygame.mouse.get_pos()[0] <= self.top[0]:
                    self.value_rect.center = (
                        pygame.mouse.get_pos()[0],
                        self.value_rect.center[1],
                    )
                    self.value = (self.value_rect.center[0] - self.bottom[0]) / (
                        self.top[0] - self.bottom[0]
                    )
                    self.update_volume()

    def update_volume(self):
        """Upgrade volume."""
        setattr(self.parent.game, self.name + "_volume", self.value)
        if self.update_func:
            getattr(self.parent.game, self.name).update_volume(self.value)

    def display(self, surface: pygame.display, name: str):
        """
        Draw the button.

        :param surface: pygame.display
        :param name: name of the button

        """
        self.hover()
        self.slide()
        pygame.draw.rect(surface, "#FFBC42", self.rect, 0, 10)
        pygame.draw.rect(surface, "#3D0814", self.rect.inflate(5, 5), 10, 10)

        text_surface = self.font.render(name, 0, UI_SETTINGS["UI_FONT_COLOR"])
        text_rect = text_surface.get_rect(
            topleft=(
                self.rect.left + int(self.rect.w * 0.02),
                self.rect.top + int(self.rect.h * 0.08),
            )
        )

        surface.blit(text_surface, text_rect)

        self.display_bar(surface, self.value, self.max_value)
