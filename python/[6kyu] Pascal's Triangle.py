"""
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
where n denotes a row of the triangle, and k is a position of a term in the row.

You can read Wikipedia article on Pascal's Triangle for more information.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]

"""

def pascals_triangle(n):
    if n <= 0:
        return []

    result = []

    for i in range(n):
        current_row = [1] * (i + 1)

        if i > 1:
            previous_row = [result[j] for j in range(len(result) - i, len(result))]

            for j in range(1, i):
                current_row[j] = previous_row[j - 1] + previous_row[j]

        result += current_row

    return result
