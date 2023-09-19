# This file is a collection of functions for list oparations.
# Any other work, need to be done in a diffrent file. 
# lst = list variables.

# Task D counts wether a value is equal or greater than a numbers in a list.
# returns the amount of numbers that satisfy the parameter.
def count_greater_equal(lst, value):
    count = 0
    for num in lst:
        if num >= value:
            count += 1
    return count

# Task E
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


# task F

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

# todo Task G

