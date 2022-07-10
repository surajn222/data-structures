# Python3 program to determine whether given expression is balanced/parenthesis expression or not.

# Function to check if two brackets are matching or not.
def isMatching(a, b):
    dict_brackets = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    if ((dict_brackets[a] == b) or a == 'X'):
        return True

    # if ((a == '{' and b == '}') or (a == '[' and b == ']') or (a == '(' and b == ')') or a == 'X'):
    #     return 1

    return 0


# Recursive function to check if given expression is balanced or not.
def isBalanced(string_brackets, list_temp_brackets, index):
    # Base case.
    # If the string is balanced then all the opening brackets had been popped and stack should be empty after string is traversed completely.
    if (index == len(string_brackets)):
        if len(list_temp_brackets) == 0:
            return True
        else:
            return False

    # Variable to store element at the top of the stack.
    # char topEle;

    # Variable to store result of recursive call.
    # int res;

    list_opening_brackets = ['{', '(', '[']
    list_closing_brackets = ['}', ')', ']']

    # Case 1: When current element is an opening bracket, then push that element in the stack.
    if (string_brackets[index] in list_opening_brackets):
        list_temp_brackets.append(string_brackets[index])
        return isBalanced(string_brackets, list_temp_brackets, index + 1)

    # Case 2: When current element is a closing bracket, then check for matching bracket at the top of the stack.
    elif (string_brackets[index] in list_closing_brackets):

        # If stack is empty then there is no matching opening bracket for current closing bracket and the expression is not balanced.
        if (len(list_temp_brackets) == 0):
            return False

        top_element = list_temp_brackets[-1]
        list_temp_brackets.pop()

        # Check bracket is matching or not.
        if (isMatching(top_element, string_brackets[index]) == 0):
            return False

        return isBalanced(string_brackets, list_temp_brackets, index + 1)

    # Case 3: If current element is 'X' then check for both the cases when 'X' could be opening or closing bracket.
    elif (string_brackets[index] == 'X'):
        tmp = list_temp_brackets
        tmp.append(string_brackets[index])
        res = isBalanced(string_brackets, tmp, index + 1)

        if (res):
            return 1
        if (len(list_temp_brackets) == 0):
            return 0

        list_temp_brackets.pop()

        return isBalanced(string_brackets, list_temp_brackets, index + 1)

def main():
    # Driver Code
    string_brackets = "{(X}[]"
    list_temp_brackets = []

    if (isBalanced(string_brackets, list_temp_brackets, 0)):
        print("Balanced")
    else:
        print("Not Balanced")

main()