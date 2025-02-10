# Completed
# Find floor and ceil of a number in a sorted array (Recursive solution)

# Given: arr1, n, find floor & ceil of n

# Sol1:
# 1. Traverse the array, when you find the integer larger than n, stop and collect index
# This can be done iteratively and recursively
# This solution is linear search

# Sol2:
# Instead of using linear search, binary search is used, this reduces complexity

# Function to get index of ceiling of x in arr[low..high] */
def ceilSearch(arr, x):
    # If x is smaller than or equal to first element, then return the first element */
    if x <= arr[0]:
        return 0

    # Otherwise, linearly search for ceil value */
    i = 0
    for i in range(len(arr)-1):
        if arr[i] == x:
            return i

        # if x lies between arr[i] and arr[i+1] including, arr[i+1], then return arr[i+1] */
        if arr[i] < x and arr[i + 1] >= x:
            return i + 1

    # If we reach here then x is greater than the last element of the array, return -1 in this case */
    return -1


# Driver program to check above functions */
arr = [1, 2, 8, 10, 10, 12, 19]
x = 3
index = ceilSearch(arr, x);

if index == -1:
    print("Ceiling of %d doesn't exist in array " % x)
else:
    print("ceiling of %d is %d" % (x, arr[index]))

# This code is contributed by Shreyanshi Arun


print("floor ceil recursive")
# Recursive solution
def floorrecursive(arr, x, count):
    # print(x)
    # print(count)
    print("count ", count, " arr ", arr[0])
    if arr[0] == x:
        print("Found the element at index1", count)
        return count, count+1
    if arr[0] > x:
        print("Found the element at index2", count)
        return count - 1, count
    arr = arr[1:]
    return floorrecursive(arr, x, count+1)


arr = [1, 2, 8, 10, 20, 23, 27]
x = 0

if x < arr[0]:
    print("No floor")

print(floorrecursive(arr, 10, 0))
