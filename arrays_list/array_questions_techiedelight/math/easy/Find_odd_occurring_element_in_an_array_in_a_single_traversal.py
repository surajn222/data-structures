# Xor works in binary in such a way
# If 5 ^ 5  -> 5 + 5
# If 5 ^ 5 ^ 5  -> 5 + 5 - 5
# Function to find an odd occurring element in a given list
# https://leetcode.com/problems/single-number/ #Pending
def findOddOccuring(arr):
	xor = 0
	for i in arr:
		xor = xor ^ i

	return xor


if __name__ == '__main__':
	arr = [4, 3, 6, 2, 6, 4, 2, 3, 4, 3, 3]
	print('The odd occurring element is', findOddOccuring(arr))
