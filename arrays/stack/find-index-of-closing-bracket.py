# Python program to find index of closing
# bracket for a given opening bracket.
from collections import deque


def getIndex(s, i):
    # If input is invalid.
    if s[i] != '[':
        return -1

    # Create a deque to use it as a stack.
    d = deque()

    # Traverse through all elements
    # starting from i.
    for k in range(i, len(s)):

        # Pop a starting bracket
        # for every closing bracket
        if s[k] == ']':
            d.popleft()

        # Push all starting brackets
        elif s[k] == '[':
            d.append(s[i])

        # If deque becomes empty
        if not d:
            return k

    return -1


# Driver code to test above method.
def test(s, i):
    matching_index = getIndex(s, i)
    print(s + ", " + str(i) + ": " + str(matching_index))


def main():
    test("[ABC[23]][89]", 0)  # should be 8
    test("[ABC[23]][89]", 4)  # should be 7
    test("[ABC[23]][89]", 9)  # should be 12
    test("[ABC[23]][89]", 1)  # No matching bracket


if __name__ == "__main__":
    main()