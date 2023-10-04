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
    late = input("Was it handed in late? ")
    if late.lower() == "yes":
        score -= 10
    
    #Score is now calculated
    if score < 50:
        print("Fail")
    elif 70 > score >= 50:
        print("Grade C")
    elif 90 > score >= 70:
        print("Grade B")
    elif score >= 90:
        print("Grade A")
