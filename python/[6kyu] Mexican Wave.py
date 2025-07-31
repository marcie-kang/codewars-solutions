"""
1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array. 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Examples
"hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
" s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
"""

def wave(people):
    answer = []

    for idx in range(len(people)):
        if people[idx] != " ":
            current_char = people[idx].upper()
            pre_word = people[:idx]
            final_word = pre_word + current_char + people[idx + 1:]
            answer.append(final_word)

    return answer
