"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

def prime_factors(n):
    divider = 2
    current = n
    result = ""

    while current > 1:
        divider_count = 0

        if current % divider == 0:
            while current % divider == 0:
                divider_count += 1
                current /= divider

            if divider_count >=2:
                result += f"({divider}**{divider_count})"
            else:
                result += f"({divider})"

        if divider * divider > current and current > 1:
            result += f"({int(current)})"
            break

        divider += 1

    return result
