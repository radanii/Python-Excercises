#This module is used for storing game results:


class Result:
    def __init__(self, player_name, attempts, date, secret, wrongs, mode):
        self.player_name = player_name
        self.attempts = attempts
        self.date = date
        self.secret = secret
        self.wrongs = wrongs
        self.mode = mode
