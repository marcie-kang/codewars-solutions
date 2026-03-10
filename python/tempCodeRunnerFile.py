def move_zeros(lst):
    zeros = []
    for num in lst:
        if num == 0:
            lst.pop()
            zeros.append(0)

    return lst + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))