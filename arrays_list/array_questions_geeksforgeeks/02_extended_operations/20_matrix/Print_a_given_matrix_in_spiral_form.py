# TODO: Pending
# Print_a_given_matrix_in_spiral_form
def spiralOrder(matrix):
	ans = []

	if (len(matrix) == 0):
		return ans

	m = len(matrix)
	n = len(matrix[0])
	seen = [[0 for i in range(n)] for j in range(m)]
	dr = [0, 1, 0, -1]
	dc = [1, 0, -1, 0]
	x = 0
	y = 0
	di = 0

	# Iterate from 0 to R * C - 1
	for i in range(m * n):
		ans.append(matrix[x][y])
		seen[x][y] = True
		cr = x + dr[di]
		cc = y + dc[di]

		if (0 <= cr and cr < m and 0 <= cc and cc < n and not (seen[cr][cc])):
			x = cr
			y = cc
		else:
			di = (di + 1) % 4
			x += dr[di]
			y += dc[di]
	return ans


# Driver code
a = [[1, 2, 3, 4],
	 [5, 6, 7, 8],
	 [9, 10, 11, 12],
	 [13, 14, 15, 16]]

for x in spiralOrder(a):
	print(x, end=" ")
print()


# -------------------------------------------
# Python3 program to print
# given matrix in spiral form


def spiralPrint(m, n, a):
	k = 0
	l = 0

	''' k - starting row index
		m - ending row index
		l - starting column index
		n - ending column index
		i - iterator '''

	while (k < m and l < n):

		# Print the first row from
		# the remaining rows
		for i in range(l, n):
			print(a[k][i], end=" ")

		k += 1

		# Print the last column from
		# the remaining columns
		for i in range(k, m):
			print(a[i][n - 1], end=" ")

		n -= 1

		# Print the last row from
		# the remaining rows
		if (k < m):

			for i in range(n - 1, (l - 1), -1):
				print(a[m - 1][i], end=" ")

			m -= 1

		# Print the first column from
		# the remaining columns
		if (l < n):
			for i in range(m - 1, k - 1, -1):
				print(a[i][l], end=" ")

			l += 1


# Driver Code
a = [[1, 2, 3, 4],
	 [5, 6, 7, 8],
	 [9, 10, 11, 12],
	 [13, 14, 15, 16]]

R = 4
C = 4

# Function Call
spiralPrint(R, C, a)


# This code is contributed by Nikita Tiwari.


# -------------------------------------------
# Python3 program for the above approach

# Function for printing matrix in spiral
# form i, j: Start index of matrix, row
# and column respectively m, n: End index
# of matrix row and column respectively


def printdata(arr, i, j, m, n):
	# If i or j lies outside the matrix
	if (i >= m or j >= n):
		return

	# Print First Row
	for p in range(i, n):
		print(arr[i][p], end=" ")

	# Print Last Column
	for p in range(i + 1, m):
		print(arr[p][n - 1], end=" ")

	# Print Last Row, if Last and
	# First Row are not same
	if ((m - 1) != i):
		for p in range(n - 2, j - 1, -1):
			print(arr[m - 1][p], end=" ")

	# Print First Column, if Last and
	# First Column are not same
	if ((n - 1) != j):
		for p in range(m - 2, i, -1):
			print(arr[p][j], end=" ")

	printdata(arr, i + 1, j + 1, m - 1, n - 1)


# Driver code
R = 4
C = 4
arr = [[1, 2, 3, 4],
	   [5, 6, 7, 8],
	   [9, 10, 11, 12],
	   [13, 14, 15, 16]]

# Function Call
printdata(arr, 0, 0, R, C)

# This code is contributed by avsadityavardhan
