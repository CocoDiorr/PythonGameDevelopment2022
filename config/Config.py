import os

# WINDOW_RESOLUTION = (800, 600)
WINDOW_RESOLUTION = (1280, 720)
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60
TILESIZE = 16

LEVEL_0_PIC_PATH = os.path.join("map_graphics/levels/0", "map_0.png")
LEVEL_0_DETAILS = os.path.join("map_graphics/levels/0/", "level_0_Details.csv")
LEVEL_0_ENTITIES = os.path.join("map_graphics/levels/0/", "level_0_Entities.csv")
LEVEL_0_FLOOR = os.path.join("map_graphics/levels/0/", "level_0_Floor.csv")
LEVEL_0_FLOORBLOCKS = os.path.join("map_graphics/levels/0/", "level_0_Floorblocks.csv")
LEVEL_0_GRASS = os.path.join("map_graphics/levels/0/", "level_0_Grass.csv")
LEVEL_0_OBJECTS = os.path.join("map_graphics/levels/0/", "level_0_Objects.csv")
LEVEL_0_PLAYER = os.path.join("map_graphics/levels/0/", "level_0_Player.csv")

ENTITY_SPEED_FADE = 0.8

SOLID_PATH = os.path.join("pics", "red_square.jpg")
BORDER_PATH = os.path.join("pics", "green_border.png")


PLAYER_ABS_ACCEL = 1 
PLAYER_MAX_SPEED = 5
# PLAYER_SPRITE_PATH = os.path.join("pics", "red_square.jpg")
PLAYER_SPRITE_PATH = os.path.join("map_graphics/pics", "Special1.png")
PLAYER_HEALTH = 100

BASE_ENEMY_ABS_ACCEL = 1
BASE_ENEMY_MAX_SPEED = 3
BASE_ENEMY_SPRITE_PATH = os.path.join("pics", "blue_rect.png")
BASE_ENEMY_HEALTH = 10
BASE_ENEMY_ATTACK_RADIUS = 150
BASE_ENEMY_NOTICE_RADIUS = 300

TURRET_HEALTH = 20
TURRET_ATTACK_RADIUS = 350
TURRET_NOTICE_RADIUS = 450
TURRET_PATH = os.path.join("pics", "red_square.jpg")

FAST_SHOOTER_ABS_ACCEL = 1
FAST_SHOOTER_MAX_SPEED = 3
FAST_SHOOTER_HEALTH = 10
FAST_SHOOTER_ATTACK_RADIUS = 170
FAST_SHOOTER_NOTICE_RADIUS = 250
FAST_SHOOTER_PATH = os.path.join("pics", "blue_rect.png")

SWORDSMAN_ABS_ACCEL = 1
SWORDSMAN_MAX_SPEED = 2
SWORDSMAN_HEALTH = 10
SWORDSMAN_ATTACK_RADIUS = 100
SWORDSMAN_NOTICE_RADIUS = 250
SWORDSMAN_PATH = os.path.join("pics", "blue_rect.png")

WEAPON_COOLDOWN = 0.1
BULLET_SPEED = 10
BULLET_DAMAGE = 1
BULLET_RANGE = 500
BULLET_SPRITE_PATH = os.path.join("pics", "green_square.png")

SHIELD_SPRITE_PATH = os.path.join("pics", "white_rect.png")
SHIELD_DISTANCE = 100
SHIELD_COOLDOWN = 0.5
SHIELD_ALPHA = 90
BULLET_REFLECTION_ACCELERATION = 2
BULLET_REFLECTION_DAMAGE_UP = 2 # multiplier for damage of reflected bullet

COLD_STEEL_SPRITE_PATH = os.path.join("pics", "white_rect.png")
COLD_STEEL_DISTANCE = 100
COLD_STEEL_COOLDOWN = 0.5
COLD_STEEL_ALPHA = 90
COLD_STEEL_DAMAGE = 1

SWORD_SPRITE_PATH = os.path.join("pics", "white_rect.png")
SWORD_DISTANCE = 30
SWORD_COOLDOWN = 0.5
SWORD_ALPHA = 90
SWORD_DAMAGE = 1

WORLD_MAP = [
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', 'p', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]