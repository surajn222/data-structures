# TODO: Study
# Maximum_of_all_subarrays_of_size_'k'_using_Sliding_Window_Technique
# Python program to find the maximum for
# each and every contiguous subarray of
# size k

# Method to find the maximum for each
# and every contiguous subarray
# of size k
def printMax(arr, n, k):
	max = 0

	for i in range(n - k + 1):
		max = arr[i]
		for j in range(1, k):
			if arr[i + j] > max:
				max = arr[i + j]
		print(str(max) + " ", end="")


# Driver method
if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	n = len(arr)
	k = 3
	printMax(arr, n, k)


# This code is contributed by Shiv Shankar


# -----------------------------------------------
# Python code for the above approach
def findKMaxElement(arr, k, n):
	# creating the max heap ,to get max element always
	queue = []

	res = []
	i = 0

	while (i < k):
		queue.append(arr[i])
		i += 1

	queue.sort(reverse=True)

	# adding the maximum element among first k elements
	res.append(queue[0])

	# removing the first element of the array
	queue.remove(arr[0])

	# iterarting for the next elements
	while (i < n):
		# adding the new element in the window
		queue.append(arr[i])
		queue.sort(reverse=True)

		# finding & adding the max element in the
		# current sliding window
		res.append(queue[0])

		# finally removing the first element from front
		# end of queue
		queue.remove(arr[i - k + 1])
		i += 1
	return res


# Driver Code
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k, n = 4, len(arr)
res = findKMaxElement(arr, k, n)
for x in res:
	print(x, end=" ")

# This code is contributed by shinjanpatra


# ----------------------------------------------
# Python program to find the maximum for
# each and every contiguous subarray of
# size k

from collections import deque


# A Deque (Double ended queue) based
# method for printing maximum element
# of all subarrays of size k
def printMax(arr, n, k):
	""" Create a Double Ended Queue, Qi that
	will store indexes of array elements.
	The queue will store indexes of useful
	elements in every window and it will
	maintain decreasing order of values from
	front to rear in Qi, i.e., arr[Qi.front[]]
	to arr[Qi.rear()] are sorted in decreasing
	order"""
	Qi = deque()

	# Process first k (or first window)
	# elements of array
	for i in range(k):

		# For every element, the previous
		# smaller elements are useless
		# so remove them from Qi
		while Qi and arr[i] >= arr[Qi[-1]]:
			Qi.pop()

		# Add new element at rear of queue
		Qi.append(i);

	# Process rest of the elements, i.e.
	# from arr[k] to arr[n-1]
	for i in range(k, n):

		# The element at the front of the
		# queue is the largest element of
		# previous window, so print it
		print(str(arr[Qi[0]]) + " ", end="")

		# Remove the elements which are
		# out of this window
		while Qi and Qi[0] <= i - k:
			# remove from front of deque
			Qi.popleft()

		# Remove all elements smaller than
		# the currently being added element
		# (Remove useless elements)
		while Qi and arr[i] >= arr[Qi[-1]]:
			Qi.pop()

		# Add current element at the rear of Qi
		Qi.append(i)

	# Print the maximum element of last window
	print(str(arr[Qi[0]]))


# Driver code
if __name__ == "__main__":
	arr = [12, 1, 78, 90, 57, 89, 56]
	k = 3
	printMax(arr, len(arr), k)

# This code is contributed by Shiv Shankar
