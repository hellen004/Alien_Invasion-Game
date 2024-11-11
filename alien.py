import pygame

import random

from settings import Settings

class Alien:
    def __init__(self):
        ai_settings = Settings()
        self.image = pygame.image.load("images/Alien.png")
        self.rect = self.image.get_rect(midtop=(random.randint(0, ai_settings.screen_width - 40), 0))
        self.speed = 3

        def move(self):
            self.rect.y += self.speed

        def draw(self, surface):
            surface.blit(self.image, self.rect)