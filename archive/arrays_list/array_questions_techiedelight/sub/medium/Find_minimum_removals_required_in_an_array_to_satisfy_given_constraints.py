def findMin(arr):
	# Stores the length of the maximum size subarray
	max_range = 0

	# Traverse the array and consider each element as a starting point of a subarray
	for i in range(len(arr)):

		'''
			Subarray invariant: max < 2×min
		'''

		# To keep track of the minimum and the maximum elements in a subarray
		min_arr = max_arr = arr[i]

		# Find the maximum size subarray `arr[i…j]` that satisfies
		# the above invariant
		for j in range(i, len(arr)):

			# Find the minimum and the maximum elements in the current subarray.
			# We must do this in constant time.
			min_arr = min(min_arr, arr[j])
			max_arr = max(max_arr, arr[j])

			# Discard the subarray if the invariant is violated
			if 2 * min_arr <= max_arr:
				break

			# Update `max_range` when a bigger subarray is found
			max_range = max(max_range, j - i + 1)

	# Return array size - length of the maximum size subarray
	return len(arr) - max_range


if __name__ == '__main__':
	arr = [4, 6, 1, 7, 5, 9, 2]
	print("The minimum number of removals is", findMin(arr))
