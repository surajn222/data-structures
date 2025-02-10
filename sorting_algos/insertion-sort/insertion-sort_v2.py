print("Insertion sort")

# Whenever there are two for loops, the outer for loop is the iteration loop, the inner for loop is the operation loop

# Step 1
# In order to understand bubble sort, understand the inner loop first
array_arr = [3, 4, 10, 8, 4]

# This is inner loop.
# This loop will push the only biggest element to the end of the array.
# Lets try to fix one element - array_arr[3] = 8
int_index_iteration_loop = 3
current_element_to_be_rearranged_value = array_arr[int_index_iteration_loop]
int_index_operation_loop = int_index_iteration_loop - 1

while int_index_operation_loop > 0 and current_element_to_be_rearranged_value < array_arr[int_index_operation_loop]:
	print("Current element " + str(current_element_to_be_rearranged_value))
	print("Element from the array j " + str(array_arr[int_index_operation_loop]))
	array_arr[int_index_operation_loop + 1] = array_arr[int_index_operation_loop]
	int_index_operation_loop = int_index_operation_loop - 1

print("Start")

# This is the entire program
array_arr = [10, 8, 6, 4, 2]

for int_index_iteration_loop in range(1, len(array_arr)):
	current_element_to_be_rearranged_value = array_arr[int_index_iteration_loop]
	int_index_operation_loop = int_index_iteration_loop - 1

	while int_index_operation_loop >= 0 and current_element_to_be_rearranged_value < array_arr[int_index_operation_loop]:
		print("Current element " + str(current_element_to_be_rearranged_value))
		print("Element to be compared j " + str(array_arr[int_index_operation_loop]))
		# array_arr[int_index_operation_loop + 1], array_arr[int_index_operation_loop] = array_arr[int_index_operation_loop], array_arr[int_index_operation_loop + 1]
		array_arr[int_index_operation_loop + 1] = array_arr[int_index_operation_loop]
		int_index_operation_loop = int_index_operation_loop - 1
	array_arr[int_index_operation_loop + 1] = current_element_to_be_rearranged_value
	print(array_arr)

# Worst case time complexity is n^2, because of two loops
