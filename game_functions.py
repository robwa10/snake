import sys

import pygame


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


def check_events(snake):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def update_screen(screen, settings, snake):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    snake.draw_snake(settings)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
