# TODO: Pending study
# Longest_Span_with_same_Sum_in_two_Binary_arrays
# A Simple python program to find longest common
# subarray of two binary arrays with same sum

# Returns length of the longest common subarray
# with same sum
def longestCommonSum(arr1, arr2, n):
	# Initialize result
	maxLen = 0

	# One by one pick all possible starting points
	# of subarrays
	for i in range(0, n):

		# Initialize sums of current subarrays
		sum1 = 0
		sum2 = 0

		# Consider all points for starting with arr[i]
		for j in range(i, n):

			# Update sums
			sum1 += arr1[j]
			sum2 += arr2[j]

			# If sums are same and current length is
			# more than maxLen, update maxLen
			if (sum1 == sum2):
				len = j - i + 1
				if (len > maxLen):
					maxLen = len

	return maxLen


# Driver program to test above function
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print("Length of the longest common span with same "
	  "sum is", longestCommonSum(arr1, arr2, n))


# This code is contributed by
# Smitha Dinesh Semwal


# ------------------------------------------------
# Python program to find longest common
# subarray of two binary arrays with
# same sum

def longestCommonSum(arr1, arr2, n):
	# Initialize result
	maxLen = 0

	# Initialize prefix sums of two arrays
	presum1 = presum2 = 0

	# Create a dictionary to store indices
	# of all possible sums
	diff = {}

	# Traverse both arrays
	for i in range(n):

		# Update prefix sums
		presum1 += arr1[i]
		presum2 += arr2[i]

		# Compute current diff which will be
		# used as index in diff dictionary
		curr_diff = presum1 - presum2

		# If current diff is 0, then there
		# are same number of 1's so far in
		# both arrays, i.e., (i+1) is
		# maximum length.
		if curr_diff == 0:
			maxLen = i + 1
		elif curr_diff not in diff:
			# save the index for this diff
			diff[curr_diff] = i
		else:
			# calculate the span length
			length = i - diff[curr_diff]
			maxLen = max(maxLen, length)

	return maxLen


# Driver program
arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
print("Length of the longest common",
	  " span with same", end=" ")
print("sum is", longestCommonSum(arr1,
								 arr2, len(arr1)))

# This code is contributed by Abhijeet Nautiyal
