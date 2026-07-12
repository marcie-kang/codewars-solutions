"""
You are a junior employee who was recently hired to work in an office. On your first day, your colleagues played a prank on you by locking your PC and leaving you stickers with a coded arrow password. You were able to write a decoder function for the arrow code and unlock your PC. Now you decide to respond to your colleagues in kind. You want to lock your colleagues' PCs when they go to lunch. Bringing your lunch, you sit and hold the stickers in your hands and glance at your colleagues, who suspect nothing. You realize that there are many PCs in the office and writing arrow code by hand will take a long time, so you need a function that will encode a sequence of numbers into arrow code. You decide to complicate the encoding by adding an additional arrow type and the letter d, which deletes the previous character. The number *n still repeats the previous character.

+---+---+---+     +---sticker---+
| 7 | 8 | 9 |     |             |
+---+---+---+     |  1→↑→       |
| 4 | 5 | 6 |     |             |
+---+---+---+     |             |
| 1 | 2 | 3 |     +-------------+
+---+---+---+         encoded
| 0 |                   1256
+---+
Task
Your task is to write a function that encodes an arrow PIN code. The input is a list of digits, and your function must return a string containing a valid arrow PIN code. An incorrect sequence is considered to be arrows leading beyond the numeric keypad.

A list with a length of 4 to 16 digits will be submitted at the entrance.
The input list will not consist entirely of identical digits. There will be at least two different digits.
The output string must begin with a number and continue with arrows.
If you need to go through a number that is not in the input list, you need to add the latter d after it.
The letter d deletes the previous character.
The length of identical consecutive digits will be in the range 1 < n < 11
If numbers are repeated, leave one digit and add the number of repetitions after it using the * symbol
The digit *n must be in the range 0 < *n < 10
Example: [1, 1, 1, 1, 2, 2, 2, 2] ==> “1*3→*3”
the set of arrows you plan to use ↗, ↖, ↘, ↙, →, ←, ↑, ↓
When encoding a pin code, different pin code options may be generated for the same sequence of digits Example:
                +---> “1↑d↑↘d↓d↙↗d↑d↖” ---+
[1, 7, 0, 7] ---|                         |---> [1, 7, 0, 7]
                +---> “1↑d↑↓d↓d↓↗d↑d↖” ---+
Both variants are valid when decoding, resulting in [1, 7, 0, 7].

Examples
[1, 5, 9, 6]  ==>  "1↗↗↓"
[1, 6, 2, 3]  ==>  "1→d↗↙→"
[1, 6, 4, 3]  ==>  "1→d↗↙d↖↘d→"
[1, 7, 0, 7]  ==>  "1↑d↑↘d↓d↙↗d↑d↖"
[1, 7, 7, 7]  ==>  "1↑d↑*2"
Unknown sequences
[0, 1, 1, 2, 3, 5, 8]  ==>  "0↑*1→→↖↑"
[2, 1, 3, 4, 7]  ==>  "2←→d→←d↖↑"
Only iron discipline and a sharp sword mind will lead you to victory.
"""

KEYPAD = {'7': (-1, 1), '8': (0, 1), '9': (1, 1),
          '4': (-1, 0), '5': (0, 0), '6': (1, 0),
          '1': (-1, -1), '2': (0, -1), '3': (1, -1),
          '0': (-1, -2)}
COORDS = {v: k for k, v in KEYPAD.items()}
ARROWS = {(0, 1): '↑', (0, -1): '↓',
          (1, 0): '→', (-1, 0): '←',
          (1, 1): '↗', (-1, 1): '↖',
          (1, -1): '↘', (-1, -1): '↙'}

def get_path(start_num, end_num):
    if start_num == end_num:
        return ""

    start_x, start_y = KEYPAD[str(start_num)]
    end_x, end_y = KEYPAD[str(end_num)]

    path = ""
    curr_x, curr_y = start_x, start_y

    while (curr_x, curr_y) != (end_x, end_y):
        dx = (end_x > curr_x) - (end_x < curr_x)
        dy = (end_y > curr_y) - (end_y < curr_y)

        if dx != 0 and dy != 0 and (curr_x + dx, curr_y + dy) not in COORDS:
            dy = 0

        curr_x += dx
        curr_y += dy
        path += ARROWS[(dx, dy)]

    return path

def compress_sequence(digits):
    if not digits:
        return []

    compressed = []
    curr_num = digits[0]
    count = 1

    for num in digits[1:]:
        if num == curr_num:
            count += 1
        else:
            compressed.append((curr_num, count))
            curr_num = num
            count = 1
    compressed.append((curr_num, count))

    return compressed

def coding_arrow_pin_code(arr):
    groups = compress_sequence(arr)
    first_num, first_count = groups[0]
    result = str(first_num)

    if first_count > 1:
        result += f"*{first_count - 1}"

    curr_num = first_num

    for next_num, next_count in groups[1:]:
        start_x, start_y = KEYPAD[str(curr_num)]
        end_x, end_y = KEYPAD[str(next_num)]

        cx, cy = start_x, start_y

        while (cx, cy) != (end_x, end_y):
            dx = (end_x > cx) - (end_x < cx)
            dy = (end_y > cy) - (end_y < cy)

            if (cx + dx, cy + dy) not in COORDS:
                if dx != 0:
                    dy = 0
                else:
                    dx = 0

            cx += dx
            cy += dy
            arrow = ARROWS[(dx, dy)]
            result += arrow

            if (cx, cy) != (end_x, end_y):
                result += "d"

        if next_count > 1:
            result += f"*{next_count - 1}"

        curr_num = next_num

    return result
