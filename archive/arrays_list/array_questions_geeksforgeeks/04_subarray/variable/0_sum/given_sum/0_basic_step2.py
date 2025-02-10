# TODO: Pending study
# Step 1: List down all the subarrays first
# Step 2: In the inner loop, stop the subarray when the current_sum > target_sum
# Step 3:
# Step 4:
def findSublist2(array_1, target_sum):
	print(array_1)

	i = j = 0
	# size_of_subarray = 9

	common_subarray = []
	current_sum = 0
	while i <= len(array_1) - 1:
		print("i = " + str(i) + ", j = " + str(j))

		while j < len(array_1):
			if current_sum > target_sum:
				print("Current sum " + str(current_sum) + " is greater than target sum, so breaking")
				break
			print("----------------")
			common_subarray.append(array_1[j])
			current_sum = sum(common_subarray)
			print("subarray size match: " + str(common_subarray))
			print("current sum: " + str(current_sum))
			print("Incrementing j now")
			j += 1

		print("i = " + str(i) + ", j = " + str(j))
		if i < len(array_1) - 1:
			current_sum = current_sum - array_1[i]
			common_subarray.pop(0)
			print("subarray size match2: " + str(common_subarray))
			print("current sum: " + str(current_sum))
			print("Incrementing i now")
		i += 1


if __name__ == '__main__':
	# a list of positive integers
	nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 14

	# findSublist(nums, target)
	findSublist2(nums, target)
