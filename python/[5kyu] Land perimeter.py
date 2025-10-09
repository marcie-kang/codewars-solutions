"""
Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']
which represents:

should return: "Total land perimeter: 24".

Following input:

['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']
which represents:

should return: "Total land perimeter: 18"
"""

def land_perimeter(arr):
    rows = len(arr)
    cols = len(arr[0])
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == "X":

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    is_in_bounds = (0 <= nr < rows) and (0<= nc < cols)

                    if not is_in_bounds:
                        perimeter += 1
                    elif arr[nr][nc] == "O":
                        perimeter += 1

    return f"Total land perimeter: {perimeter}"
