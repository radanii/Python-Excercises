
from player_list import *
import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self. weight_kg = weight_kg



class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self. red_cards = red_cards

    def save_into_football_list(self):
        fplayer_list = get_playerlist_f()
        fplayer_list.append(self.__dict__)

        with open("footballplayer.txt", "w") as listf:
            listf.write(json.dumps(fplayer_list))

class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def save_into_basketball_list(self):
        bplayer_list = get_playerlist_b()
        bplayer_list.append(self.__dict__)

        with open("basketballplayer.txt", "w") as listb:
            listb.write(json.dumps(bplayer_list))

