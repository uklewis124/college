import random

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(myList)


# Sorting starts here
def BubbleSort(myList):
    sorted = False
    length = len(myList)
    while sorted == False:
        for i in myList:
            for i in range(0,length-1):
                if myList[i-1] > myList[i]:
                    tempVal = myList[i-1]
                    myList[i-1] = myList[i]
                    myList[i] = tempVal
                    print("Number Swapped")
                elif myList[i-1] < myList[i] or myList[i-1] == myList[i]:
                    print("Number remains as is")
                else:
                    sorted = True
    return myList
    

print("Sorted")
print(BubbleSort(myList))