/*
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
*/

SELECT
  str,
  (LENGTH(str) - LENGTH(REPLACE(str, 'a', ''))) +
  (LENGTH(str) - LENGTH(REPLACE(str, 'e', ''))) +
  (LENGTH(str) - LENGTH(REPLACE(str, 'i', ''))) +
  (LENGTH(str) - LENGTH(REPLACE(str, 'o', ''))) +
  (LENGTH(str) - LENGTH(REPLACE(str, 'u', ''))) AS res
FROM getcount;
