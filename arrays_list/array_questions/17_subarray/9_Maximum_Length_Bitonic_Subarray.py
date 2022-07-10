# Maximum_Length_Bitonic_Subarray
# Python program to find length of the longest bitonic subarray

def bitonic(arr, n):
	# Length of increasing subarray ending at all indexes
	inc = [None] * n

	# Length of decreasing subarray starting at all indexes
	dec = [None] * n

	# length of increasing sequence ending at first index is 1
	inc[0] = 1

	# length of increasing sequence starting at first index is 1
	dec[n - 1] = 1

	# Step 1) Construct increasing sequence array
	for i in range(n):
		if arr[i] >= arr[i - 1]:
			inc[i] = inc[i - 1] + 1
		else:
			inc[i] = 1

	# Step 2) Construct decreasing sequence array
	for i in range(n - 2, -1, -1):
		if arr[i] >= arr[i - 1]:
			dec[i] = inc[i - 1] + 1
		else:
			dec[i] = 1

	# Step 3) Find the length of maximum length bitonic sequence
	max = inc[0] + dec[0] - 1
	for i in range(n):
		if inc[i] + dec[i] - 1 > max:
			max = inc[i] + dec[i] - 1

	return max


# Driver program to test above function

arr = [12, 4, 78, 90, 45, 23]
n = len(arr)
print("nLength of max length Bitonic Subarray is ", bitonic(arr, n))
