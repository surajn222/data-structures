def subArraySum(arr, n, sum_):
	# Initialize curr_sum as
	# value of first element
	# and starting point as 0
	curr_sum = arr[0]
	start = 0
	map_sum = {}
	# Add elements one by one to curr_sum and if the curr_sum exceeds the sum, then remove starting element
	i = 1
	while i <= n:
		map_sum[curr_sum] = i
		print(map_sum)

		if curr_sum - sum_ == 0:
			print("Found subarray")
			print(str(0) + " " + str(i))

		if curr_sum - sum_ in map_sum:
			print("Found subarray")
			print(str(map_sum[curr_sum - sum_]) + " " + str(i))

		# If curr_sum exceeds
		# the sum, then remove
		# the starting elements
		# print(arr[i])
		if i < len(arr):
			curr_sum = curr_sum + arr[i]
			print(curr_sum)

		i += 1

	# If we reach here,
	# then no subarray
	print("No subarray found")
	return 0


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 17

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
