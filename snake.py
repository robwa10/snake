import pygame
from pygame.sprite import Sprite


class Snake(Sprite):
    """A class to model a piece of the snake in the game."""

    def __init__(self, screen, settings, x, y):
        """ Initialize the snake piece's size, color and starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Create a rect to represent a piece of the snake body.
        self.rect = pygame.Rect(0, 0, settings.piece_width,
                                settings.piece_height)

        # Set the rect's position
        self.rect.x = x
        self.rect.y = y

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.top < 0:
            return True
        elif self.rect.left < 0:
            return True
        elif self.rect.bottom > screen_rect.bottom:
            return True

    def draw_snake_rect(self):
        """Draw a snake rect to the screen."""
        pygame.draw.rect(self.screen, self.settings.snake_color, self.rect)
