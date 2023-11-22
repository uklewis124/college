# Laser Maze by 101Computing.net - www.101computing.net/laser-maze/
import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def drawMaze():
    print("")
    print("    1 2 3 4 5 6 7 8 9 10")
    for i in range(0, 12):
        line = ""
        for j in range(0, 12):
            line = line + maze[i][j]
        if i > 0 and i < 10:
            print(" " + str(i) + line)
        elif i == 0 or i == 11:
            print("  " + line)
        elif i == 10:
            print("10" + line)

def placeBombs(numberOfBombs):
    for i in range(0, numberOfBombs):
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        maze[row][col] = "<>"


def placeReflectors():
    global maze
    numberOfReflectors = int(input("How many reflectors do you want to place? "))
    for i in range (0, numberOfReflectors):
        row = int(input(f"Please enter the row of the {i+1} reflector: "))
        col = int(input(f"Please enter the column of the {i+1} reflector: "))
        directionOfReflector = input(f"Please enter the direction of the {i+1} reflector: ")
        try:
            if directionOfReflector == "//":
                if maze[row][col] == "  ":
                    if maze[row][col].strip() != "<>":
                        maze[row][col] = "//"
                    else:
                        print("There is a bomb in this location.")
                else:
                    print("There is a wall in this location.")
            elif directionOfReflector == "\\\\":
                if maze[row][col] == "  ":
                    if maze[row][col].strip() != "<>":
                        maze[row][col] = "\\\\"
                    else:
                        print("There is a bomb in this location.")
                else:
                    print("There is a wall in this location.")
        except IndexError:
            print("That location is outside the maze.")

def shoot():
    global direction
    state = "shooting"
    row = source[0]
    col = source[1]

    placeReflectors()
    while state == "shooting":
        clear_screen()
        if direction == "right":
            col = col + 1
        ## Add code here to allow the laser to move in all 4 directions

        if maze[row][col] == "  ":
            print("")
            maze[row][col] = "++"
        elif maze[row][col] == "[]":
            print("Exit Gate Reached! Level Cleared!")
            state = "win"
        elif maze[row][col] == "<>":
            print("Laser beam hits a bomb! Game Over!")
            state = "lost"
        elif maze[row][col] == " |" or maze[row][col] == "| " or maze[row][col] == "--":
            print("Laser beam hits a wall! Game Over!")
            state = "lost"
        elif maze[row][col] == ">>":
            print("Laser beam hits its source! Game Over!")
            state = "lost"
        ## Add code here to redirect the laser in a different direction (top, right, bottom, left) when a reflector wall // or \\ is hit.
        
        drawMaze()
        time.sleep(0.2)

# Initialise maze, bombs, laser source, and exit gate
maze = [
    [" -", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "- "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
    [" -", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "- "]
]

source = (random.randint(1, 10), 0)
direction = "right"
maze[source[0]][source[1]] = ">>"

exit = (random.randint(1, 10), 11)
maze[exit[0]][exit[1]] = "[]"

placeBombs(3)
drawMaze()

## Collect inputs (row and column numbers) to find out where the user wants to point reflection walls: // and \\
## Add reflection walls to the maze as instructed by the user

shoot()
