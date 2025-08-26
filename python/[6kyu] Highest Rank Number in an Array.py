"""
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""
#second solution
from collections import Counter

def highest_rank(arr):
    if arr:
        c = Counter(arr)
        m = max(c.values())
        return max(k for k,v in c.items() if v==m)

#first solution
def highest_rank(arr):
    dict = {}

    for num in arr:
        if num in dict:
            dict[num] += 1
        else:
            dict[num] = 1

    sorted_dict = sorted(dict.items(), key=lambda kv: (kv[1], kv[0]))

    return sorted_dict[-1][0]
