import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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

        # This first line tells Pygame to figure out a window size
        # that will fill the screen.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # # We use the width and height attributes of the screen's rect to 
        # # update the settings object.
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game states, and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Setting the backgroud color.
        self.bg_color = (230, 230, 230)

        # Making a ship instance.
        # The call to Ship() requires one argument: an instance
        # of AlienInvasion. The self argument here refers to the
        # current instance of AlienInvasion. This is the parameter
        # that gives Ship access to the game's resources, such as
        # the screen object.
        self.ship = Ship(self)

        # When calling update() on a group, the group automatically
        # calls update() for each sprite in the group.
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.game_active = False

        self.play_button = Button(self, "Play")

    # A function that controls the game.
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            # Event: left click is pressed.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            # Event: a movement key is pressed.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Event: a movement key is released.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            # Reset game stats
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            self.game_active = True

            # Empty screen of existing assets
            self.bullets.empty()
            self.aliens.empty()

            # Initialize start game state
            self._create_fleet()
            self.ship.center_ship()

            # Hide cursor
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_RETURN:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update the position of bullets and get rid of old bullets"""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Checks and removes collisions between bullets and alien sprites
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for alien in collisions.values():
                self.stats.score += self.settings.alien_points * len(alien)

            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

            self.ship.center_ship()

    # Creates and adds a single alien instance to the fleet
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    # Creates alien fleet, scaling to screen size
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self):
        """Responds appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()

        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached bottom of screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the
        # loop.
        self.screen.fill(self.settings.bg_color)

        # Invokes the draw_bullet() function per bullet object within
        # the bullets group.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # After filling the background, we draw the ship
        # on the screen by calling ship.blitme(), so the 
        # ship appears on top of the background.
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw scoreboard
        self.sb.show_score()

        # If the game is not active, draw play button
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        # This creates the illusion of smooth movement.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
