import pygame


class Snake():
    """A class to model the snake in the game."""

    def __init__(self, screen, settings):
        """ Initialize the snake's size, color and starting position."""
        self.screen = screen

        # Create the initial snake rect.
        self.rect = pygame.Rect(0, 0, settings.snake_width,
                                settings.snake_height)

        # Start the snake in the middle of the screen.
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def draw_snake(self, settings):
        """Draw the snake to the screen."""
        pygame.draw.rect(self.screen, settings.color, self.rect)
