# Function to check if `X` can be derived from `Y` by rotating it
def check(X, Y):
	# if string lengths are different, they can't be
	# derived from each other
	if len(X) != len(Y):
		return False

	# Invariant: At the i'th iteration of this loop,
	# the string `X` will be rotated by `i` units
	for i in range(len(X)):

		# left rotate string `X` by 1 unit
		X = X[1:] + X[0]

		# return true if `X` becomes equal to `Y`
		if X == Y:
			return True

	# return false if no rotation is matched
	return False


if __name__ == '__main__':

	X = 'ABCD'
	Y = 'DABC'

	if check(X, Y):
		print('Given strings can be derived from each other')
	else:
		print('Given strings cannot be derived from each other')
