# Recursive function to replace each element in the list with the product
# of every other element without using the division operator
def findProduct(A, n, left=1, i=0):
	# base case: no elements left on the right
	if i == n:
		return 1

	# take backup of the current element
	curr = A[i]

	# calculate the product of the right sublist
	right = findProduct(A, n, left * A[i], i + 1)

	# replace the current element with the product of the left and right sublist
	A[i] = left * right

	# return product of right the sublist, including the current element
	return curr * right


if __name__ == '__main__':
	A = [5, 3, 4, 2, 6, 8]

	findProduct(A, len(A))

	# print the modified list
	print(A)
