# Python3 program to
# mark balanced and
# unbalanced parenthesis.
def identifyParenthesis(a):
    st = []

    # run the loop upto
    # end of the string
    for i in range(len(a)):

        # if a[i] is opening
        # bracket then push
        # into stack
        if (a[i] == '('):
            st.append(a[i])

        # if a[i] is closing bracket ')'
        elif (a[i] == ')'):

            # If this closing bracket
            # is unmatched
            if (len(st) == 0):
                a = a.replace(a[i], "-1", 1)

            else:

                # replace all opening brackets with 0
                # and closing brackets with 1
                a = a.replace(a[i], "1", 1)
                print("replace 1: " + str(a))
                a = a.replace(st[-1], "0", 1)
                print("replace 0: " + str(a))
                st.pop()

    # if stack is not empty
    # then pop out all
    # elements from it and
    # replace -1 at that
    # index of the string
    while (len(st) != 0):
        a = a.replace(st[-1], 1, "-1");
        st.pop()

    # print final string
    print(a)


# Driver code
if __name__ == "__main__":
    st = "(a) + (b) +(a+b)"
    identifyParenthesis(st)

# This code is contributed by Chitranayal