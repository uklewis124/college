leet_dict = {
"a":"4",
"b":"13",
"c":"(",
"d":"[)",
"e":"3",
"f":"|=",
"g":"6",
"h":"|-|",
"i":"|",
"j":".]",
"k":"|<",
"l":"1",
"m":"|Y|",
"n":"/\\/",
"o":"0",
"p":"|>",
"q":"0,",
"r":"|2",
"s":"5",
"t":"7",
"u":"[_]",
"v":"\\/",
"w":"\v/",
"x":"}{",
"y":"'/",
"z":"2",
}

def l33t_request():
    """
    Converts a string to l33t speak using the leet_dict dictionary.
    """
    user_input = input("Enter a string to convert to l33t speak: ")
    leet = ""
    for letter in user_input:
        if letter.lower() in leet_dict:
            leet = leet + leet_dict[letter.lower()]
        else:
            leet = leet + letter
    return leet
print(l33t_request())