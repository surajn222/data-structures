# Find maximum length sublist with sum `S` present in a given list
def findMaxLenSublist(nums, S):
	# create an empty dictionary to store the ending index of the first
	# sublist having some sum
	d = {}

	# insert (0, -1) pair into the set to handle the case when a
	# sublist with sum `S` starts from index 0
	d[0] = -1

	target = 0

	# `length` stores the maximum length of sublist with sum `S`
	length = 0

	# stores ending index of the maximum length sublist having sum `S`
	ending_index = -1

	# traverse the given list
	for i in range(len(nums)):

		# target of elements so far
		target += nums[i]

		# if the sum is seen for the first time, insert the sum with its
		# into the dictionary
		if target not in d:
			d[target] = i

		# update length and ending index of the maximum length sublist
		# having sum `S`
		if target - S in d and length < i - d[target - S]:
			length = i - d[target - S]
			ending_index = i

	# print the sublist
	print((ending_index - length + 1, ending_index))


if __name__ == '__main__':
	nums = [5, 6, -5, 5, 3, 5, 3, -2, 0]
	target = 8

	findMaxLenSublist(nums, target)
