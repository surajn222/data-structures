# Python3 program to check for balanced brackets.

# function to check if brackets are balanced

# Pseudologic
# 1. Traverse the string
# string = "{()}[]"
#       case:
#       a.
#           if current_char_in_string is open_bracket:
#               add current_char_in_string to stack_temp
#           else if current_char_in_string is not open_bracket:
#               get the element_on_top_of_stack_temp
#               compare if the current_char_in_string with element_on_top_of_stack_temp are not opposites:
#                   then its not a balanced string
#
#       b.
#           if stack_temp is not empty
#               string is not balanced
#       c. string is balanced

def areBracketsBalanced(string_expression):
    stack_temp = []

    # Traversing the Expression
    for char_in_expression in string_expression:

        # if clause 1
        if char_in_expression in ["(", "{", "["]:
            # Push the element in the stack_temp
            stack_temp.append(char_in_expression)

        # else clause 1
        else:
            # If current character is not opening bracket, then it must be closing.

            # 1.a. So stack_temp cannot be empty at this point.
            if not stack_temp:
                return False

            # 1.b.
            dict_brackets = {"(": ")", "{": "}", "[": "]"}
            current_char_in_stack_temp = stack_temp.pop()
            if dict_brackets[current_char_in_stack_temp] != char_in_expression:
                return False

    # Check Empty stack_temp
    if stack_temp:
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
