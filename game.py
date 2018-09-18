import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from snake import Snake


def run_game():
    """Initialize the game, settings and create a screen object."""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                     settings.screen_height))
    pygame.display.set_caption("Snake")

    # Make a snake.
    snake = Snake(screen, settings)
    # Make a group to store food in.
    food = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(food, screen, settings, snake)
        gf.check_snake_food_collisions(food, screen, settings, snake)
        snake.update()
        gf.update_screen(food, screen, settings, snake)


run_game()
