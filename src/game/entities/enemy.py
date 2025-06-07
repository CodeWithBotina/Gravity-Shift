import pygame
import random
from .soldier import Soldier
from ..config.settings import TILE_SIZE

class Enemy(Soldier):
    def __init__(self, x, y, scale, speed, ammo):
        super().__init__('enemies/reaper_drone', x, y, scale, speed, ammo, 0)
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0

    def ai(self, player, world, bullet_group):
        if self.alive and player.alive:
            # Update animations based on state
            if self.idling:
                self.update_action(0)  # Idle animation
            elif self.vision.colliderect(player.rect):
                self.update_action(0)  # Idle animation for shooting
                self.shoot(bullet_group)
            else:
                self.update_action(1)  # Run animation
            
            if not self.idling and random.randint(1, 200) == 1:
                self.idling = True
                self.idling_counter = 50
            
            if not self.idling:
                if self.facing_right:
                    self.move(False, True, world)
                else:
                    self.move(True, False, world)
                    
            # Update AI vision as the enemy moves
            self.vision.center = (self.rect.centerx + 75 * self.direction, self.rect.centery)

            if self.move_counter > TILE_SIZE:
                self.direction *= -1
                self.move_counter *= -1
        else:
            self.idling_counter -= 1
            if self.idling_counter <= 0:
                self.idling = False

    def _handle_movement(self, world):
        if not self.idling:
            if self.direction == 1:
                ai_moving_right = True
            else:
                ai_moving_right = False
            ai_moving_left = not ai_moving_right
            
            self.move(ai_moving_left, ai_moving_right, world)
