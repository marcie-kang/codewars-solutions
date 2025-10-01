"""
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:


# Use the `next' attribute to get the following node
node.next
Notes:

do NOT mutate the nodes!
in some cases there may be only a loop, with no dangling piece
Thanks to shadchnev, I broke all of the methods from the Hash class.

Don't miss dmitry's article in the discussion after you pass the Kata !! 
"""

def loop_size(node):
    if node is None:
        return 0

    tortoise = node.next
    hare = node.next

    if hare is not None:
        hare = hare.next

    met = False

    while hare and hare.next:
        if hare == tortoise:
            met = True
            break

        tortoise = tortoise.next
        hare = hare.next.next

    if not met:
        return 0

    loop_length = 1
    hare = hare.next

    while hare != tortoise:
        hare = hare.next
        loop_length += 1

    return loop_length
