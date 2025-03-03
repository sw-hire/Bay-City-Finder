import pandas as pd


#create homePrice dataframe
homePrice = pd.read_csv('home_price.csv', usecols = ['Year', 'City', 'Medprice'])
homePrice1 = homePrice.query('Year == 2021')
homePrice1 = homePrice1.drop(columns = ['Year'])
#print(homePrice)

#create commute dataframe
commuteType = pd.read_csv('commute_mode.csv', usecols = ['Year', 'City', 'Mode', 'Share'])
#filtering commute by time to match homePrice
commuteType1 = commuteType.query('Year == 2021')
commuteType1 = commuteType1.drop(columns = 'Year')
#print(commuteType)

#time dataframe
timeCommute = pd.read_csv('commute_time.csv', usecols = ['City', 'Mode', 'Avg_Commute_Time'])
timeCommute = timeCommute.query('Mode == "Overall"')
timeCommute = timeCommute.drop(columns = ['Mode'])
#print(timeCommute)

from tabulate import tabulate

def findcity (budget, choice, time, pref):
    temp_cities = pd.merge(pd.merge(homePrice1, commuteType1, on ='City', how ='outer'), timeCommute, on ='City', how ='outer')
    temp_cities.Share *= 100
    print(temp_cities.columns)
    #temp_cities['Mode'] = temp_cities['Mode'].str.strip().str.lower()

    # Assuming `pref` is the ranking string entered by the user (e.g., 'BMT')
    if pref[0] == "B":  # First priority is Budget
        if pref[1] == "M":  # Second priority is Mode
            # Budget > Mode > Time
            temp_cities = temp_cities.query('Medprice <= @budget')
            minTime = temp_cities['Avg_Commute_Time'].min()
            temp_cities = temp_cities.query('Mode == @choice')
            if time < minTime:
                temp_cities = temp_cities.sort_values(['Share', 'Avg_Commute_Time'], ascending=[False, True])
                print(
                    "Unfortunately, we were not able to find a city with average commute times in your ideal range.\nHowever, the following cities may meet your other criteria!")
            else:
                temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
                temp_cities = temp_cities.sort_values('Share', ascending=False)
                print("The following cities may meet your other criteria!")

        elif pref[1] == "T":  # Second priority is Commute Time
            # Budget > Time > Mode
            temp_cities = temp_cities.query('Medprice <= @budget')
            temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
            temp_cities = temp_cities.query('Mode == @choice')
            temp_cities = temp_cities.sort_values('Share', ascending=False)
            print("The following cities may meet your other criteria!")

    elif pref[0] == "M":  # First priority is Mode
        if pref[1] == "B":  # Second priority is Budget
            # Mode > Budget > Time
            temp_cities = temp_cities.query('Mode == @choice')
            temp_cities = temp_cities.query('Medprice <= @budget')
            minTime = temp_cities['Avg_Commute_Time'].min()
            if time < minTime:
                temp_cities = temp_cities.sort_values(['Share', 'Avg_Commute_Time'], ascending=[False, True])
                print(
                    "Unfortunately, we were not able to find a city with average commute times in your ideal range.\nHowever, the following cities may meet your other criteria!")
            else:
                temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
                temp_cities = temp_cities.sort_values('Share', ascending=False)
                print("The following cities may meet your other criteria!")

        elif pref[1] == "T":  # Second priority is Commute Time
            # Mode > Time > Budget
            temp_cities = temp_cities.query('Mode == @choice')
            temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
            temp_cities = temp_cities.query('Medprice <= @budget')
            temp_cities = temp_cities.sort_values('Share', ascending=False)
            print("The following cities may meet your other criteria!")

    elif pref[0] == "T":  # First priority is Commute Time
        if pref[1] == "B":  # Second priority is Budget
            # Time > Budget > Mode
            temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
            temp_cities = temp_cities.query('Medprice <= @budget')
            temp_cities = temp_cities.query('Mode == @choice')
            temp_cities = temp_cities.sort_values('Share', ascending=False)
            print("The following cities may meet your other criteria!")

        elif pref[1] == "M":  # Second priority is Mode
            # Time > Mode > Budget
            temp_cities = temp_cities.query('Avg_Commute_Time <= @time')
            temp_cities = temp_cities.query('Mode == @choice')
            minPrice = temp_cities['Medprice'].min()
            if budget < minPrice:
                temp_cities = temp_cities.sort_values(['Share', 'Medprice'], ascending=[False, True])
                print(
                    "Unfortunately, we were not able to find a city with a budget in your ideal range.\nHowever, the following cities may meet your other criteria!")
            else:
                temp_cities = temp_cities.query('Medprice <= @budget')
                temp_cities = temp_cities.sort_values('Share', ascending=False)
                print("The following cities may meet your other criteria!")
    else:
        print("Invalid ranking! Please enter a valid ranking (e.g., 'BMT', 'BTM', etc.).")

    headers = ["City", "Median Home Price", "Mode of Transportation", "Percent of Pop. Using Mode", "Avg. Commute Time"]
    print(tabulate(temp_cities, headers = headers, tablefmt="grid"))