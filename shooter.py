import random
import pygame
import sys
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
from boom import Boom
from background import Background
from game_stats import GameStats
from button import Button
from sounds import Sounds
from scoreboard import Scoreboard

class Shooter():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings = Settings()
        self.stats = GameStats(self)
        self.settings.screen_w, self.settings.screen_h = self.screen.get_rect().size
        self.sb = Scoreboard(self)
        self.sounds = Sounds()

        pygame.display.set_caption("Игра на питоне")

        self.button = Button(self, "Начать игру")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.booms = pygame.sprite.Group()

        self.backgrounds = pygame.sprite.Group()
        background = Background(self)
        background.rect.bottom = self.screen.get_rect().bottom
        self.backgrounds.add(background)


    def run_game(self):
        while True:
            self._check_events()
            self.stats.update()
            if self.stats.game_status:
                if len(self.backgrounds) < 2:
                    self._create_background()
                self._update_backgrounds()
                self._update_bullets()
                if len(self.aliens) < self.settings.number_aliens:
                    self._create_alien()
                self._update_aliens()
                self._update_booms()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                position = event.pos
                if ((0 + self.ship.rect.width / 2 <= position[0] <= self.settings.screen_w - self.ship.rect.width / 2)
                and (0 + self.ship.rect.width / 2 <= position[1] <= self.settings.screen_h - self.ship.rect.width / 2)):
                    self.ship.update(position)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(event.pos)
                self._create_bullet()

    def _check_play_button(self, position):
        if not self.stats.game_status:
            if self.button.rect.collidepoint(position):
                pygame.mixer.music.load('sounds/soundtrack.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.5)
                self.stats.reset_stats()
                self.stats.game_status = True
                pygame.mouse.set_visible(False)
                self.sb.prep_score()

                self.aliens.empty()
                self.bullets.empty()
            pygame.time.delay(100)

    def _create_background(self):
        background = Background(self)
        background.y = self.screen.get_rect().top - 1.5 * background.rect.height
        self.backgrounds.add(background)

    def _update_backgrounds(self):
        self.backgrounds.update()
        for bg in self.backgrounds.sprites():
            if bg.rect.top >= self.screen.get_rect().bottom:
                bg.y = self.screen.get_rect().top - 1.5 * bg.rect.height

    def _create_bullet(self):
        if self.stats.game_status:
            self.sounds.shoot_sound.play()
            num_bullet = self.settings.number_bullets
            new_bullet = Bullets(self, num_bullet)
            self.bullets.add(new_bullet)
            self.settings.number_bullets += 1

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._collision_bullet_alien()

    def _collision_bullet_alien(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions:
            for alien in collisions.values():
                self.stats.score += self.stats.alien_cost * len(alien)
                self.stats.alien_cost += self.stats.score_scale
                self.sb.prep_score()
        for hit in collisions.values():
            position = hit[0].rect.center
            self._get_boom(position)

    def _ship_hit(self):
        self.stats.ship_lifes -= 1
        if self.stats.ship_lifes < 1:
            self.stats.game_status = False
            pygame.mouse.set_visible(True)
            pygame.mixer.music.stop()

    def _update_booms(self):
        self.booms.update()


    def _get_boom(self, position):
        boom = Boom(self)
        self.booms.add(boom)
        boom.get_boom(position)
        self.sounds.boom_sound.play()

    def _create_alien(self):
        new_alien = Alien(self)
        self.alien_width = new_alien.rect.width
        self.alien_height = new_alien.rect.height
        new_alien.x = random.randint(0 + self.alien_width, self.settings.screen_w - self.alien_width)
        new_alien.rect.x = new_alien.x
        new_alien.y = random.randint(-self.settings.screen_h, 0)
        new_alien.rect.y = new_alien.y
        self.aliens.add(new_alien)

    def _update_aliens(self):
        self.aliens.update()
        collisions = pygame.sprite.spritecollideany(self.ship, self.aliens)
        if collisions:
            pos = collisions.rect.center
            self._get_boom(pos)
            self.aliens.remove(collisions)
            self._ship_hit()
        self._check_escape()

    def _check_escape(self):
        for alien in self.aliens.sprites():
            if alien.rect.top >= self.settings.screen_h:
                self.aliens.remove(alien)

    def time_counter(self):
        tick = pygame.time.get_ticks() / 1000
        if tick - self.stats.time >= 1:
            self.stats.seconds += 1
            self.stats.time = tick
            self.sb.prep_time()

        if self.stats.seconds >= 60:
            self.stats.seconds = 0
            self.stats.minutes += 1
            self.sb.prep_time()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.backgrounds.draw(self.screen)
        if self.stats.game_status:
            self.time_counter()
        self.sb.blit_score()
        self.ship.blitme()
        self.stats.blitme()
        self.aliens.draw(self.screen)
        self.booms.draw(self.screen)
        self.bullets.draw(self.screen)
        if not self.stats.game_status:
            self.button.draw_button()
        pygame.display.flip()

game = Shooter()
game.run_game()