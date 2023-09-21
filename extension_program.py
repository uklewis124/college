import sys

def get_user_details():
    username = input("Enter your name: ")
    age = int(input("Enter your age: "))
    device = input("What device are you using? ")
    study = input("What are you studying? ")
    return username, age, device, study

def greet_user(name,age,device,study):
    print(f"hello {name}, you are {age} years old, and you are using {device}. I bet you are studying {study}!")

def main():
    name, age, device, study = get_user_details()
    greet_user(name,age,device,study)
    
if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(str(e))
    
