# Python3 program to determine whether
# given expression is balanced/ parenthesis
# expression or not.

# Function to check if two brackets are
# matching or not.
def isMatching(a, b):
    if ((a == '{' and b == '}') or
            (a == '[' and b == ']') or
            (a == '(' and b == ')') or
            a == 'X'):
        return 1

    return 0


# Recursive function to check if given
# expression is balanced or not.
def isBalanced(s, ele, ind):
    # Base case.
    # If the string is balanced then all the
    # opening brackets had been popped and
    # stack should be empty after string is
    # traversed completely.
    if (ind == len(s)):
        if len(ele) == 0:
            return True
        else:
            return False

    # Variable to store element at the top
    # of the stack.
    # char topEle;

    # Variable to store result of
    # recursive call.
    # int res;

    # Case 1: When current element is an
    # opening bracket then push that
    # element in the stack.
    if (s[ind] == '{' or s[ind] == '(' or
            s[ind] == '['):
        ele.append(s[ind])
        return isBalanced(s, ele, ind + 1)

    # Case 2: When current element is a closing
    # bracket then check for matching bracket
    # at the top of the stack.
    elif (s[ind] == '}' or s[ind] == ')' or
          s[ind] == ']'):

        # If stack is empty then there is no matching
        # opening bracket for current closing bracket
        # and the expression is not balanced.
        if (len(ele) == 0):
            return 0

        topEle = ele[-1]
        ele.pop()

        # Check bracket is matching or not.
        if (isMatching(topEle, s[ind]) == 0):
            return 0

        return isBalanced(s, ele, ind + 1)

    # Case 3: If current element is 'X' then check
    # for both the cases when 'X' could be opening
    # or closing bracket.
    elif (s[ind] == 'X'):
        tmp = ele
        tmp.append(s[ind])
        res = isBalanced(s, tmp, ind + 1)

        if (res):
            return 1
        if (len(ele) == 0):
            return 0

        ele.pop()

        return isBalanced(s, ele, ind + 1)


# Driver Code
s = "{(X}[]"
ele = []

if (isBalanced(s, ele, 0)):
    print("Balanced")
else:
    print("Not Balanced")