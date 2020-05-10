import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.settings = game.settings

        self.image = pygame.image.load("images/space_double-1920.jpg").convert()
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bg_speed
        self.rect.y = self.y
