"""
Short Intro

Some of you might remember spending afternoons playing Street Fighter 2 in some Arcade back in the 90s or emulating it nowadays with the numerous emulators for retro consoles.

Can you solve this kata? Suuure-You-Can!

UPDATE: a new kata's harder version is available here.
"""

def street_fighter_selection(fighters, initial_position, moves):
    current = initial_position
    answer = []

    for move in moves:
        if move == "right":
            if current[1] + 1 > len(fighters[current[0]]) - 1:
                current = (current[0], 0)
            else:
                current = (current[0], current[1] + 1)
        elif move == "left":
            if (current[1] - 1) * -1 > len(fighters[current[0]]):
                current = (current[0], len(fighters[current[0]]) - 1)
            else:
                current = (current[0], current[1] - 1)
        elif move == "up":
            if current[0] != 0:
                current = (current[0] - 1, current[1])
        elif move == "down":
            if current[0] != 1:
                current = (current[0] + 1, current[1])

        answer.append(fighters[current[0]][current[1]])

    return answer
