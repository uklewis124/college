from colorama import Fore, Style, Back
import os


def color_example():
    possible_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    count = 0
    while count < len(possible_colors):
        print(possible_colors[count] + f'Loading Color Libary! {count}')
        count += 1
    count = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


clear()

# ### Ready for the real code now ###
def cycle():
    # Beginning of cycle of decryption

    # First, just printing every line of the file and adding it to a list
    lines_of_text = []
    file = '2023/12/Advent_Of_Code/day1_part2/day1_test_input_2.txt'
    with open(file, 'r') as open_file:
        for line in open_file:
            line = line.strip('\n')
            lines_of_text.append(line)
    finalised_lines = []

    # Second, Grabbing every number in each line and adding it to a list
    possible_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    possible_str_numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i,line in enumerate(lines_of_text):
        real_line = []
        numbers_in_line = []
        # Grabbing all int numbers in the line
        for letter in line:
            if letter in possible_numbers:
                numbers_in_line.append(int(letter))

        # Grabbing all str numbers in the line
        new_line = line
        for num in possible_numbers:
            if num in new_line:
                new_line = new_line.replace(num, "")
        print(new_line)
        possible_new_line = line
        for possible in possible_str_numbers:
            if possible in new_line:
                possible_new_line = possible_new_line.replace(possible, "")
        finalised_lines.append(numbers_in_line)
"""
    print(finalised_lines)

    # Third, Grabbing first and last number in each line and adding it to a list
    # If only one number in the line, then that number is both the first and last number
    new_finalised_lines = []
    for line in finalised_lines:
        if len(line) == 1:
            new = f"{line[0]}{line[0]}"
            new = int(new)
            line = new
        elif len(line) == 2:
            # Keeping a list with 2 nums the same, and joining them together
            new = f"{line[0]}{line[1]}"
            line = int(new)
        else:
            # For a list with more than 2 nums, grab first and last num
            first = line[0]
            last = line[-1]
            new = f"{first}{last}"
            line = int(new)
        new_finalised_lines.append(line)
    print(new_finalised_lines)

    # Fourth, Adding all the numbers together
    total = 0
    for line in new_finalised_lines:
        total += line
    
    print(total)
"""

cycle()
