# Function to check if consecutive integers form a list
def isConsecutive(A):
	# base case
	if len(A) <= 1:
		return True

	# compute the minimum and maximum element in a list
	minimum = min(A)
	maximum = max(A)

	# for a list to contain consecutive integers, the difference between
	# the maximum and minimum element in it should be exactly `n-1`
	if maximum - minimum != len(A) - 1:
		return False

	# create an empty set (we can also use a visited list)
	visited = set()

	# traverse the list and checks if each element appears only once
	for i in A:
		# if an element is seen before, return false
		if i in visited:
			return False

		# mark element as seen
		visited.add(i)

	# we reach here when all elements in the list are distinct
	return True


if __name__ == '__main__':

	A = [-1, 5, 4, 2, 0, 3, 1]

	if isConsecutive(A):
		print("The array contains consecutive integers")
	else:
		print("Array do contain consecutive not integers")
