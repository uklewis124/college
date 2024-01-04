def add(value1,value2):
    if not isinstance(value1, int):
        raise TypeError("Value 1 must be an integer.")
    if not isinstance(value2, int):
        raise TypeError("Value 2 must be an integer.")
    
    return value1 + value2

def subtract(value1, value2):
    if not isinstance(value1, int):
        raise TypeError("Value 1 must be an integer.")
    if not isinstance(value2, int):
        raise TypeError("Value 2 must be an integer.")
    
    return value1 - value2

def multiply(value1, value2):
    if not isinstance(value1, int):
        raise TypeError("Value 1 must be an integer.")
    if not isinstance(value2, int):
        raise TypeError("Value 2 must be an integer.")
    
    return value1 * value2

def divide(value1, value2):
    if not isinstance(value1, int):
        raise TypeError("Value 1 must be an integer.")
    if not isinstance(value2, int):
        raise TypeError("Value 2 must be an integer.")
    if value1 == 0 and value2 == 0:
        raise ValueError("Cannot divide zero by zero.")
    
    return value1 / value2
