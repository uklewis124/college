def phone_num():
    flag = True

    while flag:
        number = input("Please enter your phone number: ")

        try:
            int(number)
        except:
            print("Sorry, you did not enter a valid number")
            flag = True
        else:
            if len(number) <= 2:
                print("Sorry, you did not enter a valid number")
                flag = True
            else:
                for digit in number:
                    if digit.isdigit() == False:
                        print("Sorry, you did not enter a valid name")
                        flag = True
                    else:
                        return number

phone_num()