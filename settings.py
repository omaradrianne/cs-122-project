import pygame

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initializing the game's settings."""
        # Screen settings

        # Setting the background color.
        # (255, 0, 0) is red
        # (0, 255, 0) is green
        # (0, 0, 255) is blue
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.bg_image = pygame.image.load("images/space_background.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        # Scaling settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change through the game"""

        # Speed settings
        self.ship_speed = 2.87
        self.bullet_speed = 3.5
        self.alien_speed = 1.0

        # Score settings
        self.alien_points = 50

        # fleet_direction of 1 = right, -1 = left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases speed settings"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
