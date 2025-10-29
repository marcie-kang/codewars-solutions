"""
Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number

Examples:

N = 3 Output: [[1,2,3],[8,9,4],[7,6,5]]

1    2    3
8    9    4
7    6    5
N = 4 Output: [[1,2,3,4],[12,13,14,5],[11,16,15,6],[10,9,8,7]]

1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
N = 5 Output: [[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]]

1   2   3   4   5
16  17  18  19  6
15  24  25  20  7
14  23  22  21  8
13  12  11  10  9
"""

def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []

    spiral = [[0] * n for i in range(n)]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    row, col, current_direction = 0, 0, 0

    for num in range(1, n * n + 1):
        spiral[row][col] = num

        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

        if (next_row < 0 or next_row >= n or
            next_col < 0 or next_col >= n or
            spiral[next_row][next_col] != 0):

            current_direction = (current_direction + 1) % 4

            next_row = row + directions[current_direction][0]
            next_col = col + directions[current_direction][1]

        row = next_row
        col = next_col

    return spiral
