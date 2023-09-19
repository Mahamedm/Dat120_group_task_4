# Field to test the functions
from list_operations import *

# Task E

numbers = [1, 3, 7, 12, 20, 25]
differences = calculate_differences(numbers)
print("E: Differences between consecutive numbers:", differences)

# optional
data = [10, 15, 20, 25, 30, 35, 40, 45, 50]
e = 2  # Number of elements for averaging(current data point + the two next data points)
moving_avg = calculate_moving_averages(data, e)
derivative = calculate_derivative_of_averages(moving_avg)
print("E: Moving Averages:", moving_avg)
print("E: Numerical Derivative of Averages:", derivative)


# task F 
numbers = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
print("F: Length of longest sequence of 0s:", longest_continuous_sequence_of_zeros(numbers))

# optional 
integers =  [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19] #[2, 2, 2, 4, 4, 4, 4, 1, 1, 2, 2, 2, 2, 2]
length, value = longest_sequence_of_same_value(integers)
print(f"F: Length of longest sequence of {value}s:", length)

