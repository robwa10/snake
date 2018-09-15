import pygame


class Snake():
    """A class to model the snake in the game."""

    def __init__(self, screen):
        """ Initialize the snake's size, color and starting position."""
        self.screen = screen

        # Set the inital snake dimensions and color
        self.snake_width = 30
        self.snake_height = 10 
        self.color = (0, 0, 0)

        # Create the initial snake rect.
        self.rect = pygame.Rect(0, 0, self.snake_width, self.snake_height)

        # Start the snake in the middle of the screen.
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def draw_snake(self):
        """Draw the snake to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
