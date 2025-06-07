import pygame

class InputManager:
    def __init__(self):
        self.moving_left = False
        self.moving_right = False
        self.shoot = False
        self.grenade = False
        self.grenade_thrown = False
        self.jump = False

    def process_input(self, player=None, audio=None):
        """Process input events and update game state"""
        keys = pygame.key.get_pressed()
        
        # Movement
        self.moving_left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        self.moving_right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        
        # Jump (with Space or W or Up)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and player and not player.in_air:
            self.jump = True
            if audio:
                audio.play('jump')
        else:
            self.jump = False
        
        # Combat
        self.shoot = keys[pygame.K_f]  # Shoot with F
        self.grenade = keys[pygame.K_q]  # Throw grenade with Q
        if player and self.grenade and not self.grenade_thrown and audio:
            self.grenade_thrown = True
            audio.play('grenade')
        else:
            self.grenade_thrown = False

        # Process quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                    
        return True
