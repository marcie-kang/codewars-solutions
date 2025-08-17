"""
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""

def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0

    for a in array_of_arrays:
        if a is None or len(a) == 0:
            return 0

    lengths = sorted(len(a) for a in array_of_arrays)

    for prev, curr in zip(lengths, lengths[1:]):
        if curr != prev + 1:
            return prev + 1

    return 0
