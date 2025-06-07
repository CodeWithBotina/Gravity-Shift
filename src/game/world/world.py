import pygame
import logging
from ..config.settings import TILE_SIZE, img_list, SCREEN_WIDTH
from ..entities.soldier import Soldier
from ..entities.player import Player  # Add this import
from ..entities.sprites import Water, Decoration
from ..ui.hud.components import HealthBar  # Updated import path
from ..managers.physics_manager import PhysicsManager  # Add this import
from ..managers.collision_manager import CollisionManager  # Add this import

class World:
    def __init__(self):
        self.obstacle_list = []
        self.level_length = 0
        self.physics_manager = PhysicsManager()
        self.collision_manager = CollisionManager()  # Initialize collision manager

    def process_data(self, data, sprite_groups):
        self.level_length = len(data[0])
        self.obstacle_list = []
        player = None
        health_bar = None

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)

                    if tile >= 0 and tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 9 and tile <= 10:
                        sprite_groups['water'].add(Water(img, x * TILE_SIZE, y * TILE_SIZE))
                    elif tile >= 11 and tile <= 14:
                        sprite_groups['decoration'].add(Decoration(img, x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 15:  # Player spawn
                        player = Player(x * TILE_SIZE, y * TILE_SIZE, 1.65, 5, 20, 5)
                        player.world = self  # Give player reference to world
                        health_bar = HealthBar(10, 10, player.health, player.max_health)
                    elif tile == 16:
                        enemy = Soldier('enemies/reaper_drone', x * TILE_SIZE, y * TILE_SIZE, 1.65, 2, 20, 0)
                        sprite_groups['enemy'].add(enemy)

        return player, health_bar

    def draw(self, surface, scroll):
        if not surface:
            logging.error("Invalid surface in World.draw")
            return
            
        # Add boundary check for level edges
        if scroll > 0:  # Moving left
            if self.obstacle_list and self.obstacle_list[0][1].x >= 0:
                scroll = 0
        elif scroll < 0:  # Moving right
            if self.obstacle_list:
                rightmost = max(tile[1].right for tile in self.obstacle_list)
                if rightmost <= SCREEN_WIDTH:
                    scroll = 0
                    
        for tile in self.obstacle_list:
            tile[1].x += scroll
            surface.blit(tile[0], tile[1])
