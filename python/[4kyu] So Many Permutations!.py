"""
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
Note: The order of the permutations doesn't matter.

Good luck!
"""

def permutations(s):
    if len(s) <= 1:
        return [s]

    result = set()

    for i in range(len(s)):
        fixed = s[i]
        rest = s[:i] + s[i + 1:]
        for p in permutations(rest):
            result.add(fixed + p)

    return result
