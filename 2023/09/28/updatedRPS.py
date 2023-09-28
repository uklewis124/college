import random

testing = True

options = ["spock","rock","scissors","lizard","paper"]
ways_to_win = [["vaporises","smashes"],["crushes","crushes"],["decapitates","cuts"],["eats","poisons"],["disproves","covers"]]

def get_user_choice():
    player_choice = ""
    while player_choice not in options:
        player_choice = input("You can choose from: spock, rock, scissors, lizard, paper\n, Your choice: ")
    return player_choice

def get_computer_choice():
    computer_choice = random.randint(0,len(options)-1)
    computer_choice = options[computer_choice]
    return computer_choice
## Grabbing the index of what the user chose
user_choice = get_user_choice()
computer_choice = get_computer_choice()
if testing == True:
    computer_choice = "scissors"
player_choice_get_index = options.index(user_choice)
## Finish

## Defines the two ways the player can win
beats_option_one = (player_choice_get_index + 1) % len(options) #Defines the first way the player can win
#print("The player can win if the computer chooses a " + options[player_wins_against_one])
beats_option_two = (player_choice_get_index + 2) % len(options) #Defines the second way the player can win
#print("The player can also win if the computer chooses a " +options[player_wins_against_two])
## Finish
computer_beats_option_one = (player_choice_get_index - 1) % len(options)
computer_beats_option_two = (player_choice_get_index - 2) % len(options)

print()

computer_choice_index = options.index(computer_choice)
## Begin checking if the player won
if computer_choice == beats_option_one:
    print("The player wins because " + user_choice + " " + ways_to_win[player_choice_get_index][0] + " " + options[beats_option_one])
elif computer_choice == beats_option_two:
    print("The player wins because " + user_choice + " " + ways_to_win[player_choice_get_index][1], " ", options[beats_option_two])
elif computer_choice == user_choice:
    print("It's a draw!")
else:
    print("The computer wins because ", computer_choice, "beats", user_choice)


