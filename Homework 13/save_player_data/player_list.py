# This module defines functions for sorting and showing the playerlist on console:

import json


def get_playerlist():
    with open("player.txt", "r") as openfile:
        actual_list = json.loads(openfile.read())
        return actual_list


def print_playerlist():
    player_list = get_playerlist()

    for player_dict in player_list:
        print(player_dict["first_name"] + " " +
        print(player_dict["last_name"] + "\n" + "height: " +
        print(player_dict["height"] + "\n" + "weight")))

