"""
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    copied_arr = source_array
    odds = [(index, num) for index, num in enumerate(copied_arr) if num % 2 != 0]
    sorted_arr = sorted(odds, key=lambda x: x[1])

    for index in range(len(sorted_arr)):
        copied_arr[odds[index][0]] = sorted_arr[index][1]

    return copied_arr
