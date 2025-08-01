/*
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string
*/

SELECT
  x,
  regexp_replace(regexp_replace(x, '[0-4]', '0', 'g'), '[5-9]', '1', 'g') AS res
FROM
  fakebin;
