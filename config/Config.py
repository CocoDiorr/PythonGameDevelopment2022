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
COMPANION_FONT = os.path.join("fonts", "Pixeltype.ttf")
COMPANION_FONT_SIZE = 36
COMPANION_COLORS = {"COMPANION_MAIN_COLOR": (219, 153, 90),\
                    "COMPANION_OUTLINE_COLOR": (101, 66, 54),\
                    "COMPANION_FONT_COLOR": (0, 0, 0)}
