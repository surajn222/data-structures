# Function to find an odd occurring element in a given list
def findOddOccuring(arr):
	xor = 0
	for i in arr:
		xor = xor ^ i

	return xor


if __name__ == '__main__':
	arr = [4, 3, 6, 2, 6, 4, 2, 3, 4, 3, 3]
	print('The odd occurring element is', findOddOccuring(arr))
