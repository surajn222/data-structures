''' Python3 code for k largest elements in an array'''


def kLargest(arr, k):
	# Sort the given array arr in reverse
	# order.
	arr.sort()
	# Print the first kth largest elements
	for i in range(k):
		print(arr[i], end=" ")


# Driver program
arr = [1, 23, 12, 9, 30, 2, 50]
# n = len(arr)
k = 3
kLargest(arr, k)

# This code is contributed by shreyanshi_arun.
