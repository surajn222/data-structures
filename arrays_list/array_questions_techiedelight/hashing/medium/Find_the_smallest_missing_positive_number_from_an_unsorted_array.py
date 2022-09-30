# Function to find the smallest missing positive number from an unsorted array
def findSmallestMissing(nums):
	# initialize the set from array elements
	distinct = {*nums}

	# return first smallest missing positive number from the set
	index = 1
	while True:
		if index not in distinct:
			return index
		index += 1


if __name__ == '__main__':
	nums = [1, 4, 2, -1, 6, 5]
	print('The smallest missing positive number from the array is',
		  findSmallestMissing(nums))
