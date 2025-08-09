"""
Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'
"""

def dashatize(n):
    s = str(abs(n))
    result = []

    for i, char in enumerate(s):
        digit = int(char)

        if digit % 2 != 0:
            result.append(f"-{char}-")
        else:
            result.append(char)

    result_str = "".join(result)
    result_str = result_str.replace("--", "-")
    result_str = result_str.strip("-")

    return result_str
