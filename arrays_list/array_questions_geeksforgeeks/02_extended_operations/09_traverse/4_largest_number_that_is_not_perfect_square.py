# python program to find
# the largest non perfect
# square number among n numbers

import math


def check(n):
	# takes the sqrt of the number
	d = int(math.sqrt(n))

	# checks if it is a
	# perfect square number
	if (d * d == n):
		return True

	return False


# function to find the largest
# non perfect square number
def largestNonPerfectSquareNumber(a, n):
	# stores the maximum of all
	# non perfect square numbers
	maxi = -1

	# traverse for all elements
	# in the array
	for i in range(0, n):

		# store the maximum if
		# not a perfect square
		if (check(a[i]) == False):
			maxi = max(a[i], maxi)

	return maxi


# driver code
a = [16, 20, 25, 2, 3, 10]
n = len(a)

# function call
print(largestNonPerfectSquareNumber(a, n))

# This code is contributed by Gitanjali.
