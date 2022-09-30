# Find the index of 0 to replace with 1 to get the maximum sequence of continuous 1's
def findIndexofZero(A):
	# base case
	if len(A) == 1 and A[0] == 0:
		return 0

	# A[i] now stores the length of consecutive 1's ending at `A[i]`
	for i in range(1, len(A)):
		if A[i] == 1:
			A[i] += A[i - 1]

	count = 0

	# traverse the list from right to left
	for i in reversed(range(len(A))):

		# update the count to the number of adjacent 1's, which includes the
		# current element
		count = max(A[i], count)

		# update the list with the count of adjacent 1's for each
		# non-zero element
		if A[i]:
			A[i] = count
		else:
			# reset the count if the current element is 0
			count = 0

	max_count = 0  # stores the maximum number of 1's (including 0)
	max_index = -1  # stores the index of 0 to be replaced

	# consider each index `i` in the list
	for i in range(len(A)):

		# if the current element is 0
		if A[i] == 0:
			# update maximum count and index of 0 to be replaced if
			# required by taking a left and right element count

			if i == 0:
				if max_count < A[i + 1] + 1:
					max_count = A[i + 1] + 1
					max_index = i

			elif i == len(A) - 1:
				if max_count < A[i - 1] + 1:
					max_count = A[i - 1] + 1
					max_index = i

			elif max_count < A[i - 1] + A[i + 1] + 1:
				max_count = A[i - 1] + A[i + 1] + 1
				max_index = i

	# restore the original list
	for i in range(1, len(A)):
		if A[i]:
			A[i] = 1

	# return the index of 0 to be replaced, or -1 if the list contains all 1's
	return max_index


if __name__ == '__main__':

	A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

	index = findIndexofZero(A)

	if index != -1:
		print("Index to be replaced is", index)
	else:
		print("Invalid input")
