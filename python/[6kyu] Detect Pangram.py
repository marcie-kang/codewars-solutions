"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def is_pangram(st):
    sentence = st.lower()
    arr = set()

    for char in sentence:
        if ord(char) >= 97 and ord(char) <= 122:
            if ord(char) not in arr:
                arr.add(ord(char))

    return True if len(arr) == 26 else False
