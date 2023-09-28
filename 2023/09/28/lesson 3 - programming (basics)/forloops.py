'''
number = int(input("Enter a number: "))
print("The timestable for", number, "is:")
for i in range(1, 13):
    print(i, "x", number, "=", i * number)
'''

number_of_times = int(input("What number of timestables do you want to output? "))

for i in range(number_of_times):
    print("The times table of", i + 1, "is:")
    for item in range(number_of_times+1):
        print(item, "x", i+1, "=", item*(i+1))

print("END")