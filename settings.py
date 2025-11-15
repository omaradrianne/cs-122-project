class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initializing the game's settings."""
        # Screen settings

        # Setting the backgroud color.
        # (255, 0, 0) is red
        # (0, 255, 0) is green
        # (0, 0, 255) is blue
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 2.87