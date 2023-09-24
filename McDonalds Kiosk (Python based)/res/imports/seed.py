#Seed Generator
#Generates a random seed for the program to use
#This is used to generate random numbers

#Importing random
import random

#Importing time
import time

#Setting up the seed

def test():
    print("Just a test function!")
    
def seed():
    print("Generating seed...")
    #Generating the seed
    seed = random.seed(time.time())
    print("Generated seed!")
    return seed