vips = {
    66512: {"Name":"Jimmy", "access":True, "Username":"jimmy123", "Password":"jimmy123"},
    23195: {"Name":"Sarah", "access":False, "Username":"sarah123", "Password":"sarah123"},
    14856: {"Name":"Bob", "access":True, "Username":"bob123", "Password":"bob123"},
    12453: {"Name":"Jeff", "access":False, "Username":"jeff123", "Password":"jeff123"},
    12345: {"Name":"John", "access":True, "Username":"john123", "Password":"john123"},
    54321: {"Name":"Jane", "access":False, "Username":"jane123", "Password":"jane123"},
    98765: {"Name":"Jack", "access":True, "Username":"jack123", "Password":"jack123"}
}

while True:
    username_input = input("Username: ")
    password_input = input("Password: ")
    correct = False
    for users in vips:
        if username_input == vips[users]["Username"] and password_input == vips[users]["Password"]:
            # Correct Password, Logged In
            correct = True
            print(f"Hello, {vips[users]['Name']}.")
            if vips[users]["access"] is True:
                print("You are granted access.")
            else:
                print("You are not granted access.")
            pass
    if correct != True:
        print("Incorrect Username or Password.")