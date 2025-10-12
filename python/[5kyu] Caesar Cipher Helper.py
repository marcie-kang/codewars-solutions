"""
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].
"""

class CaesarCipher(object):
    ALPHABET_SIZE = 26
    ORD_A = 65

    def __init__(self, shift):
        self.shift_num = shift % self.ALPHABET_SIZE

    def cryptographer(self, st, shift_num):
        result = ""

        for text in st.upper():
            char_ord = ord(text)

            if char_ord >= self.ORD_A and char_ord <= 90:
                index_from_a = char_ord - self.ORD_A
                wrapped_index = (index_from_a + shift_num) % self.ALPHABET_SIZE
                new_ord = wrapped_index + self.ORD_A

                result += chr(new_ord)
            else:
                result += text

        return result

    def encode(self, st):
        return self.cryptographer(st, self.shift_num)

    def decode(self, st):
        return self.cryptographer(st, self.shift_num * -1)
