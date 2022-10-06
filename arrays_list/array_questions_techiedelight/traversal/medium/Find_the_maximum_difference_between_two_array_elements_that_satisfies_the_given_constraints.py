import sys


# Function to calculate the maximum difference between two elements in a
# list such that a smaller element appears before a larger element

# Maximum diff between two elements in a list = max((Max element) - (minimum element before it))
#												Keep looking for max element, then keep looking for minimum element before it
# 												then keep looking for max diff

# current_diff
# max_so_far

# Update max_so_far ELSE max_so_far - A[5]
# Update max_so_far ELSE max_so_far - A[4]
# Update max_so_far ELSE max_so_far - A[3]
# Update max_so_far ELSE max_so_far - A[2]
# Update max_so_far ELSE max_so_far - A[1]
# Update max_so_far ELSE max_so_far - A[0]


def getMaxDiff(A):
	diff = -sys.maxsize
	n = len(A)

	# Case 1
	if n == 0:
		return diff

	# Case 2
	max_so_far = A[n - 1]

	# traverse the list from the right and keep track of the maximum element
	for i in reversed(range(n - 1)):

		print(i)
		# update `max_so_far` if the current element is greater than the
		# maximum element
		if A[i] >= max_so_far:
			max_so_far = A[i]

		# if the current element is less than the maximum element,
		# then update the difference if required
		else:
			diff = max(diff, max_so_far - A[i])

	# return difference
	return diff


if __name__ == '__main__':

	A = [2, 7, 9, 5, 1, 3, 5]
	diff = getMaxDiff(A)
	if diff != -sys.maxsize:
		print("The maximum difference is", diff)
