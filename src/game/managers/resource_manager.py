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
        for path in required_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"Required resource path not found: {path}")
        self._load_images()
        self._load_sounds()

    def _load_images(self):
        # Load background images
        bg_path = 'assets/sprites/environments/omega_district/background_layers'
        self.images['background'] = {
            name: self._load_image(f'{bg_path}/{name}.png')
            for name in ['pine1', 'pine2', 'mountain', 'sky_cloud', 'cloud']
        }
        # Load tiles
        self.images['tiles'] = [
            pygame.transform.scale(self._load_image(f'assets/sprites/environments/omega_district/structures/{x}.png'), (TILE_SIZE, TILE_SIZE))
            for x in range(TILE_TYPES)
        ]
        # Load UI images
        ui_path = 'assets/sprites/ui/menus'
        self.images['ui'] = {
            name: self._load_image(f'{ui_path}/{name}.png')
            for name in ['start_btn', 'exit_btn', 'restart_btn']
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
