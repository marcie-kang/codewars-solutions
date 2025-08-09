"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters
"""

def kebabize(st):
    string_filtered = ''.join(filter(lambda x: not x.isdigit(), st))
    first_idx = 0
    last_idx = 0
    stack = []

    for i, alp in enumerate(string_filtered):
        if alp.isupper():
            stack.append(string_filtered[first_idx:i].lower())
            first_idx = i

        if i == len(string_filtered) - 1:
            stack.append(string_filtered[first_idx:].lower())

    return "-".join(stack).strip("-")
