# Find_lost_element_from_a_duplicated_array
# Python3 program to find missing
# element from same arrays
# (except one missing element)

# Function to find missing element based
# on binary search approach. arr1[] is
# of larger size and N is size of it.
# arr1[] and arr2[] are assumed
# to be in same order.
def findMissingUtil(arr1, arr2, N):
	# special case, for only element
	# which is missing in second array
	if N == 1:
		return arr1[0];

	# special case, for first
	# element missing
	if arr1[0] != arr2[0]:
		return arr1[0]

	# Initialize current corner points
	lo = 0
	hi = N - 1

	# loop until lo < hi
	while (lo < hi):

		mid = (lo + hi) / 2

		# If element at mid indices
		# are equal then go to
		# right subarray
		if arr1[mid] == arr2[mid]:
			lo = mid
		else:
			hi = mid

		# if lo, hi becomes
		# contiguous, break
		if lo == hi - 1:
			break

	# missing element will be at
	# hi index of bigger array
	return arr1[hi]


# This function mainly does basic
# error checking and calls
# findMissingUtil
def findMissing(arr1, arr2, M, N):
	if N == M - 1:
		print("Missing Element is",
			  findMissingUtil(arr1, arr2, M))
	elif M == N - 1:
		print("Missing Element is",
			  findMissingUtil(arr2, arr1, N))
	else:
		print("Invalid Input")


# Driver Code
arr1 = [1, 4, 5, 7, 9]
arr2 = [4, 5, 7, 9]
M = len(arr1)
N = len(arr2)
findMissing(arr1, arr2, M, N)


# This code is contributed by Smitha Dinesh Semwal


# ------------------------------------------------
# Python 3 program to find
# missing element from one array
# such that it has all elements
# of other array except
# one. Elements in two arrays
# can be in any order.

# This function mainly does XOR of all elements
# of arr1[] and arr2[]
def findMissing(arr1, arr2, M, N):
	if (M != N - 1 and N != M - 1):
		print("Invalid Input")
		return

	# Do XOR of all element
	res = 0
	for i in range(0, M):
		res = res ^ arr1[i];
	for i in range(0, N):
		res = res ^ arr2[i]

	print("Missing element is", res)


# Driver Code
arr1 = [4, 1, 5, 9, 7]
arr2 = [7, 5, 9, 4]
M = len(arr1)
N = len(arr2)
findMissing(arr1, arr2, M, N)

# This code is contributed
# by Smitha Dinesh Semwal
