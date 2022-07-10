# Python 3 program to find an array
# element that divides all numbers
# in the array using naive approach

# Function to find smallest num
def findSmallest(a, n):
	# Traverse for all elements
	for i in range(0, n):

		for j in range(0, n):

			if ((a[j] % a[i]) >= 1):
				break

		# Stores the minimum
		# if it divides all
		if (j == n - 1):
			return a[i]

	return -1


# Driver code
a = [25, 20, 5, 10, 100]
n = len(a)
print(findSmallest(a, n))

# This code is contributed by Nikita Tiwari.
