import pygame
from ..config.settings import *

class HUD:
    def __init__(self, surface):
        self.surface = surface
        self.font = pygame.font.SysFont('Futura', 30)
        self.bullet_img = pygame.image.load('assets/sprites/ui/icons/bullet.png').convert_alpha()
        self.grenade_img = pygame.image.load('assets/sprites/ui/icons/grenade.png').convert_alpha()

    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        self.surface.blit(img, (x, y))

    def draw_health_bar(self, health, max_health, x, y):
        ratio = health / max_health
        pygame.draw.rect(self.surface, BLACK, (x - 2, y - 2, 154, 24))
        pygame.draw.rect(self.surface, RED, (x, y, 150, 20))
        pygame.draw.rect(self.surface, GREEN, (x, y, 150 * ratio, 20))

    def draw_oxygen_bar(self, oxygen_level):
        ratio = oxygen_level / OXYGEN_MAX
        pygame.draw.rect(self.surface, BLACK, (10, 80, 154, 24))
        pygame.draw.rect(self.surface, RED, (12, 82, 150, 20))
        pygame.draw.rect(self.surface, (0, 191, 255), (12, 82, 150 * ratio, 20))
        self.draw_text('OXYGEN', WHITE, 45, 82)

    def draw_ammo(self, ammo):
        self.draw_text('AMMO: ', WHITE, 10, 35)
        for x in range(ammo):
            self.surface.blit(self.bullet_img, (90 + (x * 10), 40))

    def draw_grenades(self, grenades):
        self.draw_text('GRENADES: ', WHITE, 10, 60)
        for x in range(grenades):
            self.surface.blit(self.grenade_img, (135 + (x * 15), 60))
