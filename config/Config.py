import os



WINDOW_RESOLUTION = (1280, 720)
BACKGROUND_COLOR = (50, 50, 50)

FPS = 60
TILESIZE = 64

# LEVEL_0_PIC_PATH = os.path.join("map_graphics/levels/0", "map_0.png")

# LEVEL_0_DETAILS = os.path.join("map_graphics/levels/0/", "level_0_Details.csv")
# LEVEL_0_ENTITIES = os.path.join("map_graphics/levels/0/", "level_0_Entities.csv")
# LEVEL_0_FLOOR = os.path.join("map_graphics/levels/0/", "level_0_Floor.csv")
# LEVEL_0_FLOORBLOCKS = os.path.join("map_graphics/levels/0/", "level_0_Floorblocks.csv")
# LEVEL_0_GRASS = os.path.join("map_graphics/levels/0/", "level_0_Grass.csv")
# LEVEL_0_OBJECTS = os.path.join("map_graphics/levels/0/", "level_0_Objects.csv")
# LEVEL_0_PLAYER = os.path.join("map_graphics/levels/0/", "level_0_Player.csv")

LEVEL_PATH = "1/"

LEVEL_0_PIC_PATH = os.path.join("map_graphics", "levels", LEVEL_PATH, "map.png")

LEVEL_0_DETAILS = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Details.csv")
LEVEL_0_ENTITIES = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Entities.csv")
LEVEL_0_FLOOR = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Floor.csv")
LEVEL_0_FLOORBLOCKS = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Floorblocks.csv")
LEVEL_0_GRASS = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Grass.csv")
LEVEL_0_OBJECTS = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Objects.csv")
LEVEL_0_PLAYER = os.path.join("map_graphics", "levels", LEVEL_PATH, "map_Player.csv")

ENTITY_SPEED_FADE = 0.8
ENTITY_SPEED_ZERO = 1e-1


SOLID_PATH = os.path.join("pics", "red_square.jpg")
BORDER_PATH = os.path.join("pics", "green_border.png")

# UI
UI_SETTINGS = {"BAR_HEIGHT": 20,\
               "HEALTH_BAR_WIDTH": 200,\
               "ENERGY_BAR_WIDTH": 140,\
               "UI_FONT": os.path.join("fonts", "kongtext.ttf"),\
               "UI_FONT_SIZE": 18,\
               "UI_COLORS": {
                             "BG_COLOR": "#222222",\
                             "BORDER_COLOR": "#111111",\
                             "HEALTH": "red",\
                             "ENERGY": "blue"
                             }
               }



# Player
PLAYER_ABS_ACCEL = 1
PLAYER_MAX_SPEED = 5

# PLAYER_SPRITE_PATH = os.path.join("pics", "red_square.jpg")
PLAYER_SPRITE_PATH = os.path.join("map_graphics/pics", "Special1.png")


PLAYER_SIZE = (16, 16)

PLAYER_MAX_HEALTH = 100
PLAYER_MAX_ENERGY = 250

PLAYER_HEALTH = 100
PLAYER_ENERGY = 250
SOLID_PATH = os.path.join("pics", "red_square.jpg")

# Enemy
BASE_ENEMY_PATH = os.path.join("map_graphics/pics", "Faceset18.png")
BASE_ENEMY_ABS_ACCEL = 1
BASE_ENEMY_MAX_SPEED = 3
BASE_ENEMY_SPRITE_PATH = os.path.join("pics", "blue_rect.png")
BASE_ENEMY_HEALTH = 10
BASE_ENEMY_ATTACK_RADIUS = 150
BASE_ENEMY_NOTICE_RADIUS = 300

TURRET_HEALTH = 20
# TURRET_ATTACK_RADIUS = 8 * TILESIZE # 350
# TURRET_NOTICE_RADIUS = 8 * TILESIZE # 450
TURRET_PATH = os.path.join("map_graphics/pics", "Faceset19.png")
TURRET_ATTACK_RADIUS = 350
TURRET_NOTICE_RADIUS = 450
TURRET_SIZE = (16, 16)

FAST_SHOOTER_ABS_ACCEL = 1
FAST_SHOOTER_MAX_SPEED = 2 # 3
FAST_SHOOTER_HEALTH = 10

# FAST_SHOOTER_ATTACK_RADIUS = 5 * TILESIZE # 170
# FAST_SHOOTER_NOTICE_RADIUS = 8 * TILESIZE
FAST_SHOOTER_PATH = os.path.join("map_graphics/pics", "Faceset18.png")

FAST_SHOOTER_ATTACK_RADIUS = 170
FAST_SHOOTER_NOTICE_RADIUS = 250
# FAST_SHOOTER_PATH = os.path.join("pics", "blue_rect.png")
FAST_SHOOTER_SIZE = (16, 16)

SWORDSMAN_ABS_ACCEL = 1
SWORDSMAN_MAX_SPEED = 2
SWORDSMAN_HEALTH = 10
# SWORDSMAN_ATTACK_RADIUS = 1 * TILESIZE
# SWORDSMAN_NOTICE_RADIUS = 3 * TILESIZE # 250
SWORDSMAN_PATH = os.path.join("map_graphics/pics", "Faceset22.png")
SWORDSMAN_ATTACK_RADIUS = 100
SWORDSMAN_NOTICE_RADIUS = 250
# SWORDSMAN_PATH = os.path.join("pics", "blue_rect.png")
SWORDSMAN_SIZE = (16, 16)

WEAPON_COOLDOWN = 0.1
BULLET_SPEED = 10
BULLET_DAMAGE = 1
BULLET_RANGE = 500
BULLET_SPRITE_PATH = os.path.join("pics", "green_square.png")
BULLET_SIZE = (10, 10)

COMPANION_SIZE = (200, 200)
COMPANION_IMAGE = os.path.join("pics", "cat", "companion.png")
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


SHIELD_SPRITE_PATH = os.path.join("pics", "white_rect.png")
SHIELD_SIZE = (20, 5)
SHIELD_DISTANCE = 30
SHIELD_COOLDOWN = 0.5
SHIELD_ALPHA = 90
BULLET_REFLECTION_ACCELERATION = 2
BULLET_REFLECTION_DAMAGE_UP = 2 # multiplier for damage of reflected bullet

COLD_STEEL_SPRITE_PATH = os.path.join("pics", "orange_rect.png")
COLD_STEEL_DISTANCE = 100
COLD_STEEL_COOLDOWN = 0.5
COLD_STEEL_ALPHA = 90
COLD_STEEL_DAMAGE = 1

SWORD_SPRITE_PATH = os.path.join("pics", "orange_rect.png")
SWORD_SIZE = (5, 20)
SWORD_DISTANCE = 5
SWORD_COOLDOWN = 0.5
SWORD_ALPHA = 90
SWORD_DAMAGE = 1


SHOOTING_WEAPON_SPRITE_PATH = os.path.join("pics", "orange_rect.png")
SHOOTING_WEAPON_SIZE = (20, 5)
SHOOTING_WEAPON_DISTANCE = 30

BOW_IMAGE_PATH = os.path.join("pics", "Sprite.png")
BOW_IMAGE_SIZE = (21, 7)
BOW_DISTANCE = 15
BOW_COOLDOWN = 0.1

ARROW_SPEED = 10
ARROW_DAMAGE = 1
ARROW_RANGE = 500
ARROW_IMAGE_PATH = os.path.join("pics", "Arrow.png")
ARROW_SIZE = (20, 5)

MIN_SPRINT_ENERGY = 20
SPRINT_MULTIPLIER = 1.5
ENERGY_SPEND = 2
ENERGY_RECOVER = 0.3

