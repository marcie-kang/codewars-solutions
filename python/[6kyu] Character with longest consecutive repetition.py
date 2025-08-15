"""
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
Happy coding! :)
"""

def longest_repetition(chars):
    if not chars:
        return ("", 0)

    max_char = ""
    max_count = 0
    current_char = ""
    current_count = 0

    for char in chars:
        if char == current_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = current_char

            current_char = char
            current_count = 1

    if current_count > max_count:
        max_count = current_count
        max_char = current_char

    return (max_char, max_count)
