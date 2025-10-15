"""
You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

Examples
[]                   -->  0
[1, 2, 3]            -->  3
["x", "y", ["z"]]    -->  4
[1, 2, [3, 4, [5]]]  -->  7
"""

def deep_count(a):
    total_count = len(a)

    for element in a:
        if type(element) == list:
            total_count += deep_count(element)

    return total_count
