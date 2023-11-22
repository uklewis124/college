students = {
    66512: {"Name":"Jimmy", "access":True, "Username":"jimmy123", "Password":"jimmy123"},
    23195: {"Name":"Sarah", "access":False, "Username":"sarah123", "Password":"sarah123"},
    14856: {"Name":"Bob", "access":True, "Username":"bob123", "Password":"bob123"},
    12453: {"Name":"Jeff", "access":False, "Username":"jeff123", "Password":"jeff123"},
    12345: {"Name":"John", "access":True, "Username":"john123", "Password":"john123"},
    54321: {"Name":"Jane", "access":False, "Username":"jane123", "Password":"jane123"},
    98765: {"Name":"Jack", "access":True, "Username":"jack123", "Password":"jack123"}
}

student_scores = {
    "Jimmy": 100,
    "Sarah": 90,
    "Bob": 80,
    "Jeff": 70,
    "John": 60,
    "Jack": 40
}

def login():
    correct = False
    users_name = ""
    while not correct:
        username_input = input("Username: ")
        password_input = input("Password: ")
        for users in students:
            if username_input == students[users]["Username"] and password_input == students[users]["Password"]:
                # Correct Password, Logged In
                users_name = students[users]["Name"]
                correct = True
                print(f"Hello, {students[users]['Name']}.")
                if students[users]["access"] is True:
                    print("You are granted access.")
                else:
                    print("You are not granted access.")
        if correct is not True:
            print("Incorrect Username or Password.")
    return users_name

def search(users_name):
    is_there = False
    for users in students:
        if users_name == students[users]["Name"]:
            is_there = True
    return is_there