"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    arr = text.split(" ")
    answer = [arr[0]]

    for num in range(1, len(arr)):
        word = ""
        word = arr[num][0].upper() + arr[num][1:]
        answer.append(word)

    return "".join(answer)
