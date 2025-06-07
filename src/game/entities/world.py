import pygame
from ..config.settings import TILE_SIZE
from .sprites import Water, Decoration, Exit, ItemBox
from .soldier import Soldier
from ..ui.components.health_bar import HealthBar

class World:
    def __init__(self):
        self.obstacle_list = []
        self.level_length = 0

    def process_data(self, data, img_list, sprite_groups):
        self.level_length = len(data[0])
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
                    
                    if tile <= 8:
                        self.obstacle_list.append(tile_data)
                    elif tile <= 10:
                        sprite_groups['water'].add(Water(img, x * TILE_SIZE, y * TILE_SIZE))
                    elif tile <= 14:
                        sprite_groups['decoration'].add(Decoration(img, x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 15:
                        player = Soldier('alex_rook', x * TILE_SIZE, y * TILE_SIZE, 1.65, 5, 20, 5)
                        health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 16:
                        enemy = Soldier('enemies/reaper_drone', x * TILE_SIZE, y * TILE_SIZE, 1.65, 2, 20, 0)
                        sprite_groups['enemy'].add(enemy)
                    elif tile == 17:
                        sprite_groups['item_box'].add(ItemBox('Ammo', x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 18:
                        sprite_groups['item_box'].add(ItemBox('Grenade', x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 19:
                        sprite_groups['item_box'].add(ItemBox('Health', x * TILE_SIZE, y * TILE_SIZE))
                    elif tile == 20:
                        sprite_groups['exit'].add(Exit(img, x * TILE_SIZE, y * TILE_SIZE))

        return player, health_bar

    def draw(self, surface, screen_scroll):
        for tile in self.obstacle_list:
            tile[1].x += screen_scroll
            surface.blit(tile[0], tile[1])
