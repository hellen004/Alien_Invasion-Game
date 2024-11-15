import sys

import pygame

from settings import Settings
from player import Player
from alien import Alien

def run_game():
    # initializing pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    

    player = Player(screen)
    alien = Alien()
    
    # Start the main loop for the game
    while True:

        #watch for keyboard amd mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #redrwaing the screen eaach time after the loop
        screen.fill(ai_settings.bg_color)        
        player.draw(screen) 
        #making the most recently drawn screen visible.
        pygame.display.flip()

run_game()
