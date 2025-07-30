"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""
#second answer
def valid_braces(string):
    stack = []
    braces = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for char in string:
        if char in braces.keys():
            stack.append(char)
        else:
            if len(stack) == 0 or braces[stack.pop()] != char:
                return False

    return len(stack) == 0

#first answer
def valid_braces(string):
    characters = ["()", "[]", "{}"]
    count = len(string) / 2
    copied = string

    while count:
        for character in characters:
            if character in copied:
                copied = copied.replace(character, "")

        count -= 1

    return True if len(copied) == 0 else False
