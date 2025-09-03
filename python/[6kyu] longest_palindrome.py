"""
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

def longest_palindrome(s):
    if not s:
        return 0

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_length = 0

    for i in range(len(s)):
        odd_length = expand_around_center(i, i)
        even_length = expand_around_center(i, i + 1)
        max_length = max(max_length, odd_length, even_length)

    return max_length
