"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
"""

def find_missing_letter(chars):
    answer = [chr(ord(chars[idx]) + 1) for idx in range(len(chars) - 1) if ord(chars[idx]) + 1 != ord(chars[idx + 1])]

    return answer[0]
