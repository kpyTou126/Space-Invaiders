import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self, game, num_bullet):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.num_bullet = num_bullet

        if self.num_bullet % 2 == 0:
            self.image = pygame.image.load("images/bullet.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topright = game.ship.rect.midright
            self.rect.x -= 19
            self.rect.y -= 10
        else:
            self.image = pygame.image.load("images/bullet.png")
            self.rect = self.image.get_rect()
            self.rect.topleft = game.ship.rect.midleft
            self.rect.x += 19
            self.rect.y -= 10

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


