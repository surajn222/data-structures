# Python program to merge
# two sorted arrays
def mergeArrays(arr1, arr2):
	arr3 = [None] * (len(arr1 + arr2))
	i = 0
	j = 0
	k = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			print(arr1[i])
			arr3[k] = arr1[i]
			i += 1
			k += 1
		else:
			print(arr2[j])
			arr3[k] = arr2[j]
			j += 1
			k += 1

	while i < len(arr1):
		arr3[k] = arr1[i]
		i += 1
		k += 1

	while j < len(arr2):
		arr3[k] = arr2[j]
		j += 1
		k += 1

	print(arr3)

	list_str3 = map(str, arr3)

	str3 = "".join(list_str3)
	return str(str3)


# i = 0
# while i < len(arr2):
# 	print(arr2[i])
# 	i += 1
# arr3 = [None] * (n1 + n2)
# i = 0
# j = 0
# k = 0
#
# # Traverse both array
# while i < n1 and j < n2:
# 	if arr1[i] < arr2[j]:
# 		arr3[k] = arr1[i]
# 		k = k + 1
# 		i = i + 1
# 	else:
# 		arr3[k] = arr2[j]
# 		k = k + 1
# 		j = j + 1
#
# # Store remaining elements of first array
# while i < n1:
# 	arr3[k] = arr1[i];
# 	k = k + 1
# 	i = i + 1
#
# # Store remaining elements
# # of second array
# while j < n2:
# 	arr3[k] = arr2[j];
# 	k = k + 1
# 	j = j + 1
# print("Array after merging")
# for i in range(n1 + n2):
# 	print(str(arr3[i]), end=" ")
#

# Driver code
arr1 = [1, 3, 5, 7]

arr2 = [2, 4, 6, 8]

str3 = mergeArrays(arr1, arr2)
print(str3)

# This code is contributed
# by ChitraNayal
