import shelve

class GameStats:
    """Track stats for Game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize stats with each new game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        with shelve.open('hiscores.dbm') as file:
            if 'hiscore' in file:
                self.high_score = file['hiscore']
            else:
                self.high_score = 0
                file['hiscore'] = self.high_score
