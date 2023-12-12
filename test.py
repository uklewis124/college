import os
import time
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)


alphabet_lower = [chr(i) for i in range(ord('a'), ord('z') + 1)]
alphabet_higher = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


file = open("input.txt", "r").read()
temporary_list = []
for char in file:
    if char in alphabet_lower:
        temporary_list.append(alphabet_lower.index(char) + 1)
    elif char in alphabet_higher:
        temporary_list.append(alphabet_higher.index(char) + 1)
    else:
        temporary_list.append(char)

print(temporary_list)