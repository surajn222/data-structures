# Function to find the minimum index of the repeating element
def findMinIndex(A):
	minIndex = len(A)

	# create an empty set to store list elements
	s = set()

	# traverse the list from right to left
	for i in reversed(range(len(A))):

		# if the element is seen before, update the minimum index
		if A[i] in s:
			minIndex = i
		# if the element is seen for the first time, insert it into the set
		else:
			s.add(A[i])

	# invalid input
	if minIndex == len(A):
		return -1

	# return minimum index
	return minIndex


if __name__ == '__main__':

	A = [5, 6, 3, 4, 3, 6, 4]
	# A = [1, 2, 3, 4, 5, 6]

	minIndex = findMinIndex(A)

	if minIndex != len(A):
		print("The minimum index of the repeating element is", minIndex)
	else:
		print("Invalid Input")
