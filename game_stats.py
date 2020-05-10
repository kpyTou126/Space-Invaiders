import pygame

class GameStats():
    """Вся статистика игры"""
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.game_status = False
        self.ship_lifes = self.settings.ship_lifes

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.score_scale = self.settings.score_scale
        self.reset_stats()
        self.update()

    def reset_stats(self):
        self.time = 0
        self.minutes, self.seconds = 0, 0
        self.alien_cost = self.settings.alien_cost
        self.score = 0
        self.ship_lifes = self.settings.ship_lifes

    def update(self):
        self.text = f"Осталось: {self.ship_lifes} "
        if self.ship_lifes in [2,3,4]:
            self.text += "жизни"
        elif self.ship_lifes == 1:
            self.text += "жизнь"
        elif self.ship_lifes in [0, 5]:
            self.text += "жизней"

        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect = 20, 20

    def blitme(self):
        """Отображает количество оставшихся жизней у корабля"""
        self.screen.blit(self.image, self.rect)