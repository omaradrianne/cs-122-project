import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # For controlling frame rate.
        # Instance of class Clock.
        self.clock = pygame.time.Clock()

        # This is our display window.
        # The object assigned to self.screen is type surface.
        # A surface in Pygame is a part of the screen where a
        # game element can be dsiplayed. Each element in the
        # game, like an alien or a ship, is its own surface.
        # The surface returned by dsiplay.set_mode() represents
        # the entire game window.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Setting the backgroud color.
        self.bg_color = (230, 255, 230)

    # A function that controls the game.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
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

            # Redraw the screen during each pass through the
            # loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            # This creates the illusion of smooth movement.
            pygame.display.flip()

            # Frame rate set to 60.
            # Pygame will try to ensure the main loop runs
            # exactly 60 times per second.
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
