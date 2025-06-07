from ..config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, PINK
from ..entities.effects import ScreenFade

class GameState:
    def __init__(self):
        # Game flow control
        self.start_game = False
        self.start_intro = False
        self.game_paused = False
        self.game_over = False
        
        # Level management
        self.level = 1
        self.score = 0
        
        # Camera and scrolling
        self.bg_scroll = 0
        self.screen_scroll = 0
        
        # Screen effects
        self.intro_fade = ScreenFade(1, BLACK, 4)
        self.death_fade = ScreenFade(2, PINK, 4)
        
    def reset_level_state(self):
        self.bg_scroll = 0
        self.screen_scroll = 0
        return True

    def handle_level_complete(self, level_manager, world, sprite_groups):
        self.start_intro = True
        self.level += 1
        self.bg_scroll = 0
        sprite_groups.reset_all()
        return level_manager.load_level(self.level)
