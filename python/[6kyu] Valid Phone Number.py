"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

"(123) 456-7890"  => true
"(1111)555 2345"  => false
"(098) 123 4567"  => false
"""

def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False

    if phone_number[0] != "(" or phone_number[4] != ")" or phone_number[5] != " " or phone_number[9] != "-":
        return False

    parts = [phone_number]

    for i in "()- ":
        new_parts = []

        for part in parts:
            new_parts.extend(part.split(i))

        parts = new_parts

    final_list = [part for part in parts if part != ""]

    for idx, part in enumerate(final_list):

        if not part.isdigit():
            return False

    if len(final_list[0]) == 3 and len(final_list[1]) == 3 and len(final_list[2]) == 4:
        return True
    else:
        return False
