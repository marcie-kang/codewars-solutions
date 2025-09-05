"""
Given a string, return a new string that has transformed based on the input:

Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
Note: You will have to handle multiple spaces, and leading/trailing spaces.

For example:

"Example Input" ==> "iNPUT eXAMPLE"
You may assume the input only contain English alphabet and spaces.
"""

def string_transformer(s):
    answer = []

    for word in s.split(" "):
        converted = ""

        for char in word:
            if char.isupper():
                converted += char.lower()
            else:
                converted += char.upper()

        answer.append(converted)

    return " ".join(answer[::-1])
