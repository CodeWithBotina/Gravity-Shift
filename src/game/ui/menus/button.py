import pygame
from ...config.settings import *

class Button:
    def __init__(self, x, y, text, width=BUTTON_WIDTH, height=BUTTON_HEIGHT):
        self.rect = pygame.Rect(0, 0, width, height)
        # Center the button on x, y coordinates
        self.rect.centerx = x
        self.rect.centery = y
        self.text = text
        self.font = pygame.font.SysFont('Futura', 24)
        self.clicked = False
        self.hovered = False
        
    def draw(self, surface):
        action = False
        # Get mouse position and check hover
        pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(pos)
        
        # Draw button background
        color = BUTTON_HOVER if self.hovered else BUTTON_BG
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BUTTON_TEXT, self.rect, 2)  # Border
        
        # Draw text
        text_surf = self.font.render(self.text, True, BUTTON_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
        # Handle click
        if self.hovered:
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            
        return action