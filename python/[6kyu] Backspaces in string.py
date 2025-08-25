"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""

def clean_string(s):
    answer = []

    for part in s:
        if part == "#" and len(answer) >= 1:
            answer.pop()
        elif part != "#":
            answer.append(part)

    return "".join(answer)
