# Binary search algorithm to return the position of key `x` in sublist A[left…right]
def binarySearch(A, left, right, x):
	# base condition (search space is exhausted)
	if left > right:
		return -1

	# find the mid-value in the search space and
	# compares it with the key

	mid = (left + right) // 2

	# overflow can happen. Use below
	# mid = left + (right - left) // 2

	# base condition (a key is found)
	if x == A[mid]:
		return mid

	# discard all elements in the right search space,
	# including the middle element
	elif x < A[mid]:
		return binarySearch(A, left, mid - 1, x)

	# discard all elements in the left search space,
	# including the middle element
	else:
		return binarySearch(A, mid + 1, right, x)


# Returns the position of key `x` in a given list `A` of length `n`
def exponentialSearch(A, x):
	# base case
	if not A:
		return -1

	bound = 1

	# find the range in which key `x` would reside
	while bound < len(A) and A[bound] < x:
		bound *= 2  # calculate the next power of 2

	# call binary search on A[bound/2 … min(bound, n-1)]
	return binarySearch(A, bound // 2, min(bound, len(A) - 1), x)


# Exponential search algorithm
if __name__ == '__main__':

	A = [2, 5, 6, 8, 9, 10]
	key = 9

	index = exponentialSearch(A, key)

	if index != -1:
		print('Element found at index', index)
	else:
		print('Element found not in the list')
