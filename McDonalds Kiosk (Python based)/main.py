print("Initializing...")
print("Importing sys")
import sys
print("Importing tkinter")
import tkinter as tk
print("Importing os")
import os
from os import environ
print("Importing pandas")
import pandas as pd
print("Importing numpy")
import numpy as np
print("Importing PyQt5")
import PyQt5
print("Importing time")
import time
print("Importing dotenv")
from dotenv import load_dotenv
import dotenv
print("Imported all modules successfully!")

#Setting up dotenv
print("Setting up dotenv...")
load_dotenv()

print("Successfully set up dotenv!")

print("Initializing variables...")
#Variables
#Path to the folder containing the files
img_path = "/src/"
path = "/"

#Other Variables (stored in code)

#Private Variables (not stored in code)
DEVICE_ID = environ.get("DEVICE_ID")
SECRET_KEY = environ.get("SECRET_KEY")
print("Successfully initialized variables!")

print("Checking if the device is registered...")
#Checking if the device is registered
if 1 not in DEVICE_ID:
    print("Device is not registered!")
    print("Registering device...")
    #Registering the device & importing random and seeding
    print("Importing random")
    import random
    print("Importing seed generator")
    import res.imports.seed as seed
    seedgen = seed.seed()
    print(seedgen)