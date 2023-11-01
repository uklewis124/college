def main():
    user = User_Data()

    print(f"Your name is {user.name}")
    print(f"Your are is {user.age}")
    print(f"Your favourite animal is {user.animal_preference}")
    print(f"You get to college via {user.transport_method}")

class User_Data:
    def __init__(self):
        data_path = "2023/11/01/reading from files/userdata.txt"
        user_data_file = open(data_path)
        self.name = user_data_file.readline().split('\n')[0] # Fact 1
        self.age = user_data_file.readline().split('\n')[0] # Fact 2
        self.animal_preference = user_data_file.readline().split('\n')[0] # Fact 3
        self.transport_method = user_data_file.readline().split('\n')[0] # Fact 4
        user_data_file.close()

user = User_Data()

if __name__ == "__main__":
    main()