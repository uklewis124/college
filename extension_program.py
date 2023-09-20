def get_user_details():
    username = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return username, age

def greet_user(name,age):
    print(f"hello {name} you are {age} years old")

def main():
    name, age = get_user_details()
    greet_user(name,age)
    
if __name__ == "__main__":
    main()
