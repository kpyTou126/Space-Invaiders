import pygame

class Ship():
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings

        self.image_path = "images/ship.png"
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y -= 50

    def update(self, position):
        if self.game.stats.game_status:
            self.rect.center = position

    def blitme(self):
        self.screen.blit(self.image, self.rect)