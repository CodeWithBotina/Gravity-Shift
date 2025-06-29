import pygame
from src.game.config.settings import TILE_SIZE, img_list
from src.game.managers.collision_manager import CollisionManager
from src.game.managers.physics_manager import PhysicsManager
from src.game.entities.sprites import Water, Decoration  # Add sprites import
from src.game.ui.components.health_bar import HealthBar  # Add HealthBar import

class World:
    def __init__(self):
        self.obstacle_list = []
        self.level_length = 0
        self.scroll_x = 0
        self.tile_images = img_list  # Store reference to loaded images
        self.collision_manager = CollisionManager()  # Initialize collision manager
        self.physics_manager = PhysicsManager()  # Initialize physics manager

    def process_data(self, data, sprite_groups):
        self.level_length = len(data[0])
        self.obstacle_list = []
        player = None
        health_bar = None

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0 and tile < len(self.tile_images):
                    img = self.tile_images[tile]
                    if img:
                        img_rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                        tile_data = (img, img_rect)

                        if tile <= 8:  # Solid tiles
                            self.obstacle_list.append(tile_data)
                        elif tile == 15:  # Player spawn
                            from ..entities.player import Player
                            spawn_x = x * TILE_SIZE
                            spawn_y = y * TILE_SIZE
                            # Create player at the correct position
                            player = Player(spawn_x, spawn_y, 1.65, 5, 20, 5)
                            # Set the bottom of the player to the bottom of the tile
                            player.rect.x = spawn_x
                            player.rect.bottom = spawn_y + TILE_SIZE
                            # Update the position vector to match the rect
                            player.position = pygame.math.Vector2(player.rect.centerx, player.rect.centery)
                            player.world = self
                            health_bar = HealthBar(10, 10, player.health, player.health)

        return player, health_bar

    def check_collision(self, entity, dx, dy):
        return self.collision_manager.check_collision_with_tiles(entity, dx, dy, self)

    def draw(self, surface, scroll):
        for tile in self.obstacle_list:
            if not tile[0] or not tile[1]:  # Verificar que el tile existe
                continue
            tile_rect = tile[1].copy()  # Create a copy of the rect for drawing
            tile_rect.x -= scroll.x  # Aplicar scroll negativo para mover el mundo en la dirección opuesta
            tile_rect.y -= scroll.y
            # Solo dibujar los tiles que están en pantalla
            if tile_rect.right > 0 and tile_rect.left < surface.get_width():
                surface.blit(tile[0], tile_rect)  # Draw using the adjusted rect
