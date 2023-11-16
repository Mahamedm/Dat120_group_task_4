# This file is a collection of functions for list oparations.
# Any other work, need to be done in a diffrent file. 
# lst = list variables.

import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import csv
import os


# Task D counts wether a value is equal or greater than a numbers in a list.
# returns the amount of numbers that satisfy the parameter.
def count_greater_equal(lst, value):
    count = 0
    for num in lst:
        if num >= value:
            count += 1
    return count

# (Part 1)Task E
# calculates the diffrence between a list of numbers.
def calculate_differences(lst):
    differences = []
    for i in range(len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        differences.append(diff)
    return differences


# optional 1

# calculates the numerical derivative of x y lists of value.
def calculate_numerical_derivative(x_values, y_values):
    derivatives = []
    for i in range(len(x_values) - 1):
        h = x_values[i + 1] - x_values[i]
        derivative = (y_values[i + 1] - y_values[i]) / h
        derivatives.append(derivative)
    return derivatives

# optional 2

# calculates moving avarage of a list.
# indexes to avarage in a list, is determined by e variable. 
def calculate_moving_averages(lst, e):
    averages = []
    for i in range(len(lst) - e):
        avg = sum(lst[i:i + e + 1]) / (e + 1)
        averages.append(avg)
    return averages

# finds the value diffrence of the moving avarages
def calculate_derivative_of_averages(averages):
    derivatives = []
    for i in range(len(averages) - 1):
        diff = averages[i + 1] - averages[i]
        derivatives.append(diff)
    return derivatives


# (Part 1)task F
# calculates the number of zeroes in a list
def longest_continuous_sequence_of_zeros(lst):
    max_length = 0 
    current_length = 0 

    for num in lst:
        if num == 0:
            current_length += 1 
            if current_length > max_length:
                max_length = current_length  
        else:
            current_length = 0

    return max_length

# optional 1

# calculates the number of same value in a list.
# returns both the most numerous item and the amnount of times it appears.
# usage: name, repeat = longest_sequence_of_same_value(list_of_sequence)
def longest_sequence_of_same_value(lst):
    max_length = 0  
    current_length = 1 
    longest_value = lst[0]
    current_value = lst[0]

    for i in range(1, len(lst)):
        if lst[i] == current_value:
            current_length += 1 
            if current_length > max_length:
                max_length = current_length 
                longest_value = current_value 
        else:
            current_value = lst[i] 
            current_length = 1

    return max_length, longest_value

# (Part 1)task G
# calculates the trend in two lists where one is for x-values and the other for y-values
# the function returns a and b which are parametres in the linear function: ax + b
def calculate_trend(x_value_list,y_value_list):
    n = len(x_value_list)
    sum_x = 0
    sum_y = 0
    a_upper=0
    a_lower=0
    for i in range(n):
        sum_x += x_value_list[i]
        sum_y += y_value_list[i]
    x_avg = sum_x/n
    y_avg = sum_y/n

    for i in range(n):
        a_upper +=(x_value_list[i]-x_avg)*(y_value_list[i]-y_avg)
        a_lower +=(x_value_list[i]-x_avg)*(x_value_list[i]-x_avg)

    a =a_upper/a_lower
    b = y_avg-a*x_avg

    if(len(x_value_list)==len(y_value_list)):
        return a, b

    else:
        print("Cannot calculate trend, the lists have different lengths")



# (Part 1)Task H 
def calculate_plantgrowth(temp_list):
    sum_growth = 0
    for temp in temp_list:
        if temp > 5:
            growth = (temp - 5) * 1
            sum_growth += growth
    return sum_growth

# Example of functionality:
# temp_list = [4, 7, 15]
# total_growth = calculate_plantgrowth(temp_list)
# print(total_growth)

################# PART 2 ##############
# task b, c and d (function)

# usage:
# pass the correct indexes for snow depth and date from the csv data structure.
def count_skiable_days_per_season(weather_data, snow_depth_index, date_index, skiing_depth_threshold=20, min_days=0):
    skiable_days_per_season = {}

    for entry in weather_data[1:]:  # the first row is the header
        date_str = entry[date_index]
        snow_depth = entry[snow_depth_index]

        # Skip any missing snow depth data
        if snow_depth == '-' or snow_depth == '':
            continue

        # convert snow depth to an integer
        snow_depth = int(snow_depth)

        # how i calculated the winter season:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        if 10 <= date_obj.month <= 12:
            season_year = date_obj.year  # october to December belongs to the start of the winter season
        else:
            season_year = date_obj.year - 1  # january to June belongs to the tail end of the winter season

        # if this season_year is not yet in the dictionary:
        if season_year not in skiable_days_per_season:
            skiable_days_per_season[season_year] = []

        # adding snow depth to the correct season
        skiable_days_per_season[season_year].append(snow_depth)

    # counting the skiable days for each season
    skiable_days_count = {}
    for season, depths in skiable_days_per_season.items():
        if len(depths) >= min_days: # number of days filter needed for task d
            skiable_days_count[season] = count_greater_equal(depths, skiing_depth_threshold)

    return skiable_days_count

# task e (function)
def filter_temp_data(weather_data,min_days=0):
    raw_years = {}

    for column in weather_data[1:]:
        temp_data = column[5]
        if temp_data == '-' or temp_data == '':
            continue

        year = int(column[2].split('.')[2])
        temp_data=float(temp_data.replace(',','.'))

        # Adding the temperature data to the appopriate key in the dict
        if year not in raw_years:
            raw_years[year] = [temp_data]
        else:
            raw_years[year].append(temp_data)

        # Filtering out the years the are too short
    filtered_years = {}
    for year in raw_years:
        if len(raw_years[year])>(min_days-1):
            filtered_years[year]=raw_years[year]
        
    return filtered_years

# task f) function
def find_dry_season(weather_data,min_days=0):
    raw_years = {}

    for column in weather_data[1:]:
        rain_data = column[4]
        if rain_data == '-' or rain_data == '':
            continue

        year = int(column[2].split('.')[2])
        rain_data=float(rain_data.replace(',','.'))

        if year not in raw_years:
            raw_years[year] = [rain_data]
        else:
            raw_years[year].append(rain_data)

    filtered_years = {}
    for year in raw_years:
        if len(raw_years[year])>(min_days-1):
            filtered_years[year]=raw_years[year]

    # Putting the filtered lists into the function from part 1
    for years in filtered_years:
        filtered_years[years]=longest_continuous_sequence_of_zeros(filtered_years[years])


    return filtered_years
# task h) function
def analyze_wind_data(data):
    valid_years = {}  

    
    for row in data[1:]:  
        try:
            year = int(row[2].split('.')[2])  
            wind_speed = float(row[7].replace(',', '.'))  

            if year not in valid_years:
                valid_years[year] = {'wind_speeds': []}

            valid_years[year]['wind_speeds'].append(wind_speed)
        except (ValueError, IndexError):
            
            pass

    
    valid_years = {year: data for year, data in valid_years.items() if len(data['wind_speeds']) >= 300}

    return valid_years

# task i) function
def calculate_monthly_averages(weather_data, temp_index, date_index):
    monthly_temps = defaultdict(list)

    for entry in weather_data[1:]:
        date_str = entry[date_index]
        temperature = entry[temp_index]

        if temperature == '-' or temperature == '':
            continue
        temperature = float(temperature.replace(',', '.'))
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        month_year = date_obj.strftime('%B %Y')

        monthly_temps[month_year].append(temperature)

    monthly_averages = {month: sum(temps) / len(temps) for month, temps in monthly_temps.items()}
    return monthly_averages

