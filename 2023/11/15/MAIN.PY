while True:
    print("What do you want to do?")
    print("1. Call next")
    print("2. Add")
    print("3. Exit")
    choice = input("Enter your choice: ")

    choices = {
        1:['1','one','on','11','next','call next','call','c'],
        2:['2','add','a','22'],
        3:['3','exit','e','quit','q','33']
}

    if choice in choices[1]:
        print("Calling next...")
    elif choice in choices[2]:
        print("Adding...")
    elif choice in choices[3]:
        print("Exiting...")
    else:
        print("Invalid choice")
