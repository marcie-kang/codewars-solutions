"""
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

def count(s):
    answer = {}

    for char in s:
        answer[char] = answer.get(char, 0) + 1

    return answer
