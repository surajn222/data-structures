# TODO: Pending study
# Count_Strictly_Increasing_Subarrays
# Python3 program to count number
# of strictly increasing subarrays

def countIncreasing(arr, n):
	# Initialize count of subarrays as 0
	cnt = 0

	# Pick starting point
	for i in range(0, n):

		# Pick ending point
		for j in range(i + 1, n):
			if arr[j] > arr[j - 1]:
				cnt += 1

			# If subarray arr[i..j] is not strictly
			# increasing, then subarrays after it , i.e.,
			# arr[i..j+1], arr[i..j+2], .... cannot
			# be strictly increasing
			else:
				break
	return cnt


# Driver code
arr = [1, 2, 2, 4]
n = len(arr)
print("Count of strictly increasing subarrays is",
	  countIncreasing(arr, n))


# This code is contributed by Shreyanshi Arun.


# ----------------------------------------------------

# Python3 program to count number of
# strictlyincreasing subarrays in O(n) time.

def countIncreasing(arr, n):
	cnt = 0  # Initialize result

	# Initialize length of current
	# increasing subarray
	len = 1

	# Traverse through the array
	for i in range(0, n - 1):

		# If arr[i+1] is greater than arr[i],
		# then increment length
		if arr[i + 1] > arr[i]:
			len += 1

		# Else Update count and reset length
		else:
			cnt += (((len - 1) * len) / 2)
			len = 1

	# If last length is more than 1
	if len > 1:
		cnt += (((len - 1) * len) / 2)

	return cnt


# Driver program
arr = [1, 2, 2, 4]
n = len(arr)

print("Count of strictly increasing subarrays is",
	  int(countIncreasing(arr, n)))

# This code is contributed by Shreyanshi Arun.
