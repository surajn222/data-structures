# Function to left-rotate a list by one position
# https://leetcode.com/problems/rotate-array/ # Pending
def leftRotateByOne(A):
	first = A[0]
	for i in range(len(A) - 1):
		A[i] = A[i + 1]

	A[-1] = first


# Function to left-rotate a list by `r` positions
def leftRotate(A, r):
	# base case: invalid input
	if r < 0 or r >= len(A):
		return

	for i in range(r):
		leftRotateByOne(A)


if __name__ == '__main__':
	A = [1, 2, 3, 4, 5]
	r = 2

	leftRotate(A, r)
	print(A)
