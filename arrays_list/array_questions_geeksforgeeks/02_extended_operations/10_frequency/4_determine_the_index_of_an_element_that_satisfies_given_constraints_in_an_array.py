# TODO: Study
# We can easily solve this problem in linear time using some extra space.
# The idea is to create two auxiliary arrays where each index of the
# first array stores the maximum element to the left,
# and that of the second array stores the minimum element to the right.
# We find an index whose value is greater than the maximum value to its
# left but smaller than the minimum value to its right after filling up
# both arrays.
import sys


# Determine the index of an element in a list before which all elements
# are smaller and after which all are greater
def findIndex(nums):
    # get the length of the list
    n = len(nums)

    # base case
    if n <= 2:
        return -1

    # `left[i]` stores the maximum element in sublist `nums[0…i-1]`
    left = [None] * n

    # initialize `left[0]` to the minimum value
    left[0] = -sys.maxsize

    # traverse the list from left to right and fill left
    for i in range(1, n):
        left[i] = max(left[i - 1], nums[i - 1])

    # `right[i]` stores the minimum element in sublist `nums[i+1, n-1]`
    right = [None] * n

    # initialize `right[0]` to the maximum value
    right[n - 1] = sys.maxsize

    # traverse the list from right to left and fill right
    for i in reversed(range(n - 1)):
        right[i] = min(right[i + 1], nums[i + 1])

    # traverse the list and return the desired index
    for i in range(1, n - 1):
        # index found
        if left[i] < nums[i] < right[i]:
            return i

    # return negative index if the input is invalid
    return -1


if __name__ == '__main__':

    nums = [4, 2, 3, 5, 1, 6, 9, 7]

    index = findIndex(nums)
    if 0 <= index < len(nums):
        print('The required index is', index)
    else:
        print('Invalid Input')