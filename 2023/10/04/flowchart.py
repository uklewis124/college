mark = int(input("Enter your mark: "))
if mark < 0:
    print("Warning mark is too low")
elif mark > 50:
    print("Warning mark is too high")
else:
    paper = input("Which paper did they sit? ")
    if paper.upper() == "A":
        score = mark * 5
    elif paper.upper() == "B":
        score = mark * 3
    print("thier score is: ", score)
