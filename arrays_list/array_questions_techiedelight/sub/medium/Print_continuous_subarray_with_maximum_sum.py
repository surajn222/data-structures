import sys


# Function to print contiguous sublist with the largest sum
# in a given set of integers
def kadane(A):
	# base case
	if len(A) <= 1:
		return A

	# stores the maximum sum sublist found so far
	maxSoFar = -sys.maxsize

	# stores the maximum sum of sublist ending at the current position
	maxEndingHere = 0

	# stores endpoints of maximum sum sublist found so far
	start = 0
	end = 0

	# stores starting index of a positive-sum sequence
	beg = 0

	# traverse the given list
	for i in range(len(A)):

		# update the maximum sum of sublist "ending" at index `i`
		maxEndingHere = maxEndingHere + A[i]

		# if the maximum sum becomes less than the current element,
		# start from the current element
		if maxEndingHere < A[i]:
			maxEndingHere = A[i]
			beg = i

		# update result if the current sublist sum is found to be greater
		if maxSoFar < maxEndingHere:
			maxSoFar = maxEndingHere
			start = beg
			end = i

	print("The contiguous sublist with the largest sum is", A[start: end + 1])


if __name__ == '__main__':
	A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	kadane(A)
