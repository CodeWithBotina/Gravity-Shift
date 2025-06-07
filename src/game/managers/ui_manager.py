import pygame
import logging

class UIManager:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.buttons = {}
        self.initialize_menu_buttons()

    def initialize_menu_buttons(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        
        # Create start button
        start_btn = {
            'text': 'Start Game',
            'rect': pygame.Rect(screen_width//2 - 100, screen_height//2 - 25, 200, 50),
            'color': (100, 200, 100),
            'hover_color': (120, 220, 120)
        }
        self.buttons['start'] = start_btn

    def handle_button_click(self, pos):
        """Return the button identifier if a button was clicked"""
        mouse_pos = pygame.mouse.get_pos()
        for btn_name, btn in self.buttons.items():
            if btn['rect'].collidepoint(pos):
                logging.info(f"Button clicked: {btn_name}")
                return btn_name
        return None

    def draw_menu(self):
        """Draw menu and return any button that was clicked"""
        for btn_name, btn in self.buttons.items():
            mouse_pos = pygame.mouse.get_pos()
            color = btn['hover_color'] if btn['rect'].collidepoint(mouse_pos) else btn['color']
            
            pygame.draw.rect(self.screen, color, btn['rect'])
            text = self.font.render(btn['text'], True, (0, 0, 0))
            text_rect = text.get_rect(center=btn['rect'].center)
            self.screen.blit(text, text_rect)
