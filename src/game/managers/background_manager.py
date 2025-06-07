import pygame
from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BG

class BackgroundManager:
    def __init__(self):
        self.bg_images = {
            'sky': pygame.image.load('assets/sprites/environments/omega_district/background_layers/sky_cloud.png').convert_alpha(),
            'saturn': pygame.image.load('assets/sprites/environments/omega_district/background_layers/cloud.png').convert_alpha(),
            'mountain': pygame.image.load('assets/sprites/environments/omega_district/background_layers/mountain.png').convert_alpha(),
            'pine1': pygame.image.load('assets/sprites/environments/omega_district/background_layers/pine1.png').convert_alpha(),
            'pine2': pygame.image.load('assets/sprites/environments/omega_district/background_layers/pine2.png').convert_alpha()
        }
        self.bg_scroll = 0

    def draw(self, surface):
        surface.fill(BG)
        width = self.bg_images['sky'].get_width()
        
        # Draw Saturn first
        surface.blit(self.bg_images['saturn'], 
                    (SCREEN_WIDTH - self.bg_images['saturn'].get_width(), 50))
        
        # Draw parallax layers
        for x in range(5):
            surface.blit(self.bg_images['sky'], 
                        ((x * width) - self.bg_scroll * 0.5, 0))
            surface.blit(self.bg_images['mountain'], 
                        ((x * width) - self.bg_scroll * 0.6, 
                         SCREEN_HEIGHT - self.bg_images['mountain'].get_height() - 300))
            surface.blit(self.bg_images['pine1'], 
                        ((x * width) - self.bg_scroll * 0.7, 
                         SCREEN_HEIGHT - self.bg_images['pine1'].get_height() - 150))
            surface.blit(self.bg_images['pine2'], 
                        ((x * width) - self.bg_scroll * 0.8, 
                         SCREEN_HEIGHT - self.bg_images['pine2'].get_height()))

    def update_scroll(self, scroll_amount):
        self.bg_scroll -= scroll_amount
