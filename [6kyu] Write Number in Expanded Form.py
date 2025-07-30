"""
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

   12 --> "10 + 2"
   45 --> "40 + 5"
70304 --> "70000 + 300 + 4"
NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    num_str = str(num)
    answer = []

    for idx in range(len(num_str)):
        current = int(num_str[idx])

        if current != 0:
            answer.append(str(int(current) * (10 ** (len(num_str) - idx - 1))))

    return " + ".join(answer)
