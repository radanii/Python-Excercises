# This module defines functions for sorting and showing the playerlist on console:

import json


def get_playerlist_f():
    with open("footballplayer.txt", "r") as openfile:
        actual_list = json.loads(openfile.read())
        return actual_list


def get_playerlist_b():
    with open("basketballplayer.txt", "r") as openfile:
        actual_list = json.loads(openfile.read())
        return actual_list


def print_playerlist_f():
    actual_list = get_playerlist_f()
    print("Football-players: ")

    for player_dict in actual_list:
        print("\n" +
            player_dict["first_name"] + "," +
            player_dict["last_name"] + "\n" + "height: " +
            str(player_dict.get("height_cm")) + ", " + "weight: " +
            str(player_dict.get("weight_kg")) + "\n" + "goals: " +
            str(player_dict.get("goals")) + ", " + "Y-cards: " +
            str(player_dict.get("yellow_cards")) + ", " + "R-cards: " +
            str(player_dict.get("red_cards")) + "\n")


def print_playerlist_b():
    actual_list = get_playerlist_b()
    print("Basketball-players: ")

    for player_dict in actual_list:
        print("\n" +
            player_dict["first_name"] + "," +
            player_dict["last_name"] + "\n" + "height: " +
            str(player_dict.get("height_cm")) + ", " + "weight: " +
            str(player_dict.get("weight_kg")) + "\n" + "points: " +
            str(player_dict.get("points")) + ", " + "rebounds: " +
            str(player_dict.get("rebounds")) + ", " + "assists: " +
            str(player_dict.get("assists")) + "\n")
