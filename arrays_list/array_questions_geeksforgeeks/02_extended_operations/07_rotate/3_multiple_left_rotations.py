# Python3 implementation of left rotation
# of an array K number of times

# Efficient Approach:
# The above approaches work well when there is a single rotation required. The approaches also modify the original array. To handle multiple queries of array rotation, we use a temp array of size 2n and quickly handle rotations.
# Step 1: Copy the entire array two times in the temp[0..2n-1] array.
# Step 2: Starting position of the array after k rotations in temp[] will be k % n. We do k
# Step 3: Print temp[] array from k % n to k % n + n.

# Fills temp with two copies of arr
def preprocess(arr, n):
	temp = [None] * (2 * n)

	# Store arr elements at i and i + n
	for i in range(n):
		temp[i] = temp[i + n] = arr[i]
	return temp


# Function to left rotate an array k times
def leftRotate(arr, n, k, temp):
	# Starting position of array after k
	# rotations in temp will be k % n
	start = k % n

	# Print array after k rotations
	for i in range(start, start + n):
		print(temp[i], end=" ")
	print("")


# Driver program
arr = [1, 3, 5, 7, 9]
n = len(arr)
temp = preprocess(arr, n)

k = 2
leftRotate(arr, n, k, temp)

k = 3
leftRotate(arr, n, k, temp)

k = 4
leftRotate(arr, n, k, temp)

# This code is contributed by Sanghamitra Mishra
