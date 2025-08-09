"""
Your job is to create a calculator which evaluates expressions in Reverse Polish notation.

For example expression 5 1 2 + 4 * + 3 - (which is equivalent to 5 + ((1 + 2) * 4) - 3 in normal notation) should evaluate to 14.

For your convenience, the input is formatted such that a space is provided between every token.

Empty expression should evaluate to 0.

Valid operations are +, -, *, /.

You may assume that there won't be exceptional situations (like stack underflow or division by zero).
"""

def calc(expr):
    if not expr.strip():
        return 0

    stack = []
    for tok in expr.split():
        if tok.lstrip('-').replace('.', '', 1).isdigit():
            stack.append(float(tok) if '.' in tok else int(tok))
            continue

        b = stack.pop()
        a = stack.pop()

        if tok == '+':
            stack.append(a + b)
        elif tok == '-':
            stack.append(a - b)
        elif tok == '*':
            stack.append(a * b)
        elif tok == '/':
            stack.append(a / b)

    return stack[0] if stack else 0
