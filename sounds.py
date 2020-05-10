import pygame

class Sounds():
    def __init__(self):
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.shoot_sound.set_volume(0.2)

        self.boom_sound = pygame.mixer.Sound("sounds/boom.wav")
        self.boom_sound.set_volume(0.05)