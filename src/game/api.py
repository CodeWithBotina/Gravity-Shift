import pygame
import sys
import logging
import os
from pygame import mixer
from .managers.game_manager import GameManager
from .managers.level_manager import LevelManager
from .managers.input_manager import InputManager
from .managers.sprite_manager import SpriteManager
from .managers.background_manager import BackgroundManager
from .managers.resource_manager import ResourceManager
from .constants.game_states import GameState as GameStateEnum  # Add this import
from .entities.world import World
from .audio.audio import Audio
from .config.settings import *

class GameAPI:
    def __init__(self):
        self._setup_logging()
        try:
            # Initialize pygame and mixer first
            pygame.init()
            mixer.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.display.set_caption('Gravity Shift')
            logging.info("Display initialized successfully")
            
            # Load game settings
            load_assets()  # Load settings assets first
            
            # Initialize managers in correct order
            self.input_manager = InputManager()
            self.level_manager = LevelManager()
            self.resource_manager = ResourceManager()
            self.sprite_manager = SpriteManager()
            self.background_manager = BackgroundManager()  # Add this line
            
            # Initialize game manager with dependencies
            self.game_manager = GameManager(
                screen=self.screen,
                input_manager=self.input_manager,
                level_manager=self.level_manager
            )
            
            # Set background manager in game manager
            self.game_manager.background_manager = self.background_manager  # Add this line

            # Initial screen fill
            self.screen.fill(BG)
            pygame.display.flip()
            
            # Initialize clock
            self.clock = pygame.time.Clock()

        except Exception as e:
            logging.error(f"Failed to initialize game: {e}")
            raise

    def _setup_logging(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def _verify_resources(self):
        required_paths = [
            'assets/sprites/ui/menus',
            'assets/sprites/environments/omega_district',
            'assets/sprites/characters',
            'assets/audio/sfx/collectibles',
        ]
        for path in required_paths:
            if not os.path.exists(path):
                raise RuntimeError(f"Required resource path not found: {path}")

    def _load_initial_level(self):
        world_data = self.level_manager.load_level(1)
        if world_data:
            self.player, self.health_bar = self.world.process_data(
                world_data, 
                self.resource_manager.images['tiles'],
                self.game_manager.sprite_groups  # Pass game_manager's sprite groups
            )
        else:
            raise RuntimeError("Could not load initial level")

    def update(self):
        try:
            self.clock.tick(60)  # Control frame rate
            
            # Update game state through game manager
            if self.game_manager.current_state != GameStateEnum.PLAYING:
                return self.game_manager.menu_update()
            return self.game_manager.game_update()

        except Exception as e:
            logging.error(f"Error in game update: {e}", exc_info=True)
            return False
