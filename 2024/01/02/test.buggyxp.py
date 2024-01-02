def assert_method():
    import buggyxp as bx  # Import BuggyXP Library
    try:
        from colorama import Fore
    except ImportError:
        import os
        os.system("pip install colorama")
        try:
            from colorama import Fore
        except ImportError:
            quit("Please install colorama using 'pip install colorama'")

    for i in range(1000):
        for x in range(1000):
            try:
                print(Fore.RED)
                assert bx.add(i, x) == i + x, print("Addition Failed, Log: ", i, x, "Output: ", bx.add(i, x))
                assert bx.subtract(i, x) == i - x, print("Subtraction Failed, Log: ", i, x, "Output: ", bx.subtract(i, x))
                assert bx.multiply(i, x) == i * x, print("Multiplication Failed, Log: ", i, x, "Output: ", bx.multiply(i, x))
                if i != 0 and x != 0:
                    assert bx.divide(i, x) == 0, print("Division Failed, Log: ", i, x, "Output: ", bx.divide(i, x))
                else:
                    print("Division Failed, Log: ", i, x, "Output: ", bx.divide(i, x))
            except:
                NotImplemented

# assert_method()
import os
os.system("cls" if os.name == "nt" else "clear")

class Fuzzer:
    def __init__(self):
        try:
            import buggyxp as bx  # Import BuggyXP Library
            import random
            self.bx = bx
            self.random = random
            self.error_found = []
        except ImportError:
            quit()
        finally:
            self.does_add_word()


    def does_add_word(self):  # Added self parameter
        try:
            for i in range(0, 1000):
                for x in range(0, 1000):
                    assert self.bx.add(i, x), self.error_found.append(f"Division Failed, i = {i}, x = {x}, output = {self.bx.add(i,x)}")  # Access bx using self
        except:
            

my_fuzzer = Fuzzer()
