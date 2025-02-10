import sys


# Bottom-up DP function to mark if string `X[i…j]` is a palindrome
# or not for all possible values of `i` and `j`
def findAllPalindromes(X, isPalin):
	for i in reversed(range(len(X))):
		for j in range(i, len(X)):
			if i == j:
				isPalin[i][j] = True
			elif X[i] == X[j]:
				if j - i == 1:
					isPalin[i][j] = True
				else:
					isPalin[i][j] = isPalin[i + 1][j - 1]
			else:
				isPalin[i][j] = False


# Iterative function to find the minimum cuts needed in a string
# such that each partition is a palindrome
def findMinCuts(X, isPalin):
	# create a lookup table to store solutions to subproblems
	# `lookup[i]` stores the minimum cuts needed in substring `X[i…n)`
	lookup = [sys.maxsize] * len(X)

	# start from the string's end
	for i in reversed(range(len(X))):

		# if `X[i…n-1]` is a palindrome, the total cuts needed is 0
		if isPalin[i][len(X) - 1]:
			lookup[i] = 0
		else:
			# otherwise, find `lookup[i]`
			for j in range(len(X) - 2, i - 1, -1):
				if isPalin[i][j]:
					lookup[i] = min(lookup[i], 1 + lookup[j + 1])

	return lookup[0]


def findMinimumCuts(X):
	# base case
	if not X:
		return 0

	# isPalin[i][j] stores if substring X[i][j] is palindrome or not
	isPalin = [[False for x in range(len(X) + 1)] for y in range(len(X) + 1)]

	# find all substrings of `X` that are palindromes
	findAllPalindromes(X, isPalin)

	return findMinCuts(X, isPalin)


if __name__ == '__main__':
	X = 'BABABCBADCEDE'  # BAB|ABCBA|D|C|EDE

	print('The minimum cuts required are', findMinimumCuts(X))
