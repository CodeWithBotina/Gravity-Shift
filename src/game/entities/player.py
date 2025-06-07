import pygame
import os
import math
from .animation_handler import AnimationHandler
from ..config.settings import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_SPEED, ROTATION_SPEED, THRUST_POWER

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed
        self.ammo = ammo
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.direction = 1
        self.flip = False
        self.in_air = False
        self.jump = False
        self.vel_y = 0  # Initialize vertical velocity
        
        # Animation setup
        self.animation_handler = AnimationHandler()
        self.animation_handler.load_animations('alex_rook', scale)
        self.image = self.animation_handler.get_current_frame()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # Store dimensions
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Space movement properties
        self.rotation = 0
        self.thrust = False
        self.velocity = pygame.math.Vector2(0, 0)
        self.max_speed = MAX_SPEED

    def update(self):
        dx = 0
        dy = self.vel_y

        # Get input from input manager
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if keys[pygame.K_d]:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # Apply gravity
        self.vel_y += GRAVITY
        dy = self.vel_y

        # Check collisions
        if self.world:
            dx, dy = self.world.collision_manager.check_collision_with_tiles(self, dx, dy, self.world)

        # Update position
        self.rect.x += dx
        self.rect.y += dy

        # Ensure the player stays within the map boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Update animation
        if self.in_air:
            self.animation_handler.set_action(2)  # Jump
        elif dx != 0:
            self.animation_handler.set_action(1)  # Run
        else:
            self.animation_handler.set_action(0)  # Idle

        self.animation_handler.update_animation(self)

    def draw(self, surface):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)

    def reset(self):
        self.health = self.max_health
        self.velocity = pygame.math.Vector2(0, 0)
        self.in_air = False
