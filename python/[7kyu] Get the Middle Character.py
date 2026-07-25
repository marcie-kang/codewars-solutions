"""
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""

def get_middle(s):
    if len(s) == 0 or len(s) == 1:
        return s

    middle = len(s) // 2

    if len(s) % 2 == 0:
        return s[middle - 1:middle + 1]
    else:
        return s[middle]
