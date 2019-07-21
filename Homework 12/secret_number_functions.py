# This file contains all used functions for the game:
# play_game()
# get_top3_scores()
# get_full_scores()

#imports:

import random
import json
import datetime

#variables:

secret = random.randint(1, 10)
attempts = 0
wrong_guesses = []


#play_game()-function is running the actual guessing process!

def play_game():
    if __name__ == '__main__':

        player_name = str(input("Please type in your player name:"))

        while True:
            try:
                guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
                #attempts += 1

                if guess == secret:
                    print("Well done. " + str(secret) + " was my super secret number.")
                    """print("Attempts:" + str(attempts))

                    scores_list.append({"player": str(player_name),
                                        "attempts": attempts,
                                        "date": str(datetime.datetime.now()),
                                        "secret_number": secret,
                                        "wrong_guesses": wrong_guesses})

                    with open("scoreboard.txt", "w") as scores:
                        scores.write(json.dumps(scores_list))"""
                    break

                elif guess < secret:
                    print("You might be close, try a bigger number.")
                elif guess > secret:
                    print("Nice try, but I am sure my number was smaller.")

                wrong_guesses.append(guess)

            except ValueError:
                print("Please enter a number!")


