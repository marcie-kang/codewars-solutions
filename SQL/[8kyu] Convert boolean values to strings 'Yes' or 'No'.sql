/*
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
*/

SELECT
  bool,
  CASE
    WHEN bool = True THEN 'Yes'
    ELSE 'No'
  END AS res
FROM
  booltoword;
