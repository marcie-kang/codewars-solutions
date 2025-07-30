"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ",
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
"""

def tower_builder(n_floors):
    arr = []

    for i in range(n_floors):
        point = int((n_floors * 2 - 1) / 2)
        floor = ""

        for j in range(n_floors * 2 - 1):
            index = [point - i, point + i]

            if j >= index[0] and j <= index[1]:
                floor += "*"
            else:
                floor += " "

        arr.append(floor)

    return arr
