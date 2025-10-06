"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.
"""

from collections import Counter

def find_uniq(arr):
    char_sets = []

    for word in arr:
        unique_chars = sorted(list(set(word.upper())))
        char_sets.append("".join(unique_chars))

    counts = Counter(char_sets)
    unique_set_str = None

    for char_set_str, count in counts.items():
        if count == 1:
            unique_set_str = char_set_str
            break

    if unique_set_str:
        for word in arr:
            if "".join(sorted(list(set(word.upper())))) == unique_set_str:
                return word

    return None
