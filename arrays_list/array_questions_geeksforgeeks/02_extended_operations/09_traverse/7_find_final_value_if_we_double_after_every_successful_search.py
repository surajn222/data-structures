# Python program to find value if we double
# the value after every successful search

# Function to Find the value of k
def findValue(a, n, k):
	exist = True

	while exist:
		# Search for k. After every successful
		# search, double k and change exist to true
		# and search again for k from the start of array
		exist = False

		for i in range(n):
			# Check is a[i] is equal to k
			if a[i] == k:
				k *= 2
				exist = True
				break

	return k


# Driver's Code
arr = [2, 3, 4, 10, 8, 1]
k = 2
n = len(arr)
print(findValue(arr, n, k))
