FR_EN_Dictonary = {
    "Bonjour": "Hello",
    "Au Reviour": "Bye",
    "Oui": "Yes",
    "Non": "No",
    "Merci": "Thank You",
    "Et toi": "And you"
}

EN_FR_Dictionary = {
    "Hello": "Bonjour",
    "Bye": "Au Reviour",
    "Yes": "Oui",
    "No": "Non",
    "Thank You": "Merci",
    "And you": "Et toi"
}

language_choice = input("English (EN) or Français(FR): ").lower()
if language_choice == "english" or language_choice == "en":
    type = input("Translate from EN or FR: ")
    if type.upper() == "EN":
        while True:
            user_input = input("Enter a word in English: ")
            if user_input in EN_FR_Dictionary:
                print(f"The word '{user_input}' is '{EN_FR_Dictionary[user_input]}' in french.")
            else:
                print(f"Unfortunately, {user_input} is not yet in our dictionary.")
    elif type.upper() == "FR":
        while True:
            user_input = input("Enter a word in French: ")
            if user_input in FR_EN_Dictonary:
                print(f"The word {user_input} is {FR_EN_Dictonary[user_input]} in English.")
            else:
                print(f"Unfortunately the word {user_input} is not in our dictionary.")


elif language_choice.lower() == "français" or language_choice.lower == "french" or language_choice == "fr":
    print("Traduit via Google Translate.")
    while True:
        user_input = input("Entrez un mot français: ")
        if user_input in FR_EN_Dictonary:
            print(f"Le mot '{user_input}' est '{FR_EN_Dictonary[user_input]}' en anglais.")
        else:
            print(f"Malheureusement, {user_input} n'est pas dans notre dictionnaire.")
