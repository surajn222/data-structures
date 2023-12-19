# A recursive solution for subset sum
# problem


# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(arr, n, sum):
	print(f"n = {n} , sum = {sum}, sum-arr = {sum-arr[n-1]}")
	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False

	# Else, check if sum can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	new_sum = sum - arr[n - 1]
	c1 = isSubsetSum(arr, n-1, new_sum)

	new_sum = sum
	c2 = isSubsetSum(arr, n-1, new_sum)

	# c2 = isSubsetSum(arr, n - 1, sum)
	return c1 or c2
	# return (
	# 		c1 or
	# 		c2
	# )


# Driver code
if __name__ == '__main__':
	arr = [3, 34, 4, 12, 5, 2]
	sum = 6
	n = len(arr)
	if (isSubsetSum(arr, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")

# This code is contributed by Nikita Tiwari.
