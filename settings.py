class Settings():
    def __init__(self):
        self.screen_w = 1600
        self.screen_h = 800
        self.bg_color = (255, 255, 255)

        self.ship_lifes = 5
        self.bg_speed = 0.7

        self.bullet_speed = 2.5
        self.number_bullets = 0

        self.low = 1
        self.high = 3.5

        self.ship_speed = 1.5
        self.number_aliens = 20

        self.alien_cost = 100
        self.score_scale = 10