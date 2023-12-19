# TODO: Completed
# leetcod https://leetcode.com/problems/move-zeroes/ #Pending

# Given an array of random numbers, Push all the zero’s of a given array to the end of
# the array. For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0},
# it should be changed to {1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0}.
# The order of all other elements should be same.
# Expected time complexity is O(n) and extra space is O(1).

# Traverse the given array ‘arr’ from left to right.
# While traversing, maintain count of non-zero elements in array.
# Let the count be ‘count’. For every non-zero element arr[i],
# put the element at ‘arr[count]’ and increment ‘count’.
# After complete traversal, all non-zero elements have already been shifted to
# front end and ‘count’ is set as index of first 0.
# Now all we need to do is run a loop that makes all elements zero from ‘count’ till end of the array.


# Python3 code to move all zeroes
# at the end of array

# Function which pushes all
# zeros to end of an array.
def pushZerosToEnd(arr, n):
    count = 0  # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        if arr[i] != 0:
            # here count is incremented
            arr[count] = arr[i]
            count += 1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1


# Driver code
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)

# This code is contributed by "Abhishek Sharma 44"


# Method 2: Partitioning the array
#
# Approach: The approach is pretty simple. We will use 0 as a pivot element and whenever we see a non zero element we will swap it with the pivot element. So all the non zero element will come at the beginning.

# Python Program to move all zeros to the end
A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
j = 0
for i in range(n):
	if A[i] != 0:
		A[j], A[i] = A[i], A[j] # Partitioning the array
		j += 1
print(A) # Print the array

# This code is contributed by Tapesh(tapeshdua420)



