"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    answer = [[num for num in range(1, size + 1)]]
    count = 2

    while count <= size:
        multiples = []

        for i in answer[0]:
            multiples.append(i * count)

        answer.append(multiples)
        count += 1

    return answer
