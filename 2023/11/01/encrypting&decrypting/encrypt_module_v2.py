"""
Making my own encryption module.
"""
# Giving the letters values and values letters
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

# Defining encryption module
def encrypt(input_word):
    word = input_word.lower()
    # making sure sequence doesnt change first letter
    first_letter = word[0]
    encrypted_word = word[0]
    # Loop begins here to change letters to numbers
    for letter in range(1, len(word)):
        change_one = letter_to_number[word[letter]]
        change_two = letter_to_number[first_letter] # first letter because it doenst change, meaning it can be decrypted
        # adding the two numbers together
        new_third_letter_num = change_one + change_two
        if new_third_letter_num > 26:
            new_third_letter_num = new_third_letter_num - 26
            # Looping back from Z to A
        new_third_letter = number_to_letter[new_third_letter_num]
        encrypted_word = encrypted_word + new_third_letter
        print("sequential: " + encrypted_word)
    print(encrypted_word)

encrypt("encrypt")
"""
def decrypt(input_word):
    word = input_word.lower()
    first_letter = word[0]
    decrypted_word = ""
    # Loop begins here to change letters to numbers
    for letter in range(len(word)-1,0,-1): # Starts at the end of the word and goes backwards missing first letter
        
    
    
    decrypted_word = first_letter + decrypted_word

decrypt("hmttw")
"""