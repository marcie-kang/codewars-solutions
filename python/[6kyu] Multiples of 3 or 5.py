"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
"""

def solution(number):
    answer = 0

    if number < 0:
        return answer

    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            answer += num

    return answer
