#Imports
import os

#Relocated pre-determined to outside of the function
fugitive_license_plate = ["X999GHP","BD51MSR","PR05PER"]
fugitive_license_plate.append("X581GBB")

#Search function called if option 1 is selected
def fugitive_search():  
    search_plate = input("Which licence plate do you want to search for? ")
    if search_plate in fugitive_license_plate:
        print("This car may be driven by a wanted fugitive")
        print("Press enter to continue...")
    else:
        print("This person is not suspicious")
        input("Press enter to continue...")

#Add function called if option 2 is selected
def fugitive_add():
    new_plate = input("What is the new licence plate? ")
    fugitive_license_plate.append(new_plate)
    print("The new licence plate has been added.")
    input("Press enter to continue...")

#Remove function called if option 3 is selected
def fugitive_remove():
    try:
        remove_plate = input("Which license plate do you want to remove? ")
        fugitive_license_plate.remove(remove_plate)
        print("The license plate has been removed.")
        input("Press enter to continue...")
    except Exception:
        print("The license plate is not in the list.")
        input("Press enter to continue...")

def option():
    print("Please select an option:")
    print("1. Search for a license plate")
    print("2. Add a license plate")
    print("3. Remove a license plate")
    opt = input("Option: ")
    if opt == "1":
        os.system("clear")
        fugitive_search()
    elif opt == "2":
        os.system("clear")
        fugitive_add()
    elif opt == "3":
        os.system("clear")
        fugitive_remove()
    else:
        pass # Run option() again (via loop)
# Main Program #
while True:
    os.system("clear")
    option()