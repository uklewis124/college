'''import random

options = ["spock","rock","scissors","lizard","paper"]

win_words = [["vaporises","smashes"],["crushes","crushes"],["decapitates","cuts"],["eats","poisons"],["disproves","covers"]]

player_choice = ""
computer_choice =random.randint(0,len(options)-1)
options_as_string = ", ".join(options)

while player_choice not in options:
    player_choice = input("Choose from: " + options_as_string + ":").lower().strip()
    
player_choice_index = options.index(player_choice)

player_win_against_one = (player_choice_index + 1) % len(options)
player_win_against_two = (player_choice_index + 2) % len(options)
print()
print(win_words[player_choice_index][0])
print(win_words[player_choice_index][1])
print()
print(options[player_win_against_one])
print(options[player_win_against_two])
print()
print("Computer chose: " + options[computer_choice])'''


# computer chose paper
# scissors cuts paper - you lose
# rock: paper covers rock - you win
# etc

## Rebuilding the game just to make it easier to understand

#Imports
import random

#Variables
options = ["spock","rock","scissors","lizard","paper"]
win_words = [["vaporises","smashes"],["crushes","crushes"],["decapitates","cuts"],["eats","poisons"],["disproves","covers"]]
options_as_string = ", ".join(options)

'''#Define functions
def player_choice():
    player_choice = ""
    while player_choice not in options:
        player_choice = input("Choose from: " + options_as_string + ":").lower().strip()
    return player_choice

def computer_choice():
    choice = random.randint(0,len(options)-1)
    return choice

def win_check(player_choice, computer_choice, options):
    player_choice_index = options.index(player_choice)
    player_win_against_one = (player_choice_index + 1) % len(options)
    player_win_against_two = (player_choice_index + 2) % len(options)
    return player_win_against_one, player_win_against_two
    

def main():
    player_choice_input = player_choice()
    computer_choice_output = computer_choice()
    winner_grab = win_check(player_choice_input,computer_choice_output)
    print(winner_grab)

if __name__ == "__main__":
    main()


#Main program
if __name__ == "__main__":
    main()'''

## rebuilding (again)

#Imports
import random
#Variables
options = ["spock","rock","scissors","lizard","paper"]
win_words = [["vaporises","smashes"],["crushes","crushes"],["decapitates","cuts"],["eats","poisons"],["disproves","covers"]]
options_as_string = ", ".join(options)
#Ask for player choice
player_choice = ""
computer_choice =random.randint(0,len(options)-1)

while player_choice not in options:
    player_choice = input("Choose from: " + options_as_string + ":").lower().strip()
    print("You chose: "+player_choice)

player_choice_index = options.index(player_choice) # Finds out index value of player choice (spock = 0, rock = 1, etc)
print(player_choice_index) #Used for debugging

player_win_against_one = (player_choice_index + 1) % len(options) # Player choice beats *
player_win_against_two = (player_choice_index + 2) % len(options) # Player choice beats **
#print(player_win_against_one) #Used for debugging
#print(player_win_against_two) #Used for debugging

print()

print(win_words[player_choice_index][0]) # Prints out the first word in the win_words list
print(win_words[player_choice_index][1]) # Prints out the second word in the win_words list
print()
print(options[player_win_against_one]) # Prints out playerwin against one'th word in the options list
print(options[player_win_against_two]) # Prints out playerwin against two'th word in the options list
print()
print("Computer chose: " + options[computer_choice]) # Prints out what the computer chose