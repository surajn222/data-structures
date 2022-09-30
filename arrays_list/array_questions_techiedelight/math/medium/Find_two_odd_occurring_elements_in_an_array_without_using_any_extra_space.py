from math import log


def log2(x, base):
	return int(log(x) / log(base))


def findOddOccuring(arr):
	# take XOR of all list elements
	result = 0
	for i in arr:
		result = result ^ i

	# find the position of the rightmost set bit in `result`
	k = log2(result & -result, 2)

	# `x` and `y` are two odd appearing elements
	x = y = 0

	# split the list into two sublists
	for i in arr:

		# elements that have k'th bit set
		if i & (1 << k):
			x = x ^ i

		# elements that don't have k'th bit set
		else:
			y = y ^ i

	return x, y


if __name__ == '__main__':
	arr = [4, 3, 6, 2, 4, 2, 3, 4, 3, 3]
	print('The odd occurring elements are', findOddOccuring(arr))
