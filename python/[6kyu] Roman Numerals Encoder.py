"""
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

In Roman numerals:

1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
2008 is written as 2000=MM, 8=VIII; or MMVIII.
1666 uses each Roman symbol in descending order: MDCLXVI.
Example:

   1 -->       "I"
1000 -->       "M"
1666 --> "MDCLXVI"
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

"""

def solution(n):
    ones_symbol = {"I": 1, "V": 5}
    tens_symbol = {"X": 10, "L": 50}
    hundreds_symbol = {"C": 100, "D": 500}
    thousands_symbol = {"M": 1000}

    converted_num = str(n)
    nums_list = []
    answer = ""

    for idx, num in enumerate(converted_num):
        numerical_units = 10 ** (len(converted_num) - idx - 1)
        nums_list.append(int(num) * numerical_units)

    for num in nums_list:
        target = 0

        if len(str(num)) == 4:
            while target != num:
                target += thousands_symbol["M"]
                answer += "M"
            continue
        elif len(str(num)) == 3:
            if num == 900:
                answer += "CM"
            elif num == 400:
                answer += "CD"
            elif num <= 300 and num >= 100:
                while target != num:
                    target += hundreds_symbol["C"]
                    answer += "C"
            elif num >= 500 and num <= 800:
                target += hundreds_symbol["D"]
                answer += "D"
                while target != num:
                    target += hundreds_symbol["C"]
                    answer += "C"
        elif len(str(num)) == 2:
            if num == 90:
                answer += "XC"
            elif num == 40:
                answer += "XL"
            elif num <= 30 and num >= 10:
                while target != num:
                    target += tens_symbol["X"]
                    answer += "X"
            elif num >= 50 and num <= 80:
                target += tens_symbol["L"]
                answer += "L"
                while target != num:
                    target += tens_symbol["X"]
                    answer += "X"
        elif len(str(num)) == 1:
            if num == 9:
                answer += "IX"
            elif num == 4:
                answer += "IV"
            elif num <= 3 and num >= 1:
                while target != num:
                    target += ones_symbol["I"]
                    answer += "I"
            elif num >= 5 and num <= 8:
                target += ones_symbol["V"]
                answer += "V"
                while target != num:
                    target += ones_symbol["I"]
                    answer += "I"

    return answer
