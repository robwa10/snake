class Settings():
    """A class to store all the settings for Snake."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 600
        self.screen_height = 600
        self.bg_color = (240, 240, 240)

        # Snake settings
        self.piece_width = 10
        self.piece_height = 10
        self.snake_length = 3
        self.snake_color = (0, 0, 0)

        # Set the snake speed and starting direction
        self.speed = 200
        self.direction = "right"

        # Snake and food collisions
        self.food_collision = False

        # X and Y corodinates for the new block
        self.x_change = self.piece_width
        self.y_change = 0

        # Snake food settings
        self.food_block = (5, 5)
        self.food_color = (0, 0, 0)
        self.food_allowed = 5
