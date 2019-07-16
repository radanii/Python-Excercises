
import random
import json
import datetime

secret = random.randint(1, 10)
attempts = 0

print("Try to beat the following Top 3 players:")

with open("scoreboard.txt", "r") as scores:
    scores_list = json.loads(scores.read())

    for score_dict in scores_list:
        print(score_dict["player"] + " with " + str(score_dict["attempts"]) + " attempts, date: " +
              score_dict.get("date") + "(Secret = " + str(score_dict["secret_number"]) + ")")

    player_name = str(input("Please type in your name!:"))

while True:
    guess = int(input("Try to guess my secret number, which is between 1 and 10!: "))
    attempts += 1

    if guess == secret:
        print("Well done. " + str(secret) + " was my super secret number.")
        print("Attempts:" + str(attempts))

        scores_list.append({"player": str(player_name), "attempts": attempts,
                            "date": str(datetime.datetime.now()), "secret_number": secret})

        with open("scoreboard.txt", "w") as scores:
            scores.write(json.dumps(scores_list))
        break
    elif guess < secret:
        print("You might be close, try a bigger number.")
    elif guess > secret:
        print("Nice try, but I am sure my number was smaller.")



