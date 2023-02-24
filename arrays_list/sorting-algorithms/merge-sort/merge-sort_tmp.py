# Step 1: split array into left array and right array.
# Step 2:
# Step 3:

# Step 2: Visualize this divide and conquer algorithm
def merge_sort_1(unsorted_array):
	print("1 Mergesort called with array: " + str(unsorted_array))
	if len(unsorted_array) <= 1:
		print("Return Mergesort called with array: " + str(unsorted_array))
		return

	mid_element = len(unsorted_array) // 2

	unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
	unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

	print("1 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
	print("1 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

	merge_sort_2(unsorted_left_array_will_return_sorted)
	merge_sort_2(unsorted_right_array_will_return_sorted)

	print("1 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
	print("1 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
	merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
						   unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_2(unsorted_array):
	print("2 Mergesort called with array: " + str(unsorted_array))
	if len(unsorted_array) <= 1:
		print("Return Mergesort called with array: " + str(unsorted_array))
		return

	mid_element = len(unsorted_array) // 2

	unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
	unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

	print("2 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
	print("2 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

	merge_sort_3(unsorted_left_array_will_return_sorted)
	merge_sort_3(unsorted_right_array_will_return_sorted)

	print("2 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
	print("2 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
	merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
						   unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_3(unsorted_array):
	print("3 Mergesort called with array: " + str(unsorted_array))
	if len(unsorted_array) <= 1:
		print("Return Mergesort called with array: " + str(unsorted_array))
		return

	mid_element = len(unsorted_array) // 2

	unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
	unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

	print("3 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
	print("3 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

	merge_sort_4(unsorted_left_array_will_return_sorted)
	merge_sort_4(unsorted_right_array_will_return_sorted)

	print("3 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
	print("3 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
	merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
						   unsorted_array)


# Step 2: Visualize this divide and conquer algorithm
def merge_sort_4(unsorted_array):
	print("4 Mergesort called with array: " + str(unsorted_array))
	if len(unsorted_array) <= 1:
		print("4 Return Mergesort called with array: " + str(unsorted_array))
		return

	mid_element = len(unsorted_array) // 2

	unsorted_left_array_will_return_sorted = unsorted_array[:mid_element]
	unsorted_right_array_will_return_sorted = unsorted_array[mid_element:]

	print("4 ---Left array before merge: " + str(unsorted_left_array_will_return_sorted))
	print("4 ---Right array before merge: " + str(unsorted_right_array_will_return_sorted))

	merge_sort_4(unsorted_left_array_will_return_sorted)
	merge_sort_4(unsorted_right_array_will_return_sorted)

	print("4 ---Left array after merge: " + str(unsorted_left_array_will_return_sorted))
	print("4 ---Right array after merge: " + str(unsorted_right_array_will_return_sorted))
	merge_two_sorted_lists(unsorted_left_array_will_return_sorted, unsorted_right_array_will_return_sorted,
						   unsorted_array)


# Step 1: Learn how to merge two lists
def merge_two_sorted_lists(unmerged_array_1, unmerged_array_2, merged_array):  # Do this visually
	print("Arrays to merge: " + str(unmerged_array_1) + " " + str(unmerged_array_2) + " " + str(merged_array))
	len_unmerged_array_1 = len(unmerged_array_1)
	len_unmerged_array_2 = len(unmerged_array_2)

	unmerged_array_1_index = unmerged_array_2_index = merged_array_index = 0

	while unmerged_array_1_index < len_unmerged_array_1 and unmerged_array_2_index < len_unmerged_array_2:
		if unmerged_array_1[unmerged_array_1_index] <= unmerged_array_2[unmerged_array_2_index]:
			merged_array[merged_array_index] = unmerged_array_1[unmerged_array_1_index]
			unmerged_array_1_index += 1
		else:
			merged_array[merged_array_index] = unmerged_array_2[unmerged_array_2_index]
			unmerged_array_2_index += 1
		merged_array_index += 1

	while unmerged_array_1_index < len_unmerged_array_1:
		merged_array[merged_array_index] = unmerged_array_1[unmerged_array_1_index]
		unmerged_array_1_index += 1
		merged_array_index += 1

	while unmerged_array_2_index < len_unmerged_array_2:
		merged_array[merged_array_index] = unmerged_array_2[unmerged_array_2_index]
		unmerged_array_2_index += 1
		merged_array_index += 1

	print("Arrays merged: " + str(unmerged_array_1) + " " + str(unmerged_array_2) + " " + str(merged_array))


if __name__ == '__main__':
	test_cases = [
		[10, 3, 15, 7, 8, 23, 98, 29],
		[],
		[3],
		[9, 8, 7, 2],
		[1, 2, 3, 4, 5]
	]

	for unsorted_array in test_cases:
		print("------------------------------------------")
		merge_sort_1(unsorted_array)
		print(unsorted_array)

	# arr = [0,0,0,0,0,0,0,0]
	# arr1 = [1,3,5,7]
	# arr2 = [2,4,6,8]
	# merge_two_sorted_lists(arr1,arr2, arr)
	# print(arr)
