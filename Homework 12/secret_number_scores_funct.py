# This file is used to generate the chosen scoreboard:
# IF U RUN THIS FILE IT WILL DELETE THE SCORES AND INSERT A NEW EMPTY LIST!

# imports:
import json


# get the current score_list:
def get_score_list():
    with open("scoreboard.txt", "r") as scores:
        scores_list = json.loads(scores.read())
        return scores_list


# get the full scoreboard and show in console:
def get_full_scores():
    scores_list = get_score_list()
    scores_list.sort(key=lambda x: x["date"])
    full_list = sorted(scores_list, key=lambda x: x["attempts"])

    for score_dict in full_list:
        print(score_dict["player"] + " with " +
              str(score_dict["attempts"]) + " attempts, date: " +
              score_dict.get("date") + "(Secret = " +
              str(score_dict["secret_number"]) + ")" + " Wrong guesses: " +
              str(score_dict.get("wrong_guesses")) + " " + "difficulty: " +
              str(score_dict.get("mode")))


# get the top 3 scoreboard and show in console:
def get_top3_scores():
    scores_list = get_score_list()
    scores_list.sort(key=lambda x: x["date"])
    top3_list = sorted(scores_list, key=lambda x: x["attempts"])[:3]

    for score_dict in top3_list:
        print(score_dict["player"] + " with " +
              str(score_dict["attempts"]) + " attempts, date: " +
              score_dict.get("date") + " " + "(Secret = " +
              str(score_dict["secret_number"]) + ")" + " Wrong guesses: " +
              str(score_dict.get("wrong_guesses")) + " " + "difficulty: " +
              str(score_dict.get("mode")))


# delete scores in scoreboard.txt:
def delete_scores():
    open("scoreboard.txt", "w").close()
    f = open("scoreboard.txt", "w")
    f.write("[]")
    f.close()
    print("Scores deleted!")


if __name__ == '__main__':
    delete_scores()



