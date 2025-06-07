import pygame

class SpriteManager:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.grenade_group = pygame.sprite.Group()
        self.explosion_group = pygame.sprite.Group()
        self.item_box_group = pygame.sprite.Group()
        self.decoration_group = pygame.sprite.Group()
        self.water_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

    def update_all(self, screen_scroll=0):
        self.bullet_group.update()
        self.grenade_group.update()
        self.explosion_group.update()
        self.item_box_group.update()
        self.decoration_group.update()
        self.water_group.update()
        self.exit_group.update()

    def draw_all(self, surface):
        self.bullet_group.draw(surface)
        self.grenade_group.draw(surface)
        self.explosion_group.draw(surface)
        self.item_box_group.draw(surface)
        self.decoration_group.draw(surface)
        self.water_group.draw(surface)
        self.exit_group.draw(surface)

    def reset_all(self):
        self.enemy_group.empty()
        self.bullet_group.empty()
        self.grenade_group.empty()
        self.explosion_group.empty()
        self.item_box_group.empty()
        self.decoration_group.empty()
        self.water_group.empty()
        self.exit_group.empty()

    def get_groups(self):
        return {
            'enemy': self.enemy_group,
            'bullet': self.bullet_group,
            'grenade': self.grenade_group,
            'explosion': self.explosion_group,
            'item_box': self.item_box_group,
            'decoration': self.decoration_group,
            'water': self.water_group,
            'exit': self.exit_group
        }
