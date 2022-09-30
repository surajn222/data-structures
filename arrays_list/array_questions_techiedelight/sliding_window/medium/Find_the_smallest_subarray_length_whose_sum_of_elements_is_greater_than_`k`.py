import sys


# Function to find the length of the smallest sublist whose sum
# of elements is greater than the given number
def findSmallestSublistLen(A, k):
	# stores the current window sum
	windowSum = 0

	# stores the result
	length = sys.maxsize

	# stores the window's starting index
	left = 0

	# maintain a sliding window `[left…right]`
	for right in range(len(A)):

		# include the current element in the window
		windowSum += A[right]

		# the window becomes unstable if its sum becomes more than `k`
		while windowSum > k and left <= right:
			# update the result if the current window's length is less than the
			# minimum found so far
			length = min(length, right - left + 1)

			# remove elements from the window's left side till the window
			# becomes stable again
			windowSum -= A[left]
			left = left + 1

	# invalid input
	if length == sys.maxsize:
		return 0

	# return result
	return length


if __name__ == '__main__':

	# a list of positive numbers
	A = [1, 2, 3, 4, 5, 6, 7, 8]
	k = 21

	# find the length of the smallest sublist
	length = findSmallestSublistLen(A, k)

	if length != sys.maxsize:
		print("The smallest sublist length is", length)
	else:
		print("No sublist exists")
