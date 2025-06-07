import pygame
import os

class AnimationManager:
    def __init__(self):
        self.animation_cooldown = 100

    def load_animation_frames(self, char_type, scale):
        animation_list = []
        animation_types = ['Idle', 'Run', 'Jump', 'Death']
        
        for animation in animation_types:
            temp_list = []
            frame_count = len(os.listdir(f'assets/sprites/characters/{char_type}/{animation}'))
            
            for i in range(frame_count):
                img = pygame.image.load(f'assets/sprites/characters/{char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)
            animation_list.append(temp_list)
            
        return animation_list

    def update_animation(self, entity):
        if pygame.time.get_ticks() - entity.update_time > self.animation_cooldown:
            entity.update_time = pygame.time.get_ticks()
            entity.frame_index += 1
            
        if entity.frame_index >= len(entity.animation_list[entity.action]):
            if entity.action == 3:  # Death animation
                entity.frame_index = len(entity.animation_list[entity.action]) - 1
            else:
                entity.frame_index = 0

        entity.image = entity.animation_list[entity.action][entity.frame_index]
