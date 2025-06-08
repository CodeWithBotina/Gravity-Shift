import pygame
from pygame import mixer
from src.game.api import GameAPI
from src.game.config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    pygame.init()
    mixer.init()

    # Initialize the game API
    game_api = GameAPI()

    # Main game loop
    run = True
    while run:
        game_api.clock.tick(FPS)
        run = game_api.update()

    pygame.quit()

if __name__ == "__main__":
    main()
