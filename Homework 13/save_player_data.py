from classes import *

if __name__ == '__main__':
    print("Lets save some player details in a txt!")

    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")
    height = input("Enter player´s height: ")
    weight = input("Enter player´s weight: ")
    goals = input("Enter the number of goals: ")
    yellow_cards = input("Enter number of yellow cards: ")
    red_cards = input("Enter number of red cards: ")

    test_player = FootballPlayer(first_name=first_name,
                                 last_name=last_name,
                                 height_cm=float(height),
                                 weight_kg=float(weight),
                                 goals=int(goals),
                                 yellow_cards=int(yellow_cards),
                                 red_cards=int(red_cards))

    with open("player.txt", "w") as file:
        file.write(str(test_player.__dict__))

