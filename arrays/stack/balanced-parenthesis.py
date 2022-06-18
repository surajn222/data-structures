# Python3 program to check for
# balanced brackets.

# function to check if
# brackets are balanced

#Pseudologic
# 1. Traverse the string
#       a.
#           if current_char_in_string is open_bracket:
#               add current_char_in_string to stack
#           else if current_char_in_string is not open_bracket:
#               get the element_on_top_of_stack
#               compare if the current_char_in_string with element_on_top_of_stack are not opposites:
#                   then its not a balanced string
#
#       b.
#           if stack is not empty
#               string is not balanced
#       c. string is balanced

def areBracketsBalanced(expr):
    stack = []

    # Traversing the Expression
    for char_in_expr in expr:
        if char_in_expr in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char_in_expr)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char_in_stack = stack.pop()
            if current_char_in_stack == '(':
                if char_in_expr != ")":
                    return False
            if current_char_in_stack == '{':
                if char_in_expr != "}":
                    return False
            if current_char_in_stack == '[':
                if char_in_expr != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"

    # Function call
    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta