"""
For this exercise you will create a global flatten method. The method takes in any number of arguments and flattens them into a single array. If any of the arguments passed in are an array then the individual objects within the array will be flattened so that they exist at the same level as the other arguments. Any nested arrays, no matter how deep, should be flattened into the single array result.

The following are examples of how this function would be used and what the expected results would be:

flatten(1, [2, 3], 4, 5, [6, [7]]) ==> [1, 2, 3, 4, 5, 6, 7]
flatten('a', ['b', 2], 3, 666, [[4], ['c']]) ==> ['a', 'b', 2, 3, 666, 4, 'c']
"""
#solution1
def flatten(*args) -> list:
    result = []

    for arg in args:
        if isinstance(arg, list):
            result.extend(flatten(*arg))
        else:
            result.append(arg)

    return result

#solution2
def flatten(*args) -> list:
    result = []
    stack = list(args)

    while stack:
        item = stack.pop(0)

        if isinstance(item, list):
            stack = item + stack
        else:
            result.append(item)

    return result
