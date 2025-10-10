def smallest(n):
    s = str(n)
    L = len(s)
    min_val = n
    best_remove_idx = 0
    best_insert_idx = 0

    for remove_idx in range(L):
        digit_to_move = s[remove_idx]
        remaining = list(s[:remove_idx] + s[remove_idx + 1:])

        for insert_idx in range(L):
            new_digits = remaining[:insert_idx] + [digit_to_move] + remaining[insert_idx:]
            new_num_str = "".join(new_digits)

            new_val = int(new_num_str)

            if new_val < min_val:
                min_val = new_val
                best_remove_idx = remove_idx
                best_insert_idx = insert_idx
            elif new_val == min_val:
                if remove_idx < best_remove_idx or (remove_idx == best_remove_idx and insert_idx < best_insert_idx):
                    best_remove_idx = remove_idx
                    best_insert_idx = insert_idx

    return [min_val, best_remove_idx, best_insert_idx]
