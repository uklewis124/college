import login_system
import time
import os

start_time = time.perf_counter()
### Code goes below here

# grabs the first numbers in dict,
# then the contents of the dict of that id
"""
for uid, contents in login_system.vips.items():
    print(uid, contents)
"""

users_name = login_system.login() # Logs in the user

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(users_name):
    while True:
        input("Press Enter to continue...") # Stops console from clearing after loop
        clear()
        print(f"Hello, {users_name}.")
        print("What would you like to do?")
        print("1. View Student Scores")
        print("2. Add Student Scores")
        print("3. Remove Student Scores")
        print("4. Exit")
        choice = input("Choice: ")
        clear()
        if choice == "1":
            view_scores(users_name)
        elif choice == "2":
            add_scores(users_name)
        elif choice == "3":
            remove_scores(users_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid Choice.")

def view_scores(users_name):
    if login_system.search(users_name) is True:
        if users_name in login_system.student_scores.items():
            print(f"The score for {users_name} is:")
            print(login_system.student_scores[users_name])
        else:
            print("This student does not exist.")
    else:
        print("This user does not have a score.")

def add_scores(users_name):
    if login_system.search(users_name) is True:
        if users_name in login_system.student_scores.items():
            print("This student already has a score.")
        else:
            score = int(input(f"Enter {users_name}'s score: "))
            login_system.student_scores[users_name] = score
    else:
        print("This student does not exist.")

def remove_scores(users_name):
    if login_system.search(users_name) is True:
        if users_name in login_system.student_scores.items():
            login_system.student_scores.pop(users_name)
        else:
            print("This student does not have a score.")
    else:
        print("This student does not exist.")

student_scores = {
    "Jimmy": 100,
    "Sarah": 90,
    "Bob": 80,
    "Jeff": 70,
    "John": 60,
    "Jane": 50,
    "Jack": 40
}

main(users_name)
clear()

### Code goes above here
end_time = time.perf_counter()
print(f"Time Elapsed: {end_time - start_time}")
