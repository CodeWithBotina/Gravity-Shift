import pygame
import os
import math
from .animation_handler import AnimationHandler
from ..config.settings import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT, MAX_SPEED, ROTATION_SPEED, THRUST_POWER, TILE_SIZE

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
        self.velocity = pygame.math.Vector2(0, 0)  # Add velocity for physics
        self.direction = 1
        self.flip = False
        self.in_air = False
        self.jump = False
        self.vel_y = 0  # Initialize vertical velocity
        self.world = None  # Initialize the world attribute
        
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
        self.max_speed = MAX_SPEED

        # Physics properties
        self.gravity = 0.5  # Gravity constant
        self.jump_force = -10  # Jump force
        self.on_ground = False  # Track if the player is on the ground

    def update(self):
        dx = 0
        dy = self.velocity.y  # Use velocity for vertical movement

        # Get input from input manager
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Move left
            dx = -self.speed
            self.flip = True
            self.direction = -1
        elif keys[pygame.K_d]:  # Move right
            dx = self.speed
            self.flip = False
            self.direction = 1

        if keys[pygame.K_SPACE] and self.on_ground:  # Jump logic
            self.velocity.y = self.jump_force
            self.on_ground = False

        # Apply gravity
        if not self.on_ground:
            self.velocity.y += self.gravity

        dy = self.velocity.y

        # Check collisions
        if self.world:
            dx, dy = self.world.check_collision(self, dx, dy)  # Use the world's collision check method

        # Update position
        self.rect.x += dx
        self.rect.y += dy

        # Prevent being pushed off the map
        if self.rect.left < 0:
            self.rect.left = 0
        if self.world and self.rect.right > self.world.level_length * TILE_SIZE:
            self.rect.right = self.world.level_length * TILE_SIZE

        # Check if player is on the ground
        if self.world:
            # Check if player is on a platform
            on_platform = False
            for tile in self.world.obstacle_list:
                if self.rect.bottom == tile[1].top and self.rect.right > tile[1].left and self.rect.left < tile[1].right:
                    on_platform = True
                    break

            if on_platform:
                self.velocity.y = 0
                self.on_ground = True
            else:
                self.on_ground = False
        else:
            self.on_ground = False

        # Update animation
        if not self.on_ground:
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

    def jump(self):
        if self.on_ground:
            self.velocity.y = self.jump_force
            self.on_ground = False
