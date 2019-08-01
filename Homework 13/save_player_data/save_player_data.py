# coding=utf8

from classes import *
from player_list import *

if __name__ == '__main__':
    print("Lets save some player details in a txt!")

    while True:
        choice = str.upper(input("\n" + "Enter" + "\n" +
                                 "A) to create a football-player" + "\n" +
                                 "B) to create a basketball-player," + "\n" +
                                 "C) to show the player-list" + "\n" +
                                 "D) to quit the data-tool"))

        if choice == "A":

            first_name = input("Enter a first name: ")
            last_name = input("Enter a last name: ")
            height = input("Enter player´s height: ")
            weight = input("Enter player´s weight: ")
            goals = input("Enter the number of goals: ")
            yellow_cards = input("Enter number of yellow cards: ")
            red_cards = input("Enter number of red cards: ")

            football_player = FootballPlayer(first_name=first_name,
                                             last_name=last_name,
                                             height_cm=float(height),
                                             weight_kg=float(weight),
                                             goals=int(goals),
                                             yellow_cards=int(yellow_cards),
                                             red_cards=int(red_cards))

            try:
               football_player.save_into_football_list()
            except Exception:
                print("footballplayer.txt doesn't exist!")

        elif choice == "B":

            first_name = input("Enter a first name: ")
            last_name = input("Enter a last name: ")
            height = input("Enter player´s height: ")
            weight = input("Enter player´s weight: ")
            points = input("Enter player's total points: ")
            rebounds = input("Enter total number of rebounds: ")
            assists = input("Enter total number of assists: ")

            basketball_player = BasketballPlayer(first_name=first_name,
                                                 last_name=last_name,
                                                 height_cm=float(height),
                                                 weight_kg=float(weight),
                                                 points=int(points),
                                                 rebounds=int(rebounds),
                                                 assists=int(assists))

            try:
                basketball_player.save_into_basketball_list()
            except Exception:
                print("basketballplayer.txt doesn't exist!")

        elif choice == "C":
            print("Enter your choice below: " + "\n" +
                  "F) to show football-players" + "\n" +
                  "B) to show basketball-players" + "\n" +
                  "FB) to show both together")
            selection = str.upper(input(" "))

            if selection == "F":
                print_playerlist_f()

            elif selection == "B":
                print_playerlist_b()

            elif selection == "FB":
                print_playerlist_f()
                print_playerlist_b()

            else:
                print("Please choose a valid display-option: F,B,FB")

        elif choice == "D":
            break
        else:
            print("\n" "Please enter a valid Choice (A/B/C/D)!" "\n")
