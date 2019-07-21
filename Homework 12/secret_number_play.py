# This file contains the play_game()-function, which is running the actual guessing process!

# imported functions:
from secret_number_scores import get_score_list

# imports:
import random
import json
import datetime


def play_game():
    # Initialized variables:
    secret = random.randint(1, 10)
    wrong_guesses = []
    attempts = 0

    # Guessing-game:
    player_name = str(input("Please type in your player name:"))
    while True:
        try:
            guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
            attempts += 1

            if guess == secret:
                print("Well done. " + str(secret) + " was my super secret number.")
                print("Attempts:" + str(attempts))

                # Fill in scoreboard.txt, when game is finished:
                scores_list = get_score_list()
                scores_list.append({"player": str(player_name),
                                    "attempts": attempts,
                                    "date": str(datetime.datetime.now()),
                                    "secret_number": secret,
                                    "wrong_guesses": wrong_guesses})

                with open("scoreboard.txt", "w") as scores:
                    scores.write(json.dumps(scores_list))
                break
            elif guess < secret:
                print("You might be close, try a bigger number.")
            elif guess > secret:
                print("Nice try, but I am sure my number was smaller.")

            wrong_guesses.append(guess)

        except ValueError:
            print("Please enter a number!")
