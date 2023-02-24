# Find the missing number in a given sorted array
# https://leetcode.com/problems/missing-number/ # Pending
def missing(nums):
	m = len(nums)
	total = sum(nums)
	print("total: " + str(total))

	expected_total = (m * (m + 1)) / 2
	print("expected_total: " + str(expected_total))

	return expected_total - total


def getMissingNumber(arr):
	# get the array's length
	n = len(arr)

	# actual size is `n+1` since a number is missing from the list
	m = n + 1

	# get a sum of integers between 1 and `n+1`
	total = m * (m + 1) // 2

	# the missing number is the difference between the expected sum and
	# the actual sum of integers in the list
	return total - sum(arr)


if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 7, 8, 9, 10]
	arr = [3, 0, 1]
	arr = [0, 1, 2, 3, 4, 6]

	print('The missing number is', getMissingNumber(arr))
	print('The missing number is', missing(arr))
