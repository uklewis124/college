# imports
print("Importing Modules...")
import random
import time
import os
print("Modules Imported")

# Pre-initialization Variables
print("Pre-initializing Variables...")

inventory = {
    "Gold": [weight = 1, value = 15, quantity = 0],
    "Map": [weight = 1, value = 1, quantity = 0],
    "Revolver": [weight = 2, value = 10, quantity = 0],
    "Knife": [weight = 1, value = 5, quantity = 0],
    ##Chewing gum that improves values
    ## alcohol
    ## food
}

current_inventory = []


##Implementing a test inventory
def testing():
    q = input("Would you like to test the inventory? (y/n)")
    testing = False
    if q == "y":
        testing = True
    if testing == True:
        current_inventory = ["Gold", "Map", "Revolver", "Knife"]
        print_inventory(current_inventory)
        print("Adding 5 Gold to inventory...")
        time.sleep(2)
        os.system("cls")

print("Variables Pre-initialized")

# functions
print("Defining Functions...")

def print_inventory(inventory):
    print("Inventory:")
    for item in inventory:
        print(item)
    print("")