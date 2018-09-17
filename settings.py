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
        self.color = (0, 0, 0)
        self.snake_speed_factor = 5.5
