class Settings():
    """A class to store all the settings for Snake."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240, 240, 240)

        # Snake settings
        self.snake_block = (10, 10)
        self.snake_length = 3
        self.snake_color = (0, 0, 0)
        self.snake_speed_factor = 1.0

        # Snake food settings
        self.food_block = (5, 5)
        self.food_color = (0, 0, 0)
        self.food_allowed = 5
