import pygame
import csv
import logging
import sys
import os
from ..ui.menus.button import Button
from ..entities.sprites import Grenade
from ..entities.effects import ScreenFade
from ..world.world import World
from .input_manager import InputManager
from .background_manager import BackgroundManager
from ..ui.hud.hud import HUD
from .level_manager import LevelManager
from ..constants.game_states import GameState as GameStateEnum  # Rename import
from .game_state import GameState as GameStateManager  # Add this import
from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, OXYGEN_MAX, bullet_img, grenade_img, ROWS, COLS, BG, PINK, img_list, TILE_SIZE
from .camera import Camera
from .ui_manager import UIManager
from ..managers.resource_manager import ResourceManager  # Import ResourceManager
from ..world.platform import Platform  # Add this import at the top with other imports
from ..audio.audio import Audio  # Add this import

class GameManager:
    def __init__(self, screen, input_manager=None, level_manager=None):
        if not isinstance(screen, pygame.Surface):
            raise ValueError("Screen must be a pygame Surface")
        self.screen = screen
        
        # Initialize game state
        self.game_state = GameStateManager()  # Use GameStateManager for state tracking
        self.current_state = GameStateEnum.MENU  # Use GameStateEnum for state enum
        
        # Initialize managers
        self.input_manager = input_manager or InputManager()
        self.level_manager = level_manager or LevelManager()
        self.resource_manager = ResourceManager()
        self.ui_manager = UIManager(screen)
        self.camera = Camera(screen.get_width(), screen.get_height())
        self.hud = HUD(screen)  # Initialize HUD with screen
        self.audio = Audio()  # Initialize audio manager
        
        # Initialize sprite groups and game objects
        self.sprite_groups = {
            'enemy': pygame.sprite.Group(),
            'bullet': pygame.sprite.Group(),
            'grenade': pygame.sprite.Group(),
            'explosion': pygame.sprite.Group(),
            'item_box': pygame.sprite.Group(),
            'decoration': pygame.sprite.Group(),
            'water': pygame.sprite.Group(),
            'exit': pygame.sprite.Group()
        }
        
        # Initialize platforms list
        self.platforms = []
        
        # Initialize background manager and game state
        self.background_manager = BackgroundManager()
        
        # Initialize game variables
        self.score = 0
        self.level = 1
        self.player = None  # Initialize player as None
        self.bg_scroll = 0
        self.screen_scroll = 0
        self.oxygen_level = OXYGEN_MAX
        self.start_game = False
        self.game_over = False
        
        try:
            # Load resources after managers are initialized
            self._load_resources()
            # Create default level and player if level loading fails
            if not self.load_level(self.level):
                self.create_default_level()
        except Exception as e:
            logging.error(f"Failed to initialize resources: {e}")
            raise

    def _load_resources(self):
        try:
            if not hasattr(self.resource_manager, 'get_image'):
                raise AttributeError("Resource manager not properly initialized")
                
            self.button_images = {
                'start': self.resource_manager.get_image('ui', 'start_btn'),
                'exit': self.resource_manager.get_image('ui', 'exit_btn'),
                'restart': self.resource_manager.get_image('ui', 'restart_btn')
            }
            
            # Make sure we have all required images
            if any(img is None for img in self.button_images.values()):
                raise ValueError("Failed to load one or more button images")
                
            self._load_buttons()
            
        except Exception as e:
            logging.error(f"Error in _load_resources: {e}")
            raise

    def reset_game(self):
        if not self.sprite_groups:
            self.sprite_groups = {
                'enemy': pygame.sprite.Group(),
                'bullet': pygame.sprite.Group(),
                'grenade': pygame.sprite.Group(),
                'explosion': pygame.sprite.Group(),
                'item_box': pygame.sprite.Group(),
                'decoration': pygame.sprite.Group(),
                'water': pygame.sprite.Group(),
                'exit': pygame.sprite.Group()
            }

        # Clear all groups
        for group in self.sprite_groups.values():
            group.empty()

        # Reset level
        self.level = 1
        self.bg_scroll = 0
        self.screen_scroll = 0
        self.start_game = False
        self.game_over = False
        
        try:
            # Load first level
            self.load_level(self.level)
        except Exception as e:
            logging.error(f"Failed to load initial level: {e}")
            raise

    def load_level(self, level):
        try:
            self.world_data = []
            for row in range(ROWS):
                r = [-1] * COLS
                self.world_data.append(r)

            # Load level data
            level_path = f'assets/data/levels/level{level}_data.csv'
            if not os.path.exists(level_path):
                # Create a default level if file doesn't exist
                self.create_default_level()
            else:
                with open(level_path, newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for y, row in enumerate(reader):
                        for x, tile in enumerate(row):
                            if x < COLS and y < ROWS:
                                self.world_data[y][x] = int(tile)

            # Ensure world is initialized
            self.world = World()  # Initialize world object
            self.player, self.health_bar = self.world.process_data(self.world_data, self.sprite_groups)
            if self.player:
                self.player.world = self.world  # Assign world to player
            return True
        except Exception as e:
            logging.error(f"Error loading level: {e}")
            return False

    def create_default_level(self):
        """Create a basic default level if no level file exists"""
        # Create world data with default platform and player spawn
        self.world_data = [[-1] * COLS for _ in range(ROWS)]
        
        # Add solid ground platform
        for x in range(COLS):
            # Ground layer is solid (tile type 0)
            self.world_data[ROWS-1][x] = 0
            
        # Add player spawn position one tile above ground
        # Add a few solid blocks as starting platform
        start_platform_length = 5
        for x in range(start_platform_length):
            self.world_data[ROWS-2][x] = 0  # Solid platform
            
        # Place player on the starting platform
        self.world_data[ROWS-3][1] = 15  # Player tile ID
        
        # Create world and process data
        self.world = World()  # Initialize world object
        self.player, self.health_bar = self.world.process_data(self.world_data, self.sprite_groups)
        if self.player:
            self.player.world = self.world  # Assign world to player
            self.player.on_ground = False  # Ensure player starts affected by gravity
        else:
            from ..entities.player import Player
            # Create default player if processing fails
            self.player = Player(
                x=100,
                y=SCREEN_HEIGHT - 200,
                scale=1.65,
                speed=5,
                ammo=20,
                grenades=5
            )
            self.player.world = self.world  # Assign world to player

    def init_with_dependencies(self, player, world):
        self.player = player
        self.world = world
        if player:
            player.world = world  # Update world reference
        # Initialize level
        self.level = 1

    def _load_button_images(self):
        return {
            'start': pygame.image.load('assets/sprites/ui/menus/start_btn.png').convert_alpha(),
            'exit': pygame.image.load('assets/sprites/ui/menus/exit_btn.png').convert_alpha(),
            'restart': pygame.image.load('assets/sprites/ui/menus/restart_btn.png').convert_alpha()
        }
        
    def _load_buttons(self):
        self.start_button = Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, 
                                 self.button_images['start'], 1)
        self.exit_button = Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, 
                                self.button_images['exit'], 1)
        self.restart_button = Button(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 
                                   self.button_images['restart'], 2)

    def handle_click(self, pos):
        if not self.start_game:
            if self.start_button.rect.collidepoint(pos):
                logging.info("Start button clicked")
                self.start_game = True
                return True
            elif self.exit_button.rect.collidepoint(pos):
                logging.info("Exit button clicked")
                return False
        return True

    def is_game_started(self):
        return self.start_game

    def show_menu(self):
        logging.debug("Drawing menu")
        action = self.ui_manager.draw_menu()
        return action

    def menu_update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked_button = self.ui_manager.handle_button_click(event.pos)
                if clicked_button == 'start':
                    logging.info("Start button clicked, starting game")
                    self.game_state.start_game = True
                    self.current_state = GameStateEnum.PLAYING
                    self.start_new_game()
                    return True

        self.screen.fill((0, 0, 0))
        self.ui_manager.draw_menu()
        pygame.display.flip()
        return True

    def start_new_game(self):
        """Initialize game state when starting a new game"""
        try:
            # Create default level if loading fails
            if not self.load_level(self.level):
                self.create_default_level()
            
            # Initialize game state
            self.game_state.start_game = True
            self.score = 0
            self.oxygen_level = OXYGEN_MAX
            
            # Make sure we have a player
            if self.player:
                self.player.reset()
            else:
                self.create_default_level()  # This will create a player if none exists
                
            logging.info("Game successfully started")
        except Exception as e:
            logging.error(f"Error starting new game: {e}")
            raise

    def update(self):
        if not self.game_state.start_game:
            return self.menu_update()
        return self.game_update()

    def game_update(self):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.shutdown_game()  # Ensure the game shuts down properly

            if not self.player or not self.player.alive:
                logging.info("Player is dead, handling death screen...")
                self.handle_death_screen()
                return True

            # Process player input
            self.input_manager.process_input(self.player, self.audio)

            # Update player position and animation
            self.player.update()
            self.player.world = self.world  # Set the player's world attribute

            # Update camera to follow player
            if self.player:
                self.camera.update(self.player, self.world.level_length * TILE_SIZE)

            # Ensure player is not restricted unnecessarily
            if self.player.rect.right > self.world.level_length * TILE_SIZE:
                self.player.rect.right = self.world.level_length * TILE_SIZE

            # Draw game state
            self.draw_game()
            
            return True
        except Exception as e:
            logging.error(f"Error in game_update: {e}", exc_info=True)
            return False

    def _update_oxygen_and_health(self):
        """Update oxygen level and health based on oxygen depletion"""
        if not hasattr(self, 'last_oxygen_update'):
            self.last_oxygen_update = pygame.time.get_ticks()
        
        current_time = pygame.time.get_ticks()
        if current_time - self.last_oxygen_update > 1000:  # Every second
            self.oxygen_level = max(0, self.oxygen_level - 0.5)  # Decrease oxygen
            self.last_oxygen_update = current_time
            
            # When oxygen is depleted, start decreasing health
            if self.oxygen_level <= 0 and self.player:
                self.player.health = max(0, self.player.health - 1)

    def _update_player_animation(self):
        """Update player animation based on current state"""
        if not self.player:
            return
            
        # Determine animation state
        if not self.player.alive:
            self.player.update_action(3)  # Death animation
        elif self.player.in_air:
            self.player.update_action(2)  # Jump animation
        elif self.input_manager.moving_left or self.input_manager.moving_right:
            self.player.update_action(1)  # Run animation
        else:
            self.player.update_action(0)  # Idle animation

    def draw_game(self):
        # Clear screen with background color
        self.screen.fill(BG)
        
        # Draw background layers first
        self.background_manager.draw(self.screen)
        
        # Draw world elements with camera offset
        if self.world:
            # Asegurarse de que la cámara esté actualizada
            if self.player:
                self.camera.update(self.player, self.world.level_length * TILE_SIZE)
            # Dibujar el mundo con el scroll de la cámara
            self.world.draw(self.screen, self.camera.scroll)
        
        # Draw sprite groups with camera offset
        for group in self.sprite_groups.values():
            for sprite in group:
                sprite_pos = self.camera.apply(sprite)
                self.screen.blit(sprite.image, sprite_pos)

        # Draw player with camera offset if alive
        if self.player and self.player.alive:
            player_pos = self.camera.apply(self.player)
            self.screen.blit(pygame.transform.flip(self.player.image, self.player.flip, False), player_pos)
        
        # Draw HUD last (no camera offset)
        self.hud.update(self.player, self.oxygen_level)
        
        # Update the display
        pygame.display.flip()

    def handle_death_screen(self):
        if not hasattr(self, 'death_fade'):
            self.death_fade = ScreenFade(2, PINK, 4)
        
        fade_complete = self.death_fade.fade(self.screen)
        
        if fade_complete:
            action = self.ui_manager.draw_death_menu()
            if action == 'restart':
                self.death_fade = ScreenFade(2, PINK, 4)
                self.reset_level()
            elif action == 'exit':
                return False
        return True

    def throw_grenade(self, player, audio):
        if player.grenades > 0:
            grenade = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),
                             player.rect.top, player.direction)
            self.sprite_groups['grenade'].add(grenade)
            player.grenades -= 1
            audio.play('grenade')

    def draw_sprites(self):
        for group in self.sprite_groups.values():
            group.draw(self.screen)

    def update_sprites(self):
        for group in self.sprite_groups.values():
            for sprite in group:
                sprite.update(self.screen_scroll)

    def update_hud(self):
        if self.player:
            self.hud.draw_health_bar(self.player.health, self.player.max_health)
            self.hud.draw_ammo(self.player.ammo, self.bullet_img)
            self.hud.draw_grenades(self.player.grenades, self.grenade_img)
            self.hud.draw_oxygen_bar(self.oxygen_level, OXYGEN_MAX)

    def check_level_complete(self):
        return pygame.sprite.spritecollide(self.player, self.sprite_groups['exit'], False)

    def handle_level_complete(self, level_manager):
        self.start_intro = True
        self.level += 1
        self.bg_scroll = 0
        world_data = level_manager.load_level(self.level)
        if world_data:
            self.reset_level()
            self.world.process_data(world_data, self.sprite_groups)

    def reset_level(self):
        # Ensure we have a level manager
        if not hasattr(self, 'level_manager'):
            self.level_manager = LevelManager()
        
        # Reset player and world
        self.player.reset()
        self.oxygen_level = OXYGEN_MAX
        
        # Reset sprite groups
        for group in self.sprite_groups.values():
            group.empty()
            
        # Reload current level
        world_data = self.level_manager.load_level(self.level)
        if world_data:
            self.world = World()
            self.player, self.health_bar = self.world.process_data(world_data, self.sprite_groups)
            self.player.world = self.world

    def draw_game(self):
        # Clear screen with background color
        self.screen.fill(BG)
        
        # Draw background layers first
        self.background_manager.draw(self.screen)
        
        # Draw world elements with camera offset
        if self.world:
            # Asegurarse de que la cámara esté actualizada
            if self.player:
                self.camera.update(self.player, self.world.level_length * TILE_SIZE)
            # Dibujar el mundo con el scroll de la cámara
            self.world.draw(self.screen, self.camera.scroll)
        
        # Draw sprite groups with camera offset
        for group in self.sprite_groups.values():
            for sprite in group:
                sprite_pos = self.camera.apply(sprite)
                self.screen.blit(sprite.image, sprite_pos)

        # Draw player with camera offset if alive
        if self.player and self.player.alive:
            player_pos = self.camera.apply(self.player)
            self.screen.blit(pygame.transform.flip(self.player.image, self.player.flip, False), player_pos)
        
        # Draw HUD last (no camera offset)
        self.hud.update(self.player, self.oxygen_level)
        
        # Update the display
        pygame.display.flip()

    def initialize_level(self):
        """Initialize level elements"""
        # Add a ground platform
        ground = Platform(0, self.screen.get_height() - 40, self.screen.get_width(), 40)
        self.platforms.append(ground)
        
        # Add any other initial platforms
        platform1 = Platform(300, 300, 200, 20)
        self.platforms.append(platform1)
        
        # Reset player position
        self.player.position.x = 100
        self.player.position.y = self.screen.get_height() - 100

    def shutdown_game(self):
        """Handle game shutdown logic."""
        logging.info("Shutting down game...")
        pygame.quit()
        sys.exit()
