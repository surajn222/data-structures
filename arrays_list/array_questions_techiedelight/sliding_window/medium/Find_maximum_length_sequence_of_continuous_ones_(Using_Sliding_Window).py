# Find the index of 0 to replace with 1 to get the maximum sequence
# of continuous 1's using the sliding window technique
def findIndexofZero(A):
	left = 0  # represents the window's starting index
	count = 0  # stores the total number of zeros in the current window
	max_count = 0  # stores the maximum number of 1's (including 0)

	max_index = -1  # stores the index of 0 to be replaced
	prev_zero_index = -1  # stores the index of previous zero

	# maintain a window `[left…i]` containing at most one zero
	for i in range(len(A)):

		# if the current element is 0, update prev_zero_index and
		# increase zeros count in the current window by 1
		if A[i] == 0:
			prev_zero_index = i
			count = count + 1

		# the window becomes unstable if the total number of zeros in it becomes 2
		if count == 2:
			# remove elements from the window's left side till
			# we found a zero
			while A[left]:
				left = left + 1

			# remove the leftmost 0 so that window becomes stable again
			left = left + 1

			# decrement count as 0 is removed
			count = 1

		# when we reach here, window `[left…i]` contains only
		# at most one zero; update the maximum count and index of 0
		# to be replaced if required

		if i - left + 1 > max_count:
			max_count = i - left + 1
			max_index = prev_zero_index

	# return index of 0 to be replaced or -1 if the list contains all 1's
	return max_index


if __name__ == '__main__':

	A = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1]

	index = findIndexofZero(A)
	if index != -1:
		print("Index to be replaced is", index)
	else:
		print("Invalid input")
