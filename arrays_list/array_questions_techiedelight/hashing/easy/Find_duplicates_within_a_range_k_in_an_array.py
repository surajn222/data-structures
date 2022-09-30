# Given an array and a positive number k, check whether the array contains any duplicate elements within the range k. If k is more than the array’s size, the solution should check for duplicates in the complete array.
# K is the distance within which the duplicate should be present
def hasDuplicate(nums, k):
	# stores (element, index) pairs as (key, value) pairs
	d = {}

	# traverse the list
	for i, e in enumerate(nums):
		print("index: " + str(i))
		print("value: " + str(e))
		# if the current element already exists in the dictionary
		if e in d:

			# return true if the current element repeats within range of `k`

			print("get value in dict: " + str(d.get(e)))
			print("index minus value in dict: " + str(i - d.get(e)))
			print("range: " + str(k))
			if i - d.get(e) <= k:
				return True

		# store elements along with their indices
		d[e] = i
		print(d)

	# we reach here when no element repeats within range `k`
	return False


if __name__ == '__main__':

	nums = [5, 6, 8, 2, 4, 6, 9]
	k = 4

	if hasDuplicate(nums, k):
		print('Duplicates found')
	else:
		print('No duplicates were found')
