# https://leetcode.com/problems/sort-even-and-odd-indices-independently/ # Pending
# Python program to sort array
# in even and odd manner
# The odd numbers are to be
# sorted in descending order
# and the even numbers in
# ascending order

# To do two way sort. First
# sort even numbers in ascending
# order, then odd numbers in
# descending order.
def two_way_sort(arr, arr_len):
	# Current indexes l->left
	# and r->right
	l, r = 0, arr_len - 1

	# Count of number of
	# odd numbers, used in
	# slicing the array later.
	k = 0

	# Run till left(l) < right(r)
	while (l < r):

		# While left(l) is odd, if yes
		# increment the left(l) plus
		# odd count(k) if not break the
		# while for even number found
		# here to be swapped
		while (arr[l] % 2 != 0):
			l += 1
			k += 1

		# While right(r) is even,
		# if yes decrement right(r)
		# if not break the while for
		# odd number found here to
		# be swapped
		while (arr[r] % 2 == 0 and l < r):
			r -= 1

		# Swap the left(l) and right(r),
		# which is even and odd numbers
		# encountered in above loops
		if (l < r):
			arr[l], arr[r] = arr[r], arr[l]

	# Slice the number on the
	# basis of odd count(k)
	odd = arr[:k]
	even = arr[k:]

	# Sort the odd and
	# even array accordingly
	odd.sort(reverse=True)
	even.sort()

	# Extend the odd array with
	# even values and return it.
	odd.extend(even)

	return odd


# Driver code
arr_len = 6
arr = [1, 3, 2, 7, 5, 4]
result = two_way_sort(arr, arr_len)
for i in result:
	print(str(i) + " "),


# This code is contributed
# by JaySiyaRam


# ------------------------------------------------
# Python 3 program to sort array in
# even and odd manner. The odd
# numkbers are to be sorted in
# descending order and the even
# numbers in ascending order

# To do two way sort. First sort
# even numbers in ascending order,
# then odd numbers in descending order.
def twoWaySort(arr, n):
	# Make all odd numbers negative
	for i in range(0, n):

		# Check for odd
		if (arr[i] & 1):
			arr[i] *= -1

	# Sort all numbers
	arr.sort()

	# Retaining original array
	for i in range(0, n):
		if (arr[i] & 1):
			arr[i] *= -1


# Driver code
arr = [1, 3, 2, 7, 5, 4]
n = len(arr)
twoWaySort(arr, n);
for i in range(0, n):
	print(arr[i], end=" ")

# This code is contributed by Smitha Dinesh Semwal
# -----------------------------------------------------
# Python3 implementation of the approach

# Utility function to print
# the contents of the array
from functools import cmp_to_key


def printArr(arr, n):
	for i in range(n):
		print(arr[i], end=" ")


# To do two way sort. Make comparator function
# for the inbuilt sort function of c++ such that
# odd numbers are placed before even in descending
# and ascending order respectively
def compare(a, b):
	# If both numbers are even,
	# smaller number should
	# be placed at lower index
	if (a % 2 == 0 and b % 2 == 0 and a < b):
		return -1

	# If both numbers are odd larger number
	# should be placed at lower index
	if (a % 2 != 0 and b % 2 != 0 and b > a):
		return 1

	# If a is odd and b is even,
	# a should be placed before b
	if (a % 2 != 0):
		return -1

	# If b is odd and a is even,
	# b should be placed before a
	return 1


# Driver code
arr = [1, 3, 2, 7, 5, 4]
n = len(arr)

# Sort the array
arr.sort(key=cmp_to_key(compare))

# Print the sorted array
printArr(arr, n)

# This code is contributed by shinjanpatra
