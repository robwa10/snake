import pygame
from pygame.sprite import Sprite


class Snake(Sprite):
    """A class to model a piece of the snake in the game."""

    def __init__(self, screen, settings):
        """ Initialize the snake piece's size, color and starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Create a rect to represent a piece of the snake body.
        self.rect = pygame.Rect((0, 0), settings.snake_block)

        # Start a new rect in the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the rect's exact position.
        self.x = float(self.rect.x)

    def draw_snake_rect(self):
        """Draw a snake rect to the screen."""
        pygame.draw.rect(self.screen, self.settings.snake_color, self.rect)
