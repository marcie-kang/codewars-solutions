/*
Now you have to write a function that takes an argument and returns the square of it.
*/

SELECT
  n,
  CAST(POWER(n, 2) AS INT) AS res
FROM
  square
