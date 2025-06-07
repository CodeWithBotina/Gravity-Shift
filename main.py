import pygame
import sys
import logging
from src.game.api import GameAPI
from src.game.config.settings import FPS

def main():
    try:
        # Initialize game
        game = GameAPI()
        running = True

        # Game loop
        while running:
            try:
                game.clock.tick(FPS)
                running = game.update()
                pygame.display.update()
            except Exception as e:
                logging.error(f"Error during game loop: {e}")
                running = False

    except Exception as e:
        logging.error(f"Fatal error: {e}")
    finally:
        logging.info("Shutting down game...")
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()
