import sys

import pygame

from food import Food


def check_keydown_events(event, snake):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        snake.direction = "right"
    elif event.key == pygame.K_LEFT:
        snake.direction = "left"
    elif event.key == pygame.K_UP:
        snake.direction = "up"
    elif event.key == pygame.K_DOWN:
        snake.direction = "down"


def check_events(food, screen, settings, snake):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def check_food_amount(food, screen, settings):
    """Check if there is any food on the screen."""
    if len(food.sprites()) == 0:
        for x in range(5):
            new_food = Food(screen, settings)
            food.add(new_food)


def update_screen(food, screen, settings, snake):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)

    # Redraw the snake at it's new position.
    snake.draw_snake(settings)

    # Redraw all the food.
    for food in food.sprites():
        food.draw_food()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
