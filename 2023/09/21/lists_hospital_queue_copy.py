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
            print("Invalid option")
    os.system("cls")

    # Testing:
    if testing == True:
        patients = ["John","Sam","Mary","Steve","Bob","Alice"]
        priority = ["John","Sam"]
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
            while ValidPatientName == True:
            #Asking for patient's name:
                patient_name = input("Enter the patient's name: ")
                if patient_name not in patients:
                    patients.append(patient_name)
                    break
                else:
                    print("This patient is already in the queue")
                    choice = input("Do you want to try again? (y/n): ")
                    if choice == "y":
                        pass
                    elif choice == "n":
                        ValidPatientName = False
                    else:
                        print("Invalid option")
                        ValidPatientName = False         
        # Asking if patient is a priority:
            while True:
                choice = input("Is this patient a priority? (y/n): ")
                if choice == "y":
                    priority.append(patient_name)
                    #Moving patient to the front of the queue:
                    patients.insert(0,patient_name)
                    patients.remove(patients[-1])
                    break
                elif choice == "n":
                    break
                else:
                    print("Invalid option")
        # Option 2:
        elif option == "2":
            if len(patients) == 0:
                print("There are no patients in the queue")
            else:
                print("Calling",patients[0])
                if patients[0] in priority:
                    print("This patient is a priority")
                    priority.remove(patients[0])
                patients.remove(patients[0])
        # Option Quit:
        elif option.lower() == "q":
            print("Goodbye")
            break
        # Invalid option:
        else:
            print("Invalid option")

        


# End of program:
if __name__ == "__main__":
    import os
    main()