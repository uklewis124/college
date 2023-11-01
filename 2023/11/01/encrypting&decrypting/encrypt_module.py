
letter_to_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

number_to_letter = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
            15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def main():
    """
    Main function that prompts the user to choose between encryption and decryption.
    """
    while True:
        try:
            user_input = input("Encrypt or Decrypt? (E/D): ")
            if user_input == "E":
                encrypt()
            elif user_input == "D":
                decrypt()
            else:
                print("Invalid input.")
                main()
        except ValueError as e:
            print("Invalid input.")
            print(e)

def encrypt(word=""):
    """
    Function that encrypts a message entered by the user.
    """
    # Checks if the user has entered a word to encrypt, if not it asks for one
    word_to_encrypt = ""
    if word == "":
        word_to_encrypt = input("Enter message to encrypt: ")
    else:
        word_to_encrypt = word

    """
    Ignore word error, it is not detecting the change in word_to_encrypt
    """
    # encrypted string will always start with the first letter of the word
    encrypted_word = word_to_encrypt[0]
    # Each loop needs to use the previously encrypted letter when adding-
    # on the first loop, this is just the first letter of the original word
    encrypted_letter = word_to_encrypt[0]
    # Loop through all the letters in the word except from the first letter (starting at index 1)
    for x in range(1, len(word_to_encrypt)):
        #get the current letter as a number
        number_one = letter_to_number[word_to_encrypt[x]]
        number_two = letter_to_number[word_to_encrypt[x-1]]
        encrypted_number = number_one + number_two
        #wrap around if the number is greater than 26 so that is Z + 1 = A
        if encrypted_number > 26:
            encrypted_number -= 26
        # Get the letter from the number for this encrypted letter
        encrypted_letter = number_to_letter[encrypted_number]
        # Add this encrypted letter to our final word string
        encrypted_word += encrypted_letter
    print("Encrypted message: " + encrypted_word)
    return encrypted_word

def decrypt(word=""):
    word_to_decrypt = ""
    if word == "":
        word_to_decrypt = input("Enter message to decrypt: ")
    else:
        word_to_decrypt = word

    word = word_to_decrypt.lower()
    encrypted_word = word[0]
    encrypted_letter = word[0]
    
    for x in range(len(word)-1, 0, -1):
        number_one = letter_to_number[word[x]]
        number_two = letter_to_number[word[x-1]]
        encrypted_number = number_one - number_two
        if encrypted_number < 1:
            encrypted_number += 26
            print(f"Encrypted number {encrypted_number - 26} has been wrapped around to {encrypted_number}")
        encrypted_letter = number_to_letter[encrypted_number]
        encrypted_word += encrypted_letter
    print("Decrypted message: " + encrypted_word)
    return encrypted_word

if __name__ == "__main__":
    main()

