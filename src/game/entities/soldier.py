import pygame
import os
import random
import logging
from ..config.settings import GRAVITY, SCREEN_WIDTH, SCREEN_HEIGHT, SCROLL_THRESH, TILE_SIZE
from .animation_handler import AnimationHandler

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo, grenades):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.direction = 1
        self.vel_y = 0
        self.jump = False
        self.in_air = True
        self.flip = False
        self.moving_left = False
        self.moving_right = False
        
        # Animation variables
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
        
        # Load animations
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            # Count frames in folder
            num_of_frames = len(os.listdir(f'assets/sprites/characters/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'assets/sprites/characters/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        
        # Load first image and set dimensions
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # Initialize world reference
        self.world = None

        # AI specific variables
        self.move_counter = 0
        self.vision = pygame.Rect(0, 0, 150, 20)
        self.idling = False
        self.idling_counter = 0

        # Store initial position for reset
        self.initial_x = x
        self.initial_y = y
        self.position = pygame.math.Vector2(x, y)

        # Gravity variables
        self.default_gravity = 0.8  # Add default gravity constant
        self.current_gravity = self.default_gravity

    def move(self, moving_left, moving_right, world):
        screen_scroll = 0
        dx = 0
        dy = 0
        self.moving_left = moving_left
        self.moving_right = moving_right

        # Basic movement
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # Jumping
        if self.jump and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # Apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # Check collisions with world
        if world and hasattr(world, 'obstacle_list'):
            for tile in world.obstacle_list:
                # Check x direction collision
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                # Check y direction collision
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    if self.vel_y < 0:
                        self.vel_y = 0
                        dy = tile[1].bottom - self.rect.top
                    elif self.vel_y >= 0:
                        self.vel_y = 0
                        self.in_air = False
                        dy = tile[1].top - self.rect.bottom

        # Update position
        self.rect.x += dx
        self.rect.y += dy

        # Check for falling off the map
        if self.rect.bottom > SCREEN_HEIGHT:
            self.health = 0
            dy = 0

        # Update camera scroll for player
        if self.char_type == 'player':
            if ((self.rect.right > SCREEN_WIDTH - SCROLL_THRESH and dx > 0) or 
                (self.rect.left < SCROLL_THRESH and dx < 0)):
                self.rect.x -= dx
                screen_scroll = -dx

        return screen_scroll

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)  # 3: Death animation

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        
        # Update image
        self.image = self.animation_list[self.action][self.frame_index]
        
        # Check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            
        # Reset animation index
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:  # Death animation
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # Check if new action is different
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update(self, screen_scroll=0):
        # Update animation based on state
        if not self.alive:
            self.update_action(3)  # Death
        elif self.in_air:
            self.update_action(2)  # Jump
        elif self.moving_left or self.moving_right:
            self.update_action(1)  # Run
        else:
            self.update_action(0)  # Idle
            
        # Update animation frame
        self.update_animation()
        self.check_alive()
        
        # Update position with screen scroll
        self.rect.x += screen_scroll

    def ai(self, player, world):
        if self.alive and player.alive:
            if not self.idling and random.randint(1, 200) == 1:
                self.update_action(0)  # Idle
                self.idling = True
                self.idling_counter = 50

            if self.vision.colliderect(player.rect):
                # Stop and face player
                self.update_action(0)  # Idle
                self.shoot()
            else:
                if not self.idling:
                    if self.direction == 1:
                        ai_moving_right = True
                    else:
                        ai_moving_right = False
                    ai_moving_left = not ai_moving_right
                    
                    self.move(ai_moving_left, ai_moving_right, world)
                    self.update_action(1)  # Run
                    self.move_counter += 1

                    # Update AI vision
                    if self.direction == 1:
                        self.vision.center = (self.rect.centerx + 75, self.rect.centery)
                    else:
                        self.vision.center = (self.rect.centerx - 75, self.rect.centery)

                    if self.move_counter > TILE_SIZE:
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling_counter -= 1
                    if self.idling_counter <= 0:
                        self.idling = False

    def draw(self, surface):
        """Draw the soldier on the given surface"""
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipped_image, self.rect)

    def reset(self):
        """Reset the soldier to initial position and state"""
        self.position = pygame.math.Vector2(self.initial_x, self.initial_y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.is_jumping = False
        self.is_falling = False
        self.current_gravity = self.default_gravity
        self.health = self.max_health
