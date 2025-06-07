import pygame
import os
import logging
import csv
from ..config.settings import TILE_SIZE, TILE_TYPES, ROWS, COLS

class ResourceManager:
    def __init__(self):
        self.images = {
            'tiles': [],
            'ui': {},
            'background': {}
        }
        self.sounds = {}
        try:
            self._verify_and_load_resources()
        except Exception as e:
            logging.error(f"Failed to initialize ResourceManager: {e}")
            raise

    def _verify_and_load_resources(self):
        required_paths = [
            'assets/sprites/ui/menus',
            'assets/sprites/environments/omega_district',
            'assets/sprites/characters',
            'assets/audio/sfx/collectibles'
        ]
        
        # Verify paths exist
        for path in required_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Required resource path not found: {path}")
        
        # Load resources
        self._load_images()
        self._load_sounds()

        # Create default resources if not found
        if not os.path.exists('assets/data/levels/level1_data.csv'):
            self._create_default_level()
            
    def _create_default_level(self):
        """Create a default level file if none exists"""
        os.makedirs('assets/data/levels', exist_ok=True)
        level_data = [[-1] * COLS for _ in range(ROWS)]
        
        # Add basic level structure
        for x in range(COLS):
            level_data[ROWS-1][x] = 0  # Ground
        level_data[ROWS-2][1] = 15     # Player spawn
        
        # Save default level
        with open('assets/data/levels/level1_data.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(level_data)

    def _load_images(self):
        # Background images
        bg_path = 'assets/sprites/environments/omega_district/background_layers'
        self.images['background'] = {
            'pine1': self._load_image(f'{bg_path}/pine1.png'),
            'pine2': self._load_image(f'{bg_path}/pine2.png'),
            'mountain': self._load_image(f'{bg_path}/mountain.png'),
            'sky': self._load_image(f'{bg_path}/sky_cloud.png'),
            'saturn': self._load_image(f'{bg_path}/cloud.png')
        }

        # Tiles
        self.images['tiles'] = []
        for x in range(TILE_TYPES):
            path = f'assets/sprites/environments/omega_district/structures/{x}.png'
            img = self._load_image(path)
            self.images['tiles'].append(pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE)))

        # Add UI images loading
        ui_path = 'assets/sprites/ui/menus'
        self.images['ui'] = {
            'start_btn': self._load_image(f'{ui_path}/start_btn.png'),
            'exit_btn': self._load_image(f'{ui_path}/exit_btn.png'),
            'restart_btn': self._load_image(f'{ui_path}/restart_btn.png')
        }

    def _load_image(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Image not found: {path}")
        return pygame.image.load(path).convert_alpha()

    def _load_sounds(self):
        sound_files = {
            'jump': 'assets/audio/sfx/collectibles/jump.wav',
            'shot': 'assets/audio/sfx/collectibles/shot.wav',
            'grenade': 'assets/audio/sfx/collectibles/grenade.wav'
        }
        
        for name, path in sound_files.items():
            if os.path.exists(path):
                sound = pygame.mixer.Sound(path)
                sound.set_volume(0.05)
                self.sounds[name] = sound
            else:
                logging.warning(f"Sound file not found: {path}")

    def get_image(self, category, name):
        if category in self.images:
            if isinstance(self.images[category], dict):
                return self.images[category].get(name)
            elif isinstance(self.images[category], list):
                return self.images[category][name] if 0 <= name < len(self.images[category]) else None
        return None
