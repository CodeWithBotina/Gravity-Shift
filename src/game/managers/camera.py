import pygame
from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCROLL_THRESH

class Camera:
    def __init__(self, screen_width, screen_height):
        self.scroll = pygame.math.Vector2(0, 0)
        self.screen_width = screen_width
        self.screen_height = screen_height

    def apply(self, entity):
        return entity.rect.move((-self.scroll.x, -self.scroll.y))

    def update(self, player, level_width):
        # Center the camera on the player, considering SCROLL_THRESH
        target_x = player.rect.centerx - self.screen_width // 2
        target_y = player.rect.centery - self.screen_height // 2
        
        # Suavizar el movimiento de la cámara
        self.scroll.x += (target_x - self.scroll.x) * 0.1
        self.scroll.y += (target_y - self.scroll.y) * 0.1
        
        # Mantener la cámara dentro de los límites del nivel
        self.scroll.x = max(0, min(self.scroll.x, level_width - self.screen_width))
        self.scroll.y = max(0, min(self.scroll.y, level_width - self.screen_height))
