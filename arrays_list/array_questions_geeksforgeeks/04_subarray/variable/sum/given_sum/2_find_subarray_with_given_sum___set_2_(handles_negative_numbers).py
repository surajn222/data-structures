# Find_subarray_with_given_sum___Set_2_(Handles_Negative_Numbers)
# Returns true if the there is a subarray of arr[] with sum
# equal to 'sum'
# otherwise returns false. Also, prints the result

# https://leetcode.com/problems/subarray-sum-equals-k/ # Pending
def subArraySum(arr, n, Sum):
	# create an empty map
	Map = {}

	# Maintains sum of elements so far
	curr_sum = 0

	for i in range(0, n):

		# add current element to curr_sum
		curr_sum = curr_sum + arr[i]

		# if curr_sum is equal to target sum
		# we found a subarray starting from index 0
		# and ending at index i
		if curr_sum == Sum:
			print("Sum found between indexes 0 to", i)
			return

		# If curr_sum - sum already exists in map
		# we have found a subarray with target sum
		if (curr_sum - Sum) in Map:
			print("Sum found between indexes",
				  Map[curr_sum - Sum] + 1, "to", i)

			return

		Map[curr_sum] = i

	# If we reach here, then no subarray exists
	print("No subarray with given sum exists")


# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23

subArraySum(arr, n, sum_)


# This code is Contributed by shreyanshi_arun.


# ---------------------------------------------------------
# An efficient program
# to print subarray
# with sum as given sum

# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
def subArraySum(arr, n, sum_):
	# Initialize curr_sum as
	# value of first element
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
