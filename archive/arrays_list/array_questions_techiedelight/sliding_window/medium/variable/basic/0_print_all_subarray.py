def findSublist2(array_1):
	print(array_1)

	i = j = 0
	# size_of_subarray = 9

	while i <= len(array_1) - 1:
		common_subarray = []
		while j < len(array_1):
			print(str(i) + " " + str(j))
			common_subarray.append(array_1[j])
			print("subarray size match: " + str(common_subarray))
			j += 1

		common_subarray.pop(0)
		i += 1
		j = i


if __name__ == '__main__':
	# a list of positive integers
	nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 15

	# findSublist(nums, target)
	findSublist2(nums)
