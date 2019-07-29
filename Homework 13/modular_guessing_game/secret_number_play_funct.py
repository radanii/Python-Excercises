# This file contains the play_game()-function, which is running the actual guessing process!

# imported functions:
from secret_number_scores_funct import get_score_list
from time import gmtime, strftime
from result import *

# imports:
import random
import json


def play_game():
    # Initialized variables:
    secret = random.randint(1, 10)
    wrong_guesses = []
    attempts = 0

    # Guessing-game:
    try:
        mode = int(
            input("\n" + "Choose your difficulty:" + "\n" + "Enter 1 for easy and 2 for a hard game without clues!:"))

        # Difficulty 1 - with clues
        if mode == int(1):

            player_name = str(input("Please type in your player name:"))

            while True:
                try:
                    guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
                    attempts += 1

                    if guess == secret:
                        print("Well done. " + str(secret) + " was my super secret number.")
                        print("Attempts:" + str(attempts))

                        # Fill in scoreboard.txt, when game is finished:

                        new_result = Result(player=player_name,
                                            attempts=attempts,
                                            date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                                            secret=secret,
                                            wrongs=wrong_guesses,
                                            mode="easy")

                        new_result.save_into_score_list()

                        break

                    elif guess < secret:
                        print("You might be close, try a bigger number.")
                    elif guess > secret:
                        print("Nice try, but I am sure my number was smaller.")

                    wrong_guesses.append(guess)

                except ValueError:
                    print("Please enter a number!")

        # Difficulty 2 - No clues
        elif mode == int(2):

            player_name = str(input("Please type in your player name:"))

            while True:
                try:
                    guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
                    attempts += 1

                    if guess == secret:
                        print("Well done. " + str(secret) + " was my super secret number.")
                        print("Attempts:" + str(attempts))

                        # Fill in scoreboard.txt, when game is finished:
                        new_result = Result(player=player_name,
                                            attempts=attempts,
                                            date=strftime("%Y-%m-%d %H:%M:%S", gmtime()),
                                            secret=secret,
                                            wrongs=wrong_guesses,
                                            mode="hard")

                        new_result.save_into_score_list()

                        break

                    wrong_guesses.append(guess)

                except ValueError:
                    print("Please enter a number!")

        # Difficulty != 1 or 2
        else:
            print("\n" + "Please enter a valid difficulty level!")

    except ValueError:
        print("Please enter a valid number!")
