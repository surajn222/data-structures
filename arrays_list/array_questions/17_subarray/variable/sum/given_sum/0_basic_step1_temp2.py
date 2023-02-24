def findSublist(arr, target_sum):
	print(arr)
	i = 0
	j = 0
	current_subarray = []
	current_sum = arr[0]
	while i < len(arr):
		while j < len(arr):
			if current_sum == target_sum:
				print("Incrementing")
			if current_sum > target_sum:
				break
			# current_subarray = arr[i:j+1]
			# current_sum = sum(current_subarray)
			j += 1
			if j < len(arr):
				current_sum = current_sum + arr[j]
			print("J iter = i = " + str(i) + ", j = " + str(j) + ", current_sum = " + str(
				current_sum) + ", array = " + str(current_subarray))

		current_sum = current_sum - arr[i]
		i += 1
		# current_subarray = arr[i:j]
		# current_sum = sum(current_subarray)

		print("I iter = i = " + str(i) + ", j = " + str(j) + ", current_sum = " + str(current_sum) + ", array = " + str(
			current_subarray))


if __name__ == '__main__':
	# a list of positive integers
	nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
	# nums = [0, 9, 7, 2, 6, 1, 10, 3, 1, 4]
	# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 8
	# target = 3
	nums = [1, 2, 3]
	# nums = [0, 9, 7, 2, 6, 1, 10, 3, 1, 4]
	# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# target = 15
	target = 3

	findSublist(nums, target)
