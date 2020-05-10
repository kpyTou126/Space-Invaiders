import pygame
from pygame.sprite import Sprite

class Boom(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/boom.png").convert_alpha()
        self.rect = self.image.get_rect()

        self.time = 30

    def get_boom(self, position):
        self.rect.center = position

    def update(self):
        if self.time:
            self.time -= 1
            if self.time <= 0:
                self.kill()

