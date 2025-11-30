class GameStats:
    """Track stats for Game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats with each new game"""
        self.ships_left = self.settings.ship_limit