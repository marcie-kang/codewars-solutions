"""
Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""

def to_weird_case(words):
    arr = words.split()
    answer = []

    for word in arr:
        new_word = ""

        for idx in range(len(word)):
            if idx % 2 == 0:
                new_word += word[idx].upper()
            else:
                new_word += word[idx].lower()

        answer.append(new_word)

    return " ".join(answer)
