'''Learning Matplotlib'''
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Preparing data
dataframe = pd.read_csv("2023/10/09/Student Performance.csv")
# Defining columns
studentid = dataframe["STUDENT ID"]
age = dataframe["1"].astype(int)  # 1:18-21 2:22-25 3:above 25
sex = dataframe["2"].astype(int)
graduation = dataframe["3"].astype(int)  # 1:Private, 2:State, 3:Other
scholarship = dataframe["4"].astype(int)  # 1:None, 2:25%, 3:50%, 4:75%, 5:Full
work = dataframe["5"].astype(int)  # 1: Yes, 2: No
regular_sport_art = dataframe["6"].astype(int)  # 1: Yes, 2: No
partner = dataframe["7"].astype(int)  # 1:Yes, 2:No
salary = dataframe["8"].astype(int)
# salary USD 1:135-200, 2:201-70, 3:271-340, 4:341-410, 5:above 410
transport = dataframe["9"].astype(int)
# transport 1:Bus, 2: Private car/taxi, 3: Bike, 4: Other
accomodation = dataframe["10"].astype(int)
# 1:Rental, 2:Dorm, 3:Family, 4:Other
mothers_education = dataframe["11"].astype(int)
# 1:Primary, 2:Secondary, 3:High School, 4:University, 5:MSc, 6:PhD
fathers_education = dataframe["12"].astype(int)
# 1:Primary, 2:Secondary, 3:High School, 4:University, 5:MSc, 6:PhD
num_of_siblings = dataframe["13"].astype(int)  # 1-5
parental_status = dataframe["14"].astype(int)  # 1:Married, 2:Divorced, 3:Widow
mothers_occupation = dataframe["15"].astype(int)
# 1:Retired, 2:Housewife, 3:Government, 4:Private, 5:Self-employed, 6:Other
fathers_occupation = dataframe["16"].astype(int)
# 1:Retired, 2:Housewife, 3:Government, 4:Private, 5:Self-employed, 6:Other
study_hours = dataframe["17"].astype(int)
# 1:None 2:<5hrs 3:6-10hrs 4:11-20hrs 5:>20hrs
reading_freqency = dataframe["18"].astype(int)  # 1:None 2:Sometimes 3:Often


# Plotting
x = sex
y = age

# Preparing data
age_1 = 0
age_2 = 0
age_3 = 0
for i in x:
    if i == 1:
        age_1 += 1
    elif i == 2:
        age_2 += 1
    elif i == 3:
        age_3 += 1
print(age_1, age_2, age_3)
y = np.array(age_1, age_2, age_3)
print(y)
plt.bar(x, y)

# Labeling
plt.title("Cyprus Education")
plt.xlabel("Sex")
plt.ylabel("Age")

# Do not delete this line
plt.savefig("2023/10/09/matplotlib_output.png")
