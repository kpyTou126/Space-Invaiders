import pygame
from pygame.font import SysFont

class Scoreboard():
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.stats = game.stats
        self.screen_rect = self.screen.get_rect()

        self.font = SysFont(None, 70)
        self.text_color = (255, 255, 255)
        self.score = self.stats.score
        self.best = 0

        self.prep_score()
        self.prep_time()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.image_score = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.image_score.get_rect()
        self.score_rect.top = self.screen_rect.top + 20
        self.score_rect.right = self.screen_rect.right - 20

    def prep_time(self):
        format_time = "%02d:%02d" % (self.stats.minutes, self.stats.seconds)
        self.image_time = SysFont(None, 30).render(format_time, True, (150, 150, 150))
        self.time_rect = self.image_time.get_rect()
        self.time_rect.topright = self.score_rect.bottomright
        self.time_rect.top += 10

    def blit_score(self):
        self.screen.blit(self.image_score, self.score_rect)
        self.screen.blit(self.image_time, self.time_rect)