# TODO: Completed
# Python 3 program to find an array
# element that divides all numbers
# in the array using naive approach

# The logic:
# In an array, the minimum number can be the number that divides all other numbers.
# The second minimum number cannot be the number that divides all the numbers, because it wont divide the minimum number
# For eg
# [1, 2, 3, 4, 5]
# 1 can be divided by all numbers
# 2 cannot be divided by 1
# So the solution is, find the minimum number, check if it is divisible by all numbers, return true, elese false

# Function to find smallest num
def findSmallest(a, n):
	# Traverse for all elements
	for i in range(0, n):

		for j in range(0, n):
			print("== i = " + str(a[i]) + " j = " + str(a[j]))
			if ((a[j] % a[i]) >= 1):
				break

		# Stores the minimum
		# if it divides all elements
		print(" i = " + str(i) + " j = " + str(j) + " n-1 = " + str(n - 1) )
		# Code will reach this point only if j is divisible by all numbers
		# Need to check if j == n-1, because if j is the last element, a[j] % a[j] == 0 for all elements
		# if not, then the break has happened earlier, so its not divisible with all elements
		if (j == n - 1):
			return a[i]
		# if (j == n - 1):
		return a[i]

	return -1


# Driver code
a = [25, 20, 5, 10, 100]
n = len(a)
print(findSmallest(a, n))

# This code is contributed by Nikita Tiwari.


