import os

WINDOW_RESOLUTION = (1280, 720)
BACKGROUND_COLOR = (100, 100, 100)
BLACK = (0, 0, 0)

FPS = 60
TILESIZE = 32

SCALE = int(TILESIZE / 16)

LEVEL_0_PIC_PATH = os.path.join("map_graphics", "levels", "0", "map_0.png")
LEVEL_0_DETAILS = os.path.join("map_graphics", "levels", "0", "level_0_Details.csv")
LEVEL_0_ENTITIES = os.path.join("map_graphics", "levels", "0", "level_0_Entities.csv")
LEVEL_0_FLOOR = os.path.join("map_graphics", "levels", "0", "level_0_Floor.csv")
LEVEL_0_FLOORBLOCKS = os.path.join("map_graphics", "levels", "0", "level_0_Floorblocks.csv")
LEVEL_0_GRASS = os.path.join("map_graphics", "levels", "0", "level_0_Grass.csv")
LEVEL_0_OBJECTS = os.path.join("map_graphics", "levels", "0", "level_0_Objects.csv")
LEVEL_0_PLAYER = os.path.join("map_graphics", "levels", "0", "level_0_Player.csv")

ENTITY_SPEED_FADE = 0.8
ENTITY_SPEED_ZERO = 1e-1


SOLID_PATH = os.path.join("pics", "red_square.jpg")
BORDER_PATH = os.path.join("pics", "green_border.png")

# UI
UI_SETTINGS = {"BAR_HEIGHT": 20,\
               "HEALTH_BAR_WIDTH": 200,\
               "ENERGY_BAR_WIDTH": 140,\
               "UI_FONT": os.path.join("fonts", "pixelcyr_normal.ttf"),\
               "UI_FONT_SIZE": 28,\
               "UI_FONT_COLOR": (0, 0, 0),\
               "UI_COLORS": {
                             "BG_COLOR": "#222222",\
                             "BORDER_COLOR": "#111111",\
                             "HEALTH": "red",\
                             "ENERGY": "blue"
                             }
               }


ANIMATION_SPEED = 0.15

# Player
PLAYER_ABS_ACCEL = 1
PLAYER_MAX_SPEED = 5

# PLAYER_SPRITE_PATH = os.path.join("pics", "red_square.jpg")
PLAYER_SPRITE_PATH = os.path.join("map_graphics", "pics", "Special1.png")
PLAYER_ANIMATION_PATH = os.path.join("pics", "BlueNinja", "SeparateAnim", "Walk.png")

PLAYER_MAX_HEALTH = 100
PLAYER_MAX_ENERGY = 250

PLAYER_HEALTH = 100
PLAYER_ENERGY = 250

SOLID_PATH = os.path.join("pics", "red_square.jpg")

# Enemy
BASE_ENEMY_ABS_ACCEL = 1
BASE_ENEMY_MAX_SPEED = 3
BASE_ENEMY_SPRITE_PATH = os.path.join("pics", "blue_rect.png")
BASE_ENEMY_HEALTH = 10
BASE_ENEMY_ATTACK_RADIUS = 5 * TILESIZE
BASE_ENEMY_NOTICE_RADIUS = 8 * TILESIZE

TURRET_HEALTH = 20
TURRET_ATTACK_RADIUS = 8 * TILESIZE
TURRET_NOTICE_RADIUS = 8 * TILESIZE
TURRET_ANIMATION = os.path.join("pics", "Skeleton", "SeparateAnim", "Walk.png")


FAST_SHOOTER_ABS_ACCEL = 1
FAST_SHOOTER_MAX_SPEED = 2
FAST_SHOOTER_HEALTH = 10

FAST_SHOOTER_ATTACK_RADIUS = 5 * TILESIZE
FAST_SHOOTER_NOTICE_RADIUS = 8 * TILESIZE
FAST_SHOOTER_ANIMATION = os.path.join("pics", "Monk", "SeparateAnim", "Walk.png")


SWORDSMAN_ABS_ACCEL = 1
SWORDSMAN_MAX_SPEED = 2
SWORDSMAN_HEALTH = 10
SWORDSMAN_ATTACK_RADIUS = 1 * TILESIZE
SWORDSMAN_NOTICE_RADIUS = 3 * TILESIZE
SWORDSMAN_ANIMATION = os.path.join("pics", "GoldKnight", "SeparateAnim", "Walk.png")

WEAPON_COOLDOWN = 0.1
BULLET_SPEED = 10
BULLET_DAMAGE = 1
BULLET_RANGE = 500
BULLET_SPRITE_PATH = os.path.join("pics", "green_square.png")
BULLET_SIZE = (10, 10)

COMPANION_SIZE = (200, 200)
COMPANION_IMAGE = os.path.join("pics", "cat", "companion.png")
COMPANION_FONT = os.path.join("fonts", "pixelcyr_normal.ttf")
COMPANION_FONT_SIZE = 24
COMPANION_COLORS = {"MAIN_COLOR": (219, 153, 90),\
                    "OUTLINE_COLOR": (101, 66, 54),\
                    "GRADIENT": (130, 85, 70),\
                    "FONT_COLOR": (0, 0, 0)}
COMPANION_BUTTON = {"FONT": os.path.join("fonts", "pixelcyr_normal.ttf"),\
                    "FONT_SIZE": 40,\
                    "FONT_COLOR": (8, 76, 97),\
                    "MAIN_COLOR": (224, 251, 252),\
                    "OUTLINE_COLOR": (152, 193, 217)}


SHIELD_SPRITE_PATH = os.path.join("pics", "white_rect.png")
SHIELD_SIZE = (int(TILESIZE*1.5), int(TILESIZE / 3))
SHIELD_DISTANCE = TILESIZE
SHIELD_COOLDOWN = 0.5
SHIELD_ALPHA = 90
BULLET_REFLECTION_ACCELERATION = 2
BULLET_REFLECTION_DAMAGE_UP = 2 # multiplier for damage of reflected bullet

COLD_STEEL_SPRITE_PATH = os.path.join("pics", "orange_rect.png")
COLD_STEEL_DISTANCE = int(TILESIZE / 2)
COLD_STEEL_COOLDOWN = 0.5
COLD_STEEL_ALPHA = 90
COLD_STEEL_DAMAGE = 1

SWORD_SPRITE_PATH = os.path.join("pics", "Sword2", "Sprite.png")
SWORD_SIZE = (int(TILESIZE * 0.4), int(TILESIZE * 1.6))
SWORD_DISTANCE = int(TILESIZE / 2)
SWORD_COOLDOWN = 0.5
SWORD_ALPHA = 90
SWORD_DAMAGE = 1


SHOOTING_WEAPON_SPRITE_PATH = os.path.join("pics", "orange_rect.png")
SHOOTING_WEAPON_SIZE = (int(TILESIZE / 4), TILESIZE)
SHOOTING_WEAPON_DISTANCE = int(TILESIZE / 2)

BOW_IMAGE_PATH = os.path.join("pics", "Sprite.png")
BOW_IMAGE_SIZE = (int(TILESIZE * 1.2), int(TILESIZE * 0.3))
BOW_DISTANCE = int(TILESIZE / 2)
BOW_COOLDOWN = 0.5

ARROW_SPEED = 10
ARROW_DAMAGE = 1
ARROW_RANGE = 500
ARROW_IMAGE_PATH = os.path.join("pics", "Arrow.png")
ARROW_SIZE = (20, 5)

MIN_SPRINT_ENERGY = 20
SPRINT_MULTIPLIER = 1.5
ENERGY_SPEND = 2
ENERGY_RECOVER = 0.3

