# Python3 program to simplify algebraic String

# Function to simplify the String


def simplify(Str):
    Len = len(Str)

    # resultant String of max Length
    # equal to Length of input String
    res = [None] * Len
    index = 0
    i = 0

    # create empty stack
    s = []
    s.append(0)

    while (i < Len):
        if (Str[i] == '(' and i == 0):
            i += 1
            continue

    if (Str[i] == '+'):

        # If top is 1, flip the operator
        if (s[-1] == 1):
            res[index] = '-'
            index += 1

        # If top is 0, append the
        # same operator
        if (s[-1] == 0):
            res[index] = '+'
            index += 1

    elif (Str[i] == '-'):
        if (s[-1] == 1):
            res[index] = '+'
            index += 1
        elif (s[-1] == 0):
            res[index] = '-'
            index += 1
    elif (Str[i] == '(' and i > 0):
        if (Str[i - 1] == '-'):

            # x is opposite to the top of stack
            x = 0 if (s[-1] == 1) else 1
            s.append(x)

        # append value equal to top of the stack
        elif (Str[i - 1] == '+'):
            s.append(s[-1])

        # If closing parentheses pop
        # the stack once
    elif (Str[i] == ')'):
        s.pop()

        # copy the character to the result
    else:
        res[index] = Str[i]
        index += 1
    i += 1
    return res


# Driver Code
if __name__ == '__main__':

    s1 = "(a-(b+c)+d)"
    s2 = "a-(b-c-(d+e))-f"
    r1 = simplify(s1)
    for i in r1:
        if i != None:
            print(i, end=" ")
        else:
            break
    print()
    r2 = simplify(s2)
    for i in r2:
        if i != None:
            print(i, end=" ")
        else:
            break

# This code is contributed by PranchalK