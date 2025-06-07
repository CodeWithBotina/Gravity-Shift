import csv
import os
from ..config.settings import ROWS, COLS, TILE_SIZE

class LevelManager:
    def __init__(self):
        self.current_level = 1
        self.max_levels = 3
        
    def load_level(self, level_number):
        level_path = f'assets/data/levels/level{level_number}_data.csv'
        if not os.path.exists(level_path):
            print(f"Error: Level file not found: {level_path}")
            return None
            
        world_data = []
        for row in range(ROWS):
            r = [-1] * COLS
            world_data.append(r)
            
        try:
            with open(level_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for y, row in enumerate(reader):
                    for x, tile in enumerate(row):
                        if x < COLS and y < ROWS:
                            world_data[y][x] = int(tile)
            return world_data
        except Exception as e:
            print(f"Error loading level: {e}")
            return None

    def reset_level(self):
        data = []
        for row in range(ROWS):
            r = [-1] * COLS
            data.append(r)
        return data

    def next_level(self):
        if self.current_level < self.max_levels:
            self.current_level += 1
            return self.load_level(self.current_level)
        return None
