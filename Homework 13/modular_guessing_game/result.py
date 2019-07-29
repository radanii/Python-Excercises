# This module is used for storing game results as objects
# Later we still store these objects in lists, so we can use the sort function for the scoreboard.

# imports:
from secret_number_scores_funct import get_score_list
import json


class Result:
    def __init__(self, player, attempts, date, secret, wrongs, mode):
        self.player = player
        self.attempts = attempts
        self.date = date
        self.secret = secret
        self.wrongs = wrongs
        self.mode = mode

    def save_into_score_list(self):
        scores_list = get_score_list()
        scores_list.append(self.__dict__)

        with open("scoreboard.txt", "w") as scores:
            scores.write(json.dumps(scores_list))
