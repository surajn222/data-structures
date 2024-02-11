# A recursive solution for subset sum
# problem


# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(arr, n, sum, store):

	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False

	# If last element is greater than
	# sum, then ignore it

	if store[n][sum] != -1:
		return store[n][sum]
	# if (set[n - 1] > sum):
		# return isSubsetSum(set, n - 1, sum, store)
	if (arr[n-1] > sum):
		store[n][sum] = isSubsetSum(arr, n-1, sum, store)
		return store[n][sum]


	# Else, check if sum can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	c1 = isSubsetSum(arr, n-1, sum, store)
	c2 = isSubsetSum(arr, n-1, sum-arr[n-1], store)

	store[n][sum] = c1 or c2
	return c1 or c2


# Driver code
if __name__ == '__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 7
	n = len(set)
	store = [[-1 for i in range(sum + 1)] for j in range(n + 1)]
	if (isSubsetSum(set, n, sum, store) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")

# This code is contributed by Nikita Tiwari.
