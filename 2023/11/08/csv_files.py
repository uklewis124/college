import os

crashes = {}
with open('2023/11/08/Motor_Vehicle_Collisions.csv', 'r', encoding='utf-8') as crash_file:
    records = crash_file.readlines()
    for record in records:
        record = record.strip()
        fields = record.split(',')
        crashes[fields[0]] = (fields[1:])
print(crashes)

"""os.system('clear')

crash_tol = 0
for i in range(0, len(crashes)):
    crash_tol += 1

print(f"There have been {crash_tol} crashes recorded in NYC since 2012.")
print(f"The first collision recorded was on {crashes['CRASH DATE'][0]} at {crashes['CRASH TIME'][0]}.")
print(f"The most recent collision recorded was on {crashes['CRASH DATE'][-1]} at {crashes['CRASH TIME'][-1]}.")"""