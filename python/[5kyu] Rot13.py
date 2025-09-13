"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
"""

def rot13(message):
    answer = ""

    for text in message:
        converted = text

        if text.isalpha():
            num = ord(text) + 13

            if (text.islower() and num > 122) or (text.isupper() and num > 90):
                num -= 26

            converted = chr(num)

        answer += converted

    return answer
