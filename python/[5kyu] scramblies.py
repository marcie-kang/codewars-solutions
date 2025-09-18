"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""

from collections import Counter

def scramble(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)

    for k, v in c2.items():
        if not k in c1 or c1[k] < c2[k]:
            return False

    return True
