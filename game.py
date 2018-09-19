import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings


def run_game():
    """Initialize the game, settings and create a screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                     settings.screen_height))
    pygame.display.set_caption("Snake")

    # Make a group of food and snake rects.
    food = Group()
    snake_body = Group()

    # Create the snake body.
    gf.create_snake_body(settings, screen, snake_body)

    # Start the main loop for the game.
    while True:
        gf.check_events(food, screen, settings)
        gf.update_screen(food, screen, settings, snake_body)


run_game()
