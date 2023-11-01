# Import OS to join directories
import os
# Importing previous task so i dont have to program it again.
import task1
user = task1.user
print(f"Hello {user.name}.")
letter_path = "2023/11/01/reading from files/letters"
def new_letter(name):
    ret = os.path.join(f"{letter_path}/{name}")
    return ret
letter = new_letter(user.name)
money_won = 20
new_letter = open(letter, 'w')
new_letter.write(f"Hello, {user.name},\n")
new_letter.write(f"You have won: {money_won}\n")
new_letter.write("Congratulations on winning the lottery!")
new_letter.close()