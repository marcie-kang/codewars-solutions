/*
Write a function that checks if a given string (case insensitive) is a palindrome.

A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar.
*/

SELECT
  str,
  CASE
    WHEN LOWER(str) = REVERSE(LOWER(str)) THEN true
    ELSE false
  END AS res
FROM
  ispalindrome
