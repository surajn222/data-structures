# TODO: Study: Easy: https://leetcode.com/problems/find-pivot-index/description/
# Find equilibrium index of an array


# Python program to find the equilibrium
# index of an array

# Function to find the equilibrium index

def equilibrium(arr):

	# finding the sum of whole array
	total_sum = sum(arr)
	leftsum = 0
	for i in range(0, len(arr)):

		# total_sum is now right sum
		# for index i
		total_sum -= arr[i]

		if leftsum == total_sum:
			return i
		leftsum += arr[i]

	# If no equilibrium index found,
	# then return -1
	return -1


# Driver code
if __name__ == "__main__":
	arr = [-7, 1, 5, 2, -4, 3, 0]

	# Function call
	print('First equilibrium index is ',
		equilibrium(arr))

# This code is contributed by Abhishek Sharma
