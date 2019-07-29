# coding=utf8

from classes import *
from player_list import *

if __name__ == '__main__':
    print("Lets save some player details in a txt!")

    while True:
        choice = str.upper(input("\n" + "Enter" + "\n" +"A) to create a football-player and B to create a basketball-player," +
                                 "\n" + "C to show the player-list" + "\n" +
                                 "otherwise press D to quit the data-tool"))

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
                with open("player.txt", "w") as file:
                    file.write(str(football_player.__dict__))
            except Exception:
                print("player.txt doesn't exist!")

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
                with open("player.txt", "w") as file:
                    file.write(str(basketball_player.__dict__))
            except Exception:
                print("player.txt doesn't exist!")

        elif choice == "C":
            print_playerlist()

        elif choice == "D":
            break
        else:
            print("\n" "Please enter a valid Choice (A/B)!" "\n")
