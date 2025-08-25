def solve(s):
    parts = [s]

    for v in "aeiou":
        new_parts = []

        for part in parts:
            new_parts.extend(part.split(v))

        parts = new_parts

    values = [sum(ord(ch) - 96 for ch in part) for part in parts]

    return max(values) if values else 0

print(solve("zodianc"))