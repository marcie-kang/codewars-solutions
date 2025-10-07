"""
Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:

a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

a.add(b)      # should return a new Vector([4, 6, 8])
a.subtract(b) # should return a new Vector([-2, -2, -2])
a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
a.add(c)      # raises an exception
If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!

Also provide:

a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
an equals method, to check that two vectors that have the same components are equal
Note: the test cases will utilize the user-provided equals method.
"""

import math

class Vector:
    def __init__(self, components):
        self.components = components

    def _check_dimensions(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions.")

    def add(self, other):
        self._check_dimensions(other)
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def subtract(self, other):
        self._check_dimensions(other)
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other):
        self._check_dimensions(other)
        return sum(a * b for a, b in zip(self.components, other.components))

    def norm(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def equals(self, other):
        if len(self.components) != len(other.components):
            return False

        return all(a == b for a, b in zip(self.components, other.components))

    def __str__(self):
        return f"({','.join(map(str, self.components))})"

    def __repr__(self):
        return self.__str__()


