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

    # An array to hold snake pieces for removing later.
    snake_list = []

    # Create the snake body.
    gf.create_snake_body(screen, settings, snake_body, snake_list)

    # Start the main loop for the game.
    while True:
        gf.check_events(food, screen, settings)
        gf.move_snake(food, screen, settings, snake_body, snake_list)
        gf.check_collisions(food, screen, settings, snake_list)
        gf.check_snake_food(food, screen, settings)
        gf.update_screen(food, screen, settings, snake_body)

        pygame.time.wait(settings.speed)


run_game()
