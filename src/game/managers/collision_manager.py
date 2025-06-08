import pygame
from ..config.settings import TILE_SIZE, SCREEN_WIDTH

class CollisionManager:
    @staticmethod
    def check_collision_with_tiles(entity, dx, dy, world):
        # Horizontal collision
        entity.rect.x += dx
        for tile in world.obstacle_list:
            if tile[1].colliderect(entity.rect):
                if dx > 0:  # Moving right
                    entity.rect.right = tile[1].left
                    dx = 0  # Stop horizontal movement
                elif dx < 0:  # Moving left
                    entity.rect.left = tile[1].right
                    dx = 0  # Stop horizontal movement

        # Vertical collision
        entity.rect.y += dy
        collision_below = False
        
        for tile in world.obstacle_list:
            if tile[1].colliderect(entity.rect):
                if dy > 0:  # Falling down
                    entity.rect.bottom = tile[1].top
                    collision_below = True
                    dy = 0  # Stop vertical movement
                elif dy < 0:  # Moving up
                    entity.rect.top = tile[1].bottom
                    dy = 0  # Stop vertical movement and allow falling
                    entity.velocity.y = 0  # Reset vertical velocity on head collision
        
        # Update in_air state based on collision below
        entity.in_air = not collision_below
        entity.on_ground = collision_below

        if collision_below:
            entity.velocity.y = 0  # Reset vertical velocity when landing

        return dx, dy

    @staticmethod
    def check_water_collision(entity, water_group):
        if pygame.sprite.spritecollide(entity, water_group, False):
            entity.health = 0

    @staticmethod
    def check_exit_collision(entity, exit_group):
        if pygame.sprite.spritecollide(entity, exit_group, False):
            return True
        return False

    @staticmethod
    def check_explosion_damage(explosion_pos, target_pos):
        return abs(explosion_pos[0] - target_pos[0]) < TILE_SIZE * 2 and \
               abs(explosion_pos[1] - target_pos[1]) < TILE_SIZE * 2
