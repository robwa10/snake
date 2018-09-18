class Settings():
    """A class to store all the settings for Snake."""

    def __init__(self):
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240, 240, 240)

        # Snake settings
        self.snake_width = 10
        self.snake_height = 10
        self.snake_color = (0, 0, 0)
        self.snake_speed_factor = 1.5

        # Snake food settings
        self.food_width = 5
        self.food_height = 5
        self.food_color = (0, 0, 0)
        self.food_allowed = 5
