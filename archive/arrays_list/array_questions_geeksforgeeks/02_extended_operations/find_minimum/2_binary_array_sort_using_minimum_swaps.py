# TODO: Study
# Python3 code to find minimum number of
# swaps to sort a binary array

# Function to find minimum swaps to
# sort an array of 0s and 1s.
def findMinSwaps(arr, n):
	# Array to store count of zeroes
	noOfZeroes = [0] * n
	count = 0

	# Count number of zeroes
	# on right side of every one.
	noOfZeroes[n - 1] = 1 - arr[n - 1]
	for i in range(n - 2, -1, -1):
		noOfZeroes[i] = noOfZeroes[i + 1]
		if (arr[i] == 0):
			noOfZeroes[i] = noOfZeroes[i] + 1

	# Count total number of swaps by adding
	# number of zeroes on right side of
	# every one.
	for i in range(0, n):
		if (arr[i] == 1):
			count = count + noOfZeroes[i]

	return count


# Driver code
arr = [0, 0, 1, 0, 1, 0, 1, 1]
n = len(arr)
print(findMinSwaps(arr, n))


# This code is contributed by Manish Shaw
# (manishshaw1)


# -------------------------------------------------

def minswaps(arr):
	count = 0
	num_unplaced_zeros = 0

	for index in range(len(arr) - 1, -1, -1):
		if arr[index] == 0:
			num_unplaced_zeros += 1
		else:
			count += num_unplaced_zeros
	return count


arr = [0, 0, 1, 0, 1, 0, 1, 1]
print(minswaps(arr))
