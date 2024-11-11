import pygame

import settings

from settings import Settings

class Player():
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        ai_settings = Settings()
        self.image = pygame.image.load("images/Player.png")
        self.rect = self.image.get_rect(midbottom=(ai_settings.screen_width // 2, ai_settings.screen_height - 10))
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < settings.screen_width:
            self.rect.x += self.speed

    def draw(self, surface):
        """Drawing the ship at its centry location."""
        surface.blit(self.image, self.rect)