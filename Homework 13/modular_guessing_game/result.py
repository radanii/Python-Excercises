# This module is used for storing game results as objects
# Later we still store these objects in lists, so we can use the sort function for the scoreboard.


class Result:
    def __init__(self, player, attempts, date, secret, wrongs, mode):
        self.player = player
        self.attempts = attempts
        self.date = date
        self.secret = secret
        self.wrongs = wrongs
        self.mode = mode
