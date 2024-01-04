import buggyxp as bx  # Import BuggyXP Libary

while True:
    section1 = False
    section2 = False
    section3 = False
    try:
        first_val = int(input("Enter first number: "))
        section1 = True
    except ValueError:
        print("Please enter a valid number.")
        continue
    if section1:
        try:
            operator = input("Enter the operator you want to use (+, -, *, /): ")
            available_operators = ["+", "-", "*", "/"]
            if operator not in available_operators:
                raise ValueError
            section2 = True
        except ValueError:
            print("Please enter a valid operator.")
        if section2:
            try:
                second_val = int(input("Enter second number: "))
                section3 = True
            except ValueError:
                print("Please enter a valid number.")
            if section3:
                if operator == "+":
                    output = bx.add(first_val, second_val)
                elif operator == "-":
                    output = bx.subtract(first_val, second_val)
                elif operator == "*":
                    output = bx.multiply(first_val, second_val)
                else:
                    output = bx.divide(first_val, second_val)
                print(f"Output: {output}")