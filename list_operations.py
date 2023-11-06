# This file is a collection of functions for list oparations.
# Any other work, need to be done in a diffrent file. 
# lst = list variables.

import csv
from datetime import datetime

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
# task b (function)

# Usage:
# You need to pass the correct indexes for snow depth and date from your csv data structure
def count_skiable_days_per_season(weather_data, snow_depth_index, date_index, skiing_depth_threshold=20):
    # Initialize a dictionary to hold the count of skiable days per season
    skiable_days_per_season = {}

    # Skip the header row
    for entry in weather_data[1:]:  #the first row is the header
        date_str = entry[date_index]
        snow_depth = entry[snow_depth_index]

        # Skip entries with missing snow depth data
        if snow_depth == '-' or snow_depth == '':
            continue

        # Convert snow depth to an integer
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
        skiable_days_count[season] = count_greater_equal(depths, skiing_depth_threshold)

    return skiable_days_count


