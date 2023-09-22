# Field to test the functions
from list_operations import *
# lister_for_del_1.py:
temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
dogn_nedbor = [2, 5, 0, 0, 0, 3, 6, 4, 0, 0, 5, 0, 12, 12, 12, 12, 7, 19]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

# Task J
temperaturer, task_i_diffrence_print= [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2],[]
task_i_differences = calculate_differences(temperaturer)
for i in task_i_differences:
    if i < 0:
        task_i_diffrence_print.append(str(f"{i} -falling"))
    else:
        task_i_diffrence_print.append(str(f"{i} -rising"))    

print("i: Differences between consecutive numbers:", task_i_diffrence_print)

# task K
trend =calculate_trend(temperaturer_tidspunkter,temperaturer)[0]
print("K: The trend of Temperaturer is:",trend)
if (trend>0):
    print("K: The trend is rising")
elif (trend<0):
    print("K: The trend is decreasing")
else:
    print("There is no trend")

# task M
print(f"M: longest perion without precipitation is: {longest_continuous_sequence_of_zeros(dogn_nedbor)} days")

