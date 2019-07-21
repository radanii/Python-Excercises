
import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0
wrong_guesses = []

print("Try to beat the following Top 3 players:")

with open("scoreboard.txt", "r") as scores:
    scores_list = json.loads(scores.read())

    scores_list.sort(key=lambda x: x["date"])
    top3_list = sorted(scores_list, key=lambda x: x["attempts"])[:3]

    for score_dict in top3_list:
        print(score_dict["player"] + " with " +
              str(score_dict["attempts"]) + " attempts, date: " +
              score_dict.get("date") + "(Secret = " +
              str(score_dict["secret_number"]) + ")" + " Wrong guesses: " +
              str(score_dict.get("wrong_guesses")))

    player_name = str(input("Please type in your player name:"))

while True:
    try:
        guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
        attempts += 1

        if guess == secret:
            print("Well done. " + str(secret) + " was my super secret number.")
            print("Attempts:" + str(attempts))

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



