import pandas as pd
import os
import time

# Pre-Game Setup
os.chdir('/workspaces/college/2023/09/27/Lesson1_Equality_Game')

# Importing Scenarios
scenarios = pd.read_csv("resources/scenarios.csv")
print(scenarios.head())

# Clearing the screen for the game
os.system('clear')
print("Starting Game...")
time.sleep(1)
os.system('clear')

# Beginning the game
rows = scenarios.shape[0]
cols = scenarios.shape[1]
points = 0

for i in range(rows):
    print(f"\nScenario {i+1}: {scenarios.iloc[i,2]}")
    guess = input("Does this scenario break the Data Protection Act? (T)rue or (F)alse? ")
    if guess.lower() == scenarios.iloc[i,3].lower():
        print("Correct!")
        points += 1
    else:
        print("Incorrect.")
    time.sleep(1)

print(f"\nGame over! You scored {points} points out of {rows}.")