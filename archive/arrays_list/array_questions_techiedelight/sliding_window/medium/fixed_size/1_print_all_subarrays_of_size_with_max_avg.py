def print_subarrays(array_1):
	print(array_1)

	i = j = 0
	size_of_subarray = 2

	common_subarray = []
	sum = 0
	while i <= len(array_1) - size_of_subarray:
		print(str(i) + " " + str(j))
		if (j - i + 1) == size_of_subarray:
			common_subarray.append(array_1[j])
			sum = sum + array_1[j]
			print("subarray size match: " + str(common_subarray))
			print("Sum " + str(sum))
			common_subarray.pop(0)
			sum = sum - array_1[i]
			i += 1
			j += 1
		else:
			common_subarray.append(array_1[j])
			sum = sum + array_1[j]
			j += 1
		print("---------------------")


array_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print_subarrays(array_1)
