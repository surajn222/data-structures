# Function to find the maximum sum path in two given lists.
# The code is similar to the merge routine of the merge sort algorithm
def findMaxSum(X, Y):
	total = sum_x = sum_y = 0

	m = len(X)
	n = len(Y)

	# `i` and `j` denotes the current index of `X` and `Y`, respectively
	i = j = 0

	# loop till `X` and `Y` are empty
	while i < m and j < n:

		# to handle the duplicate elements in `X`
		while i < m - 1 and X[i] == X[i + 1]:
			sum_x += X[i]
			i = i + 1

		# to handle the duplicate elements in `Y`
		while j < n - 1 and Y[j] == Y[j + 1]:
			sum_y += Y[j]
			j = j + 1

		# if the current element of `Y` is less than the current element of `X`
		if Y[j] < X[i]:
			sum_y += Y[j]
			j = j + 1

		# if the current element of `X` is less than the current element of `Y`
		elif X[i] < Y[j]:
			sum_x += X[i]
			i = i + 1

		else:  # if X[i] == Y[j]
			# consider the maximum sum and include the current cell's value
			total += max(sum_x, sum_y) + X[i]

			# move both indices by 1 position
			i = i + 1
			j = j + 1

			# reset both sums
			sum_x = 0
			sum_y = 0

	# process the remaining elements of `X` (if any)
	while i < m:
		sum_x += X[i]
		i = i + 1

	# process the remaining elements of `Y` (if any)
	while j < n:
		sum_y += Y[j]
		j = j + 1

	total += max(sum_x, sum_y)
	return total


if __name__ == '__main__':
	X = [3, 6, 7, 8, 10, 12, 15, 18, 100]
	Y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]

	print('The maximum sum is', findMaxSum(X, Y))
