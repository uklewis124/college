def load():
    print("Importing required modules...")
    import os
    import time
    print("Resources plugin loaded")
    #All pre-requisites go here to be loaded before the main program runs
    patients = {}

def main():
    print("You are running this module directly, Try using the main program instead...")

def test():
    testing = False
    while True:
        user_testing = input("Are you testing the program? (y/n): ")
        if user_testing == "y":
            testing = True
            return testing
            break
        elif user_testing == "n":
            return testing
            break
        else:
            print("Invalid option - Disabled testing")
            time.sleep(1)
            break
    os.system("clear")

def options():
    print("Pick an option:\n1. Add a patient\n2. Call the next patient\nq. Quit")
    # Asking for user option:
    option = input("Enter your option: ")
    return option

def option1(doctor, patients):
    # Validating Patients Name:
    ValidPatientName = True
    tempPatientName = ""
    addingPatient = False
    while ValidPatientName == True:
        # Asking for patient's name:
        tempPatientName = input("Enter the patient's name: ")
        if tempPatientName not in patients:
            addingPatient = True
            break
        else:
            print("This patient is already in the queue")
            choice = input("Do you want to try again? (y/n): ")
            if choice.lower() == "y":
                pass
            elif choice.lower() == "n":
                ValidPatientName = False
            else:
                print("Invalid option")
                ValidPatientName = False
    # Asking if patient is a priority:
    while True:
        if addingPatient == True:
            choice = input("Is this patient a priority? (y/n): ")
            if choice == "y":
                patients[tempPatientName]["Priority"] = True
                break










## DO NOT EDIT BELOW THIS LINE
if __name__ == "__main__":
    main()
    import os
    import time