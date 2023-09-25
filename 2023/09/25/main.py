#Calulate speed for program to run
import time
timenow = time.time()

for i in range(0,9999999):
    print(i)
    
timethen = time.time()
timetaken = timethen - timenow
print(timetaken)