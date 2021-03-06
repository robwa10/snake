import sys

import pygame

from food import Food
from snake import Snake


def check_keydown_events(event, settings):
    """Respond to key presses."""
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_LEFT and settings.direction != "right":
        settings.x_change = settings.piece_width * -1
        settings.y_change = 0
        settings.direction = "left"
    elif event.key == pygame.K_RIGHT and settings.direction != "left":
        settings.x_change = settings.piece_width
        settings.y_change = 0
        settings.direction = "right"
    elif event.key == pygame.K_UP and settings.direction != "down":
        settings.x_change = 0
        settings.y_change = settings.piece_height * -1
        settings.direction = "up"
    elif event.key == pygame.K_DOWN and settings.direction != "up":
        settings.x_change = 0
        settings.y_change = settings.piece_height
        settings.direction = "down"


def check_events(food, screen, settings):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings)


def food_collision(food, settings, snake_list, stats):
    """Check if the snake collided with food."""
    for sprite in food.sprites():
        if sprite.rect.colliderect(snake_list[0]):
            # Remove the food piece
            food.remove(sprite)
            settings.food_collision = True
            stats.total_pieces += 1

            # Raise the snake speed.
            if settings.speed >= 10:
                settings.speed -= 2


def screen_collision(screen, snake_list, stats):
    """Check if the snake collided with the screen edge."""
    screen_rect = screen.get_rect()
    if (snake_list[0].rect.right > screen_rect.right or
        snake_list[0].rect.left < 0 or
        snake_list[0].rect.top < 0 or
        snake_list[0].rect.bottom > screen_rect.bottom):
        stats.game_active = False


def self_collision(snake_list, stats):
    """Check if the snake hit itself."""
    for i in range(1, len(snake_list)):
        if (snake_list[0].rect.x == snake_list[i].rect.x and 
                snake_list[0].rect.y == snake_list[i].rect.y):
            stats.game_active = False
            break


def check_collisions(food, screen, settings, snake_list, stats):
    """Check if the snake collided with food, the screen edge or itself."""
    food_collision(food, settings, snake_list, stats)
    screen_collision(screen, snake_list, stats)
    self_collision(snake_list, stats)


def create_snake_piece(piece_number, screen, settings, snake_body, snake_list):
    """Create a piece of the snake and place it in the group."""
    x = settings.piece_width * piece_number
    y = settings.piece_height
    new_piece = Snake(screen, settings, x, y)
    snake_list.append(new_piece)
    snake_body.add(new_piece)


def create_snake_body(screen, settings, snake_body, snake_list):
    """Create the full snake body."""
    for piece_number in range(settings.snake_length):
        create_snake_piece(piece_number, screen, settings, snake_body,
                           snake_list)


def move_pieces(screen, settings, snake_body, snake_list):
    """Move the snake pieces to new position."""
    # Decide the coordinates of the new piece.
    x = snake_list[0].rect.x + settings.x_change
    y = snake_list[0].rect.y + settings.y_change
    new_piece = Snake(screen, settings, x, y)

    # Place the new one in the group and list.
    snake_list.insert(0, new_piece)
    snake_body.add(new_piece)


def move_snake(food, screen, settings, snake_body, snake_list):
    """Remove the last snake piece and create a new one on the front."""
    # Remove the last snake pice from the group.
    if not settings.food_collision:
        last_piece = snake_list.pop()
        snake_body.remove(last_piece)
        move_pieces(screen, settings, snake_body, snake_list)
    else:
        settings.food_collision = False
        move_pieces(screen, settings, snake_body, snake_list)


def check_snake_food(food, screen, settings):
    """Create snake food on the screen if there is none."""
    if len(food.sprites()) == 0:
        for x in range(settings.food_allowed):
            new_food = Food(screen, settings)
            food.add(new_food)


def update_screen(food, screen, settings, snake_body):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_color)

    # Redraw the snake at it's new position.
    for piece in snake_body.sprites():
        piece.draw_snake_rect()

    for n in food.sprites():
        n.draw_food()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
