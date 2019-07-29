# Run the game here!

# imported functions:
from secret_number_play_funct import play_game
from secret_number_scores_funct import get_full_scores
from secret_number_scores_funct import get_top3_scores
from secret_number_scores_funct import delete_scores

pw = "radani"

while True:
    print("\n" + "Welcome to <--**GUESS MY SECRET NUMBER!**-->")
    menu_choice = str.upper(input("Please choose between: " + "\n" +
                                  "A) New Game" + "\n" +
                                  "B) Top 3 Scoreboard" + "\n" +
                                  "C) View Full Scoreboard" + "\n" +
                                  "D) Quit Game" + "\n" +
                                  "E) Delete Scores - (password protected)" + "\n" +
                                  "In order to select please type in A,B,C,D or E here:"))
    if menu_choice == "A":
        play_game()
    elif menu_choice == "B":
        get_top3_scores()
    elif menu_choice == "C":
        get_full_scores()
    elif menu_choice == "D":
        break
    elif menu_choice == "E":
        password = input("Please enter the password to continue: ")
        if password == pw:
            if __name__ == '__main__':
                delete_scores()
        else:
            print("Wrong password!")
    else:
        print("\n" + "Please select a VALID menu-option!" + "\n")
