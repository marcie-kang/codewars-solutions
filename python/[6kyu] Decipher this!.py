"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
there are no special characters used, only letters and spaces
words are separated by a single space
there are no leading or trailing spaces
Examples

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'
"""

#second solution
def decipher_this(s: str) -> str:
    result = []

    for word in s.split():
        i = 0

        while i < len(word) and word[i].isdigit():
            i += 1

        first_char = chr(int(word[:i]))
        tail = word[i:]

        if len(tail) >= 2:
            tail = tail[-1] + tail[1:-1] + tail[0]

        result.append(first_char + tail)

    return " ".join(result)


#first solution
def decipher_this(s):
    answer = []
    words = s.split(" ")

    for word in words:
        decoded_word = ""
        num = ""
        num_idx = 0

        for idx, text in enumerate(word):
            if text.isnumeric() and idx == len(word) - 1:
                num += text
                decoded_word += chr(int(num))
                break
            elif text.isnumeric():
                num += text
                num_idx = idx
            else:
                if num_idx + 2 == len(word):
                    decoded_word += chr(int(num)) + word[-1]
                else:
                    decoded_word += chr(int(num)) + word[-1] + word[idx + 1:-1] + word[idx]
                break

        answer.append(decoded_word)

    return " ".join(answer)
