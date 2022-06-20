# Python3 program to check for balanced brackets.

# function to check if brackets are balanced

# Pseudologic
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

def areBracketsBalanced(string_expression):
    stack = []

    # Traversing the Expression
    for char_in_expression in string_expression:

        # if clause 1
        if char_in_expression in ["(", "{", "["]:
            # Push the element in the stack
            stack.append(char_in_expression)

        # else clause 1
        else:
            # If current character is not opening bracket, then it must be closing.

            # 1.a. So stack cannot be empty at this point.
            # if clause
            if not stack:
                return False

            # 1.b.
            dict_brackets = {"(": ")", "{": "}", "(": ")"}
            current_char_in_stack = stack.pop()
            if dict_brackets[current_char_in_stack] != char_in_expression:
                return False

    # Check Empty Stack
    if stack:
        return False
    return True

# Driver Code
if __name__ == "__main__":
    string_expression = "{()}[]"

    # Function call
    if areBracketsBalanced(string_expression):
        print("Balanced")
    else:
        print("Not Balanced")

# This code is contributed by AnkitRai01 and improved
# by Raju Pitta
