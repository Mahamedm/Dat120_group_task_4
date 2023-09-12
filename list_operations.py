# This file is a collection of functions for list oparations.
# Any other work, need to be done in a diffrent file. 
# lst = list variables.

# (task d) counts wether a value is equal or greater than a numbers in a list.
# returns the amount of numbers that satisfy the parameter.
def count_greater_equal(lst, value):
    count = 0
    for num in lst:
        if num >= value:
            count += 1
    return count

# TODO: (task e)



