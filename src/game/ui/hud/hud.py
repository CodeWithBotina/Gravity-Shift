import os
import pygame
import logging
from ...config.settings import (
    OXYGEN_MAX,
    WHITE, RED, GREEN, BLACK, BLUE
)

class HUD:
    def __init__(self, screen):
        if not isinstance(screen, pygame.Surface):
            raise ValueError("HUD requires a valid pygame Surface")
        self.screen = screen
        self.font = pygame.font.SysFont('Futura', 30)
        
        # Load bullet image
        try:
            bullet_img_path = os.path.join("assets", "sprites", "ui", "icons", "bullet.png")
            self.bullet_img = pygame.image.load(bullet_img_path)
        except Exception as e:
            logging.error(f"Failed to load bullet image: {e}")
            self.bullet_img = pygame.Surface((5, 5))
            self.bullet_img.fill((255, 255, 255))

        # Load grenade image
        try:
            grenade_img_path = os.path.join("assets", "sprites", "ui", "icons", "grenade copy.png")
            self.grenade_img = pygame.image.load(grenade_img_path)
        except Exception as e:
            logging.error(f"Failed to load grenade image: {e}")
            self.grenade_img = pygame.Surface((8, 8))
            self.grenade_img.fill((255, 0, 0))  # Red square as fallback

    def draw_text(self, text, x, y, color=WHITE):
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_health_bar(self, health, max_health):
        ratio = health / max_health
        pygame.draw.rect(self.screen, BLACK, (10, 10, 154, 24))
        pygame.draw.rect(self.screen, RED, (12, 12, 150, 20))
        pygame.draw.rect(self.screen, GREEN, (12, 12, 150 * ratio, 20))

    def update(self, player, oxygen_level):
        if not player:
            return
            
        self.draw_health_bar(player.health, player.max_health)
        
        # Draw ammo count
        self.draw_text('AMMO: ', 10, 35)
        for x in range(player.ammo):
            self.screen.blit(self.bullet_img, (90 + (x * 10), 40))
            
        # Draw grenades
        self.draw_text('GRENADES: ', 10, 60)
        for x in range(player.grenades):
            self.screen.blit(self.grenade_img, (135 + (x * 15), 60))
            
        # Draw oxygen bar
        ratio = oxygen_level / OXYGEN_MAX
        pygame.draw.rect(self.screen, BLACK, (10, 80, 154, 24))
        pygame.draw.rect(self.screen, RED, (12, 82, 150, 20))
        pygame.draw.rect(self.screen, BLUE, (12, 82, 150 * ratio, 20))
        self.draw_text('OXYGEN', 45, 82)
