import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loads the alien image from the images folder
        self.image = pygame.image.load('images/tinyShip_7.png').convert_alpha()
        self.rect = self.image.get_rect()

        # Places the alien at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stores its horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True is alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien left or right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x