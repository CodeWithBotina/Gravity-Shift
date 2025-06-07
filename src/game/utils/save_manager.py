import json
import os

class SaveManager:
    def __init__(self):
        self.save_dir = 'assets/data/saves'
        self.ensure_save_directory()

    def ensure_save_directory(self):
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    def save_game(self, data, slot=0):
        save_path = f'{self.save_dir}/save_{slot}.json'
        try:
            with open(save_path, 'w') as f:
                json.dump(data, f)
            return True
        except Exception as e:
            print(f"Error saving game: {e}")
            return False

    def load_game(self, slot=0):
        save_path = f'{self.save_dir}/save_{slot}.json'
        try:
            if os.path.exists(save_path):
                with open(save_path, 'r') as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"Error loading game: {e}")
            return None

    def get_save_data(self, player, level, score, oxygen_level):
        return {
            'player': {
                'health': player.health,
                'ammo': player.ammo,
                'grenades': player.grenades,
                'score': score
            },
            'game_state': {
                'level': level,
                'oxygen_level': oxygen_level
            }
        }
