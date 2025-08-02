/*
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
*/

SELECT
  s,
  REPLACE(s, '!', '') AS res
FROM
  removeexclamationmarks;
