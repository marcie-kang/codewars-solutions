"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    index = 0

    for i in range(len(strng) - 1, -1, -1):
        if not strng[i].isdigit():
            index = i + 1
            break

    if index == len(strng):
        return strng + "1"

    num = (str(int(strng[index:]) + 1)).zfill(len(strng[index:]))

    return strng[:index] + num
