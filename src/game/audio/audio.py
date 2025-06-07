import pygame
import os

class Audio:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)
        self.sounds = {}
        self.load_sounds()

    def load_sounds(self):
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
                print(f"Warning: Sound file not found: {path}")

    def play(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()
