# https://www.techiedelight.com/count-distinct-elements-every-sub-array-size-k-array/


def print_subarrays(array_1):
	print(array_1)

	i = j = 0
	size_of_subarray = 4
	common_subarray = []
	map_freq = {}

	while i <= len(array_1) - size_of_subarray:
		print(str(i) + " " + str(j))
		if (j - i + 1) == size_of_subarray:
			common_subarray.append(array_1[j])
			map_freq[array_1[j]] = map_freq.get(array_1[j], 0) + 1
			print("subarray size match: " + str(common_subarray))
			print("Freq map: " + str(map_freq))
			print("Size of frequency map: " + str(len(map_freq)))

			# Get element at first index of common_subarray and remove it from freq_map
			remove_element = common_subarray[0]
			map_freq[remove_element] = map_freq.get(remove_element) - 1
			if map_freq.get(remove_element) == 0:
				del map_freq[remove_element]
			common_subarray.pop(0)
			i += 1
			j += 1
		else:
			common_subarray.append(array_1[j])
			map_freq[array_1[j]] = map_freq.get(array_1[j], 0) + 1
			j += 1


array_1 = [0, 1, 1, 2, 2, 3, 4, 4, 4, 4]

print_subarrays(array_1)
