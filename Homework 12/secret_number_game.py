# Run the game here!

# imported functions:
from secret_number_play import play_game
from secret_number_scores import get_full_scores
from secret_number_scores import get_top3_scores

while True:
    print("Welcome to <--**GUESS MY SECRET NUMBER!**-->")
    menu_choice = str.upper(input("Please choose between: " + "\n" +
                                  "A) New Game" + "\n" +
                                  "B) Top 3 Scoreboard" + "\n" +
                                  "C) View Full Scoreboard" + "\n" +
                                  "D) Quit Game" + "\n" + "\n" +
                                  "In order to select, please type in a,b,c or d here:"))
    if menu_choice == "A":
        play_game()
    elif menu_choice == "B":
        get_top3_scores()
    elif menu_choice == "C":
        get_full_scores()
    elif menu_choice == "D":
        break
    else:
        print("\n" + "Please select a VALID menu-option!" + "\n")