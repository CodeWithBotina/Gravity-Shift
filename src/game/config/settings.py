import pygame
import os

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60

# UI settings
MENU_CENTER_X = SCREEN_WIDTH // 2
MENU_CENTER_Y = SCREEN_HEIGHT // 2
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20
MENU_BG = (50, 50, 70)  # Dark blue-gray
BUTTON_BG = (100, 100, 120)  # Light blue-gray
BUTTON_HOVER = (120, 120, 140)  # Lighter blue-gray
BUTTON_TEXT = (255, 255, 255)  # White

# Tile settings
TILE_SIZE = 64
TILE_TYPES = 21  # Total number of different tile types

# Game dimensions
ROWS = 16
COLS = 300

# Camera settings
CAMERA_OFFSET_X = SCREEN_WIDTH // 2  # Center point for camera
CAMERA_DEADZONE = 100  # Area where camera won't move

# Game physics
GRAVITY = 0.6  # Reduced gravity for smoother fall
JUMP_SPEED = -11  # Initial jump velocity
MAX_FALL_SPEED = 10  # Maximum falling speed
JUMP_CUT_MULTIPLIER = 0.4  # How much to cut jump when button is released
COYOTE_TIME = 6  # Frames of time where player can still jump after leaving ground
JUMP_BUFFER = 6  # Frames of time where jump input is buffered
AIR_CONTROL = 0.8  # How much control player has in air (1 = full control)

# Modify scroll threshold to be center-based
SCROLL_THRESH = SCREEN_WIDTH // 4  # Distance from center before scrolling

# Physics settings
SPACE_GRAVITY = 0.1  # Reduced gravity for space environment
SPACE_FRICTION = 0.98  # Friction in space (close to 1 for low friction)
THRUST_POWER = 0.5  # Power of the player's thrusters
MAX_SPEED = 8  # Maximum movement speed
ROTATION_SPEED = 3  # Speed at which the player rotates
BOUNCE_FACTOR = 0.5  # How much velocity is retained after collision

# Colors
BG = (144, 201, 120)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PINK = (235, 65, 54)
BLUE = (0, 191, 255)

# Game states
OXYGEN_MAX = 100
MAX_LEVELS = 3

# Initialize asset variables
bullet_img = None
grenade_img = None
img_list = []

def load_assets():
    global bullet_img, grenade_img, img_list
    
    # Load bullet and grenade images
    bullet_img = pygame.image.load('assets/sprites/ui/icons/bullet.png').convert_alpha()
    grenade_img = pygame.image.load('assets/sprites/ui/icons/grenade.png').convert_alpha()
    
    # Load tile images
    img_list.clear()
    for x in range(TILE_TYPES):
        img = pygame.image.load(f'assets/sprites/environments/omega_district/structures/{x}.png')
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        img_list.append(img)

    return img_list
