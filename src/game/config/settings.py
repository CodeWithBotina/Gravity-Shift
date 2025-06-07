import pygame

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60

# Game dimensions
ROWS = 16
COLS = 300
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 21

# Camera settings
CAMERA_OFFSET_X = SCREEN_WIDTH // 2  # Center point for camera
CAMERA_DEADZONE = 100  # Area where camera won't move

# Game physics
GRAVITY = 0.75
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

# Initialize asset containers
bullet_img = None
grenade_img = None
img_list = []

# Menu settings
MENU_BG = (25, 25, 35)
BUTTON_BG = (45, 45, 55)
BUTTON_HOVER = (55, 55, 65) 
BUTTON_TEXT = (200, 200, 200)
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_MARGIN = 20

# Button positions (centered)
MENU_CENTER_X = SCREEN_WIDTH // 2
MENU_CENTER_Y = SCREEN_HEIGHT // 2

def load_assets():
    global bullet_img, grenade_img, img_list
    bullet_img = pygame.image.load('assets/sprites/ui/icons/bullet.png').convert_alpha()
    grenade_img = pygame.image.load('assets/sprites/ui/icons/grenade.png').convert_alpha()
    
    # Load tile images
    img_list.clear()
    for x in range(TILE_TYPES):
        img = pygame.image.load(f'assets/sprites/environments/omega_district/structures/{x}.png')
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        img_list.append(img)
