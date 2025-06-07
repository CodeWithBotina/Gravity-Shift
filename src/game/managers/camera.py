import pygame
from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, SCROLL_THRESH

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.scroll = 0

    def apply(self, entity):
        return entity.rect.move((-self.scroll, 0))

    def update(self, target):
        # Target is typically the player
        if target.rect.right > SCREEN_WIDTH - SCROLL_THRESH:
            self.scroll += (target.rect.right - (SCREEN_WIDTH - SCROLL_THRESH))
        elif target.rect.left < SCROLL_THRESH:
            self.scroll -= (SCROLL_THRESH - target.rect.left)

        # Keep camera within bounds
        self.scroll = max(0, min(self.scroll, SCREEN_WIDTH))
