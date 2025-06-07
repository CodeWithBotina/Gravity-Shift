import pygame
import sys

class EventManager:
    def __init__(self):
        self.reset_input_state()

    def reset_input_state(self):
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False
        self.grenade_thrown = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

        return True

    def _handle_keydown(self, event):
        if event.key == pygame.K_a:
            self.moving_left = True
        if event.key == pygame.K_d:
            self.moving_right = True
        if event.key == pygame.K_SPACE:
            self.shoot = True
        if event.key == pygame.K_q:
            self.grenade = True
        if event.key == pygame.K_w:
            self.jump = True

    def _handle_keyup(self, event):
        if event.key == pygame.K_a:
            self.moving_left = False
        if event.key == pygame.K_d:
            self.moving_right = False
        if event.key == pygame.K_SPACE:
            self.shoot = False
        if event.key == pygame.K_q:
            self.grenade = False
            self.grenade_thrown = False
