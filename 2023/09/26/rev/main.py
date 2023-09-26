# Main File (That the user will run)

# Imports
import pandas as pd
import pandas_functions as pf
#Variables
path = "/workspaces/college/2023/09/26/rev/aircrashesFullData.csv"

# Main Function
def main():
    print("Hello World!")
    df = pf.read_csv(path)
    pf.print_df(df)
    
    ## Adds sum of all casualties and assigns to variable
    total_casualties = df["Fatalities"].sum()
    print("Total Casualties starting from 1908: " + str(total_casualties))
    
    ## Adds sum of all casualties from 2007 and onwards to variable
    total_casualties_2007 = df.loc[df["Year"] >= 2007, "Fatalities"].sum()
    print("Total Casualties starting from 2007: " + str(total_casualties_2007))
    
    ## Grabs manufacturer with most crashes
    manufacturer = df["AircraftManufacturer"].value_counts().idxmax()
    print("Manufacturer with most crashes: " + manufacturer)
    
    ## Grabs manufacturer with most crashes from 2007 and onwards
    manufacturer_2007 = df.loc[df["Year"] >= 2007, "AircraftManufacturer"].value_counts().idxmax()
    print("Manufacturer with most crashes from 2007: " + manufacturer_2007)
    
    ## Grabs all aircraft, puts them in seperate series, then prints the series
    aircraft = df["Aircraft"].value_counts()
    aircraft_series = pd.Series(aircraft, name="Aircraft")
    print(aircraft_series)
    # Finds out how many of each aircraft there are with the same name
    aircraft_count = aircraft_series.value_counts()
    print(aircraft_count)
    #Prints head of aircraft series
    print(aircraft_series.head())
    
    # Works out percentages of aircraft that crashed, instead of value to account for different amounts of aircraft
    aircraft_percentages = aircraft_series / aircraft_series.sum() * 100
    print(aircraft_percentages.head())
    
    total_b737 = 11112
    #Works out percentage of existing b737 that crashed
    b737_percentage = aircraft_series["Boeing B 737"] / total_b737 * 100
    print(b737_percentage,"% of all B737s have crashed")
    
    #Works out percentage of existing b737 that crashed from 2007 and onwards
    b737_percentage_2007 = df.loc[df["Year"] >= 2007, "Aircraft"].value_counts()["Boeing B 737"] / total_b737 * 100
    print(b737_percentage_2007,"% of all B737s have crashed from 2007 onwards")
    
    

# Run Main Function
if __name__ == "__main__":
    main()