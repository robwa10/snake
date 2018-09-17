import pygame


class Snake():
    """A class to model the snake in the game."""

    def __init__(self, screen, settings):
        """ Initialize the snake's size, color and starting position."""
        self.screen = screen
        self.settings = settings

        # Create the initial snake rect.
        self.rect = pygame.Rect(0, 0, settings.snake_width,
                                settings.snake_height)

        # Start the snake in the middle of the screen.
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the snake's position.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Set the snake's initial movement direction
        self.direction = "right"

    def draw_snake(self, settings):
        """Draw the snake to the screen."""
        pygame.draw.rect(self.screen, settings.color, self.rect)

    def update(self):
        """Update the snake's position based on direction."""
        if (self.rect.right >= self.screen_rect.right
            or self.rect.left <= self.screen_rect.left
            or self.rect.top <= self.screen_rect.top
            or self.rect.bottom >= self.screen_rect.bottom):
            # End the game if the snake hit's the screen edge.
            print("You hit the edge!")
        else:
            if self.direction is "right":
                self.centerx += self.settings.snake_speed_factor
            elif self.direction is "left":
                self.centerx -= self.settings.snake_speed_factor
            elif self.direction is "down":
                self.centery += self.settings.snake_speed_factor
            elif self.direction is "up":
                self.centery -= self.settings.snake_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
