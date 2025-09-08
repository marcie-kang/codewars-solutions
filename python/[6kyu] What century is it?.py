"""
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.

Examples
"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""

def what_century(year):
    if year[2:] == "00":
        current = year[0:2]
    else:
        current = str(int(year[0:2]) + 1)

    if current[-1] == "1" and current[0] != "1":
        return f"{current}st"
    elif current[-1] == "2" and current[0] != "1":
        return f"{current}nd"
    elif current[-1] == "3" and current[0] != "1":
        return f"{current}rd"
    else:
        return f"{current}th"
