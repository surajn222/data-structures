import sys


# Function to find the maximum value of `j-i` such that nums[j] > nums[i]
def findMaxDiff(nums):
	# `diff` stores the maximum value of `j-i` such that nums[j] > nums[i]
	diff = -sys.maxsize

	# base case
	if not nums:
		return diff

	# get the length of the array
	n = len(nums)

	# create an auxiliary array of size `n`
	aux = [0] * n

	# aux[j] stores the maximum element in subarray nums[j, n-1]
	aux[n - 1] = nums[n - 1]
	for j in reversed(range(n - 1)):
		aux[j] = max(nums[j], aux[j + 1])

	# Find maximum `j-i` using the auxiliary array
	i = j = 0
	while i < n and j < n:
		if nums[i] < aux[j]:
			diff = max(diff, j - i)
			j += 1
		else:
			i += 1

	return diff


if __name__ == '__main__':
	nums = [9, 10, 2, 6, 7, 12, 8, 1]
	print('The maximum value is', findMaxDiff(nums))
