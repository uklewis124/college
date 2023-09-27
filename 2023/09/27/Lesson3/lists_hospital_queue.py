import time
def main():
    """
    This module allows users to add patients to a queue and call the next patient based on priority.
    """
    # Pre-Requisites:
    patients = []
    priority = []
    print("Welcome to the Hospital Queue Program")
    user_testing = input("Are you testing the program? (y/n): ")
    testing = False
    while True:
        if user_testing == "y":
            testing = True
            break
        elif user_testing == "n":
            break
        else:
            print("Invalid option - Disabled testing")
            time.sleep(1)
            break
    os.system("clear")

    # Testing:
    if testing == True:
        patients = ["John","Sam","Mary","Steve","Bob","Alice"]
        priority = ["John","Sam","Mary"]
    else:
        pass

    # Input:
    while True:
        print("Pick an option:\n1. Add a patient\n2. Call the next patient\nq. Quit")
        # Asking for user option:
        option = input("Enter your option: ")

        # Option 1:
        if option == "1":
            # Validating patient's name:
            ValidPatientName = True
            tempPatientName = ""
            addingPatient = False
            while ValidPatientName == True:
            #Asking for patient's name:
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
                        priority.append(tempPatientName)
                        #Moving patient to the front of the queue:
                        patients.insert(len(priority)-1,tempPatientName) ## Minus 1 because the length of the list is 1 more than the index
                        addingPatient = False
                        break
                    elif choice == "n":
                        patients.append(tempPatientName)
                        addingPatient = False
                        break
                    else:
                        print("Invalid option")
                else:
                    break
        # Option 2:
        elif option == "2":
            if len(patients) == 0:
                print("There are no patients in the queue")
            else:
                print("Calling",patients[0])
                if patients[0] in priority:
                    print("This patient is a priority")
                    priority.remove(patients[0])
                else:
                    print("Patient not a priority")
                patients.remove(patients[0])
        # Option Quit:
        elif option.lower() == "q":
            print("Goodbye")
            break
        # Invalid option:
        else:
            print("Invalid option")


# End of program:-
if __name__ == "__main__":
    import os
    main()