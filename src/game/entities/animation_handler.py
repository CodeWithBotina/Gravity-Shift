import pygame
import os

class AnimationHandler:
    def __init__(self):
        self.animation_list = []
        self.frame_index = 0
        self.action = 0  # 0: idle, 1: run, 2: jump, 3: death
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = 100

    def load_animations(self, char_type, scale):
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        for animation in animation_types:
            temp_list = []
            animation_path = f'assets/sprites/characters/{char_type}/{animation}'
            if not os.path.exists(animation_path):
                print(f"Warning: Animation path not found: {animation_path}")
                continue
                
            num_of_frames = len(os.listdir(animation_path))
            for i in range(num_of_frames):
                img_path = f'{animation_path}/{i}.png'
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

    def get_current_frame(self):
        """Get the current animation frame"""
        if not self.animation_list or self.action >= len(self.animation_list):
            # Return a default surface if no animations are loaded
            surface = pygame.Surface((32, 32))
            surface.fill((255, 0, 255))  # Fill with magenta for visibility
            return surface
            
        current_animation = self.animation_list[self.action]
        if not current_animation or self.frame_index >= len(current_animation):
            self.frame_index = 0
            
        return self.animation_list[self.action][self.frame_index]

    def set_action(self, new_action):
        """Set the current animation action"""
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def update_animation(self, sprite):
        # Update animation timing
        if pygame.time.get_ticks() - self.update_time > self.animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            
        # Check if animation has finished
        if self.frame_index >= len(self.animation_list[self.action]):
            # Keep last frame for death animation
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

        # Update sprite image
        sprite.image = self.get_current_frame()
