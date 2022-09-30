# Function to merge two sorted lists `X` and `Y`
def merge(X, Y):
	k = i = j = 0
	aux = [0] * (len(X) + len(Y))

	# while there are elements in the first and second arrays
	while i < len(X) and j < len(Y):
		if X[i] <= Y[j]:
			aux[k] = X[i]
			i = i + 1
		else:
			aux[k] = Y[j]
			j = j + 1
		k = k + 1

	# copy remaining elements
	while i < len(X):
		aux[k] = X[i]
		k = k + 1
		i = i + 1

	while j < len(Y):
		aux[k] = Y[j]
		k = k + 1
		j = j + 1

	return aux


if __name__ == '__main__':
	X = [1, 4, 7, 8, 10]
	Y = [2, 3, 9]

	aux = merge(X, Y)

	print('First Array :', X)
	print('Second Array:', Y)
	print('After Merge :', aux)
