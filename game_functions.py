import sys

import pygame

from food import Food
from snake import Snake


def check_keydown_events(event):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()


def check_events(food, screen, settings):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def create_snake_piece(piece_number, settings, screen, snake_body):
    """Create a piece of the snake and place it in the group."""
    new_piece = Snake(screen, settings)
    new_piece_width = new_piece.rect.width
    new_piece.x = new_piece_width * piece_number
    new_piece.rect.x = new_piece.x
    snake_body.add(new_piece)


def create_snake_body(settings, screen, snake_body):
    """Create the full snake body."""
    for piece_number in range(settings.snake_length):
        create_snake_piece(piece_number, settings, screen, snake_body)


def create_snake_food(food, screen, settings):
    """Check if there is any food on the screen."""
    for x in range(settings.food_allowed):
        new_food = Food(screen, settings)
        food.add(new_food)


def check_snake_food_collisions(food, screen, settings, snake):
    """Check if the snake has collided with the food."""
    collision = pygame.sprite.spritecollide(snake, food, True)
    if collision:
        settings.snake_length += 1


def update_screen(food, screen, settings, snake_body):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)

    # Redraw the snake at it's new position.
    for piece in snake_body.sprites():
        piece.draw_snake_rect()

    # Create more food if it's all gone.
    if len(food.sprites()) == 0:
        create_snake_food(food, screen, settings)

    # Make the most recently drawn screen visible.
    pygame.display.flip()
