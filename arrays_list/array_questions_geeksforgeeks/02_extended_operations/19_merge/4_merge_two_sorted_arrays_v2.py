# TODO: Completed
# Python program to merge two sorted arrays/
def mergeArrays(arr1, arr2):
	arr3 = arr1 + arr2
	# sort the whole array arr3
	arr3.sort()
	arr3 = map(str, arr3)

	str3 = "".join(arr3)
	return str3


# Driver code
if __name__ == '__main__':
	arr1 = [1, 3, 5, 7]

	arr2 = [2, 4, 6, 8]

	str3 = mergeArrays(arr1, arr2)

	print(str3)
