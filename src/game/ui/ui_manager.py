import pygame
from .menus.button import Button
from ..config.settings import *

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Futura', 30)
        self.load_images()
        self.setup_buttons()

    def load_images(self):
        self.start_img = pygame.image.load('assets/sprites/ui/menus/start_btn.png').convert_alpha()
        self.exit_img = pygame.image.load('assets/sprites/ui/menus/exit_btn.png').convert_alpha()
        self.restart_img = pygame.image.load('assets/sprites/ui/menus/restart_btn.png').convert_alpha()
        self.bullet_img = pygame.image.load('assets/sprites/ui/icons/bullet.png').convert_alpha()
        self.grenade_img = pygame.image.load('assets/sprites/ui/icons/grenade.png').convert_alpha()

    def setup_buttons(self):
        # Main menu buttons
        button_y = MENU_CENTER_Y - 100
        self.start_button = Button(MENU_CENTER_X, button_y, "Start Game")
        button_y += BUTTON_HEIGHT + BUTTON_MARGIN
        self.settings_button = Button(MENU_CENTER_X, button_y, "Settings")
        button_y += BUTTON_HEIGHT + BUTTON_MARGIN
        self.exit_button = Button(MENU_CENTER_X, button_y, "Exit")

        # Death menu buttons
        button_y = MENU_CENTER_Y - 50
        self.restart_button = Button(MENU_CENTER_X, button_y, "Try Again")
        button_y += BUTTON_HEIGHT + BUTTON_MARGIN
        self.death_exit_button = Button(MENU_CENTER_X, button_y, "Quit to Menu")

    def draw_text(self, text, color, x, y):
        img = self.font.render(text, True, color)
        self.screen.blit(img, (x, y))

    def draw_hud(self, player, oxygen_level):
        # Draw ammo
        self.draw_text('AMMO: ', WHITE, 10, 35)
        for x in range(player.ammo):
            self.screen.blit(self.bullet_img, (90 + (x * 10), 40))
        
        # Draw grenades
        self.draw_text('GRENADES: ', WHITE, 10, 60)
        for x in range(player.grenades):
            self.screen.blit(self.grenade_img, (135 + (x * 15), 60))
        
        # Draw oxygen bar
        ratio = oxygen_level / OXYGEN_MAX
        pygame.draw.rect(self.screen, BLACK, (10, 80, 154, 24))
        pygame.draw.rect(self.screen, RED, (12, 82, 150, 20))
        pygame.draw.rect(self.screen, (0, 191, 255), (12, 82, 150 * ratio, 20))
        self.draw_text('OXYGEN', WHITE, 45, 82)

    def handle_menu_input(self):
        action = None
        # Check button clicks
        if self.start_button.draw(self.screen):
            action = 'start'
        if self.exit_button.draw(self.screen):
            action = 'exit'
        if hasattr(self, 'restart_button') and self.restart_button.draw(self.screen):
            action = 'restart'
        return action

    def draw_menu(self):
        # Clear and draw background
        self.screen.fill(MENU_BG)
        
        # Draw title
        title = pygame.font.SysFont('Futura', 48).render("GRAVITY SHIFT", True, BUTTON_TEXT)
        title_rect = title.get_rect(center=(MENU_CENTER_X, MENU_CENTER_Y - 200))
        self.screen.blit(title, title_rect)
        
        # Draw buttons
        self.start_button.draw(self.screen)
        self.settings_button.draw(self.screen)
        self.exit_button.draw(self.screen)

    def draw_death_menu(self):
        self.screen.fill(MENU_BG)
        
        # Draw game over text
        gameover = pygame.font.SysFont('Futura', 48).render("GAME OVER", True, RED)
        gameover_rect = gameover.get_rect(center=(MENU_CENTER_X, MENU_CENTER_Y - 150))
        self.screen.blit(gameover, gameover_rect)
        
        # Draw buttons
        self.restart_button.draw(self.screen)
        self.death_exit_button.draw(self.screen)
