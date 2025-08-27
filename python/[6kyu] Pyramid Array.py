"""
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]
"""

def pyramid(n):
    if n == 0:
        return []

    count = 0
    answer = []

    while count < n:
        count += 1
        sub_arr = [1] * count
        answer.append(sub_arr)

    return answer
