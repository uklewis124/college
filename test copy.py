import os
import time
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)



alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(alphabet)

os.system('clear')

alphabet_new = []  # Will become decrypted alphabet

for index, char in enumerate(alphabet):
    print(char)
    os.system('clear')
    try:
        temp3 = alphabet[index + 2]
        alphabet_new.append(temp3)
    except IndexError:
        if char == "y":
            alphabet_new.append("a")
        elif char == "z":
            alphabet_new.append("b")

print(alphabet_new)

thing_to_decrypt = "map"

for char in thing_to_decrypt:
    if char in alphabet:
        print(alphabet_new[alphabet.index(char)], end="")
    else:
        print(char, end="")
