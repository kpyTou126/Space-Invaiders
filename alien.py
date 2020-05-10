import pygame, random
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.paths = ["images/alien.png", "images/alien1.png", "images/alien3.png"]

        self.image = pygame.image.load(random.choice(self.paths)).convert_alpha()
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.alien_speed = random.uniform(self.settings.low, self.settings.high)
        self.alien_speed_x = random.randint(-1, 1) / 5

    def update(self):
        self.y += self.alien_speed
        self.rect.y = self.y
        self.x += self.alien_speed_x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)