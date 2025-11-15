import pygame

class Ship:
    """A class to manage the ship."""

    # ai_game is a reference to the current instance of the
    # AlienInvasion class. This will give Ship access to all
    # the game resources defined in AlienInvasion.
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""

        # This allows us to easily access the game screen in all
        # methods of this class.
        self.screen = ai_game.screen

        # We access the screen's rect attribute using the get_rect()
        # method and assign it to self.screen_rect. Doing so allows
        # us to place the ship in the correct location on the screen.
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        # This function returns a surface object representing the
        # ship, which we assign to self.image.
        self.image = pygame.image.load('images/ship.bmp')
        
        # When the image is loaded, we call get_rect() to access
        # the ship surface's rect attribute so we can later use it
        # to place the ship.
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 3
        if self.moving_left:
            self.rect.x -= 3
        if self.moving_up:
            self.rect.y -= 3
        if self.moving_down:
            self.rect.y += 3

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

# Pygame lets us treat all game elements like rectangles (rects),
# even if they're not exactly shaped like rectangles.
# We will be treating the ship and the screen as rectangles.

# We can set any of these values to establish the current postion 
# of the rect. Options:
# center, centerx, centery, top, bottom, left, right, midbottom,
# midtop, midleft, midright.
# We could also specify the x and y attributes, which are the x-
# and y-coordinates of its top-left corner.

# In Pygame, the origin (0,0) is at the top-left corner of the
# screen, and coordinates increase as you go down and to the right.
# On a 1200x800 screen, the origin is at the top-left corner, and
# the bottom-right corner has the coordinates (1200, 800). These
# coordinates refer to the game window, not the physical screen.