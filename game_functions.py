import sys

import pygame


def check_keydown_events(event):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def update_screen(screen, settings, snake):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)
    snake.draw_snake(settings)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
