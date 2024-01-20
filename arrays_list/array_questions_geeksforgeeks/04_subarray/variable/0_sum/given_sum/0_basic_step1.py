def findSublist2(array_1, target_sum):
	print(array_1)

	i = j = 0
	# size_of_subarray = 9

	while i <= len(array_1) - 1:
		common_subarray = []
		while j < len(array_1):
			print(str(i) + " " + str(j))
			common_subarray.append(array_1[j])
			current_sum = sum(common_subarray)
			print("subarray size match: " + str(common_subarray))
			print("current sum: " + str(current_sum))
			if current_sum > target_sum:
				print("Current sum is greater than target sum, so breaking")
				break

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
	findSublist2(nums, target)
