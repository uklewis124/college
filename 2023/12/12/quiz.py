"""
Christmas Quiz
"""

# Imports
import pandas as pd
import numpy as np

import os
import sys
import time
import random

from colorama import Fore, Back, Style


# Variables
stats = {
    "user1": {"score": 0, "name": ""},
    "user2": {"score": 0, "name": ""}
}
csvs = []
# Preparing CSV Data
data = pd.DataFrame()


def clear():
    os.system("cls" if os.name == "nt" else "clear")

def setup():
    global csvs, data
    csvs = []
    for csv in os.listdir("2023/12/12/"):
        if csv.endswith(".csv"):
            csvs.append(csv)
    clear()
    print("Welcome to the Christmas Quiz!")
    print("Please select a quiz from the below options:")
    time.sleep(3)
    clear()
    chosen = False
    while not chosen:
        for csv in csvs:
            csv_path = os.path.join("2023/12/12/", csv)
            if not os.path.exists(csv_path):
                print(f"Error: {csv_path} does not exist.")
                sys.exit(1)
            else:
                print("Available Options: ")
                for i, csv in enumerate(csvs):
                    new_name = csv.replace(".csv", "")
                    print(f"{i+1}. {new_name}")
                print(f"{Fore.RED}==========================================={Fore.RESET}")
                choice = input(f"Do you want do the {new_name} quiz? (y/n) ")
                if choice.lower() == "y":
                    print(f"Using {csv_path}.")
                    data = pd.read_csv(csv_path)
                    chosen = True
                    clear()
                    break
                else:
                    print(f"Not using {csv_path}.")
                    clear()
        if data.empty:
            print(
                Fore.RED + "Error: No Quiz Selected. Please try again.",
                Fore.RESET
            )
            time.sleep(2)
            clear()


def run_quiz():
    pass


# Main
def main():
    setup()
    run_quiz()

if __name__ == "__main__":
    main()