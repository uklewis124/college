def greet_user(name,age,sport):
    print(f"hello {name} you are {age} years old and your favourite sport is {sport}")

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))69
    # Extended: Adding more parameters
    sport = input("Enter your favorite sport: ")
    
    greet_user(name,age,sport)

if __name__ == "__main__":
    main()
