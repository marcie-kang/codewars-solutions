"""
The makeLooper() function (or make_looper in your language) takes a string (of non-zero length) as an argument. It returns a function. The function it returns will return successive characters of the string on successive invocations. It will start back at the beginning of the string once it reaches the end.

For example:

abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call
Different loopers should not affect each other, so be wary of unmanaged global state.
"""

def make_looper(text):
    string_to_loop = text
    current_index = 0

    def looper():
        nonlocal current_index

        char = string_to_loop[current_index]
        current_index = (current_index + 1) % len(string_to_loop)

        return char

    return looper
