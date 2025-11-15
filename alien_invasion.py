import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        # Initializing the background settings that Pygame
        # needs to work properly.
        pygame.init()

        # For controlling frame rate.
        # Instance of class Clock.
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # This is our display window.
        # The object assigned to self.screen is type surface.
        # A surface in Pygame is a part of the screen where a
        # game element can be dsiplayed. Each element in the
        # game, like an alien or a ship, is its own surface.
        # The surface returned by dsiplay.set_mode() represents
        # the entire game window.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Setting the backgroud color.
        self.bg_color = (230, 230, 230)

        # Making a ship instance.
        # The call to Ship() requires one argument: an instance
        # of AlienInvasion. The self argument here refers to the
        # current instance of AlienInvasion. This is the parameter
        # that gives Ship access to the game's resources, such as
        # the screen object.
        self.ship = Ship(self)

    # A function that controls the game.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

            # Frame rate set to 60.
            # Pygame will try to ensure the main loop runs
            # exactly 60 times per second.
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        # To access the events that Pygame detects, we'll
        # use the pygame.event.get() function. This function
        # returns a list of events that have taken place
        # since the last time this functioin was called.
        for event in pygame.event.get(): # The event loop.
            # Inside, we write a series of statements to
            # detect and respond to specific events.
            if event.type == pygame.QUIT:
                sys.exit()
            # Event: a movement key is pressed.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_s:
                    self.ship.moving_down = True
            # Event: a movement key is released.
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
                elif event.key == pygame.K_w:
                    self.ship.moving_up = False
                elif event.key == pygame.K_s:
                    self.ship.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the
        # loop.
        self.screen.fill(self.settings.bg_color)

        # After filling the background, we draw the ship
        # on the screen by calling ship.blitme(), so the 
        # ship appears on top of the background.
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        # This creates the illusion of smooth movement.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
