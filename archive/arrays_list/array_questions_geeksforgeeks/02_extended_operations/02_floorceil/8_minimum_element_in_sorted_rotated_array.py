# Sol1:
# Traverse the array, when current > previous, stop

# Python program to find minimum element
# in a sorted and rotated array

def findMin(arr, low, high):
    # This condition is needed to handle the case when array is not
    # rotated at all
    if high < low:
        return arr[0]

    # If there is only one element left
    if high == low:
        return arr[low]

    # Find mid
    mid = int((low + high)/2)

    # Check if element (mid+1) is minimum element. Consider
    # the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]

    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]

    # Decide whether we need to go to left half or right half
    if arr[high] > arr[mid]:
        return findMin(arr, low, mid-1)
    return findMin(arr, mid+1, high)

# Driver program to test above functions
arr1 = [5, 6,  2, 3, 4]
n1 = len(arr1)
print("The minimum element is " + str(findMin(arr1, 0, n1-1)))

import sys
sys.exit()

arr6 = [5, 6, 7,  3, 4]
n6 = len(arr6)
print("The minimum element is " + str(findMin(arr6, 0, n6-1)))

arr7 = [1, 2, 3, 4, 5, 6, 7]
n7 = len(arr7)
print("The minimum element is " + str(findMin(arr7, 0, n7-1)))

# This code is contributed by Pratik Chhajer