import pandas as pd
import os


def dataframe_selection():
    dataframe_input = input('What csv do you want to use? ')
    if dataframe_input in csvs_directory: # If the csv inputted is in the csvs_directory list
        print(f"You have selected {dataframe_input}. This dataframe is available.")
        file = csv_parent + '/' + dataframe_input + '.csv' # Creates the file path for the csv
        return file  # Returns the file path
    else:
        print(f"You have selected {dataframe_input}. This dataframe is not available.")
        print("Please select a different dataframe.")


def corr_check(df, compare_1, compare_2):
    subset = df[[compare_1, compare_2]]
    corr = subset.corr()
    print(f"{compare_1} vs. {compare_2}")
    
    if(corr[compare_1][compare_2]) == 1:
        print(f"The correlation between your {compare_1} and {compare_2} is perfect!")
        print(f"As the {compare_1} increases, so does the {compare_2}. Always")

    elif(corr[compare_1][compare_2]) > 0.5:
        print(f'The correlation between {compare_1} and {compare_2} is notable.')
        print(f'As the {compare_1} increases, so does the {compare_2}, usually.')

    elif(corr[compare_1][compare_2]) == 0:
        print(f"The corelation between {compare_1} and {compare_2} does not exist.")
        print(f"{compare_1} and {compare_2} have no correlation")

    elif(corr[compare_1][compare_2]) == -1:
        print(f"The correlation between your {compare_1} and {compare_2} is perfect!")
        print(f"As the {compare_1} increases, the {compare_2} decreases. Always.")

    elif(corr[compare_1][compare_2]) < -0.5:
        print(f"The correlation between {compare_1} and {compare_2} is notable.")
        print(f"As the {compare_1} increases, the {compare_2} decreases, sometimes.")

    elif(corr[compare_1][compare_2]) > -0.5 and (corr[compare_1][compare_2]) < 0:
        print(f"The correlation between {compare_1} and {compare_2} is not notable.")
        print(f"As the {compare_1} increases, the {compare_2} decreases, sometimes.")

    elif(corr[compare_1][compare_2]) < 0.5 and (corr[compare_1][compare_2]) > 0:
        print(f"The correlation between {compare_1} and {compare_2} is not notable.")
        print(f"As the {compare_1} increases, the {compare_2} increases, sometimes.")

    return corr[compare_1][compare_2]


pd.set_option('display.max_rows', None) # Displays all rows
csv_parent = '2023/10/12/res' # The directory where the csvs are stored
csvs = os.listdir(csv_parent) # Lists all the csvs in the directory
csvs_directory = [] # Creates an empty list
for csv in csvs: # For every csv in the csvs list
    if csv.endswith('.csv'): # If the csv ends with .csv (checks file is actually a csv)
        csv = str(csv.split('.csv')[0]) # Removes the .csv from the csv name for display purposes
        print(csv)
        csvs_directory.append(csv) # Adds the csv to the csvs_directory list

dataframe = dataframe_selection() # Runs the dataframe_selection function
df = pd.read_csv(dataframe)
print(df.columns)
object_1_selected = False
object_2_selected = False
banned_objects = ['model', 'transmission', 'fuelType']
while not object_1_selected:
    object_1 = input('What is the first object you want to compare? ')
    if object_1 in df.columns:

        if object_1 in banned_objects:
            print(f'You cannot compare a {object_1} to numbers. Please select a different object.')
            object_1_selected = False
        else:
            object_1_selected = True
            # DEBUG print('DEBUG: ', 'The object1 is in the dataframe')
    else:
        print('Please select a different object.')
while not object_2_selected:
    object_2 = input('What is the second object you want to compare? ')
    if object_2 == object_1:
        print('You cannot compare an object to itself. Please select a different object.')
        object_2_selected = False
        pass
    if object_2 in df.columns:
        if object_2 in banned_objects:
            print(f'You cannot compare a {object_1} to numbers. Please select a different object.')
            object_2_selected = False
        else:
            object_2_selected = True
            # DEBUG print('DEBUG: ', 'The object2 is in the dataframe')

    else:
        print('Please select a different object.')
# DEBUG print('DEBUG: ', 'df collection complete')
ret = corr_check(df, object_2, object_1)
# DEBUG print('DEBUG: ', 'The retention value is', ret)
