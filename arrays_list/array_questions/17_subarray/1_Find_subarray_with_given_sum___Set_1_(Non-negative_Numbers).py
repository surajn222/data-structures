# Find_subarray_with_given_sum___Set_1_(Non-negative_Numbers)

# Returns true if the there is a subarray of arr[] with sum equal to 'sum'
# otherwise returns false. Also, prints the result
def subArraySum(arr, n, sum):
	# Pick a starting point
	for i in range(n):
		curr_sum = arr[i]

		# try all subarrays
		# starting with 'i'
		j = i + 1
		while j <= n:

			if curr_sum == sum_:
				print("Sum found between")
				print("indexes % d and % d" % (i, j - 1))

				return 1

			if curr_sum > sum_ or j == n:
				break

			curr_sum = curr_sum + arr[j]
			j += 1

	print("No subarray found")
	return 0


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)


# This code is Contributed by shreyanshi_arun.


# ---------------------------------------------------------

# An efficient program to print subarray with sum as given sum

# Returns true if the there is a subarray of arr[] with sum
# equal to 'sum'
# otherwise returns false. Also, prints the result.
def subArraySum(arr, n, sum_):
	# Initialize curr_sum as value of first element
	# and starting point as 0
	curr_sum = arr[0]
	start = 0

	# Add elements one by
	# one to curr_sum and
	# if the curr_sum exceeds
	# the sum, then remove
	# starting element
	i = 1
	while i <= n:

		# If curr_sum exceeds
		# the sum, then remove
		# the starting elements
		while curr_sum > sum_ and start < i - 1:
			curr_sum = curr_sum - arr[start]
			start += 1

		# If curr_sum becomes
		# equal to sum, then
		# return true
		if curr_sum == sum_:
			print("Sum found between indexes")
			print("% d and % d" % (start, i - 1))
			return 1

		# Add this element
		# to curr_sum
		if i < n:
			curr_sum = curr_sum + arr[i]
		i += 1

	# If we reach here,
	# then no subarray
	print("No subarray found")
	return 0


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)

# This code is Contributed by shreyanshi_arun.
