from random import randrange


# Utility function to swap elements `A[i]` and `A[j]` in a list
def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# Function to shuffle a list `A`
def shuffle(A):
	# read list from the lowest index to highest
	for i in range(len(A) - 1):
		# generate a random number `j` such that `i <= j < n`
		j = randrange(i, len(A))

		# swap the current element with the randomly generated index
		swap(A, i, j)


if __name__ == '__main__':
	A = [1, 2, 3, 4, 5, 6]

	shuffle(A)

	# print the shuffled list
	print(A)
