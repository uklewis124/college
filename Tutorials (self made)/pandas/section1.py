# The user writes the code here, they then run the tutorial and the tutorial program checks if the code is correct.
# The tutorial program will then give the user a score based on how many of the tests they pass.
import sys
tutorial = '/workspaces/college/Tutorials (self made)/tutorial.py'
import tutorial
def main():
    print("You are running section1.py. Try running tutorial.py instead.")
    sys.exit()
    
def check():
    result1 = tutorial.section1()
    if result1 == "1":
        print("Correct!")
    else:
        print("Incorrect.")
    
if __name__ == "__main__":
    main()