import os


WINDOW_RESOLUTION = (1280, 720)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

ENTITY_SPEED_FADE = 0.8

PLAYER_ABS_ACCEL = 1
PLAYER_MAX_SPEED = 5
PLAYER_SPRITE_PATH = os.path.join("pics", "red_square.jpg")
PLAYER_HEALTH = 100

BASE_ENEMY_ABS_ACCEL = 1
BASE_ENEMY_MAX_SPEED = 3
BASE_ENEMY_SPRITE_PATH = os.path.join("pics", "blue_rect.png")
BASE_ENEMY_HEALTH = 10

WEAPON_COOLDOWN = 0.1
BULLET_SPEED = 10
BULLET_DAMAGE = 1
BULLET_RANGE = 500
BULLET_SPRITE_PATH = os.path.join("pics", "green_square.png")

COMPANION_SIZE = (200, 200)
COMPANION_IMAGE = os.path.join("pics", "cat","companion.png")
COMPANION_FONT = os.path.join("fonts", "kongtext.ttf")
COMPANION_FONT_SIZE = 20
COMPANION_COLORS = {"MAIN_COLOR": (219, 153, 90),\
                    "OUTLINE_COLOR": (101, 66, 54),\
                    "GRADIENT": (130, 85, 70),\
                    "FONT_COLOR": (0, 0, 0)}
COMPANION_BUTTON = {"FONT": os.path.join("fonts", "kongtext.ttf"),\
                    "FONT_SIZE": 40,\
                    "FONT_COLOR": (8, 76, 97),\
                    "MAIN_COLOR": (224, 251, 252),\
                    "OUTLINE_COLOR": (152, 193, 217)}
