"""
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""


def spin_words(sentence):
    words = sentence.split()

    for num in range(len(words)):
        if len(words[num]) > 4:
            words[num] = words[num][::-1]

    return " ".join(words)
