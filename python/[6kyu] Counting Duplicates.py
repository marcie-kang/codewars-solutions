"""
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice

"""

def duplicate_count(text):
    count_str = {}
    answer = 0

    for str in text:
        str_check = str.upper()

        if str_check in count_str:
            count_str[str_check] += 1
        else:
            count_str[str_check] = 1

    for key, value in count_str.items():
        if value > 1:
            answer += 1

    return answer
