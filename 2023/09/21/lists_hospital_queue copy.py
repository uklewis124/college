#Pre-requisites:
patients = []
priority = []

##########################
#Testing
patients = ["John","Mary","Steve","Sam","Bob"]
priority = ["John","Sam"]
# Sorting priorities in patients list
for i, patient in enumerate(patients):
    if patient in priority:
        patients.insert(0, patient)
        patients.pop(i+1)
    else:
        pass
##########################

#Input:
while True:
    print("""
Pick an option:
1. Add a patient
2. View the queue
3. Remove a patient
4. Exit
            """)
    while True:
        try:
            choice = int(input("Enter your option: "))
            if choice == 1:
                patients.append(input("Enter the patient's name: "))
                while True:
                    try:
                        priority_ask = input("Is this patient a priority? (y/n): ")
                        if priority_ask == "y":
                            patients.insert(0,patients[-1])
                            patients.remove(patients[-1])
                            priority.append(patients[0])
                            break
                        elif priority_ask == "n":
                            break
                    except Exception as e:
                        print("An error occurred:", e,"at line",e.__traceback__.tb_lineno)
                        print("Please enter a valid option (y/n)") 
                    break
            elif choice == 2:
                try:
                    print("The next patient is:",patients[0])
                    if patients[0] in priority:
                        print("This patient is a priority")
                    elif patients[0] not in priority:
                        print("This patient is not a priority")
                    else:
                        pass
                    patients.remove(patients[0])
                    priority.remove(priority[0])
                except Exception as e:
                    print("There are no patients in the queue")
            elif choice == 3:
                while True:
                    try:
                        patients.remove(input("Enter the patient's name: "))
                        break
                    except IndexError as e:
                        print("An error occurred:", e,"at line",e.__traceback__.tb_lineno)
                        print("That patient is not in the queue")
                    except Exception as e:
                        print("An error occurred:", e,"at line",e.__traceback__.tb_lineno)
                        print("An error occurred:", e)
            elif choice == 4:
                break
        except Exception as e:
            print("An error occurred:", e,"at line",e.__traceback__.tb_lineno)
            print("Please enter a valid number (1-4)")
    break