def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if (char == ")" and top != "(") or \
               (char == "]" and top != "[") or \
               (char == "}" and top != "{"):
                return False
    return len(stack) == 0

expression = input("Enter a string containing parentheses: ")
if is_balanced(expression):
    print("The string contains correctly balanced parentheses.")
else:
    print("The string contains incorrectly balanced parentheses.")
